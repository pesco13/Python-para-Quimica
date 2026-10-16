---
title: "00 · Bienvenida a Google Colab"
sidebar_label: "00 · Bienvenida a Colab"
description: "Qué pasa cuando se ejecuta una celda, por qué importa el orden y cómo no perder el trabajo."
sidebar_position: 1
slug: 00-bienvenida-a-colab
---

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pesco13/Python-para-Quimica/blob/main/notebooks/00_Bienvenida_a_Colab.ipynb)

El código de esta práctica está en Colab. Esta página explica lo que pasa por detrás, reúne los errores más frecuentes y propone retos para después de clase.

## Conceptos

### ¿Por qué Python en química?

Python es un lenguaje de programación gratuito con muchas bibliotecas científicas. En química sirve para automatizar cálculos repetitivos, analizar datos de laboratorio, consultar bases de datos, dibujar y comparar moléculas y hacer cálculos de química computacional. Lo que en una hoja de cálculo obliga a copiar una fórmula fila por fila, en Python se escribe una vez y se aplica a mil compuestos.

### ¿Qué pasa cuando ejecuto una celda?

Colab no ejecuta el código en su computador sino en una máquina virtual de Google. Dentro de ella hay un programa de Python encendido, el entorno de ejecución, que recuerda todo lo que se ha ejecutado en la sesión:

| Lo que usted ve | Lo que pasa por detrás |
|---|---|
| Presiona Shift + Enter | El texto de la celda se envía al entorno de ejecución |
| Aparece `[3]` a la izquierda | Es la tercera instrucción que recibió en esta sesión |
| Se define `masa = 18.015` | El entorno guarda `masa` en su memoria |
| Otra celda usa `masa` | Funciona solo si la celda anterior ya se ejecutó en esta sesión |

Por eso cuenta el orden en que se ejecutan las celdas, no el orden en que aparecen en la pantalla. Si ejecuta la celda 5 antes que la 2, el resultado puede cambiar. Los números entre corchetes muestran el orden real.

### La sesión es temporal

La máquina virtual se apaga después de un rato sin uso o cuando se reinicia el entorno. Cuando eso pasa se pierden las variables, las bibliotecas instaladas con `pip` y los archivos creados en el panel de archivos (por ejemplo, un `.csv` guardado con pandas).

El notebook no se pierde si está guardado en su Drive. Por eso conviene empezar siempre con *Archivo › Guardar una copia en Drive*.

### Celdas de código y celdas de texto

Las celdas de texto usan Markdown, un formato sencillo para dar estilo:

```markdown
## Un título
**negrita**, *cursiva*, `código`
* un elemento de lista
H₂O, CO₂ (los subíndices se copian como caracteres Unicode)
```

Un buen notebook de laboratorio explica con texto qué se calcula y por qué. El código solo no basta.

## Errores comunes

### `NameError: name 'masa' is not defined`

La variable se definió en una celda que no se ha ejecutado en esta sesión, o la sesión se reinició. Ejecute las celdas anteriores o use *Entorno de ejecución › Ejecutar celdas anteriores*.

### `ModuleNotFoundError: No module named 'rdkit'`

La biblioteca no viene en Colab, o se instaló en una sesión que ya terminó. Vuelva a ejecutar la celda con `!pip install -q rdkit`.

### `SyntaxError: invalid syntax` o `unterminated string literal`

Falta cerrar un paréntesis o unas comillas, o se escribió una coma decimal (`2,5` en lugar de `2.5`). Revise la línea que señala el mensaje y también la anterior. Python usa punto decimal.

### `IndentationError: unexpected indent`

Hay espacios de más al inicio de la línea. En Python la sangría tiene significado, así que borre esos espacios o alinee la línea con las demás del mismo bloque.

### Los cambios desaparecieron

Probablemente se trabajó en el notebook abierto desde GitHub sin guardar una copia propia. Guarde la copia en Drive antes de empezar a escribir.

## Retos adicionales

1. Calcule en una sola celda la masa molar de la glucosa (C₆H₁₂O₆) con C = 12.011, H = 1.008 y O = 15.999.
2. Cree una celda de texto con un título, una lista de tres reactivos del laboratorio y la fórmula del ácido sulfúrico con subíndices.
3. Defina una variable en una celda, reinicie la sesión (*Entorno de ejecución › Reiniciar sesión*) y ejecute otra celda que la use. Explique con sus palabras el mensaje que aparece.
4. Instale la biblioteca `pubchempy` con `pip` y muestre su versión con `pubchempy.__version__`.

## Glosario

| Término | Significado |
|---|---|
| Notebook | Documento que combina texto, código y resultados (archivo `.ipynb`) |
| Celda | Bloque de un notebook; puede ser de código o de texto |
| Entorno de ejecución | Programa de Python que ejecuta las celdas y guarda las variables |
| Biblioteca | Conjunto de herramientas listas para usar (pandas, RDKit, PySCF) |
| `pip` | Programa que instala bibliotecas de Python |
| Markdown | Formato de texto simple para títulos, listas y estilos |

## Para saber más

- [Preguntas frecuentes de Google Colab](https://research.google.com/colaboratory/faq.html) (en inglés)
- [Tutorial oficial de Python](https://docs.python.org/es/3/tutorial/) (en español)
- [Guía básica de Markdown](https://www.markdownguide.org/basic-syntax/) (en inglés)
