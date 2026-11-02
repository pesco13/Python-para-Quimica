---
title: "Sesión 03 · Curva de calibración"
sidebar_label: "03 · Curva de calibración"
description: "Concentración de una muestra problema con su intervalo de confianza, residuales, LOD y LOQ."
sidebar_position: 4
slug: calibracion
---

# Sesión 03 · Curva de calibración

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pesco13/Python-para-Quimica/blob/main/notebooks/09_Calibracion_y_error.ipynb)

**Objetivo.** Determinar la concentración de una muestra problema a partir de su propia curva de calibración, con su incertidumbre, su límite de detección y su gráfica de residuales.

**Duración.** 2 horas.

| Tiempo | Qué se hace |
|---|---|
| 0:00 – 0:30 | Ley de Beer, mínimos cuadrados, qué dice y qué no dice el R² |
| 0:30 – 1:00 | Residuales, desviación estándar del ajuste, incertidumbre de la pendiente |
| 1:00 – 1:10 | Pausa |
| 1:10 – 1:50 | Construcción del entregable |
| 1:50 – 2:00 | Verificación y entrega |

## Antes de la sesión

- Repase de su curso de análisis qué son el LOD y el LOQ.
- Tenga a mano su número de lista: los datos salen de él.

## Paso a paso del entregable

1. Descargue `generar_datos.py` y obtenga sus datos con `calibracion(SU_NUMERO)`. Imprima el analito que le tocó y la longitud de onda.
2. Calcule el promedio y la desviación estándar de las tres réplicas de cada nivel y preséntelos en una tabla.
3. Ajuste la recta con `linregress` sobre **todas** las medidas individuales, no sobre los promedios. Reporte pendiente e intercepto con sus incertidumbres.
4. Calcule los residuales y haga la figura de dos paneles: arriba el ajuste con los puntos, abajo los residuales frente a la concentración. Guárdela a 300 dpi.
5. Mire los residuales y escriba en una celda de texto si ve estructura o no, y qué significa. Si el nivel más alto se desvía sistemáticamente, dígalo.
6. Calcule la desviación estándar residual, la concentración de la muestra problema y su incertidumbre con la fórmula de la práctica.
7. Convierta esa incertidumbre en un intervalo de confianza del 95 % usando el valor **t de Student**, no 1,96. Reporte el resultado con el número de cifras que la incertidumbre permite.
8. Calcule el LOD y el LOQ y diga si su muestra está por encima del límite de cuantificación.
9. Repita el ajuste quitando el nivel de concentración más alto y compare: ¿cambia la concentración de la muestra más de lo que dice su propia incertidumbre?
10. Escriba la conclusión en dos frases y añada la declaración de uso de IA.

## Criterios de aceptación

- [ ] La concentración de la muestra se reporta como valor ± margen, con unidad y con cifras significativas coherentes.
- [ ] El intervalo del 95 % usa el t de Student con n−2 grados de libertad.
- [ ] La figura tiene los dos paneles, ejes etiquetados con unidades y está guardada a 300 dpi.
- [ ] Hay una frase propia sobre lo que muestran los residuales.
- [ ] Está la comparación con el ajuste sin el nivel más alto y una conclusión sobre si la diferencia es significativa.

## Entrega

Archivo `S03_Apellido_Nombre.ipynb` más `calibracion_residuales.png`.

## Errores que van a aparecer

**La concentración sale negativa** · Está dividiendo mal: revise que despejó la concentración como la absorbancia menos el intercepto, todo dividido por la pendiente, y no al revés.

**El intervalo sale absurdamente pequeño** · Usó la desviación estándar de las tres réplicas de la muestra en vez de la desviación residual del ajuste. La incertidumbre de la calibración casi siempre pesa más.

**`ValueError: array must not contain infs or NaNs`** · Hay un valor cero o negativo en algún sitio donde calcula un logaritmo o un inverso. Imprima el arreglo antes de operar.

**El R² da 0,9998 y el ajuste es malo igual** · Es exactamente el punto de la sesión. Mire los residuales, no el R².

