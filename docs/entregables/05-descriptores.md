---
title: "Sesión 05 · Descriptores moleculares"
sidebar_label: "05 · Descriptores con RDKit"
description: "Descriptores de doce compuestos propios, regla de Lipinski e interpretación química de los valores."
sidebar_position: 6
slug: descriptores
---

# Sesión 05 · Descriptores moleculares

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pesco13/Python-para-Quimica/blob/main/notebooks/03_Moleculas_con_RDKit.ipynb)

**Objetivo.** Calcular los descriptores de los doce compuestos de su familia e interpretar qué dicen sobre su comportamiento físico, no solo producir la tabla.

**Duración.** 2 horas.

| Tiempo | Qué se hace |
|---|---|
| 0:00 – 0:35 | SMILES, InChIKey y cómo lee RDKit una molécula ([práctica 03](../practicas/03-moleculas-con-rdkit.md)) |
| 0:35 – 1:05 | Descriptores: log P, TPSA, donadores y aceptores; regla de Lipinski y sus límites |
| 1:05 – 1:15 | Pausa |
| 1:15 – 1:50 | Construcción del entregable |
| 1:50 – 2:00 | Verificación y entrega |

## Antes de la sesión

- Tenga a mano su archivo `mi_familia_ampliada.csv` de la sesión 2.
- Lea en la [práctica 03](../practicas/03-moleculas-con-rdkit.md) qué mide cada descriptor.

## Paso a paso del entregable

1. Cargue su tabla de doce compuestos y conviértalos todos en objetos de RDKit. Verifique con un `assert` que ninguno quedó en `None`.
2. Calcule para cada uno: masa molar, log P, TPSA, donadores y aceptores de puente de hidrógeno, y número de enlaces rotables.
3. Añada el InChIKey de cada compuesto. Explique en una frase para qué sirve el primer bloque de catorce letras.
4. Aplique la regla de Lipinski y añada una columna booleana con el resultado. Cuente cuántos la cumplen.
5. Ordene la tabla por log P y haga una figura de barras con los doce compuestos. Marque de otro color los que no cumplen Lipinski.
6. Elija los **dos compuestos más parecidos estructuralmente** de su familia y explique, con la estructura en la mano, por qué sus log P difieren en lo que difieren.
7. Dibuje la cuadrícula con las doce estructuras y guárdela como imagen.
8. Escriba cuatro frases: qué tipo de compuestos son los de su familia según los descriptores, cuál esperaría que fuera más soluble en agua, cuál tendería a acumularse en tejido graso y por qué.
9. Guarde la tabla con descriptores como `descriptores_mi_familia.csv` y añada la declaración de uso de IA.

## Criterios de aceptación

- [ ] La tabla tiene doce filas y las seis columnas de descriptores, sin valores vacíos.
- [ ] Hay un `assert` que comprueba que todos los SMILES se leyeron bien.
- [ ] La figura distingue visualmente los compuestos que cumplen Lipinski de los que no.
- [ ] Está la comparación razonada entre los dos compuestos más parecidos.
- [ ] Están las cuatro frases de interpretación química.

## Entrega

Archivo `S05_Apellido_Nombre.ipynb`, `descriptores_mi_familia.csv` y la imagen de la cuadrícula.

## Errores que van a aparecer

**`AttributeError: 'NoneType' object has no attribute 'GetNumAtoms'`** · Uno de sus SMILES no se pudo leer y RDKit devolvió `None`. Encuentre cuál recorriendo la lista e imprimiendo los que fallan.

**`Explicit valence for atom # 1 N, 4, is greater than permitted`** · Un nitrógeno con cuatro enlaces necesita carga: escriba `[N+]`.

**El log P del compuesto iónico sale raro** · Los descriptores de RDKit están pensados para moléculas neutras. Las sales con punto en el SMILES se tratan como dos fragmentos; dígalo en la interpretación.

**La cuadrícula no se dibuja** · Falta importar `Draw` o falta la última línea sin `print` que devuelve el objeto para que Colab lo muestre.

