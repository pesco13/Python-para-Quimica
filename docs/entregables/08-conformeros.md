---
title: "Sesión 08 · Estructuras 3D y conformeros"
sidebar_label: "08 · Conformeros"
description: "Búsqueda conformacional con ETKDG y MMFF94, poblaciones de Boltzmann y geometría de mínima energía en XYZ."
sidebar_position: 9
slug: conformeros
---

# Sesión 08 · Estructuras 3D y conformeros

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pesco13/Python-para-Quimica/blob/main/notebooks/06_Estructuras_3D_y_conformeros.ipynb)

**Objetivo.** Generar y analizar los conformeros de la molécula más flexible de su familia, y entregar su geometría de menor energía en formato XYZ.

**Duración.** 2 horas.

| Tiempo | Qué se hace |
|---|---|
| 0:00 – 0:35 | De 2D a 3D con ETKDG, qué calcula un campo de fuerza ([práctica 06](../practicas/06-estructuras-3d-y-conformeros.md)) |
| 0:35 – 1:05 | Búsqueda conformacional y poblaciones de Boltzmann |
| 1:05 – 1:15 | Pausa |
| 1:15 – 1:50 | Construcción del entregable |
| 1:50 – 2:00 | Verificación y entrega |

## Antes de la sesión

- Mire la columna de enlaces rotables de su tabla de la sesión 5 e identifique su compuesto más flexible y el más rígido.

## Paso a paso del entregable

1. Elija de su familia el compuesto con más enlaces rotables. Diga cuántos tiene y por qué eso anticipa muchos conformeros.
2. Genere su estructura 3D con ETKDG, añadiendo hidrógenos explícitos antes de embeber. Use una semilla fija para que el resultado sea reproducible.
3. Optimice con MMFF94 y verifique que la optimización convergió, es decir que devolvió cero.
4. Genere entre 50 y 100 conformeros, optimícelos todos y arme una tabla con la energía de cada uno.
5. Haga un histograma de las energías. ¿Hay grupos separados o un continuo? Comente qué significa cada caso.
6. Calcule la diferencia de energía entre el conformero más estable y el siguiente grupo, y estime con la distribución de Boltzmann qué fracción de moléculas habría en cada uno a 25 °C.
7. Visualice el conformero más estable con py3Dmol y guarde su geometría en un archivo `.xyz`.
8. Repita los pasos 2 a 4 con su compuesto **más rígido** y compare el número de conformeros distintos y el rango de energías. Una frase de conclusión.
9. Escriba tres frases sobre qué limitaciones tiene este análisis: qué no puede describir un campo de fuerza.
10. Declaración de uso de IA.

## Criterios de aceptación

- [ ] Se añadieron los hidrógenos antes de generar la geometría 3D y se usó semilla fija.
- [ ] Se comprobó que la optimización convergió.
- [ ] El histograma de energías está presente y comentado.
- [ ] El archivo XYZ del conformero más estable se entrega y se abre correctamente.
- [ ] Está la comparación entre el compuesto flexible y el rígido, y las limitaciones del campo de fuerza.

## Entrega

Archivo `S08_Apellido_Nombre.ipynb`, el archivo `.xyz` y el histograma.

## Errores que van a aparecer

**`EmbedMolecule` devuelve −1** · No encontró una geometría válida. Aumente `maxAttempts`, o revise si el SMILES tiene una valencia imposible.

**La geometría sale aplastada o los hidrógenos mal puestos** · Olvidó `Chem.AddHs(mol)` antes de embeber. RDKit no puede colocar átomos que no existen en el objeto.

**MMFF no funciona con su compuesto** · El campo de fuerza no tiene parámetros para metales ni para algunos elementos poco comunes. Si su familia tiene una sal, trabaje con el fragmento orgánico y dígalo.

**El visor 3D no aparece** · En Colab hay que habilitar la salida personalizada. La práctica 06 trae la línea necesaria; ejecútela antes de crear el visor.

