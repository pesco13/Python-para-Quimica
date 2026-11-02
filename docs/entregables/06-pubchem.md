---
title: "Sesión 06 · Consultas a PubChem"
sidebar_label: "06 · PubChem"
description: "Enriquecer la tabla propia con datos de PubChem manejando errores, pausas entre consultas y archivo de respaldo."
sidebar_position: 7
slug: pubchem
---

# Sesión 06 · Consultas a PubChem

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pesco13/Python-para-Quimica/blob/main/notebooks/04_PubChem_desde_Python.ipynb)

**Objetivo.** Enriquecer su tabla con datos de PubChem mediante consultas automáticas, y dejar documentado qué compuestos fallaron y por qué. El manejo de los fallos es parte del entregable, no un accidente.

**Duración.** 2 horas.

| Tiempo | Qué se hace |
|---|---|
| 0:00 – 0:35 | Qué es una API, códigos de estado, identificadores de PubChem ([práctica 04](../practicas/04-pubchem-desde-python.md)) |
| 0:35 – 1:05 | Leer una respuesta JSON, consultar sin saturar el servidor, manejar errores |
| 1:05 – 1:15 | Pausa |
| 1:15 – 1:50 | Construcción del entregable |
| 1:50 – 2:00 | Verificación y entrega |

## Antes de la sesión

- Tenga su archivo `descriptores_mi_familia.csv` de la sesión 5.
- Entre a PubChem desde el navegador y busque uno de sus compuestos: mire qué propiedades ofrece.

## Paso a paso del entregable

1. Escriba una función `consultar(smiles)` que pida a PubChem el CID, la fórmula, la masa molar, el XLogP y la TPSA de un compuesto, y devuelva un diccionario.
2. Haga que la función **no se caiga** cuando algo sale mal: si la respuesta no es 200, debe devolver un diccionario con el código de error en vez de lanzar una excepción.
3. Añada una pausa de 0,2 a 0,3 segundos entre consultas. Explique en una frase por qué hace falta.
4. Recorra sus doce compuestos y arme una tabla con las respuestas. Imprima cuántos tuvieron éxito y cuántos fallaron.
5. Para cada fallo, escriba en una celda de texto cuál fue el código y qué cree que lo causó. Un SMILES con caracteres especiales, un compuesto que PubChem no reconoce y un servidor ocupado son causas distintas.
6. Una la tabla de PubChem con la suya de la sesión 5 usando el nombre del compuesto como clave. Verifique que no perdió filas en la unión.
7. Compare el XLogP de PubChem con el log P que calculó RDKit: haga una figura de dispersión con la línea de identidad y comente por qué no coinciden.
8. Si la red falla durante la sesión, use `datos/pubchem_respaldo.csv` del repositorio y **dígalo en el notebook**. Trabajar con el respaldo no resta puntos; ocultarlo sí.
9. Guarde el resultado como `mi_familia_pubchem.csv` y añada la declaración de uso de IA.

## Criterios de aceptación

- [ ] La función maneja los errores sin detener el programa y devuelve el código cuando falla.
- [ ] Hay una pausa entre consultas y está explicada.
- [ ] La tabla final conserva las doce filas tras la unión.
- [ ] La figura compara los dos log P con la línea de identidad y hay un comentario sobre la diferencia.
- [ ] Los fallos, si los hubo, están documentados con su código.

## Entrega

Archivo `S06_Apellido_Nombre.ipynb` y `mi_familia_pubchem.csv`.

## Errores que van a aparecer

**`404` con `PUGREST.NotFound`** · PubChem no tiene ese compuesto con ese identificador. Pruebe con el nombre en inglés o con el SMILES canónico.

**`400` con `PUGREST.BadRequest`** · Casi siempre es un SMILES con `#` o `/` enviado dentro de la URL. Envíelo en el cuerpo de la petición con `requests.post`, no en la dirección.

**`503` con `PUGREST.ServerBusy`** · El servidor está saturado, probablemente porque toda la clase está consultando a la vez. Aumente la pausa, reintente dos o tres veces, y si sigue fallando use el archivo de respaldo.

**`KeyError: 'PropertyTable'`** · La respuesta no tiene la forma esperada porque fue un error. Imprima `respuesta.text` antes de convertirlo a JSON.

