---
title: "02 · Tablas de datos con pandas"
sidebar_label: "02 · Tablas con pandas"
description: "Cómo organiza pandas una tabla, su equivalencia con Excel y cómo leer archivos CSV guardados en español."
sidebar_position: 3
slug: 02-tablas-con-pandas
---

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pesco13/Python-para-Quimica/blob/main/notebooks/02_Tablas_con_pandas.ipynb)

El código de esta práctica está en Colab. Esta página explica la teoría que la acompaña, reúne los errores más frecuentes y propone retos para después de clase.

## Conceptos

### Las piezas de una tabla en pandas

| Pieza | Qué es | Ejemplo en el curso |
|---|---|---|
| `DataFrame` | La tabla completa | `df` con los 25 compuestos |
| `Series` | Una columna (o una fila) | `df["smiles"]` |
| Índice | La etiqueta de cada fila (por defecto 0, 1, 2…) | La columna gris de la izquierda |
| `dtype` | El tipo de dato de cada columna | `object` (texto), `float64`, `int64` |

Los tipos se revisan con `df.dtypes`. Si una columna de números aparece como `object`, pandas la está tratando como texto y no podrá hacer cálculos con ella.

### Datos ordenados

pandas trabaja mejor cuando cada fila es una observación (un compuesto, una muestra, una medición), cada columna es una variable (nombre, categoría, masa molar) y cada celda tiene un solo valor.

Las tablas de laboratorio suelen romper estas reglas con celdas combinadas, unidades pegadas al número (`"25 °C"`) o varias mediciones en una misma celda. Vale la pena ordenarlas antes de analizarlas.

### De Excel a pandas

| En Excel | En pandas |
|---|---|
| Filtro automático | `df[df["categoria"] == "Solvente"]` |
| Ordenar de mayor a menor | `df.sort_values("columna", ascending=False)` |
| Columna con fórmula | `df["nueva"] = df["a"] / df["b"]` |
| `CONTAR.SI` | `df["categoria"].value_counts()` |
| `PROMEDIO.SI` / tabla dinámica | `df.groupby("categoria")["columna"].mean()` |
| `BUSCARV` | `pd.merge(tabla1, tabla2, on="nombre")` |

La diferencia más grande es que en pandas cada paso queda escrito. Si llegan datos nuevos, basta con volver a ejecutar el notebook.

### Archivos CSV guardados en español

Un CSV es texto plano, con una fila por línea y las columnas separadas por un carácter. Excel configurado en español suele guardarlos con punto y coma como separador y coma decimal:

```text
nombre;densidad
Etanol;0,789
Acetona;0,784
```

Para leerlos bien hay que indicarlo:

```python
df = pd.read_csv("mis_datos.csv", sep=";", decimal=",", encoding="utf-8")
```

Si las tildes aparecen como símbolos raros (`Ã¡`), pruebe con `encoding="latin-1"`.

### ¿Qué gráfico usar?

| Quiero mostrar… | Gráfico | En pandas |
|---|---|---|
| Cantidades por categoría | Barras | `kind="bar"` o `"barh"` |
| La relación entre dos variables numéricas | Dispersión | `kind="scatter", x=..., y=...` |
| Cómo cambia algo con el tiempo o la temperatura | Líneas | `kind="line"` |
| Cómo se reparten los valores | Histograma | `kind="hist"` |

Todo gráfico científico necesita nombres en los ejes, con sus unidades.

## Errores comunes

### `KeyError: 'Categoria'`

El nombre de la columna no coincide exactamente: cambian una mayúscula, una tilde o un espacio. Imprima `df.columns.tolist()` y copie el nombre tal como aparece.

### Toda la tabla quedó en una sola columna

El archivo usa `;` como separador y pandas esperaba `,`. Léalo con `pd.read_csv(..., sep=";")`.

### Los números no se pueden sumar ni promediar

La columna se leyó como texto, casi siempre por la coma decimal. Use `pd.read_csv(..., decimal=",")` o convierta la columna con `pd.to_numeric(df["col"].str.replace(",", "."))`.

### `ValueError: The truth value of a Series is ambiguous`

Se unieron dos condiciones con `and` u `or`. En pandas se usan `&` (y) y `|` (o), con cada condición entre paréntesis:
`df[(df["categoria"] == "Fármaco") & (df["largo_smiles"] > 20)]`.

### `HTTPError: HTTP Error 404: Not Found`

La dirección del CSV está mal escrita o el archivo cambió de lugar. Abra la URL en el navegador para comprobar que muestra el archivo.

## Retos adicionales

1. Construya una tabla propia con cinco solventes del laboratorio y su punto de ebullición (consúltelos en una fuente confiable). Guárdela como CSV, léala de nuevo y ordénela de menor a mayor punto de ebullición.
2. Muestre en una sola tabla los compuestos que son conservantes o aromas.
3. Use `df["smiles"].str.contains("N")` para contar cuántos compuestos de cada categoría contienen nitrógeno. ¿Qué problema tiene buscar la letra `N` en un SMILES? (Pista: piense en el sodio.)
4. Haga un gráfico de barras horizontales del `largo_smiles` promedio por categoría, ordenado de mayor a menor, con título y nombres en los ejes.

## Glosario

| Término | Significado |
|---|---|
| DataFrame | Tabla de pandas, con filas y columnas |
| Series | Una sola columna (o fila) de un DataFrame |
| Índice | Etiqueta que identifica cada fila |
| CSV | Archivo de texto con valores separados por comas (o por punto y coma) |
| Filtro | Condición que deja solo las filas donde se cumple |
| `groupby` | Agrupa las filas según una columna para resumirlas |

## Para saber más

- [10 minutos con pandas](https://pandas.pydata.org/docs/user_guide/10min.html), guía oficial (en inglés)
- [Comparación entre pandas y las hojas de cálculo](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spreadsheets.html) (en inglés)
- [Tutoriales de Matplotlib](https://matplotlib.org/stable/tutorials/index.html) (en inglés)
- Wickham, H. (2014). Tidy data. *Journal of Statistical Software*, 59(10), 1–23.
