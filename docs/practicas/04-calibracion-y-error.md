---
title: "04 · Curva de calibración y error experimental"
sidebar_label: "04 · Calibración y error"
description: "Ley de Beer, mínimos cuadrados, residuales, incertidumbre del resultado, t de Student, LOD y LOQ."
sidebar_position: 5
slug: 04-calibracion-y-error
---

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pesco13/Python-para-Quimica/blob/main/notebooks/04_Calibracion_y_error.ipynb)

El código de esta práctica está en Colab. Esta página explica la teoría que la acompaña, reúne los errores más frecuentes y propone retos para después de clase.

## Conceptos

### Cómo llegan los datos a su notebook

El archivo `generar_datos.py` **no contiene los datos**: contiene la receta que los construye a partir de un número que actúa de semilla. Por eso ocupa 8 kB en vez de treinta tablas y por eso la misma semilla da siempre los mismos valores.

Hay tres formas de llegar a ellos, según lo que quiera hacer.

**Llamar a las funciones.** Devuelven objetos `DataFrame` de pandas, listos para trabajar:

```python
from generar_datos import calibracion, cinetica, mi_familia

patrones, problema = calibracion(7)   # 18 filas × 2 columnas; 3 × 2
serie = cinetica(7)                   # 48 × 3
tabla = mi_familia(7)                 # 6 × 4
```

**Guardarlos como archivo**, si los necesita fuera de Python, por ejemplo para abrirlos en una hoja de cálculo:

```python
from generar_datos import guardar
guardar(7)      # crea la carpeta datos_07/ con cuatro CSV
```

o, sobre cualquier tabla que ya tenga en memoria, `patrones.to_csv("mis_patrones.csv", index=False)`.

**Leer las tablas de compuestos directamente.** Esas sí son archivos CSV publicados en el sitio, porque son datos reales y los mismos para todos:

```python
import pandas as pd
S = "https://pesco13.github.io/Python-para-Quimica/datos"
compuestos = pd.read_csv(f"{S}/compuestos_familias.csv")   # 150 × 4
```

### Mirar una tabla antes de usarla

Antes de calcular nada conviene responder cuatro preguntas. Son una línea cada una:

| Pregunta | Cómo se responde | Qué revela |
|---|---|---|
| ¿Cuántos datos hay? | `df.shape` | Devuelve (filas, columnas) |
| ¿Cómo se llaman las columnas? | `df.columns.tolist()` | Los nombres exactos, con sus mayúsculas |
| ¿De qué tipo es cada una? | `df.dtypes` | `float64` o `int64` son números; `object` es texto |
| ¿Qué valores toman? | `df.head()` y `df.describe()` | Las primeras filas; y cuenta, media, desviación, mínimo, máximo y cuartiles |

La tercera es la que más errores evita. Una columna de números que aparece como `object` llegó como texto —por una coma decimal, un espacio o un guion— y cualquier promedio sobre ella fallará o, peor, concatenará cadenas en vez de sumar. `pd.to_numeric(df["columna"], errors="coerce")` la convierte y deja como vacíos los valores que no pueda interpretar.

### La ley de Beer–Lambert y sus límites

Para una disolución diluida, la absorbancia es proporcional a la concentración:

$$A = \varepsilon\,\ell\,c$$

con $\varepsilon$ la absortividad molar, $\ell$ el paso óptico y $c$ la concentración. La proporcionalidad se rompe por encima de una absorbancia de aproximadamente 1: las moléculas empiezan a interaccionar entre sí, la luz dispersada deja de ser despreciable y la respuesta se curva hacia abajo. Por eso una calibración no se extiende indefinidamente: tiene un **intervalo lineal** que hay que determinar.

### Qué significa cada número de un ajuste lineal

| Número | Qué es | Qué le dice |
|---|---|---|
| Pendiente $m$ | Cambio de señal por unidad de concentración | La sensibilidad del método |
| Intercepto $b$ | Señal a concentración cero | El sesgo del blanco; debería ser pequeño |
| $s_m$, $s_b$ | Incertidumbre de ambos | Cuánto se moverían si repitiera la calibración |
| $s_{y/x}$ | Dispersión de los puntos alrededor de la recta | El ruido del método |
| $R^2$ | Fracción de la variación explicada | Mucho menos de lo que la gente cree |

### Por qué el R² no basta

El $R^2$ compara la variación explicada con la variación total. En una calibración la variación total es enorme, porque el intervalo de concentraciones es ancho a propósito. Eso hace que casi cualquier modelo dé un $R^2$ alto, incluso uno que se curva de forma sistemática.

El diagnóstico correcto es la gráfica de **residuales**, que muestra $y_i - \hat{y}_i$ frente a la concentración:

| Lo que ve | Lo que significa |
|---|---|
| Nube sin forma alrededor del cero | El modelo lineal describe los datos |
| Curva o U | Falta curvatura: el intervalo lineal se quedó corto |
| Embudo que se abre | La dispersión crece con la señal: conviene un ajuste ponderado |
| Un punto muy alejado | Posible error de medida; investíguelo antes de quitarlo |

### La incertidumbre del resultado

La concentración de la muestra se obtiene despejando, pero su incertidumbre no es la de las réplicas de la muestra: hereda también la de la calibración.

$$s_{c_0} = \frac{s_{y/x}}{m}\sqrt{\frac{1}{M} + \frac{1}{n} + \frac{(\bar{A}_0-\bar{y})^2}{m^2 S_{xx}}}$$

El tercer término crece cuando la muestra cae lejos del centro de la calibración. De ahí una regla práctica del laboratorio: **diluya la muestra hasta que su señal caiga en la mitad del intervalo calibrado**.

Para pasar de desviación estándar a intervalo de confianza del 95 % hay que multiplicar por el valor $t$ de Student con $n-2$ grados de libertad. Con pocos datos ese valor es claramente mayor que 1,96: usar 1,96 subestima la incertidumbre.

### Límite de detección y de cuantificación

$$\text{LOD} = \frac{3 s}{m} \qquad \text{LOQ} = \frac{10 s}{m}$$

donde $s$ es la desviación del blanco o, a falta de suficientes blancos, $s_{y/x}$. El LOD es la concentración que se distingue del ruido; el LOQ, la mínima que se puede medir con precisión aceptable. Un resultado por debajo del LOQ se reporta como "menor que el LOQ", no con un número.

### Cifras significativas

La incertidumbre se redondea a una o dos cifras significativas y el resultado se da con el mismo último decimal. Escribir `4,3127 ± 0,34` es un error: lo correcto es `4,31 ± 0,34`.

## Errores comunes

### La concentración sale negativa

Revise el despeje. Es la absorbancia menos el intercepto, dividido entre la pendiente; invertirlo da un valor sin sentido.

### El intervalo de confianza sale minúsculo

Usó la desviación de las tres réplicas de la muestra en lugar de la desviación residual del ajuste. La incertidumbre de la calibración suele dominar.

### `linregress` devuelve `nan`

Hay valores faltantes en los datos, o todos los valores de x son iguales. Imprima los arreglos antes de ajustar.

### El `stderr` del intercepto no aparece

En versiones antiguas de SciPy el resultado de `linregress` no traía `intercept_stderr`. Actualice SciPy o calcúlelo a mano.

### Se usó 1,96 en lugar del t de Student

Con 18 medidas y 16 grados de libertad el valor correcto está cerca de 2,12, un 8 % mayor. Con menos puntos la diferencia crece rápido.

## Retos adicionales

1. Simule una calibración con ruido proporcional a la señal y ajústela de dos formas, con mínimos cuadrados normales y ponderados. ¿Cambia la concentración calculada de una muestra diluida?
2. Calcule el intervalo de confianza de la **recta** completa, no solo de un punto y dibújelo como una banda alrededor del ajuste.
3. Tome su calibración y quite un punto cada vez, rehaciendo el ajuste. ¿Hay algún punto que cambie el resultado mucho más que los demás?
4. Busque en la literatura el criterio del LOD basado en la regresión de la IUPAC y compárelo con el de 3s/m.

## Glosario

| Término | Significado |
|---|---|
| Patrón | Disolución de concentración conocida usada para calibrar |
| Blanco | Medida sin analito, que da la señal de fondo |
| Residual | Diferencia entre el valor medido y el que predice el modelo |
| $s_{y/x}$ | Desviación estándar de los puntos respecto a la recta |
| LOD / LOQ | Límite de detección / de cuantificación |
| t de Student | Factor que convierte una desviación en intervalo de confianza con pocos datos |
| Intervalo lineal | Zona de concentraciones donde la respuesta es proporcional |

## Para saber más

- Miller, J. N., Miller, J. C. (2018). *Statistics and Chemometrics for Analytical Chemistry*, 7.ª ed., capítulo 5.
- [Documentación de `scipy.stats.linregress`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html) (en inglés)
- Currie, L. A. (1995). Nomenclature in evaluation of analytical methods including detection and quantification capabilities. *Pure Appl. Chem.*, 67, 1699–1723.

