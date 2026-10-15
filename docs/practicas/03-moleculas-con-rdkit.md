---
title: "03 · Moléculas en la computadora con RDKit"
sidebar_label: "03 · Moléculas con RDKit"
description: "Cómo se escribe un SMILES, qué guarda un InChIKey y qué dicen (y qué no) los descriptores y la regla de Lipinski."
sidebar_position: 4
slug: 03-moleculas-con-rdkit
---

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pesco13/QI452-Python-Quimica/blob/main/notebooks/03_Moleculas_con_RDKit.ipynb)

El código de esta práctica está en Colab. Esta página explica la teoría que la acompaña, reúne los errores más frecuentes y propone retos para después de clase.

## Conceptos

### Formas de representar una molécula

| Representación | Ejemplo (etanol) | Ventaja | Limitación |
|---|---|---|---|
| Nombre | etanol, alcohol etílico | Fácil de leer | Varios nombres para lo mismo |
| Fórmula molecular | C₂H₆O | Compacta | El dimetil éter tiene la misma |
| SMILES | `CCO` | Texto corto y fácil de escribir | Una molécula admite varias cadenas |
| InChI | `InChI=1S/C2H6O/c1-2-3/h3H,2H2,1H3` | Única y estándar | Difícil de leer |
| InChIKey | `LFQSCWFLJHTTHZ-UHFFFAOYSA-N` | Longitud fija, buena para buscar | No se puede convertir de vuelta en la molécula |
| Coordenadas 3D | archivo XYZ o MOL | Describe la forma | Depende del conformero |

### Cómo se escribe un SMILES

| Regla | Ejemplo | Molécula |
|---|---|---|
| C, N, O y otros átomos comunes van sin corchetes; los H se suponen | `C`, `CC` | metano, etano |
| `=` es doble enlace y `#` triple | `C=C`, `C#N` | eteno, grupo nitrilo |
| Las ramificaciones van entre paréntesis | `CC(=O)O` | ácido acético |
| En los anillos, un número abre y el mismo número cierra | `C1CCCCC1` | ciclohexano |
| Las minúsculas son átomos aromáticos | `c1ccccc1` | benceno |
| Los corchetes indican cargas, isótopos u otros elementos | `[Na+].[Cl-]` | cloruro de sodio |
| El punto separa fragmentos que no están enlazados | `[NH4+].[Cl-]` | cloruro de amonio |
| `@` y `@@` indican la quiralidad | `C[C@H](N)C(=O)O` | L-alanina |
| `/` y `\` indican la geometría cis/trans | `C/C=C/C` | *trans*-2-buteno |

Un mismo compuesto admite muchos SMILES (`CCO`, `OCC`, `C(C)O`). El SMILES canónico es el que elige el programa con un algoritmo fijo. Tenga en cuenta que el canónico de RDKit puede no coincidir con el de otro programa.

### ¿Qué hay dentro de un InChIKey?

Un InChIKey tiene 27 caracteres repartidos en tres bloques, por ejemplo `LFQSCWFLJHTTHZ-UHFFFAOYSA-N`. Las primeras 14 letras resumen el esqueleto (qué átomos hay y cómo se conectan). Las 10 siguientes resumen la estereoquímica, los isótopos y otros detalles; `UHFFFAOYSA` quiere decir que no hay estereoquímica. La última letra indica el estado de protonación (`N` es neutro).

Por eso dos estereoisómeros comparten el primer bloque y difieren en el segundo. Como el InChIKey es un resumen cifrado del InChI, no se puede reconstruir la molécula a partir de él.

### Lo que miden los descriptores

El log P es el logaritmo del coeficiente de reparto entre octanol y agua:

$$
\log P = \log_{10}\frac{[\text{soluto}]_{\text{octanol}}}{[\text{soluto}]_{\text{agua}}}
$$

Si es positivo, el compuesto prefiere la fase grasa (es lipofílico); si es negativo, prefiere el agua. En la industria y en química ambiental, un log P alto se toma como señal de posible bioacumulación. RDKit lo estima con el método de Crippen, sumando contribuciones de cada átomo, así que es un valor calculado y no medido.

La TPSA (área superficial polar topológica) suma la superficie de los átomos polares (N, O y sus H) y se relaciona con la facilidad para atravesar membranas. HBD y HBA cuentan los donadores (O–H, N–H) y los aceptores (N, O) de puentes de hidrógeno.

### La regla de Lipinski y sus límites

Lipinski y sus colaboradores, en Pfizer, analizaron en 1997 fármacos que se absorben bien por vía oral y vieron que casi todos cumplían límites en múltiplos de 5. De ahí el nombre de «regla del 5». Es una guía estadística, no una ley. Muchos antibióticos y productos naturales no la cumplen y funcionan bien por vía oral. Además, solo habla de absorción, no de actividad ni de toxicidad. En compuestos como solventes o monómeros no tiene una interpretación farmacológica, aunque sirve para practicar.

## Errores comunes

### `SMILES Parse Error` y luego `AttributeError: 'NoneType' object has no attribute ...`

El SMILES no es válido, por ejemplo porque un anillo no se cierra o falta un paréntesis. `MolFromSmiles` devuelve `None` y la línea siguiente falla. Lea el primer mensaje, que es el que explica el problema. Conviene comprobar la molécula antes de usarla: `if mol is None: print("SMILES inválido")`.

### `Explicit valence for atom # 1 N, 4, is greater than permitted`

Un átomo tiene más enlaces de los que admite. Pasa mucho con iones escritos sin carga, como el amonio. Escriba la carga entre corchetes: `[NH4+]`, `C[N+](C)(C)C`.

### `Can't kekulize mol`

Se escribió en minúsculas (aromático) un anillo que no puede serlo, o le falta un H a un N aromático, como en el pirrol (`c1cc[nH]c1`). Revise los átomos aromáticos o escriba el anillo con enlaces simples y dobles alternados.

### La celda no muestra el dibujo

Colab dibuja automáticamente solo el valor de la última línea de la celda. Ponga la molécula sola en la última línea, o use `display(mol)`.

## Retos adicionales

1. Escriba a mano el SMILES del ácido láctico, el nitrobenceno, la glicina y el cloruro de sodio. Verifíquelos con RDKit y compárelos con el SMILES canónico.
2. Escriba la L-alanina y la D-alanina usando `@` y `@@`. Calcule el InChIKey de ambas y explique qué bloque cambia y por qué.
3. Busque en PubChem el SMILES de tres colorantes o aditivos alimentarios, calcule sus descriptores y diga cuáles cumplirían la regla de Lipinski.
4. Ordene los compuestos del curso por log P. ¿Cuáles tenderían más a acumularse en tejidos grasos? Justifique con la estructura.

## Glosario

| Término | Significado |
|---|---|
| SMILES | Cadena de texto que describe cómo están unidos los átomos de una molécula |
| SMILES canónico | El SMILES único que un programa asigna a cada molécula |
| InChI / InChIKey | Identificador estándar de la IUPAC y su resumen de 27 caracteres |
| Descriptor | Número calculado a partir de la estructura |
| log P | Lipofilia: cómo se reparte el compuesto entre octanol y agua |
| TPSA | Área superficial polar topológica (Å²) |
| HBD / HBA | Donadores / aceptores de puentes de hidrógeno |

## Para saber más

- [Teoría de SMILES](https://www.daylight.com/dayhtml/doc/theory/theory.smiles.html), de Daylight (en inglés)
- [Primeros pasos con RDKit en Python](https://www.rdkit.org/docs/GettingStartedInPython.html) (en inglés)
- [InChI Trust](https://www.inchi-trust.org) (en inglés)
- Weininger, D. (1988). SMILES, a chemical language and information system. *J. Chem. Inf. Comput. Sci.*, 28, 31–36.
- Lipinski, C. A. et al. (1997). Experimental and computational approaches to estimate solubility and permeability in drug discovery and development settings. *Adv. Drug Deliv. Rev.*, 23, 3–25.
