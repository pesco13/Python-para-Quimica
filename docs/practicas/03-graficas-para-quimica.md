---
title: "03 · Gráficas para química"
sidebar_label: "03 · Gráficas para química"
description: "numpy, la anatomía de una figura de matplotlib, barras de error y qué debe llevar una gráfica de informe."
sidebar_position: 4
slug: 03-graficas-para-quimica
---

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pesco13/Python-para-Quimica/blob/main/notebooks/03_Graficas_para_quimica.ipynb)

El código de esta práctica está en Colab. Esta página explica la teoría que la acompaña, reúne los errores más frecuentes y propone retos para después de clase.

## Conceptos

### Por qué un arreglo y no una lista

Una lista de Python es un contenedor general: puede guardar números, textos y otras listas a la vez y por eso no sabe sumar. Un arreglo de `numpy` guarda un solo tipo de dato en memoria contigua y eso permite aplicar una operación a todos los elementos de una vez, sin escribir un bucle. Se llama **vectorización**.

| Operación | Lista | Arreglo |
|---|---|---|
| `x * 2` | repite la lista | duplica cada número |
| `x + 1` | error | suma 1 a cada número |
| `x.mean()` | no existe | promedio |
| Velocidad con 10⁶ datos | lenta | decenas de veces más rápida |

En química el dato natural es una serie de medidas, así que casi siempre quiere un arreglo.

### Desviación estándar muestral y poblacional

`numpy` calcula por defecto la desviación **poblacional**, que divide entre n. En el laboratorio casi nunca se tiene la población entera: se tienen tres réplicas de una muestra. La desviación **muestral** divide entre n−1 y es la correcta en ese caso:

$$s = \sqrt{\frac{\sum (x_i - \bar{x})^2}{n-1}}$$

En código, `x.std(ddof=1)`. Con tres réplicas la diferencia entre dividir por 3 o por 2 no es menor: el valor cambia alrededor de un 22 %.

### La figura y los ejes

`matplotlib` separa dos cosas que es fácil confundir:

- La **figura** (`fig`) es la hoja: tiene un tamaño en pulgadas y una resolución.
- El **eje** (`ax`) es cada gráfico dibujado sobre ella: tiene datos, etiquetas y límites.

`fig, ax = plt.subplots()` crea las dos a la vez. A partir de ahí todo se le pide al eje. La alternativa, `plt.plot()`, dibuja sobre "el eje actual", que es una variable oculta: funciona para un gráfico rápido y se vuelve impredecible en cuanto hay dos.

### Qué debe llevar una figura de informe

| Elemento | Por qué |
|---|---|
| Etiqueta en ambos ejes, con unidad | Sin unidad el número no significa nada |
| Título que diga la conclusión | "Solubilidad vs temperatura" no informa; "la solubilidad del KNO₃ se multiplica por veinte" sí |
| Barras de error si hubo réplicas | Un promedio sin dispersión oculta la calidad del dato |
| 300 dpi al guardar | Por debajo se ve pixelado al imprimir |
| Leyenda solo si hay más de una serie | Una leyenda con una entrada es ruido |

### Qué gráfico usar

| Si quiere mostrar | Use |
|---|---|
| Cómo cambia algo con una variable continua | Línea con marcadores |
| Comparar categorías | Barras |
| Relación entre dos medidas | Dispersión |
| Una medida con su incertidumbre | `errorbar` |
| Distribución de muchos valores | Histograma o caja |

## Errores comunes

### `TypeError: can't multiply sequence by non-int of type 'float'`

Está operando sobre una lista en vez de un arreglo. Conviértala con `np.array(...)` antes.

### El promedio salió un solo número cuando esperaba varios

Usó `.mean()` sin `axis`. Con `axis=1` promedia cada fila, con `axis=0` cada columna. Imprima la forma con `.shape` para saber qué tiene entre manos.

### La figura guardada sale en blanco

Llamó a `plt.show()` antes de `fig.savefig(...)`. `show()` vacía la figura. Guarde primero.

### Las etiquetas aparecen cortadas en el archivo

Falta `bbox_inches="tight"` en `savefig`, que recorta ajustándose al contenido en vez de al tamaño nominal.

### Los subíndices no se ven

Las fórmulas van entre signos de dólar: `$KNO_3$`. Fuera de ellos, el guion bajo se imprime tal cual.

## Retos adicionales

1. Dibuje la presión de vapor del agua frente a la temperatura y, en un segundo panel, el logaritmo de la presión frente al inverso de la temperatura. ¿Cuál de los dos es una recta y por qué?
2. Tome las solubilidades del KNO₃ y calcule, con `np.diff`, cuánto aumenta por grado en cada intervalo. ¿Dónde crece más rápido?
3. Haga una figura con cuatro paneles en dos filas que compare cuatro sales distintas, con el mismo eje vertical en todas.
4. Genere 1000 medidas simuladas de una absorbancia con ruido normal y dibuje su histograma. Marque con una línea vertical el promedio y con una banda la desviación estándar.

## Glosario

| Término | Significado |
|---|---|
| Arreglo (`array`) | Serie de números del mismo tipo sobre la que se opera a la vez |
| Vectorización | Aplicar una operación a todos los elementos sin bucle |
| `ddof` | Grados de libertad que se restan al calcular la desviación |
| Figura / eje | La hoja y cada gráfico dibujado en ella |
| dpi | Puntos por pulgada: la resolución de la imagen |
| `errorbar` | Gráfico de puntos con su barra de incertidumbre |

## Para saber más

- [Guía de inicio de numpy](https://numpy.org/doc/stable/user/absolute_beginners.html) (en inglés)
- [Guía de usuario de matplotlib](https://matplotlib.org/stable/users/index.html) (en inglés)
- Rougier, N. P., Droettboom, M., Bourne, P. E. (2014). Ten simple rules for better figures. *PLoS Comput. Biol.*, 10, e1003833.

