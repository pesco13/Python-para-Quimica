---
title: "Sesión 07 · Espacio químico"
sidebar_label: "07 · Similitud y PCA"
description: "Matriz de Tanimoto, PCA estandarizado y tres conclusiones defendibles sobre la familia asignada."
sidebar_position: 8
slug: espacio-quimico
---

# Sesión 07 · Espacio químico

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pesco13/Python-para-Quimica/blob/main/notebooks/05_Similitud_y_espacio_quimico.ipynb)

**Objetivo.** Construir el mapa del espacio químico de su familia y defender por escrito tres conclusiones que se puedan sostener con él.

**Duración.** 2 horas.

| Tiempo | Qué se hace |
|---|---|
| 0:00 – 0:35 | Huellas de Morgan y coeficiente de Tanimoto ([práctica 05](../practicas/05-similitud-y-espacio-quimico.md)) |
| 0:35 – 1:05 | PCA: qué es una componente principal y qué significa la varianza explicada |
| 1:05 – 1:15 | Pausa |
| 1:15 – 1:50 | Construcción del entregable |
| 1:50 – 2:00 | Verificación y entrega |

## Antes de la sesión

- Tenga su archivo `mi_familia_pubchem.csv`.
- Lea qué es el principio de similitud y qué supone.

## Paso a paso del entregable

1. Calcule la huella de Morgan de sus doce compuestos con radio 2 y 2048 bits.
2. Construya la matriz de similitud de Tanimoto de todos contra todos y represéntela como un mapa de calor con los nombres en ambos ejes.
3. Identifique el par más parecido y el par más distinto. Dibuje las cuatro estructuras y comente si la similitud calculada coincide con lo que ve.
4. Haga un PCA sobre los descriptores numéricos de su tabla. **Estandarice antes**: si no lo hace, la masa molar domina el mapa por tener los números más grandes.
5. Reporte qué porcentaje de la varianza explican las dos primeras componentes. Si suman menos del 60 %, dígalo: el mapa plano pierde información.
6. Haga el gráfico de dispersión de las dos primeras componentes, con los nombres de los compuestos etiquetados o al menos los de los extremos.
7. Mire los coeficientes de la primera componente y diga qué descriptor pesa más en ella. Traduzca eso a lenguaje químico: si pesa el log P, la primera componente separa compuestos por lipofilia.
8. Escriba **tres conclusiones** sobre su familia que se puedan defender con las dos figuras, y **una** que le gustaría sacar pero que los datos no permiten.
9. Guarde las dos figuras a 300 dpi y añada la declaración de uso de IA.

## Criterios de aceptación

- [ ] Los descriptores están estandarizados antes del PCA y se nota en el código.
- [ ] Se reporta la varianza explicada de las dos primeras componentes.
- [ ] El mapa de calor de Tanimoto tiene los nombres legibles en ambos ejes.
- [ ] Hay tres conclusiones defendibles y una que se reconoce como no defendible.
- [ ] La interpretación de la primera componente está en lenguaje químico, no solo en números.

## Entrega

Archivo `S07_Apellido_Nombre.ipynb` y las dos figuras.

## Errores que van a aparecer

**`DeprecationWarning` al calcular la huella** · La función antigua sigue funcionando pero va a desaparecer. Use el generador de huellas nuevo de RDKit; la práctica 05 trae la línea exacta.

**Un solo descriptor domina el mapa** · Olvidó estandarizar. Reste la media y divida por la desviación estándar, o use `StandardScaler` de scikit-learn.

**Todas las similitudes dan muy altas** · Es normal dentro de una misma familia química: comparten esqueleto. Compare con un compuesto de otra familia para tener referencia.

**Las etiquetas se amontonan** · Con doce puntos, etiquete solo los extremos y los dos más parecidos, y deje el resto sin nombre.

