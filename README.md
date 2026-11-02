# Python para Química

Notebooks introductorios de Python aplicado a la química.

Sitio web con la teoría, los errores comunes y retos de cada práctica: https://pesco13.github.io/Python-para-Quimica/

Todo funciona en **Google Colab**: solo se necesita un navegador y una cuenta de Google. No hay que instalar nada en el computador.

## Contenido

| N.º | Notebook |
|---|---|
| 00 | [Bienvenida a Colab](https://colab.research.google.com/github/pesco13/Python-para-Quimica/blob/main/notebooks/00_Bienvenida_a_Colab.ipynb) |
| 01 | [Python basico para quimica](https://colab.research.google.com/github/pesco13/Python-para-Quimica/blob/main/notebooks/01_Python_basico_para_quimica.ipynb) |
| 02 | [Tablas con pandas](https://colab.research.google.com/github/pesco13/Python-para-Quimica/blob/main/notebooks/02_Tablas_con_pandas.ipynb) |
| 03 | [Moleculas con RDKit](https://colab.research.google.com/github/pesco13/Python-para-Quimica/blob/main/notebooks/03_Moleculas_con_RDKit.ipynb) |
| 04 | [PubChem desde Python](https://colab.research.google.com/github/pesco13/Python-para-Quimica/blob/main/notebooks/04_PubChem_desde_Python.ipynb) |
| 05 | [Similitud y espacio quimico](https://colab.research.google.com/github/pesco13/Python-para-Quimica/blob/main/notebooks/05_Similitud_y_espacio_quimico.ipynb) |
| 06 | [Estructuras 3D y conformeros](https://colab.research.google.com/github/pesco13/Python-para-Quimica/blob/main/notebooks/06_Estructuras_3D_y_conformeros.ipynb) |
| 07 | [Primer calculo cuantico PySCF](https://colab.research.google.com/github/pesco13/Python-para-Quimica/blob/main/notebooks/07_Primer_calculo_cuantico_PySCF.ipynb) |
| 08 | [Graficas para quimica](https://colab.research.google.com/github/pesco13/Python-para-Quimica/blob/main/notebooks/08_Graficas_para_quimica.ipynb) |
| 09 | [Calibracion y error experimental](https://colab.research.google.com/github/pesco13/Python-para-Quimica/blob/main/notebooks/09_Calibracion_y_error.ipynb) |
| 10 | [Cinetica y ajuste no lineal](https://colab.research.google.com/github/pesco13/Python-para-Quimica/blob/main/notebooks/10_Cinetica_y_ajuste.ipynb) |
| 11 | [Informe reproducible](https://colab.research.google.com/github/pesco13/Python-para-Quimica/blob/main/notebooks/11_Informe_reproducible.ipynb) |

Cada notebook termina con ejercicios y soluciones plegables (*Ver solución*), y con celdas de autocomprobación (`assert`) que avisan si algo quedó mal.

## Organización sugerida

Las doce prácticas se pueden recorrer en orden o consultarse de forma aislada.

* **Primeros pasos** (00 a 02): entorno, lenguaje y tablas.
* **Datos de laboratorio** (08 a 10): gráficas, calibración y cinética.
* **Moléculas** (03 a 07): estructura, bases de datos, similitud, 3D y estructura electrónica.
* **Cierre** (11): trabajo reproducible.

Las prácticas 00 a 07 por sí solas forman un recorrido completo, que cabe en tres sesiones de 4 h.

## Herramientas

`herramientas/revisar.py` comprueba las cosas mecánicas que se olvidan al terminar un trabajo y que invalidan un resultado o hacen ilegible una figura: ejes sin unidad, columnas que quedaron como texto, figuras guardadas a 100 dpi, incertidumbres con más cifras de las que soportan, residuales con estructura. No juzga el contenido científico.

```python
!wget -q https://raw.githubusercontent.com/pesco13/Python-para-Quimica/main/herramientas/revisar.py
from revisar import Informe

inf = Informe()
inf.tabla(df, filas=12, columnas=["nombre", "smiles"])
inf.figura(fig)
inf.archivo("calibracion.png", dpi_minimo=300)
inf.resultado(4.3127, 0.34, "mg/L")     # -> "Reporte el resultado asi: 4.3 ± 0.3 mg/L"
inf.residuales(x, y - prediccion)
inf.resumen()
```

El informe distingue fallos (✗), que hay que corregir, de avisos (!), que conviene mirar. La comprobación de residuales usa la prueba de rachas de Wald–Wolfowitz: si el modelo se desvía de forma sistemática, lo detecta aunque el R² sea alto.

## Datos

| Archivo | Qué contiene |
|---|---|
| `datos/compuestos_industriales.csv` | 25 compuestos de uso industrial con su SMILES. Es el conjunto de las prácticas 02 a 07 |
| `datos/compuestos_familias.csv` | 150 compuestos repartidos en 25 familias temáticas |
| `datos/pubchem_respaldo.csv` | Propiedades de esos 150 compuestos ya descargadas de PubChem, para trabajar sin conexión |
| `datos/generar_datos.py` | Genera series sintéticas de calibración y de cinética a partir de una semilla |

El mismo número de semilla da siempre los mismos valores, y números distintos dan series distintas con el mismo comportamiento físico.

```python
!wget -q -O generar_datos.py https://raw.githubusercontent.com/pesco13/Python-para-Quimica/main/datos/generar_datos.py
from generar_datos import calibracion, cinetica, mi_asignacion
print(mi_asignacion(7))
```

Todos los SMILES se validaron con RDKit.

## Cómo usar

1. Abra el notebook con el botón *Abrir en Colab*.
2. Archivo › *Guardar una copia en Drive*.
3. Ejecute las celdas en orden con Shift + Enter.

## Autoría

Material elaborado por **Paulina Escobar** ([ORCID 0009-0009-1454-212X](https://orcid.org/0009-0009-1454-212X)) · [p.escobar@utp.edu.co](mailto:p.escobar@utp.edu.co)

Si usa este material, cítelo según `CITATION.cff`.

## Créditos y referencias

La estructura de los temas se inspira en el curso de quimioinformática del grupo DIFACQUIM (UNAM), disponible bajo licencia MIT en https://github.com/DIFACQUIM/Cursos, y en TeachOpenCADD (https://github.com/volkamerlab/teachopencadd).

* RDKit: Open-source cheminformatics. https://www.rdkit.org
* Kim, S. et al. PubChem (PUG-REST). https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest
* Sun, Q. et al. (2020). Recent developments in the PySCF program package. *J. Chem. Phys.*, 153, 024109.
* Sydow, D. et al. (2019). TeachOpenCADD: a teaching platform for computer-aided drug design using open source packages and data. *J. Cheminform.*, 11, 29.

## Licencia

El **código** (notebooks y scripts) se distribuye bajo licencia MIT, ver `LICENSE`.

El **texto didáctico** del sitio (`docs/`) se distribuye bajo [Creative Commons BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.es): puede reutilizarse y adaptarse citando la fuente.

Si usa el material, el archivo `CITATION.cff` indica cómo citarlo.

## Reproducir el entorno

En Colab no hace falta instalar nada salvo lo que indica cada notebook. Para trabajar en un computador propio, `requirements.txt` recoge las bibliotecas y las versiones con las que se verificó el material.

## Sitio web

El sitio está hecho con [Docusaurus](https://docusaurus.io) y se publica solo en GitHub Pages cada vez que se sube un cambio a la rama `main`. Sus páginas están en `docs/practicas/`, una por notebook, escritas en Markdown. Para cambiar el texto de una práctica, edite el archivo `.md` correspondiente.
