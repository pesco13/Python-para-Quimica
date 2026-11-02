"""
Genera series sinteticas de datos de laboratorio para practicar ajustes.

Produce una curva de calibracion UV-Vis y un seguimiento cinetico a cuatro
temperaturas a partir de un numero entero que actua de semilla. El mismo
numero da siempre los mismos valores, y numeros distintos dan series
distintas con el mismo comportamiento fisico. Util para practicar una
regresion, un ajuste no lineal o una grafica de Arrhenius sin depender de
haber medido antes en el laboratorio.

Uso en Google Colab
-------------------
    !wget -q https://raw.githubusercontent.com/pesco13/Python-para-Quimica/main/datos/generar_datos.py
    from generar_datos import calibracion, cinetica, mi_familia, mi_asignacion

    NUMERO = 7                      # la semilla que quiera
    print(mi_asignacion(NUMERO))
    patrones, problema = calibracion(NUMERO)
    serie = cinetica(NUMERO)
    tabla = mi_familia(NUMERO)

Uso desde la terminal
---------------------
    python generar_datos.py 7       # escribe los CSV en datos_07/
"""

from __future__ import annotations

import os
import sys

import numpy as np
import pandas as pd

AQUI = os.path.dirname(os.path.abspath(__file__))
RUTA_FAMILIAS = os.path.join(AQUI, "compuestos_familias.csv")
URL_FAMILIAS = (
    "https://raw.githubusercontent.com/pesco13/Python-para-Quimica/"
    "main/datos/compuestos_familias.csv"
)

# Analitos que se pueden medir por absorcion UV-Vis, con su longitud de onda
# de trabajo y su absortividad molar aproximada. Son valores didacticos.
ANALITOS = [
    ("Azul de metileno", 664, 74000.0),
    ("Permanganato de potasio", 525, 2400.0),
    ("Dicromato de potasio", 350, 3160.0),
    ("Complejo Fe(II)-fenantrolina", 510, 11100.0),
    ("Rojo de metilo", 520, 23400.0),
    ("Anaranjado de metilo", 464, 27000.0),
    ("Complejo Cu(II)-amoníaco", 610, 50.0),
    ("Nitrato de cobalto(II)", 510, 4.8),
    ("Verde de bromocresol", 616, 36000.0),
    ("Cromato de potasio", 372, 4800.0),
]

# Reacciones de seguimiento cinetico, con el orden real que hay que
# descubrir a partir de los datos y una energia de activacion de referencia
# en kJ/mol. Ninguno de los dos valores aparece en los CSV generados.
REACCIONES = [
    ("Descomposición del peróxido de hidrógeno", 1, 75.0),
    ("Hidrólisis del acetato de etilo en medio básico", 2, 47.0),
    ("Decoloración del cristal violeta con NaOH", 1, 58.0),
    ("Reacción del tiosulfato con ácido", 1, 65.0),
    ("Dimerización del ciclopentadieno", 2, 69.0),
    ("Hidrólisis de la sacarosa", 1, 108.0),
    ("Yodación de la acetona", 1, 82.0),
    ("Descomposición del pentóxido de dinitrógeno", 1, 103.0),
    ("Saponificación del acetato de fenilo", 2, 52.0),
    ("Oxidación del yoduro por persulfato", 2, 56.0),
]

R_GAS = 8.314462618e-3  # kJ / (mol K)


def _generador(numero: int, bloque: int) -> np.random.Generator:
    """Un generador distinto por semilla y por tipo de dato."""
    if not isinstance(numero, (int, np.integer)) or numero < 1:
        raise ValueError("La semilla debe ser un entero mayor o igual a 1.")
    return np.random.default_rng(1000 * bloque + int(numero))


def mi_asignacion(numero: int) -> dict:
    """Devuelve que familia de compuestos, que analito y que reaccion corresponden a la semilla."""
    tabla = cargar_familias()
    familias = sorted(tabla["familia"].unique())
    analito, lam, eps = ANALITOS[(numero - 1) % len(ANALITOS)]
    reaccion, orden, ea = REACCIONES[(numero - 1) % len(REACCIONES)]
    return {
        "numero": numero,
        "familia": familias[(numero - 1) % len(familias)],
        "analito": analito,
        "longitud_de_onda_nm": lam,
        "reaccion": reaccion,
    }


def cargar_familias() -> pd.DataFrame:
    """Lee compuestos_familias.csv del disco o, si no esta, desde GitHub."""
    if os.path.exists(RUTA_FAMILIAS):
        return pd.read_csv(RUTA_FAMILIAS)
    return pd.read_csv(URL_FAMILIAS)


def mi_familia(numero: int) -> pd.DataFrame:
    """Los seis compuestos de la familia que corresponde a la semilla."""
    tabla = cargar_familias()
    familias = sorted(tabla["familia"].unique())
    elegida = familias[(numero - 1) % len(familias)]
    return tabla[tabla["familia"] == elegida].reset_index(drop=True)


def calibracion(numero: int):
    """Curva de calibracion UV-Vis y muestra problema.

    Devuelve dos DataFrames:
      patrones: concentracion (mg/L) y absorbancia, seis niveles por triplicado.
      problema: tres replicas de la absorbancia de la muestra desconocida.

    Los datos llevan una pequena desviacion del cero, ruido que crece con la
    senal y un nivel alto ligeramente fuera del intervalo lineal: es lo que se
    ve en un espectrofotometro real.
    """
    rng = _generador(numero, 1)
    analito, lam, _ = ANALITOS[(numero - 1) % len(ANALITOS)]

    niveles = np.array([0.0, 2.0, 4.0, 6.0, 8.0, 10.0])
    pendiente = rng.uniform(0.055, 0.115)      # unidades de A por (mg/L)
    intercepto = rng.normal(0.004, 0.006)      # pequeno sesgo del blanco
    curvatura = rng.uniform(0.0004, 0.0012)    # desviacion de la ley de Beer

    conc, absor = [], []
    for c in niveles:
        ideal = intercepto + pendiente * c - curvatura * c**2
        sigma = 0.0025 + 0.012 * ideal         # ruido proporcional a la senal
        for _ in range(3):
            conc.append(c)
            absor.append(float(ideal + rng.normal(0.0, sigma)))
    patrones = pd.DataFrame({
        "concentracion_mg_L": conc,
        "absorbancia": np.round(absor, 4),
    })

    c_real = rng.uniform(3.0, 7.5)
    ideal = intercepto + pendiente * c_real - curvatura * c_real**2
    problema = pd.DataFrame({
        "replica": [1, 2, 3],
        "absorbancia": np.round(ideal + rng.normal(0.0, 0.0035, 3), 4),
    })

    patrones.attrs["analito"] = analito
    patrones.attrs["longitud_de_onda_nm"] = lam
    problema.attrs["analito"] = analito
    return patrones, problema


def cinetica(numero: int) -> pd.DataFrame:
    """Seguimiento de la concentracion frente al tiempo a tres temperaturas.

    Devuelve un DataFrame con columnas temperatura_C, tiempo_min y
    concentracion_M. El orden de reaccion y la energia de activacion no se
    revelan: son justamente lo que hay que determinar.
    """
    rng = _generador(numero, 2)
    _, orden, ea = REACCIONES[(numero - 1) % len(REACCIONES)]

    c0 = rng.uniform(0.040, 0.120)
    t_ref = 298.15
    k_ref = rng.uniform(0.012, 0.045) if orden == 1 else rng.uniform(0.6, 2.4)
    temperaturas = [25.0, 35.0, 45.0, 55.0]

    filas = []
    for t_c in temperaturas:
        t_k = t_c + 273.15
        k = k_ref * np.exp(-ea / R_GAS * (1.0 / t_k - 1.0 / t_ref))
        # Cada corrida se sigue hasta un 90 % de conversion: a mayor
        # temperatura se muestrea durante menos tiempo, como en el laboratorio.
        t_max = np.log(10.0) / k if orden == 1 else 9.0 / (k * c0)
        tiempos = np.round(np.linspace(0.0, t_max, 12), 2)
        if orden == 1:
            ideal = c0 * np.exp(-k * tiempos)
        else:
            ideal = c0 / (1.0 + k * c0 * tiempos)
        ruido = rng.normal(0.0, 0.002 * c0 + 0.015 * ideal)
        filas.append(pd.DataFrame({
            "temperatura_C": t_c,
            "tiempo_min": tiempos,
            "concentracion_M": np.round(np.maximum(ideal + ruido, 1e-4), 5),
        }))
    return pd.concat(filas, ignore_index=True)


def guardar(numero: int, carpeta: str | None = None) -> str:
    """Escribe los CSV de esa semilla y devuelve la carpeta creada."""
    carpeta = carpeta or f"datos_{numero:02d}"
    os.makedirs(carpeta, exist_ok=True)
    patrones, problema = calibracion(numero)
    patrones.to_csv(os.path.join(carpeta, "calibracion_patrones.csv"), index=False)
    problema.to_csv(os.path.join(carpeta, "calibracion_problema.csv"), index=False)
    cinetica(numero).to_csv(os.path.join(carpeta, "cinetica.csv"), index=False)
    mi_familia(numero).to_csv(os.path.join(carpeta, "mi_familia.csv"), index=False)
    return carpeta


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Uso: python generar_datos.py SEMILLA")
    n = int(sys.argv[1])
    print(mi_asignacion(n))
    print("Datos escritos en:", guardar(n))
