# Python para Química

Notebooks introductorios de Python aplicado a la química para el programa de Química Industrial de la Universidad Tecnológica de Pereira (UTP).

🌐 **Sitio web:** https://pesco13.github.io/QI452-Python-Quimica/

Todo funciona en **Google Colab**: solo se necesita un navegador y una cuenta de Google. No hay que instalar nada en el computador.

## Contenido

| N.º | Notebook |
|---|---|
| 00 | [Bienvenida a Colab](https://colab.research.google.com/github/pesco13/QI452-Python-Quimica/blob/main/notebooks/00_Bienvenida_a_Colab.ipynb) |
| 01 | [Python basico para quimica](https://colab.research.google.com/github/pesco13/QI452-Python-Quimica/blob/main/notebooks/01_Python_basico_para_quimica.ipynb) |
| 02 | [Tablas con pandas](https://colab.research.google.com/github/pesco13/QI452-Python-Quimica/blob/main/notebooks/02_Tablas_con_pandas.ipynb) |
| 03 | [Moleculas con RDKit](https://colab.research.google.com/github/pesco13/QI452-Python-Quimica/blob/main/notebooks/03_Moleculas_con_RDKit.ipynb) |
| 04 | [PubChem desde Python](https://colab.research.google.com/github/pesco13/QI452-Python-Quimica/blob/main/notebooks/04_PubChem_desde_Python.ipynb) |
| 05 | [Similitud y espacio quimico](https://colab.research.google.com/github/pesco13/QI452-Python-Quimica/blob/main/notebooks/05_Similitud_y_espacio_quimico.ipynb) |
| 06 | [Estructuras 3D y conformeros](https://colab.research.google.com/github/pesco13/QI452-Python-Quimica/blob/main/notebooks/06_Estructuras_3D_y_conformeros.ipynb) |
| 07 | [Primer calculo cuantico PySCF](https://colab.research.google.com/github/pesco13/QI452-Python-Quimica/blob/main/notebooks/07_Primer_calculo_cuantico_PySCF.ipynb) |

Organización sugerida (3 sesiones de 4 h):

* **Sesión 1:** notebooks 00, 01 y 02 (Colab, Python básico, tablas).
* **Sesión 2:** notebooks 03 y 04 (moléculas con RDKit, PubChem).
* **Sesión 3:** notebooks 05, 06 y 07 (similitud, 3D, primer cálculo cuántico).

Cada notebook termina con ejercicios y soluciones plegables (*Ver solución*).

## Datos

`datos/compuestos_industriales.csv`: 25 compuestos de uso industrial (solventes, conservantes, aromas, fármacos, monómeros) con su SMILES. Datos preparados para fines didácticos.

## Cómo usar

1. Abra el notebook con el botón *Abrir en Colab*.
2. Archivo › *Guardar una copia en Drive*.
3. Ejecute las celdas en orden con Shift + Enter.

## Créditos y referencias

La estructura de los temas se inspira en el curso de quimioinformática del grupo DIFACQUIM (UNAM), disponible bajo licencia MIT en https://github.com/DIFACQUIM/Cursos, y en TeachOpenCADD (https://github.com/volkamerlab/teachopencadd).

* RDKit: Open-source cheminformatics. https://www.rdkit.org
* Kim, S. et al. PubChem (PUG-REST). https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest
* Sun, Q. et al. (2020). Recent developments in the PySCF program package. *J. Chem. Phys.*, 153, 024109.
* Sydow, D. et al. (2019). TeachOpenCADD: a teaching platform for computer-aided drug design using open source packages and data. *J. Cheminform.*, 11, 29.

## Licencia

MIT (ver `LICENSE`).

## Sitio web

El sitio se genera con [Docusaurus](https://docusaurus.io) a partir de los notebooks de `notebooks/` y se publica automáticamente en GitHub Pages cada vez que se sube un cambio a la rama `main`. Para agregar o editar una práctica basta con modificar el notebook: `scripts/notebooks_a_paginas.py` crea la página correspondiente.
