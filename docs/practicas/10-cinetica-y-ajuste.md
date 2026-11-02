---
title: "10 · Cinética química y ajuste no lineal"
sidebar_label: "10 · Cinética y ajuste"
description: "Órdenes de reacción, por qué linealizar distorsiona, curve_fit, comparación de modelos y ecuación de Arrhenius."
sidebar_position: 11
slug: 10-cinetica-y-ajuste
---

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pesco13/Python-para-Quimica/blob/main/notebooks/10_Cinetica_y_ajuste.ipynb)

El código de esta práctica está en Colab. Esta página explica la teoría que la acompaña, reúne los errores más frecuentes y propone retos para después de clase.

## Conceptos

### Qué es el orden de reacción

La velocidad de una reacción depende de la concentración elevada a un exponente que **se mide, no se deduce** de la ecuación balanceada:

$$v = -\frac{d[A]}{dt} = k[A]^n$$

Integrando se obtienen tres expresiones distintas:

| Orden | Concentración frente al tiempo | Recta en | Unidades de $k$ | Vida media |
|---|---|---|---|---|
| 0 | $[A] = [A]_0 - kt$ | $[A]$ vs $t$ | mol L⁻¹ s⁻¹ | $[A]_0/2k$ |
| 1 | $[A] = [A]_0 e^{-kt}$ | $\ln[A]$ vs $t$ | s⁻¹ | $\ln 2/k$ |
| 2 | $1/[A] = 1/[A]_0 + kt$ | $1/[A]$ vs $t$ | L mol⁻¹ s⁻¹ | $1/(k[A]_0)$ |

Dos detalles que distinguen a quien entendió de quien copió el procedimiento: en primer orden la vida media **no depende** de la concentración inicial, y las unidades de $k$ son distintas en cada orden. Si reporta una constante de primer orden en L mol⁻¹ s⁻¹, algo no cuadra.

### Por qué linealizar distorsiona

El método clásico transforma los datos para que queden en línea recta. Es cómodo pero tiene un costo: la transformación cambia el tamaño relativo de los errores.

Si el ruido del instrumento es aproximadamente constante en $[A]$, al calcular $1/[A]$ los puntos de concentración baja, que son los más ruidosos en términos relativos, se amplifican y pasan a dominar el ajuste. El resultado es una $k$ sesgada, y una incertidumbre que no significa lo que parece.

El ajuste **no lineal** evita el problema porque minimiza los residuales sobre los datos tal como se midieron. Es lo que hace `scipy.optimize.curve_fit`.

### Cómo funciona `curve_fit`

Recibe una función modelo, los datos y una estimación inicial de los parámetros, y busca los valores que minimizan la suma de cuadrados. Devuelve dos cosas:

- `parametros`: los valores ajustados.
- `covarianza`: una matriz cuya diagonal contiene las varianzas. Su raíz cuadrada es la incertidumbre de cada parámetro.

La estimación inicial importa. Una regla que casi siempre funciona: para la concentración inicial, el primer valor medido; para la constante, algo del orden del inverso del tiempo total del experimento.

### Comparar modelos honestamente

Cuando los modelos tienen el mismo número de parámetros, basta comparar la suma de cuadrados residual: gana el menor. Cuando no, hay que penalizar la complejidad con un criterio como el AIC, porque un modelo con más parámetros siempre ajusta mejor.

Y hay un tercer caso, el más honesto de todos: que dos modelos den sumas parecidas. Entonces los datos **no permiten distinguirlos**, y eso es lo que hay que escribir en el informe, en vez de elegir el que da el resultado esperado.

### La ecuación de Arrhenius

$$k = A e^{-E_a/RT} \qquad\Longrightarrow\qquad \ln k = \ln A - \frac{E_a}{R}\cdot\frac{1}{T}$$

La pendiente de $\ln k$ frente a $1/T$ vale $-E_a/R$. Con $R$ en kJ mol⁻¹ K⁻¹ la energía de activación sale directamente en kJ/mol.

| Energía de activación | Interpretación habitual |
|---|---|
| menos de 20 kJ/mol | Proceso controlado por difusión |
| 40 a 120 kJ/mol | Intervalo típico en disolución |
| más de 200 kJ/mol | Ruptura de un enlace fuerte en el paso determinante |

La extrapolación fuera del intervalo medido solo es válida si el mecanismo no cambia, y eso no se puede comprobar con los datos del ajuste.

## Errores comunes

### `RuntimeError: Optimal parameters not found`

La estimación inicial está demasiado lejos, o el modelo no puede describir los datos. Dibuje el modelo con los valores de `p0` antes de ajustar: si la curva ni se parece, cambie `p0`.

### `OptimizeWarning: Covariance of the parameters could not be estimated`

El ajuste convergió pero los parámetros no están bien determinados, normalmente porque hay pocos puntos o porque dos parámetros son redundantes. La incertidumbre que devuelva no es fiable.

### La energía de activación sale negativa

Invirtió el signo de la pendiente, o puso $T$ en lugar de $1/T$ en el eje. La pendiente de Arrhenius es negativa y $E_a$ es menos esa pendiente por $R$.

### La constante no crece con la temperatura

Casi siempre significa que eligió el orden equivocado. Vuelva a comparar los tres modelos.

### Las unidades de k no coinciden con el orden

Revise qué modelo ajustó. Es el error que más delata un procedimiento seguido mecánicamente.

## Retos adicionales

1. Ajuste sus datos dejando el orden como parámetro libre, con un modelo numérico que integre la ecuación diferencial. ¿El orden que sale es cercano a un entero?
2. Simule datos de primer orden con distintos niveles de ruido y vea a partir de qué nivel deja de poder distinguirse del segundo orden.
3. Calcule la entalpía y la entropía de activación a partir de la ecuación de Eyring y compare con la energía de activación de Arrhenius.
4. Tome una reacción real de la literatura, extraiga sus datos de la figura publicada y repita el análisis. Compare con el valor reportado.

## Glosario

| Término | Significado |
|---|---|
| Orden de reacción | Exponente al que aparece la concentración en la ley de velocidad |
| Ley integrada | Expresión de la concentración frente al tiempo |
| `curve_fit` | Ajuste de un modelo no lineal por mínimos cuadrados |
| Matriz de covarianza | Matriz cuya diagonal da la varianza de cada parámetro ajustado |
| SCR | Suma de cuadrados residual |
| Energía de activación | Barrera energética que controla la dependencia de k con T |
| Factor preexponencial | El valor A de la ecuación de Arrhenius |

## Para saber más

- Atkins, P., de Paula, J. (2018). *Physical Chemistry*, 11.ª ed., capítulo sobre cinética química.
- [Documentación de `scipy.optimize.curve_fit`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html) (en inglés)
- Transtrum, M. K., Sethna, J. P. (2012). Improvements to the Levenberg–Marquardt algorithm for nonlinear least-squares minimization. *arXiv*:1201.5885.

