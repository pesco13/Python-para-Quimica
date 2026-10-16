---
title: "01 · Python básico para química"
sidebar_label: "01 · Python básico"
description: "Decimales, unidades, listas, diccionarios y funciones: lo que hay detrás de los cálculos químicos en Python."
sidebar_position: 2
slug: 01-python-basico-para-quimica
---

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pesco13/Python-para-Quimica/blob/main/notebooks/01_Python_basico_para_quimica.ipynb)

El código de esta práctica está en Colab. Esta página explica la teoría que la acompaña, reúne los errores más frecuentes y propone retos para después de clase.

## Conceptos

### Python no conoce las unidades

Para Python, `46.07` es solo un número. No sabe si son g/mol, kg o °C, así que las unidades quedan a cargo de quien programa. Ayuda mucho poner la unidad en el nombre de la variable (`masa_g`, `volumen_L`, `T_K`) y convertir todo a un sistema coherente antes de calcular. En la ecuación de los gases ideales

$$
PV = nRT
$$

con $R = 0.082057\ \mathrm{L\,atm\,mol^{-1}\,K^{-1}}$, la presión va en atm, el volumen en L y la temperatura en K.

### Los decimales no son exactos

La computadora guarda los `float` en binario, y muchos decimales no tienen una representación exacta. Si escribe `0.1 + 0.2` en Colab, el resultado es `0.30000000000000004`.

En la práctica, esto tiene dos consecuencias. Al mostrar resultados, redondee: `f"{valor:.3f}"` da 3 decimales y `f"{valor:.2e}"` da notación científica, útil para constantes como $K_a$. Al comparar decimales, no use `==`. En lugar de `pH == 7`, use una tolerancia: `abs(pH - 7) < 0.01`.

### ¿Lista o diccionario?

| Use una lista cuando… | Use un diccionario cuando… |
|---|---|
| Importa el orden | Importa encontrar un dato por su nombre |
| Los datos son del mismo tipo | Cada dato tiene una etiqueta |
| Ej.: temperaturas de un experimento | Ej.: masas atómicas por símbolo |
| Se accede por posición: `T[0]` | Se accede por clave: `masas["O"]` |

Una tabla periódica, una lista de reactivos con su concentración o las propiedades de un compuesto se guardan con naturalidad en un diccionario.

### ¿Por qué escribir funciones?

Una función convierte un cálculo en una herramienta que se puede reutilizar. Si mañana necesita la masa molar de 200 compuestos, la función `masa_molar_de` del notebook ya está escrita y probada.

Una buena función hace una sola cosa y tiene un nombre que dice cuál. Al inicio lleva un texto entre `"""` que explica sus entradas y unidades. Además, devuelve el resultado con `return` en lugar de solo imprimirlo, para poder usarlo en otros cálculos.

### Logaritmos en química

El pH y muchas constantes se expresan con logaritmos en base 10:

$$
\mathrm{pH} = -\log_{10}[\mathrm{H^+}] \qquad\qquad \mathrm{p}K_a = -\log_{10} K_a
$$

En Python se escribe `import math` y luego `math.log10(x)`. Ojo: `math.log(x)` es el logaritmo natural (ln), el que aparece en las ecuaciones de Arrhenius y de Nernst.

## Errores comunes

### `KeyError: 'Cl'` o `KeyError: 'cl'`

El diccionario no tiene esa clave. Las claves distinguen mayúsculas, así que `"Cl"` y `"cl"` son distintas. Revise con `print(masas.keys())` que el elemento esté y que esté escrito igual.

### `TypeError: can only concatenate str (not "float") to str`

Se intentó unir texto y número con `+`, como en `"Masa: " + 18.0`. Use un f-string: `f"Masa: {18.0}"`.

### `ZeroDivisionError: float division by zero`

Algún denominador vale cero, por ejemplo un volumen `V_L = 0` o una variable que no se actualizó. Imprima los valores antes del cálculo para encontrar cuál es.

### El resultado es una tupla: `(2, 5)`

Se escribió `x = 2,5` con coma decimal y Python lo leyó como dos números. Use punto: `x = 2.5`.

### `clasificar_pH(7.0000001)` dice «básica»

La comparación `pH == 7` es exacta, y un valor medido nunca es exactamente 7. Compare con tolerancia, como se explica en *Los decimales no son exactos*.

## Retos adicionales

1. Escriba una función `porcentaje_masa(composicion, elemento)` que devuelva el porcentaje en masa de un elemento en un compuesto. Pruébela con el carbono en la glucosa (debe dar ≈ 40.0 %).
2. Convierta la lista de presiones `[760, 745, 730, 700]`, en mmHg, a atm (1 atm = 760 mmHg) y muéstrelas con 3 decimales.
3. Escriba una función `volumen_stock(C1, C2, V2)` que use $C_1V_1 = C_2V_2$ para calcular cuántos mL de HCl 12 M se necesitan para preparar 250 mL de HCl 0.5 M.
4. Modifique `clasificar_pH` para que use una tolerancia de 0.05 y considere neutra cualquier solución entre 6.95 y 7.05.
5. Construya un diccionario con las densidades (g/mL) de cinco solventes del laboratorio y una función que convierta un volumen de cualquiera de ellos a masa.

## Glosario

| Término | Significado |
|---|---|
| Variable | Nombre que guarda un valor |
| `int`, `float`, `str`, `bool` | Entero, decimal, texto y verdadero/falso |
| Lista | Colección ordenada de valores: `[1, 2, 3]` |
| Diccionario | Colección de pares clave–valor: `{"H": 1.008}` |
| Función | Bloque de código con nombre que recibe argumentos y devuelve un resultado |
| f-string | Texto con variables dentro: `f"{x:.2f}"` |

## Para saber más

- [Tutorial oficial de Python](https://docs.python.org/es/3/tutorial/) (en español)
- [Scientific Computing for Chemists with Python](https://weisscharlesj.github.io/SciCompforChemists/), libro abierto de C. Weiss (en inglés)
- [Python Data and Scripting for Biochemists and Molecular Biologists](https://education.molssi.org/python-scripting-biochemistry/), curso de MolSSI (en inglés)
