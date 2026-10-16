---
title: Inicio
slug: /
sidebar_position: 1
---

# Python para Química

Ocho prácticas introductorias de Python aplicado a la química.

El código de cada práctica se trabaja en Google Colab, así que solo se necesita un navegador y una cuenta de Google; no hay que instalar nada en el computador. Este sitio acompaña a los notebooks. En cada práctica encontrará la teoría que hay detrás del código, los errores más frecuentes y cómo resolverlos, retos para después de clase, un glosario y lecturas para profundizar.

## Contenido

| N.º | Práctica | Tema |
|---|---|---|
| 00 | [Bienvenida a Colab](./practicas/00-bienvenida-a-colab.md) | Notebooks, celdas e instalación de bibliotecas |
| 01 | [Python básico para química](./practicas/01-python-basico-para-quimica.md) | Variables, listas, diccionarios, funciones |
| 02 | [Tablas con pandas](./practicas/02-tablas-con-pandas.md) | Leer, filtrar, agrupar y graficar datos |
| 03 | [Moléculas con RDKit](./practicas/03-moleculas-con-rdkit.md) | SMILES, descriptores, regla de Lipinski |
| 04 | [PubChem desde Python](./practicas/04-pubchem-desde-python.md) | Consultar una base de datos química por API |
| 05 | [Similitud y espacio químico](./practicas/05-similitud-y-espacio-quimico.md) | Huellas moleculares, Tanimoto, PCA |
| 06 | [Estructuras 3D y conformeros](./practicas/06-estructuras-3d-y-conformeros.md) | Geometrías 3D y campo de fuerza MMFF94 |
| 07 | [Primer cálculo cuántico con PySCF](./practicas/07-primer-calculo-cuantico-pyscf.md) | Hartree–Fock, DFT, HOMO/LUMO |

## Organización sugerida

Tres sesiones de 4 horas:

- Sesión 1: prácticas 00, 01 y 02 (Colab, Python básico, tablas).
- Sesión 2: prácticas 03 y 04 (moléculas con RDKit, PubChem).
- Sesión 3: prácticas 05, 06 y 07 (similitud, 3D, primer cálculo cuántico).

Cada notebook termina con ejercicios resueltos. Los retos de este sitio son distintos y no tienen solución publicada.

## Cómo usar

1. Antes de la sesión, lea los conceptos de la práctica en este sitio.
2. Abra el notebook con el botón *Abrir en Colab* que aparece al inicio de cada página y guarde una copia (*Archivo › Guardar una copia en Drive*).
3. Ejecute las celdas en orden con Shift + Enter. Si algo falla, busque el mensaje en la sección de errores comunes.
4. Después de clase, resuelva los retos.

## Datos

[`datos/compuestos_industriales.csv`](https://github.com/pesco13/Python-para-Quimica/blob/main/datos/compuestos_industriales.csv): 25 compuestos de uso industrial (solventes, conservantes, aromas, fármacos, monómeros) con su SMILES. Datos preparados para fines didácticos.

## Créditos y referencias

La estructura de los temas se inspira en el curso de quimioinformática del grupo DIFACQUIM (UNAM), disponible bajo licencia MIT en [github.com/DIFACQUIM/Cursos](https://github.com/DIFACQUIM/Cursos), y en [TeachOpenCADD](https://github.com/volkamerlab/teachopencadd).

- RDKit: Open-source cheminformatics. [https://www.rdkit.org](https://www.rdkit.org)
- Kim, S. et al. PubChem (PUG-REST). [https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest](https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest)
- Sun, Q. et al. (2020). Recent developments in the PySCF program package. *J. Chem. Phys.*, 153, 024109.
- Sydow, D. et al. (2019). TeachOpenCADD: a teaching platform for computer-aided drug design using open source packages and data. *J. Cheminform.*, 11, 29.

## Licencia

MIT (ver [`LICENSE`](https://github.com/pesco13/Python-para-Quimica/blob/main/LICENSE)).
