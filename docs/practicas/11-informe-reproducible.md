---
title: "11 · El informe final reproducible"
sidebar_label: "11 · Informe reproducible"
description: "Estructura de carpetas, nombres de archivo, registro del entorno, estilo común de figuras y cómo se escribe un método."
sidebar_position: 12
slug: 11-informe-reproducible
---

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pesco13/Python-para-Quimica/blob/main/notebooks/11_Informe_reproducible.ipynb)

El código de esta práctica está en Colab. Esta página explica la teoría que la acompaña, reúne los errores más frecuentes y propone retos para después de clase.

## Conceptos

### Tres niveles de confianza en un resultado

| Nivel | Quién lo repite | Qué hace falta |
|---|---|---|
| Repetible | Usted, en su máquina | El notebook y los datos guardados |
| Reproducible | Otra persona, con sus datos y su código | Además: datos accesibles, versiones anotadas, orden de ejecución claro |
| Replicable | Otra persona, desde cero | Además: el método descrito con suficiente detalle |

El objetivo razonable para un trabajo de curso es el nivel intermedio. Los dos obstáculos habituales son el notebook que solo funciona si se ejecutan las celdas en un orden que solo su autor conoce y el archivo de datos que estaba en el escritorio de un computador concreto.

### La estructura de carpetas

```
mi_informe/
├── datos/              entradas, nunca se modifican
├── resultados/         todo lo que produce el código
│   └── figuras/
├── informe.ipynb       va de datos/ a resultados/
└── README.md           qué es esto y cómo se corre
```

La regla que sostiene todo: **los datos de entrada no se tocan**. Si hay que corregir algo, lo corrige el código y escribe el resultado en `resultados/`. Así siempre se puede volver al punto de partida y la corrección queda documentada en el propio código en vez de en la memoria de alguien.

### Nombres de archivo

| Regla | Por qué |
|---|---|
| Sin espacios ni tildes | Los espacios rompen comandos y las tildes se corrompen entre sistemas |
| Número delante cuando el orden importa | `fig01`, `fig02` se ordenan solos |
| Fechas como 2026-03-15 | Ordenadas alfabéticamente quedan en orden cronológico |
| Minúsculas y guiones bajos | Evita problemas entre Windows, macOS y Linux |

### Por qué anotar las versiones

Las bibliotecas cambian. RDKit ha cambiado la función de huellas moleculares, SciPy ha añadido campos a sus resultados, pandas ha cambiado el comportamiento por defecto de varias operaciones. Un resultado que no dice con qué versión se obtuvo no se puede defender dentro de dos años, porque no se podrá distinguir un error de un cambio de la herramienta.

Un archivo `entorno.txt` con la fecha, la versión de Python y la de cada biblioteca cuesta una celda y resuelve el problema.

### Cómo se escribe una sección de métodos

Cuatro preguntas, en este orden: **qué datos**, **qué se les hizo**, **con qué herramienta** y **con qué parámetros**.

> Se ajustaron los datos y se obtuvo la energía de activación.

no permite repetir nada. En cambio:

> La concentración frente al tiempo se ajustó al modelo integrado de segundo orden por mínimos cuadrados no lineales (`scipy.optimize.curve_fit`, SciPy 1.17.1), con estimación inicial de 0,08 mol L⁻¹ para la concentración inicial y 0,02 para la constante. Las incertidumbres se tomaron como la raíz de la diagonal de la matriz de covarianza.

describe las **decisiones**, no el código línea por línea. Esa es la diferencia.

### Un estilo común para las figuras

`plt.rcParams` fija los valores por defecto de toda la sesión: tamaño, resolución, tipo de letra, bordes. Se escribe una vez al principio del notebook y todas las figuras lo heredan. Es la diferencia entre un informe y una carpeta de imágenes.

### Comprobar el trabajo con código

Revisar a mano si una figura tiene unidades, si un CSV quedó como texto o si una incertidumbre tiene demasiadas cifras es justo el tipo de tarea que conviene automatizar. El repositorio incluye [`herramientas/revisar.py`](https://github.com/pesco13/Python-para-Quimica/blob/main/herramientas/revisar.py) para eso:

```python
!wget -q https://pesco13.github.io/Python-para-Quimica/herramientas/revisar.py
from revisar import Informe

inf = Informe()
inf.tabla(df, filas_minimas=12, columnas=["nombre", "smiles"])
inf.figura(fig)
inf.archivo("fig01_calibracion.png", dpi_minimo=300)
inf.resultado(4.3127, 0.34, "mg/L")
inf.residuales(concentracion, residuales)
inf.resumen()
```

Separa **fallos**, que invalidan el resultado, de **avisos**, que no bloquean pero casi siempre valen la pena. La comprobación de residuales aplica la prueba de rachas de Wald–Wolfowitz sobre el signo de los residuales ordenados: pocas rachas significan desviación sistemática, que es lo que el R² no detecta.

## Errores comunes

### El notebook no corre tras *Reiniciar y ejecutar todo*

Hay celdas que dependen de variables definidas en otro notebook o en una celda que se borró. Todo lo que el informe necesita debe estar en el informe o cargarse desde `datos/`.

### `FileNotFoundError` en otra máquina

Usó una ruta absoluta del tipo `/content/drive/MiUnidad/...`. Use rutas relativas a la carpeta del informe.

### Las figuras no se parecen entre sí

Se generaron en sesiones distintas con estilos distintos. Regenere las principales tras aplicar `rcParams`.

### El archivo de datos cambió y ya no se sabe cómo era

Alguien editó un CSV de `datos/` a mano. Es irreversible si no hay copia. Por eso la regla de no tocar las entradas.

### Los acentos salen como símbolos raros

Falta `encoding="utf-8"` al abrir o guardar archivos de texto. Añádalo siempre.

## Retos adicionales

1. Escriba una función que recorra su carpeta de resultados y genere automáticamente la lista de figuras con su pie, en Markdown.
2. Añada al registro del entorno el *hash* de los archivos de datos, de modo que se pueda detectar si alguno cambió.
3. Convierta su informe a PDF desde Colab y revise que las figuras conserven la resolución.
4. Suba su carpeta a un repositorio de GitHub con un README y compruebe que otra persona puede ejecutarlo siguiendo solo esas instrucciones.

## Glosario

| Término | Significado |
|---|---|
| Reproducible | Que otra persona obtiene el mismo resultado con los mismos datos y código |
| `rcParams` | Diccionario de valores por defecto de matplotlib |
| Ruta relativa | Camino a un archivo desde la carpeta del proyecto, no desde la raíz del disco |
| Registro de entorno | Archivo con las versiones usadas en una ejecución |
| Pie de figura | Texto numerado que dice qué muestra la figura y con qué n |

## Para saber más

- Sandve, G. K. et al. (2013). Ten simple rules for reproducible computational research. *PLoS Comput. Biol.*, 9, e1003285.
- Rule, A. et al. (2019). Ten simple rules for writing and sharing computational analyses in Jupyter Notebooks. *PLoS Comput. Biol.*, 15, e1007007.
- [The Turing Way: guía de ciencia de datos reproducible](https://the-turing-way.netlify.app) (en inglés)

