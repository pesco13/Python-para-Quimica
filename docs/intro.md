---
title: Inicio
slug: /
sidebar_position: 1
---

# Python para Química

Notebooks introductorios de Python aplicado a la química para el curso **QI452 Informática II** del programa de Química Industrial de la Universidad Tecnológica de Pereira (UTP).

Todo funciona en **Google Colab**: solo se necesita un navegador y una cuenta de Google. No hay que instalar nada en el computador.

## Contenido

| N.º | Notebook | Tema |
|---|---|---|
| 00 | [Bienvenida a Colab](./hands-on/00-bienvenida-a-colab.mdx) | Notebooks, celdas e instalación de bibliotecas |
| 01 | [Python básico para química](./hands-on/01-python-basico-para-quimica.mdx) | Variables, listas, diccionarios, funciones |
| 02 | [Tablas con pandas](./hands-on/02-tablas-con-pandas.mdx) | Leer, filtrar, agrupar y graficar datos |
| 03 | [Moléculas con RDKit](./hands-on/03-moleculas-con-rdkit.mdx) | SMILES, descriptores, regla de Lipinski |
| 04 | [PubChem desde Python](./hands-on/04-pubchem-desde-python.mdx) | Consultar una base de datos química por API |
| 05 | [Similitud y espacio químico](./hands-on/05-similitud-y-espacio-quimico.mdx) | Huellas moleculares, Tanimoto, PCA |
| 06 | [Estructuras 3D y conformeros](./hands-on/06-estructuras-3d-y-conformeros.mdx) | Geometrías 3D y campo de fuerza MMFF94 |
| 07 | [Primer cálculo cuántico con PySCF](./hands-on/07-primer-calculo-cuantico-pyscf.mdx) | Hartree–Fock, DFT, HOMO/LUMO |

## Organización sugerida

Tres sesiones de 4 horas:

- **Sesión 1:** notebooks 00, 01 y 02 (Colab, Python básico, tablas).
- **Sesión 2:** notebooks 03 y 04 (moléculas con RDKit, PubChem).
- **Sesión 3:** notebooks 05, 06 y 07 (similitud, 3D, primer cálculo cuántico).

Cada notebook termina con ejercicios y soluciones plegables (*Ver solución*).

## Cómo usar

1. Abra el notebook con el botón **Abrir en Colab** que aparece al inicio de cada página.
2. Archivo › *Guardar una copia en Drive*.
3. Ejecute las celdas en orden con **Shift + Enter**.

## Datos

[`datos/compuestos_industriales.csv`](https://github.com/pesco13/QI452-Python-Quimica/blob/main/datos/compuestos_industriales.csv): 25 compuestos de uso industrial (solventes, conservantes, aromas, fármacos, monómeros) con su SMILES. Datos preparados para fines didácticos.

## Créditos y referencias

Material elaborado por Paulina Escobar Martínez. La estructura de los temas se inspira en el curso de quimioinformática del grupo DIFACQUIM (UNAM), disponible bajo licencia MIT en [github.com/DIFACQUIM/Cursos](https://github.com/DIFACQUIM/Cursos), y en [TeachOpenCADD](https://github.com/volkamerlab/teachopencadd).

- RDKit: Open-source cheminformatics. [https://www.rdkit.org](https://www.rdkit.org)
- Kim, S. et al. PubChem (PUG-REST). [https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest](https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest)
- Sun, Q. et al. (2020). Recent developments in the PySCF program package. *J. Chem. Phys.*, 153, 024109.
- Sydow, D. et al. (2019). TeachOpenCADD: a teaching platform for computer-aided drug design using open source packages and data. *J. Cheminform.*, 11, 29.

## Licencia

MIT (ver [`LICENSE`](https://github.com/pesco13/QI452-Python-Quimica/blob/main/LICENSE)).
