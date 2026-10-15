---
title: "04 · Consultar PubChem desde Python"
sidebar_label: "04 · PubChem desde Python"
description: "Cómo se comunica Python con un servidor, cómo leer las respuestas de PubChem y cómo consultar sin saturarlo."
sidebar_position: 5
slug: 04-pubchem-desde-python
---

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pesco13/QI452-Python-Quimica/blob/main/notebooks/04_PubChem_desde_Python.ipynb)

El código de esta práctica está en Colab. Esta página explica la teoría que la acompaña, reúne los errores más frecuentes y propone retos para después de clase.

## Conceptos

### ¿Qué es una API?

Una API (interfaz de programación de aplicaciones) es una puerta para que un programa le pida datos a otro sin pasar por la página web hecha para personas. Funciona como pedir en un mostrador: Python envía una dirección web con `requests.get(url)`, el servidor de PubChem busca el compuesto y responde con un código de estado y los datos, casi siempre en formato JSON.

### Códigos de estado HTTP

| Código | Significado | Qué hacer |
|---|---|---|
| 200 | Todo salió bien | Leer los datos |
| 400 | La petición está mal escrita | Revisar la URL (una propiedad mal escrita, caracteres raros) |
| 404 | No se encontró | El nombre o el identificador no existe en PubChem |
| 503 | El servidor está ocupado | Esperar y hacer las consultas más despacio |

Revise `r.status_code` antes de usar `r.json()`.

### Identificadores de PubChem

PubChem tiene tres bases de datos enlazadas:

| Sigla | Qué identifica | Ejemplo |
|---|---|---|
| CID | Un compuesto (una estructura única) | Cafeína: 2519 |
| SID | Una sustancia tal como la registró una fuente | Puede haber cientos por cada CID |
| AID | Un ensayo biológico | Resultados de actividad |

Buscar por nombre es cómodo pero ambiguo, porque un nombre comercial o en español puede no existir o apuntar a otro compuesto. Para un análisis serio, guarde y use el CID o el InChIKey.

### Cómo leer una respuesta JSON

JSON es texto con diccionarios y listas, unos dentro de otros. La respuesta de propiedades tiene esta forma:

```json
{
  "PropertyTable": {
    "Properties": [
      {"CID": 2519, "MolecularFormula": "C8H10N4O2", "MolecularWeight": "194.19"}
    ]
  }
}
```

Por eso el notebook escribe `r.json()["PropertyTable"]["Properties"][0]`: entra al diccionario, luego a la lista y toma el primer elemento. `MolecularWeight` llega como texto, así que hay que convertirlo con `float()`.

### Datos calculados y datos experimentales

Muchas propiedades de PubChem, como XLogP o TPSA, las calcula un programa; no son mediciones. Los datos experimentales (punto de fusión, solubilidad) están en otra sección de la ficha y vienen de fuentes diversas. Si los usa en un informe, diga de dónde salen.

### Consultar sin saturar el servidor

PubChem pide no pasar de 5 consultas por segundo, y quien lo supera puede quedar bloqueado un rato. Guarde los resultados en un CSV para no repetir las mismas consultas en cada sesión. Si necesita datos de muchos compuestos, pida varios a la vez separando los CID con comas en una sola consulta.

## Errores comunes

### `404` con `PUGREST.NotFound`

El nombre no existe en PubChem, casi siempre porque está en español o mal escrito. Use el nombre en inglés (*caffeine*, no *cafeína*) o busque por SMILES o por CID.

### `400` con `PUGREST.BadRequest`

La URL tiene un error, por ejemplo una propiedad mal escrita (`MolecularWeigth`). Compárela con la [lista oficial de propiedades](https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest#section=Compound-Property-Tables).

### `KeyError: 'PropertyTable'`

La respuesta fue un error (un JSON con la clave `Fault`) y no una tabla de propiedades. Revise `r.status_code` y `r.text` antes de leer el JSON.

### `503` con `PUGREST.ServerBusy`

Se hicieron demasiadas consultas seguidas. Aumente la pausa con `time.sleep` y vuelva a intentarlo en unos segundos.

### Un SMILES con `#` o `/` da error

Esos caracteres tienen un significado especial dentro de una dirección web. Envíe el SMILES dentro de la petición, con POST:

```python
r = requests.post(f"{BASE}/compound/smiles/property/MolecularFormula/JSON",
                  data={"smiles": "CC#N"})
```

## Retos adicionales

1. Para cinco compuestos del CSV del curso, obtenga el CID y el InChIKey a partir del SMILES (no del nombre), usando POST.
2. Para diez compuestos, compare el XLogP de PubChem con el log P de RDKit (práctica 03). Haga un gráfico de dispersión y comente las diferencias.
3. Consulte los sinónimos de la aspirina (`/compound/name/aspirin/synonyms/JSON`) y muestre los diez primeros. ¿Por qué buscar por nombre puede ser ambiguo?
4. Escriba una función que consulte una lista de nombres y devuelva dos tablas: los compuestos encontrados y los que fallaron, con el código de error de cada uno.

## Glosario

| Término | Significado |
|---|---|
| API | Interfaz para que un programa le pida datos a otro |
| PUG-REST | La API de PubChem, que funciona con direcciones web |
| HTTP | Protocolo con el que se comunican el navegador (o Python) y el servidor |
| Código de estado | Número que indica si la petición funcionó (200) o falló (4xx, 5xx) |
| JSON | Formato de texto con diccionarios y listas anidados |
| CID | Identificador de un compuesto en PubChem |

## Para saber más

- [Documentación de PUG-REST](https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest) (en inglés)
- [Tutorial de PUG-REST](https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest-tutorial) (en inglés)
- [Documentación de la biblioteca requests](https://requests.readthedocs.io) (en inglés)
- Kim, S. et al. (2023). PubChem 2023 update. *Nucleic Acids Res.*, 51, D1373–D1380.
