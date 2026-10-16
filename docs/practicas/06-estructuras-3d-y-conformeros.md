---
title: "06 · Estructuras 3D y conformeros"
sidebar_label: "06 · Estructuras 3D"
description: "Qué calcula un campo de fuerza, cómo se generan los conformeros y cuántas moléculas hay en cada uno a temperatura ambiente."
sidebar_position: 7
slug: 06-estructuras-3d-y-conformeros
---

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pesco13/Python-para-Quimica/blob/main/notebooks/06_Estructuras_3D_y_conformeros.ipynb)

El código de esta práctica está en Colab. Esta página explica la teoría que la acompaña, reúne los errores más frecuentes y propone retos para después de clase.

## Conceptos

### ¿Por qué importa la forma 3D?

Un SMILES dice qué átomos están unidos, pero no dónde está cada uno en el espacio. De la forma 3D dependen el momento dipolar, cómo encaja una molécula en una enzima y cómo se acomoda en un cristal. También es el punto de partida de cualquier cálculo de química cuántica.

### De 2D a 3D con ETKDG

RDKit genera la primera geometría con el método ETKDG. Primero estima qué distancias son posibles entre cada par de átomos, a partir de longitudes de enlace y ángulos, y busca coordenadas que las respeten. Después prefiere los ángulos de torsión que aparecen más a menudo en estructuras cristalinas reales.

El resultado es una geometría razonable pero sin optimizar. Por eso después se ajusta con un campo de fuerza.

### Qué calcula un campo de fuerza

La mecánica molecular trata los átomos como esferas y los enlaces como resortes. La energía es una suma de términos de la física clásica:

$$
E = E_{\text{enlace}} + E_{\text{ángulo}} + E_{\text{torsión}} + E_{\text{van der Waals}} + E_{\text{electrostática}}
$$

El término de enlace, por ejemplo, penaliza estirar o comprimir un enlace respecto a su longitud ideal $r_0$:

$$
E_{\text{enlace}} = k_b\,(r - r_0)^2
$$

Los valores de $k_b$, $r_0$ y los demás parámetros se ajustan con datos experimentales y cuánticos. MMFF94 es un conjunto de parámetros pensado para moléculas orgánicas.

Un campo de fuerza es muy rápido: optimiza miles de conformeros en segundos. A cambio, no describe los electrones, así que no puede formar ni romper enlaces ni predecir espectros. Además, sus energías solo tienen sentido como diferencias entre conformeros de una misma molécula.

### Conformeros y cuántas moléculas hay en cada uno

Al girar los enlaces simples, una molécula pasa por muchos conformeros. La optimización encuentra el mínimo de energía más cercano a la geometría de partida (un mínimo local). Para encontrar el de menor energía de todos (el mínimo global) se generan muchos puntos de partida.

A una temperatura $T$, la fracción de moléculas en el conformero $i$ sigue la distribución de Boltzmann:

$$
p_i = \frac{e^{-\Delta E_i / RT}}{\sum_j e^{-\Delta E_j / RT}}
$$

A 298 K, $RT \approx 0.593\ \text{kcal/mol}$.

Tomemos el butano. El conformero *gauche* está unos 0.8 kcal/mol por encima del *anti*, y hay dos *gauche* (uno a cada lado). Cada *gauche* pesa entonces $e^{-0.8/0.593} \approx 0.26$ frente a 1 del *anti*:

$$
p_{\text{anti}} = \frac{1}{1 + 2(0.26)} \approx 0.66
$$

A temperatura ambiente, cerca de un tercio de las moléculas de butano están en conformación *gauche*.

### Formatos de archivo 3D

| Formato | Contenido | Uso típico |
|---|---|---|
| XYZ | Símbolo y coordenadas (Å) | Entrada para química cuántica |
| MOL / SDF | Coordenadas, enlaces y cargas; un SDF puede tener varias moléculas | Pasar moléculas entre programas, bases de datos |
| PDB | Coordenadas de proteínas y ligandos | Biología estructural |

Para las energías, recuerde que 1 kcal/mol = 4.184 kJ/mol.

## Errores comunes

### `EmbedMolecule` devuelve `-1`

El método no encontró coordenadas que cumplan las restricciones. Es frecuente en anillos grandes o moléculas muy tensionadas. Pruebe otra semilla (`randomSeed`) o `AllChem.EmbedMolecule(mol, useRandomCoords=True)`.

### La geometría sale aplastada o los H quedan mal ubicados

Faltó `Chem.AddHs` antes de generar la geometría 3D. Agregue los hidrógenos antes de `EmbedMolecule`.

### La optimización devuelve `1` en lugar de `0`

El primer valor que devuelve `MMFFOptimizeMolecule` (y cada pareja de `MMFFOptimizeMoleculeConfs`) indica si la optimización terminó: `0` quiere decir que sí y `1` que se acabaron las iteraciones antes. Aumente el límite con `MMFFOptimizeMolecule(mol, maxIters=2000)`.

### MMFF no funciona con metales

MMFF94 no tiene parámetros para muchos elementos (Fe, Cu, Pt…). En esos casos use el campo de fuerza UFF: `AllChem.UFFOptimizeMolecule(mol)`.

### El visor 3D no aparece

Falta `.show()` al final de la celda, o el código se ejecutó fuera de Colab o Jupyter. Termine la celda con `vista.show()`.

## Retos adicionales

1. Con las energías de los 20 conformeros del ibuprofeno, calcule la población de Boltzmann de cada uno a 298 K. ¿Cuántos conformeros suman el 90 % de la población?
2. Genere conformeros del ciclohexano y compare las energías de la silla y del bote torcido. ¿Coincide con lo que dice su libro de química orgánica?
3. Calcule el RMSD entre los dos conformeros más estables del ibuprofeno con `rdMolAlign.GetBestRMS`. ¿Son formas realmente distintas?
4. Para el butano, compare la diferencia *anti*–*gauche* que da MMFF94 con la que da UFF. ¿Cuál se acerca más al valor experimental, que está entre 0.6 y 0.9 kcal/mol?

## Glosario

| Término | Significado |
|---|---|
| Conformero | Forma 3D de una molécula que se obtiene al girar enlaces simples |
| Campo de fuerza | Función y parámetros que dan la energía de una geometría |
| MMFF94 / UFF | Campos de fuerza: para moléculas orgánicas / para casi todos los elementos |
| ETKDG | Método de RDKit para generar las primeras coordenadas 3D |
| Mínimo local / global | Geometría estable más cercana / la de menor energía de todas |
| Distribución de Boltzmann | Fracción de moléculas en cada estado según su energía |
| RMSD | Desviación promedio entre las posiciones de los átomos de dos estructuras |

## Para saber más

- [Moléculas 3D en RDKit](https://www.rdkit.org/docs/GettingStartedInPython.html#working-with-3d-molecules) (en inglés)
- [3Dmol.js](https://3dmol.org), el visor que usa py3Dmol (en inglés)
- Riniker, S. & Landrum, G. A. (2015). Better informed distance geometry: using what we know to improve conformation generation. *J. Chem. Inf. Model.*, 55, 2562–2574.
- Halgren, T. A. (1996). Merck molecular force field. I. *J. Comput. Chem.*, 17, 490–519.
