"""
Comprobaciones de calidad para un trabajo de quimica hecho en Python.

No corrige el contenido cientifico: verifica las cosas mecanicas que se
olvidan y que invalidan un resultado o hacen ilegible una figura. Pensado
para correrse al final de un notebook, antes de dar el trabajo por terminado.

    !wget -q https://raw.githubusercontent.com/pesco13/Python-para-Quimica/main/herramientas/revisar.py
    from revisar import Informe

    inf = Informe()
    inf.tabla(df, filas=12, columnas=["nombre", "smiles"])
    inf.figura(fig)
    inf.archivo("calibracion.png", dpi_minimo=300)
    inf.resultado(4.312, 0.34, "mg/L")
    inf.residuales(x, y - prediccion)
    inf.resumen()

Cada comprobacion devuelve True o False y deja constancia en el informe.
Los avisos no cuentan como fallo: son cosas que conviene mirar.
"""

from __future__ import annotations

import math
import os
import re
import unicodedata

OK, AVISO, FALLO = "ok", "aviso", "fallo"

_SIMBOLOS = {OK: "\u2713", AVISO: "!", FALLO: "\u2717"}

# Pistas de que una etiqueta de eje lleva unidad: parentesis, corchetes,
# una barra de division o notacion matematica de LaTeX.
_PISTA_UNIDAD = re.compile(r"[\(\[].+[\)\]]|/|\$")

# Magnitudes que no llevan unidad y por tanto no deben dar aviso.
_SIN_UNIDAD = ("absorbancia", "ph", "r2", "r²", "transmitancia", "pka",
               "componente", "cuenta", "frecuencia", "ln k", "indice",
               "similitud", "tanimoto", "fraccion", "fracción")


def _sin_tildes(texto: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", texto)
                   if not unicodedata.combining(c))


class Informe:
    """Acumula comprobaciones y las resume al final."""

    def __init__(self):
        self.lineas = []

    # -- registro interno ------------------------------------------------
    def _anota(self, estado, texto):
        self.lineas.append((estado, texto))
        return estado != FALLO

    # -- comprobaciones --------------------------------------------------
    def tabla(self, df, filas=None, filas_minimas=None, columnas=None,
              sin_vacios=True):
        """Comprueba el tamano, las columnas y los huecos de un DataFrame."""
        bien = True
        n = len(df)
        if filas is not None:
            bien &= self._anota(OK if n == filas else FALLO,
                                f"La tabla tiene {n} filas (se esperaban {filas})")
        elif filas_minimas is not None:
            bien &= self._anota(OK if n >= filas_minimas else FALLO,
                                f"La tabla tiene {n} filas (minimo {filas_minimas})")
        else:
            self._anota(OK, f"La tabla tiene {n} filas")

        if columnas:
            faltan = [c for c in columnas if c not in df.columns]
            bien &= self._anota(OK if not faltan else FALLO,
                                "Estan todas las columnas pedidas" if not faltan
                                else f"Faltan columnas: {', '.join(faltan)}")
        if sin_vacios:
            huecos = int(df.isna().sum().sum())
            bien &= self._anota(OK if huecos == 0 else FALLO,
                                "No hay celdas vacias" if huecos == 0
                                else f"Hay {huecos} celdas vacias")
        return bien

    def figura(self, fig):
        """Comprueba que los ejes de una figura se puedan leer."""
        bien = True
        ejes = [a for a in fig.axes if a.get_visible()]
        if not ejes:
            return self._anota(FALLO, "La figura no tiene ningun eje")

        for i, ax in enumerate(ejes):
            etq = f"panel {i + 1}: " if len(ejes) > 1 else ""
            for nombre, texto in (("x", ax.get_xlabel()), ("y", ax.get_ylabel())):
                if not texto.strip():
                    bien &= self._anota(FALLO, f"{etq}el eje {nombre} no tiene etiqueta")
                elif (not _PISTA_UNIDAD.search(texto)
                      and not any(p in _sin_tildes(texto).lower() for p in _SIN_UNIDAD)):
                    self._anota(AVISO, f"{etq}la etiqueta del eje {nombre} "
                                       f"parece no llevar unidad: \"{texto}\"")
                else:
                    self._anota(OK, f"{etq}el eje {nombre} esta etiquetado")

            series = len(ax.lines) + len(ax.collections) + len(ax.containers)
            if series > 1 and ax.get_legend() is None:
                self._anota(AVISO, f"{etq}hay {series} series y ninguna leyenda")

        titulos = [a.get_title().strip() for a in ejes]
        tiene = any(titulos) or bool(getattr(fig, "_suptitle", None)
                                     and fig._suptitle.get_text().strip())
        if not tiene:
            self._anota(AVISO, "La figura no tiene titulo")
        return bien

    def archivo(self, ruta, dpi_minimo=None, tamano_minimo_kb=None):
        """Comprueba que un archivo existe, su nombre y, si es imagen, su resolucion."""
        if not os.path.exists(ruta):
            return self._anota(FALLO, f"No existe el archivo {ruta}")
        bien = self._anota(OK, f"Existe {ruta}")

        nombre = os.path.basename(ruta)
        if " " in nombre or _sin_tildes(nombre) != nombre:
            self._anota(AVISO, f"El nombre \"{nombre}\" tiene espacios o tildes; "
                               f"eso da problemas al compartirlo")

        if tamano_minimo_kb:
            kb = os.path.getsize(ruta) / 1024
            bien &= self._anota(OK if kb >= tamano_minimo_kb else FALLO,
                                f"{nombre} ocupa {kb:.0f} kB "
                                f"(minimo {tamano_minimo_kb} kB)")

        if dpi_minimo and ruta.lower().endswith((".png", ".tif", ".tiff", ".jpg")):
            try:
                from PIL import Image
                dpi = Image.open(ruta).info.get("dpi")
                valor = round(min(dpi)) if dpi else None
            except Exception:
                valor = None
            if valor is None:
                self._anota(AVISO, f"{nombre} no guarda su resolucion; "
                                   f"anada dpi=300 en savefig")
            else:
                bien &= self._anota(OK if valor >= dpi_minimo else FALLO,
                                    f"{nombre} esta a {valor} dpi "
                                    f"(minimo {dpi_minimo})")
        return bien

    def resultado(self, valor, incertidumbre, unidad=""):
        """Comprueba que el valor y su incertidumbre tengan cifras coherentes."""
        if incertidumbre is None or incertidumbre <= 0:
            return self._anota(FALLO, "La incertidumbre debe ser un numero positivo")
        if valor is not None and incertidumbre > abs(valor):
            self._anota(AVISO, "La incertidumbre es mayor que el valor: "
                               "el resultado no distingue nada")

        # La incertidumbre se redondea a una cifra significativa, salvo que
        # empiece por 1 o 2: entonces la convencion es conservar dos.
        exponente = int(math.floor(math.log10(incertidumbre)))
        primera = int(incertidumbre / 10 ** exponente)
        decimales = max(0, -exponente + (1 if primera <= 2 else 0))
        bonito = f"{valor:.{decimales}f} \u00b1 {incertidumbre:.{decimales}f}"
        if unidad:
            bonito += f" {unidad}"
        self._anota(OK, f"Reporte el resultado asi: {bonito}")
        return True

    def residuales(self, x, residuales, alfa=0.05):
        """Avisa si los residuales tienen estructura en vez de repartirse al azar.

        Usa la prueba de rachas de Wald-Wolfowitz sobre el signo de los
        residuales ordenados por x. Pocas rachas significa que el modelo se
        desvia de forma sistematica: curvatura, por ejemplo.
        """
        import numpy as np

        x = np.asarray(x, dtype=float)
        r = np.asarray(residuales, dtype=float)
        orden = np.argsort(x)
        signos = np.sign(r[orden])
        signos = signos[signos != 0]
        n = signos.size
        if n < 8:
            return self._anota(AVISO, "Hay muy pocos puntos para juzgar los residuales")

        n1 = int((signos > 0).sum())
        n2 = n - n1
        if n1 == 0 or n2 == 0:
            return self._anota(FALLO, "Todos los residuales tienen el mismo signo: "
                                      "el modelo esta sesgado")
        rachas = 1 + int((signos[1:] != signos[:-1]).sum())
        media = 2 * n1 * n2 / n + 1
        var = 2 * n1 * n2 * (2 * n1 * n2 - n) / (n ** 2 * (n - 1))
        if var <= 0:
            return self._anota(AVISO, "No se puede evaluar la estructura de los residuales")
        z = (rachas - media) / math.sqrt(var)
        if z < -1.96:
            return self._anota(AVISO,
                               f"Los residuales tienen estructura ({rachas} rachas frente "
                               f"a {media:.1f} esperadas): el modelo puede no ser el correcto")
        return self._anota(OK, f"Los residuales se reparten al azar "
                               f"({rachas} rachas, {media:.1f} esperadas)")

    def columna_calculada(self, df, columna, minimo=None, maximo=None):
        """Comprueba que una columna sea numerica y caiga en un intervalo sensato."""
        from pandas.api.types import is_numeric_dtype

        if columna not in df.columns:
            return self._anota(FALLO, f"No existe la columna {columna}")
        serie = df[columna]
        if not is_numeric_dtype(serie):
            return self._anota(FALLO, f"La columna {columna} no es numerica: "
                                      f"revise si quedo como texto")
        bien = self._anota(OK, f"{columna} es numerica")
        if minimo is not None and serie.min() < minimo:
            bien &= self._anota(FALLO, f"{columna} baja hasta {serie.min():.3g}, "
                                       f"por debajo de {minimo}")
        if maximo is not None and serie.max() > maximo:
            bien &= self._anota(FALLO, f"{columna} sube hasta {serie.max():.3g}, "
                                       f"por encima de {maximo}")
        return bien

    # -- salida ----------------------------------------------------------
    def resumen(self, mostrar=True):
        """Imprime el informe y devuelve el recuento por estado."""
        cuenta = {OK: 0, AVISO: 0, FALLO: 0}
        for estado, _ in self.lineas:
            cuenta[estado] += 1
        if mostrar:
            for estado, texto in self.lineas:
                print(f" {_SIMBOLOS[estado]}  {texto}")
            print("-" * 62)
            if cuenta[FALLO]:
                print(f"{cuenta[FALLO]} fallo(s), {cuenta[AVISO]} aviso(s). "
                      f"Corrija los fallos antes de entregar.")
            elif cuenta[AVISO]:
                print(f"Sin fallos, {cuenta[AVISO]} aviso(s). "
                      f"Mire los avisos: no bloquean, pero casi siempre valen la pena.")
            else:
                print("Todo en orden.")
        return cuenta

    @property
    def hay_fallos(self):
        return any(e == FALLO for e, _ in self.lineas)
