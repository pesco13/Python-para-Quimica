---
title: "Sesión 02 · Tablas y gráficas"
sidebar_label: "02 · Tablas y gráficas"
description: "Tabla propia de doce compuestos y dos figuras con calidad de informe, a 300 dpi y con ejes etiquetados."
sidebar_position: 3
slug: tablas-y-graficas
---

# Sesión 02 · Tablas y gráficas

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pesco13/Python-para-Quimica/blob/main/notebooks/02_Tablas_con_pandas.ipynb) [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pesco13/Python-para-Quimica/blob/main/notebooks/08_Graficas_para_quimica.ipynb)

**Objetivo.** Armar una tabla propia de al menos doce compuestos y producir dos figuras con calidad de informe a partir de ella.

**Duración.** 2 horas.

| Tiempo | Qué se hace |
|---|---|
| 0:00 – 0:35 | pandas: leer, filtrar, ordenar, agrupar ([práctica 02](../practicas/02-tablas-con-pandas.md)) |
| 0:35 – 1:05 | numpy y la anatomía de una figura ([notebook 08](https://github.com/pesco13/Python-para-Quimica/blob/main/notebooks/08_Graficas_para_quimica.ipynb)) |
| 1:05 – 1:15 | Pausa |
| 1:15 – 1:50 | Construcción del entregable |
| 1:50 – 2:00 | Verificación y entrega |

## Antes de la sesión

- Consulte qué familia de compuestos le tocó en la [tabla de asignación](./00-como-funciona.md).
- Busque en PubChem **seis compuestos más** de esa misma familia, distintos de los seis que ya están en el archivo del curso, y anote su nombre y su SMILES.

## Paso a paso del entregable

1. Cargue `datos/compuestos_familias.csv` desde la URL del repositorio y quédese solo con las filas de su familia. Son seis.
2. Construya un `DataFrame` con los seis compuestos que buscó usted, con las mismas columnas: `familia`, `nombre`, `smiles`, `uso`.
3. Una las dos tablas con `pd.concat` y verifique que la tabla final tiene doce filas y ninguna celda vacía.
4. Agregue una columna calculada: el número de caracteres del SMILES (`df["smiles"].str.len()`). Es un indicador crudo del tamaño de la molécula y sirve mientras no se entra en RDKit.
5. Ordene la tabla por esa columna y guárdela como `mi_familia_ampliada.csv` con `index=False`.
6. **Figura 1:** un gráfico de barras horizontales con los doce compuestos y su tamaño de SMILES, ordenados. Eje etiquetado, título que diga la conclusión, guardado a 300 dpi.
7. **Figura 2:** la que usted decida, con una condición: debe comparar dos grupos dentro de su tabla (por ejemplo los seis originales frente a los seis que buscó, o dos subgrupos por uso). Justifique en una celda de texto por qué eligió ese tipo de gráfico.
8. En una celda de texto escriba tres frases: qué muestra cada figura y qué no se puede concluir de ellas.
9. Añada la celda de declaración de uso de IA.

## Criterios de aceptación

- [ ] La tabla final tiene doce filas y las cuatro columnas, sin valores vacíos.
- [ ] Los seis compuestos añadidos son de la familia asignada y sus SMILES se cargan sin error.
- [ ] Las dos figuras tienen ambos ejes etiquetados **con unidades** cuando corresponde.
- [ ] Las dos figuras están guardadas con `dpi=300` y aparecen los archivos en la celda de verificación.
- [ ] Están las tres frases de interpretación y la declaración de IA.

## Entrega

Archivo `S02_Apellido_Nombre.ipynb` más los dos PNG, por enlace de Drive.

## Errores que van a aparecer

**Toda la tabla quedó en una sola columna** · El CSV usa punto y coma como separador. Añada `sep=";"` a `read_csv`, o revise que copió bien la URL del archivo *raw* y no la de la página de GitHub.

**`KeyError: 'Familia'`** · Los nombres de columna distinguen mayúsculas: aquí son `familia`, `nombre`, `smiles`, `uso`.

**La figura sale vacía** · Guardó con `savefig` después de `plt.show()`. `show()` vacía la figura; guarde primero y muestre después.

**Las etiquetas del eje y se cortan** · Añada `bbox_inches="tight"` a `savefig`, o aumente el tamaño con `figsize`.

