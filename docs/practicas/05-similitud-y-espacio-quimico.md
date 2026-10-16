---
title: "05 · Similitud molecular y espacio químico"
sidebar_label: "05 · Similitud y espacio químico"
description: "Cómo se construye una huella de Morgan, de dónde sale el coeficiente de Tanimoto y cómo leer un mapa de PCA."
sidebar_position: 6
slug: 05-similitud-y-espacio-quimico
---

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pesco13/Python-para-Quimica/blob/main/notebooks/05_Similitud_y_espacio_quimico.ipynb)

El código de esta práctica está en Colab. Esta página explica la teoría que la acompaña, reúne los errores más frecuentes y propone retos para después de clase.

## Conceptos

### El principio de similitud

La quimioinformática parte de una idea: moléculas con estructuras parecidas suelen tener propiedades parecidas. Por eso buscar compuestos similares a uno conocido sirve para encontrar sustitutos de un solvente, alternativas a un conservante o candidatos a fármaco.

La idea tiene excepciones. A veces un cambio pequeño, de un solo átomo, cambia mucho una propiedad. A esas parejas de moléculas casi iguales con comportamiento muy distinto se les llama acantilados de actividad.

### Cómo se construye una huella de Morgan

Una huella de Morgan (también llamada ECFP) describe el entorno de cada átomo en varios pasos. Primero, a cada átomo se le asigna un código según su elemento, sus enlaces y sus vecinos (radio 0). Luego el código de cada átomo se combina con los de sus vecinos directos (radio 1), y después con los vecinos de los vecinos (radio 2). Con `radius=2`, cada fragmento llega hasta dos enlaces desde el átomo central.

Al final, cada fragmento distinto se convierte en un número y se acomoda en un vector de `fpSize` bits (2048 en el notebook), donde el bit correspondiente se pone en 1. Como hay más fragmentos posibles que bits, a veces dos fragmentos distintos encienden el mismo bit. Con 2048 bits y moléculas pequeñas, esas coincidencias pesan poco.

### El coeficiente de Tanimoto

Si $a$ es el número de bits encendidos en la molécula A, $b$ el de la molécula B y $c$ el de los bits encendidos en ambas:

$$
T(A,B) = \frac{c}{a + b - c}
$$

Por ejemplo, si A tiene 10 bits, B tiene 12 y comparten 8, entonces $T = 8 / (10 + 12 - 8) = 8/14 \approx 0.57$.

Un valor de 1 indica huellas idénticas, que casi siempre corresponden a la misma molécula, y uno de 0 indica que no comparten ningún fragmento. No hay un umbral universal a partir del cual dos moléculas sean «parecidas», porque depende del tipo de huella y del radio. Compare solo valores calculados con el mismo método.

### PCA: un mapa del espacio químico

En el notebook cada compuesto se describe con 6 descriptores, así que es un punto en un espacio de 6 dimensiones. El análisis de componentes principales (PCA) busca las direcciones en las que los datos varían más y proyecta los puntos sobre las dos primeras, PC1 y PC2.

Antes del PCA hay que estandarizar. MolWt va de 18 a 300 y HBD de 0 a 5; sin `StandardScaler`, la masa dominaría el mapa solo por tener números más grandes.

`pca.explained_variance_ratio_` dice qué fracción de la información conserva cada eje. Si PC1 y PC2 suman 0.85, el mapa muestra el 85 % de la variación. Por su parte, `pca.components_` da las cargas, es decir, cuánto pesa cada descriptor en cada eje, y sirve para interpretar qué significa estar a la derecha o arriba en el mapa.

Tenga presente que dos puntos cercanos en el mapa pueden estar lejos en las dimensiones que el mapa no muestra.

## Errores comunes

### `IndexError: single positional indexer is out-of-bounds`

`df.loc[df.nombre == "Cafeina", "fp"].iloc[0]` no encontró el nombre, por ejemplo porque falta la tilde (en el CSV dice «Cafeína»). Copie el nombre exacto desde `df["nombre"].tolist()`.

### `ArgumentError` o `ValueError` al calcular Tanimoto

Si aparece `ArgumentError`, una de las huellas es `None` porque el SMILES no era válido. Si aparece `ValueError`, se están comparando huellas de tamaños distintos. Genere todas las huellas con el mismo generador y revise que ninguna molécula sea `None`.

### `DeprecationWarning` con `GetMorganFingerprintAsBitVect`

Es la forma antigua de calcular huellas en RDKit y todavía aparece en muchos tutoriales. Use el generador, como en el notebook: `rdFingerprintGenerator.GetMorganGenerator(radius=2, fpSize=2048)`.

### Un solo descriptor domina el mapa de PCA

Faltó estandarizar los datos. Aplique `StandardScaler().fit_transform(X)` antes del PCA.

## Retos adicionales

1. Calcule a mano el coeficiente de Tanimoto para A = {1, 4, 7, 9} y B = {1, 4, 8} (los números son las posiciones de los bits encendidos). Luego verifíquelo en Python usando conjuntos (`set`).
2. Compare la similitud entre el metilparabeno y el propilparabeno con radios 1, 2 y 3. ¿Cómo cambia y por qué?
3. Construya la matriz de similitud 25 × 25 de todos los compuestos del curso y dibújela como mapa de calor con `plt.imshow`. ¿Qué grupos aparecen?
4. Busque en los datos del curso dos compuestos con Tanimoto alto pero log P muy distinto. ¿Se trata de un acantilado?
5. Repita el PCA sin `StandardScaler` y compare los dos mapas. Explique la diferencia usando las cargas.

## Glosario

| Término | Significado |
|---|---|
| Huella molecular | Vector de bits que indica qué fragmentos tiene una molécula |
| Huella de Morgan (ECFP) | Huella basada en el entorno circular de cada átomo |
| Coeficiente de Tanimoto | Similitud entre 0 y 1: fragmentos comunes sobre fragmentos totales |
| Espacio químico | Conjunto de moléculas representadas como puntos según sus descriptores |
| PCA | Técnica que resume muchas variables en pocos ejes |
| Varianza explicada | Fracción de la información que conserva cada componente |
| Cargas | Peso de cada variable original en un componente del PCA |
| Acantilado de actividad | Dos moléculas muy parecidas con propiedades muy distintas |

## Para saber más

- [Huellas moleculares en RDKit](https://www.rdkit.org/docs/GettingStartedInPython.html#fingerprinting-and-molecular-similarity) (en inglés)
- [PCA en scikit-learn](https://scikit-learn.org/stable/modules/decomposition.html#pca) (en inglés)
- Rogers, D. & Hahn, M. (2010). Extended-connectivity fingerprints. *J. Chem. Inf. Model.*, 50, 742–754.
- Bajusz, D., Rácz, A. & Héberger, K. (2015). Why is Tanimoto index an appropriate choice for fingerprint-based similarity calculations? *J. Cheminform.*, 7, 20.
- Maggiora, G. et al. (2014). Molecular similarity in medicinal chemistry. *J. Med. Chem.*, 57, 3186–3204.
