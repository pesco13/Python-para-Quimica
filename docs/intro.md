---
title: Inicio
slug: /
sidebar_position: 1
---

# Python para Química

Doce prácticas introductorias de Python aplicado a la química.

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
| 08 | [Gráficas para química](./practicas/08-graficas-para-quimica.md) | numpy, figuras con calidad de informe |
| 09 | [Calibración y error](./practicas/09-calibracion-y-error.md) | Regresión, incertidumbre, LOD y LOQ |
| 10 | [Cinética y ajuste](./practicas/10-cinetica-y-ajuste.md) | Orden de reacción, `curve_fit`, Arrhenius |
| 11 | [Informe reproducible](./practicas/11-informe-reproducible.md) | Entorno, estructura y métodos |

## Organización sugerida

Las doce prácticas están pensadas para recorrerse en orden, pero cada una se sostiene por sí sola y puede consultarse de forma aislada.

- **Primeros pasos** (00 a 02): el entorno, el lenguaje y las tablas.
- **Datos de laboratorio** (08 a 10): gráficas, ajuste de una calibración y de una cinética.
- **Moléculas** (03 a 07): estructura, bases de datos, similitud, geometría 3D y estructura electrónica.
- **Cierre** (11): cómo dejar un trabajo que otra persona pueda repetir.

El bloque de datos de laboratorio solo necesita las prácticas 00 a 02; el de moléculas, además, la 03. Si dispone de poco tiempo, las prácticas 00 a 07 forman un recorrido completo por sí mismas.

Cada notebook termina con ejercicios resueltos y con celdas de autocomprobación (`assert`). Los retos de este sitio son distintos y no tienen solución publicada.

## Cómo usar

1. Antes de la sesión, lea los conceptos de la práctica en este sitio.
2. Abra el notebook con el botón *Abrir en Colab* que aparece al inicio de cada página y guarde una copia (*Archivo › Guardar una copia en Drive*).
3. Ejecute las celdas en orden con Shift + Enter. Si algo falla, busque el mensaje en la sección de errores comunes.
4. Después de clase, resuelva los retos.

## Datos

| Archivo | Qué contiene |
|---|---|
| [`compuestos_industriales.csv`](https://github.com/pesco13/Python-para-Quimica/blob/main/datos/compuestos_industriales.csv) | 25 compuestos de uso industrial con su SMILES |
| [`compuestos_familias.csv`](https://github.com/pesco13/Python-para-Quimica/blob/main/datos/compuestos_familias.csv) | 150 compuestos repartidos en 25 familias temáticas |
| [`pubchem_respaldo.csv`](https://github.com/pesco13/Python-para-Quimica/blob/main/datos/pubchem_respaldo.csv) | Propiedades de esos 150 compuestos ya descargadas de PubChem, para trabajar sin conexión |
| [`generar_datos.py`](https://github.com/pesco13/Python-para-Quimica/blob/main/datos/generar_datos.py) | Genera series sintéticas de calibración y de cinética a partir de una semilla |

`generar_datos.py` produce conjuntos de datos sintéticos de calibración y de cinética a partir de un número entero que actúa de semilla: el mismo número da siempre los mismos valores, y números distintos dan series distintas con el mismo comportamiento físico. Sirve para practicar un ajuste sin depender de haber medido antes en el laboratorio.

Todos los SMILES se validaron con RDKit.

## Autoría

Material elaborado por **Paulina Escobar** ([ORCID 0009-0009-1454-212X](https://orcid.org/0009-0009-1454-212X)).

Para erratas y sugerencias: [p.escobar@utp.edu.co](mailto:p.escobar@utp.edu.co), o abra un [issue en el repositorio](https://github.com/pesco13/Python-para-Quimica/issues).

Si usa este material, cítelo según [`CITATION.cff`](https://github.com/pesco13/Python-para-Quimica/blob/main/CITATION.cff).

## Créditos y referencias

La estructura de los temas se inspira en el curso de quimioinformática del grupo DIFACQUIM (UNAM), disponible bajo licencia MIT en [github.com/DIFACQUIM/Cursos](https://github.com/DIFACQUIM/Cursos), y en [TeachOpenCADD](https://github.com/volkamerlab/teachopencadd).

- RDKit: Open-source cheminformatics. [https://www.rdkit.org](https://www.rdkit.org)
- Kim, S. et al. PubChem (PUG-REST). [https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest](https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest)
- Sun, Q. et al. (2020). Recent developments in the PySCF program package. *J. Chem. Phys.*, 153, 024109.
- Sydow, D. et al. (2019). TeachOpenCADD: a teaching platform for computer-aided drug design using open source packages and data. *J. Cheminform.*, 11, 29.

## Licencia

El **código** (notebooks y scripts) se distribuye bajo licencia MIT, ver [`LICENSE`](https://github.com/pesco13/Python-para-Quimica/blob/main/LICENSE).

El **texto de este sitio** se distribuye bajo [Creative Commons BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.es): puede reutilizarse y adaptarse citando la fuente.
