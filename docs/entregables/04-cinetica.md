---
title: "Sesión 04 · Cinética y energía de activación"
sidebar_label: "04 · Cinética y Arrhenius"
description: "Orden de reacción justificado, constantes de velocidad a cuatro temperaturas y energía de activación por Arrhenius."
sidebar_position: 5
slug: cinetica
---

# Sesión 04 · Cinética y energía de activación

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pesco13/Python-para-Quimica/blob/main/notebooks/10_Cinetica_y_ajuste.ipynb)

**Objetivo.** Determinar el orden de su reacción, la constante de velocidad a cuatro temperaturas y la energía de activación, con una justificación de por qué eligió ese orden y no otro.

**Duración.** 2 horas.

| Tiempo | Qué se hace |
|---|---|
| 0:00 – 0:30 | Leyes de velocidad integradas y linealizaciones |
| 0:30 – 1:00 | Ajuste no lineal con `curve_fit`, incertidumbres desde la covarianza |
| 1:00 – 1:10 | Pausa |
| 1:10 – 1:50 | Construcción del entregable |
| 1:50 – 2:00 | Verificación y entrega |

## Antes de la sesión

- Repase las tres leyes integradas (orden 0, 1 y 2) y qué representación da una recta en cada caso.
- Repase qué es la energía de activación y en qué intervalo suele caer en reacciones en disolución.

## Paso a paso del entregable

1. Obtenga sus datos con `cinetica(SU_NUMERO)` e imprima qué reacción le tocó. Diga cuántos puntos y cuántas temperaturas tiene.
2. Para la temperatura más baja, pruebe las tres linealizaciones y haga la figura de tres paneles con el R² de cada una.
3. Decida el orden y **justifíquelo por escrito en una celda de texto**, mencionando qué vio en los puntos y no solo el R².
4. Ajuste el modelo correspondiente con `curve_fit`, sin linealizar, y reporte la constante de velocidad con su incertidumbre y con las unidades que corresponden a ese orden.
5. Compare las sumas de cuadrados residuales de los tres modelos en una tabla. Si dos quedan parecidos, dígalo y explique qué haría falta para distinguirlos.
6. Repita el ajuste en las cuatro temperaturas y arme la tabla de constantes de velocidad.
7. Haga la gráfica de Arrhenius y obtenga la energía de activación con su incertidumbre. Guárdela a 300 dpi.
8. Calcule el tiempo de vida media a cada temperatura y comente si depende o no de la concentración inicial, según el orden que encontró.
9. Quite una temperatura y rehaga el ajuste de Arrhenius. ¿La energía de activación cambia más que su incertidumbre? Escriba la respuesta.
10. Conclusión en tres frases y declaración de uso de IA.

## Criterios de aceptación

- [ ] El orden de reacción está justificado con un argumento propio, no solo con el R² más alto.
- [ ] La constante de velocidad lleva las unidades correctas para ese orden.
- [ ] La energía de activación se reporta como valor ± incertidumbre en kJ/mol y cae en un intervalo químicamente razonable.
- [ ] La figura de Arrhenius tiene los ejes etiquetados y está guardada a 300 dpi.
- [ ] Está el análisis de qué pasa al quitar una temperatura.

## Entrega

Archivo `S04_Apellido_Nombre.ipynb` más `cinetica_ordenes.png` y `arrhenius.png`.

## Errores que van a aparecer

**`RuntimeError: Optimal parameters not found`** · La estimación inicial `p0` está muy lejos. Use el primer valor medido como concentración inicial y algo del orden de 1 dividido por el tiempo final como constante.

**La energía de activación sale negativa** · Confundió el signo de la pendiente o invirtió el eje. En la gráfica de Arrhenius la pendiente es negativa y la energía de activación es menos esa pendiente por R.

**Las unidades de k no cuadran** · Dependen del orden: min⁻¹ en primer orden, L mol⁻¹ min⁻¹ en segundo. Si no coinciden con el orden que eligió, revise el ajuste.

**La constante no crece con la temperatura** · Casi siempre significa que eligió el orden equivocado. Vuelva al paso 3.

