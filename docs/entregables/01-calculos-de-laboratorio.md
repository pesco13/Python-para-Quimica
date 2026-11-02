---
title: "Sesión 01 · Cálculos de laboratorio"
sidebar_label: "01 · Cálculos de laboratorio"
description: "Hoja de cálculo programable con masa molar, moles, preparación de disoluciones y diluciones para tres reactivos propios."
sidebar_position: 2
slug: calculos-de-laboratorio
---

# Sesión 01 · Cálculos de laboratorio

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pesco13/Python-para-Quimica/blob/main/notebooks/00_Bienvenida_a_Colab.ipynb) [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pesco13/Python-para-Quimica/blob/main/notebooks/01_Python_basico_para_quimica.ipynb)

**Objetivo.** Construir una hoja de cálculo programable que resuelva, para tres reactivos que usted elija, la masa molar, los moles contenidos en una masa dada y el volumen necesario para preparar una disolución.

**Duración.** 2 horas.

| Tiempo | Qué se hace |
|---|---|
| 0:00 – 0:20 | Colab: celdas, orden de ejecución, guardar copia en Drive |
| 0:20 – 0:55 | Variables, listas, diccionarios y funciones ([práctica 01](../practicas/01-python-basico-para-quimica.md)) |
| 0:55 – 1:05 | Pausa |
| 1:05 – 1:45 | Construcción del entregable |
| 1:45 – 2:00 | Reiniciar y ejecutar todo, renombrar, compartir y entregar |

## Antes de la sesión

- Lea los conceptos de las prácticas [00](../practicas/00-bienvenida-a-colab.md) y [01](../practicas/01-python-basico-para-quimica.md).
- Elija **tres reactivos** que haya usado en el laboratorio este semestre y anote su fórmula molecular. Sirve cualquiera: NaCl, H₂SO₄, KMnO₄, glucosa.

## Paso a paso del entregable

1. Abra un notebook nuevo en Colab y guárdelo como copia en su Drive. En la primera celda de texto escriba su nombre, su número de lista y la fecha.
2. Cree un diccionario `masas_atomicas` con los símbolos de los elementos que aparecen en sus tres reactivos y su masa atómica. Al terminar, `masas_atomicas` debe tener al menos cinco entradas.
3. Escriba una función `masa_molar(composicion)` que reciba un diccionario del tipo `"Na": 1, "Cl": 1` y devuelva la masa molar en g/mol. Compruébela con el NaCl: debe dar 58,44.
4. Use la función con sus tres reactivos y guarde los resultados en un diccionario `mis_masas_molares`. Imprímalo.
5. Escriba una función `moles(masa_g, masa_molar)` que devuelva los moles, y otra `masa_para(moles, masa_molar)` que haga lo contrario. Cada una con su `docstring` de una línea explicando qué hace.
6. Calcule qué masa de cada reactivo necesita para preparar 250 mL de una disolución 0,100 mol/L. Imprima el resultado con dos decimales y con la unidad.
7. Escriba una función `dilucion(c1, v1, c2)` que aplique C₁V₁ = C₂V₂ y devuelva el volumen final. Úsela para calcular a qué volumen debe llevar 10,0 mL de su disolución 0,100 mol/L para obtener una 0,0150 mol/L.
8. Añada una celda final de texto con el título **Uso de asistentes de IA** y declare si usó alguno y para qué.

## Criterios de aceptación

- [ ] El notebook corre completo tras *Reiniciar y ejecutar todo*, sin errores.
- [ ] `masa_molar` devuelve 58,44 para el NaCl, comprobado en una celda.
- [ ] Las tres funciones tienen `docstring` y nombres en minúsculas y sin tildes.
- [ ] Cada resultado numérico se imprime con su unidad y con un número razonable de decimales.
- [ ] Está la celda de declaración de uso de IA.

## Entrega

Archivo `S01_Apellido_Nombre.ipynb`, enlace de Drive con permiso de lectura para cualquiera, antes del final de la sesión.

## Errores que van a aparecer

**`KeyError: 'na'`** · Los diccionarios distinguen mayúsculas de minúsculas y en química los símbolos llevan la primera en mayúscula: `Na`, no `na` ni `NA`.

**`TypeError: can only concatenate str (not "float") to str`** · Está sumando un número a un texto. Use una f-string: `f"La masa es de 58.44 g/mol"` escrita como `f"La masa es de {m:.2f} g/mol"`.

**El resultado sale `0`** · En Python 3 la división `/` da decimales, pero `//` da la división entera. Revise que no escribió doble barra.

**La celda 7 falla porque no existe `c1`** · Las celdas se ejecutan en el orden en que usted las corre, no en el que están escritas. Reinicie el entorno y ejecútelas de arriba abajo.

