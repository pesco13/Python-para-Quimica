---
title: "07 · Primer cálculo de química cuántica con PySCF"
sidebar_label: "07 · Química cuántica con PySCF"
description: "Las aproximaciones detrás de Hartree–Fock y DFT, cómo elegir un conjunto base y cómo leer las energías."
sidebar_position: 8
slug: 07-primer-calculo-cuantico-pyscf
---

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pesco13/Python-para-Quimica/blob/main/notebooks/07_Primer_calculo_cuantico_PySCF.ipynb)

El código de esta práctica está en Colab. Esta página explica la teoría que la acompaña, reúne los errores más frecuentes y propone retos para después de clase.

## Conceptos

### El problema que se quiere resolver

En principio, toda la química de una molécula está en la ecuación de Schrödinger independiente del tiempo:

$$
\hat{H}\,\Psi = E\,\Psi
$$

$\hat{H}$, el hamiltoniano, suma las energías cinéticas y las atracciones y repulsiones entre núcleos y electrones; $\Psi$ es la función de onda y $E$ la energía. La ecuación solo tiene solución exacta para sistemas de un electrón, como el átomo de hidrógeno. Para todo lo demás se necesitan aproximaciones.

La primera es la de Born–Oppenheimer. Los núcleos pesan miles de veces más que los electrones, así que se dejan quietos en su lugar (por eso el cálculo pide coordenadas) y solo se resuelve el movimiento de los electrones.

La segunda es usar orbitales. Cada electrón ocupa un orbital molecular, que se escribe como combinación de funciones conocidas centradas en los átomos, llamadas conjunto base:

$$
\phi_i = \sum_{\mu} c_{\mu i}\,\chi_{\mu}
$$

El cálculo consiste en encontrar los coeficientes $c_{\mu i}$.

### Hartree–Fock y el ciclo autoconsistente

En Hartree–Fock cada electrón siente a los demás solo como una nube promedio. Esa nube depende de los orbitales que se están buscando, así que el cálculo se hace por rondas. Se propone un juego inicial de orbitales, con ellos se calcula el campo promedio de los electrones, en ese campo se obtienen orbitales nuevos y se repite hasta que la energía y los orbitales dejan de cambiar.

Este procedimiento se llama campo autoconsistente (SCF, por su sigla en inglés). Por eso PySCF escribe `converged SCF energy` al terminar.

### Correlación electrónica y DFT

Al usar un promedio, Hartree–Fock no tiene en cuenta que los electrones se esquivan unos a otros en cada instante. La energía que falta por eso se llama energía de correlación:

$$
E_{\text{corr}} = E_{\text{exacta}} - E_{\text{HF}}
$$

Es menos del 1 % de la energía total, pero es del mismo tamaño que las energías de enlace y de reacción, así que en química importa mucho.

La teoría del funcional de la densidad (DFT) calcula la energía a partir de la densidad electrónica e incluye la correlación de forma aproximada mediante un funcional. B3LYP, el del notebook, es un funcional híbrido porque mezcla una parte de Hartree–Fock. Hay cientos de funcionales, y elegir uno es parte de diseñar el cálculo.

### Conjuntos base

| Base | Tipo | Comentario |
|---|---|---|
| STO-3G | Mínima | Una función por orbital atómico. Rápida y poco exacta |
| 6-31G* | Valencia desdoblada con polarización | Buen equilibrio para moléculas orgánicas |
| cc-pVDZ | Familia de correlación consistente | Se puede mejorar paso a paso (cc-pVTZ, cc-pVQZ…) |

Con más funciones, los electrones se describen con más libertad: la energía baja y el cálculo se vuelve más lento. El costo de Hartree–Fock crece más o menos con la cuarta potencia del número de funciones, así que duplicar la base puede hacer el cálculo unas 16 veces más lento.

### Unidades de energía

PySCF trabaja en hartree (Ha), la unidad atómica de energía:

| 1 Ha equivale a | |
|---|---|
| electronvoltios | 27.2114 eV |
| kcal/mol | 627.509 kcal/mol |
| kJ/mol | 2625.50 kJ/mol |

La energía total de una molécula (unos −76 Ha para el agua) no dice nada por sí sola. Lo que tiene sentido químico son las diferencias de energía calculadas con el mismo método y la misma base.

### HOMO, LUMO y moléculas con electrones desapareados

El HOMO es el orbital ocupado de mayor energía y el LUMO el desocupado de menor energía. La diferencia entre los dos se relaciona con la reactividad y con la luz que absorbe la molécula. Según el teorema de Koopmans, en Hartree–Fock el valor $-\varepsilon_{\text{HOMO}}$ se aproxima a la energía de ionización; con DFT esa relación es menos confiable.

Los métodos restringidos (RHF, RKS) ponen dos electrones en cada orbital. Funcionan para moléculas con todos los electrones apareados, pero no para radicales ni para enlaces que se rompen; en esos casos se usan los métodos no restringidos (UHF, UKS). Por eso la curva del H₂ del notebook falla a distancias grandes.

## Errores comunes

### `Electron number 9 and spin 0 are not consistent`

La molécula tiene un número impar de electrones (es un radical, como el OH) y se dejó `spin=0`. Indique los electrones desapareados con `spin=1` y use un método no restringido: `scf.UHF(mol)`.

### `SCF not converged`

El ciclo no se estabilizó dentro del número de rondas permitido. Pasa a menudo con geometrías malas o con metales. Parta de una geometría razonable (práctica 06), aumente las rondas con `mf.max_cycle = 200` o use `mf.level_shift = 0.3`.

### Las energías no tienen sentido

Las coordenadas estaban en bohr y PySCF las leyó en Å, que es lo que espera por defecto (o al revés). Si sus coordenadas están en bohr, indíquelo: `gto.M(..., unit="Bohr")`.

### Se comparan energías de métodos o bases distintos

Una energía B3LYP/6-31G* y otra HF/cc-pVDZ no se pueden comparar. Calcule todas las especies de una reacción con el mismo método y la misma base.

### La sesión de Colab se cae o tarda demasiado

La base o la molécula son demasiado grandes para la memoria o el tiempo disponibles. Pruebe primero con una base pequeña (STO-3G) y amplíela después, y use moléculas con pocos átomos pesados.

## Retos adicionales

1. Calcule la energía del radical hidroxilo (OH) con `spin=1` y `scf.UHF`. ¿Qué pasa si intenta usar `scf.RHF`?
2. Calcule con B3LYP/6-31G* la diferencia de energía entre el etanol y el dimetil éter (isómeros C₂H₆O), con geometrías generadas en la práctica 06. ¿Cuál es más estable y por cuántos kJ/mol?
3. Repita la curva de energía potencial del H₂ con `dft.UKS` y compárela con la de `RKS`. Para que UKS se separe de la solución restringida, parta de una densidad inicial asimétrica. Explique por qué solo UKS se acerca al valor correcto a distancias grandes.
4. Calcule el momento dipolar del CO₂ y del H₂O y explique la diferencia a partir de la geometría de cada molécula.

## Glosario

| Término | Significado |
|---|---|
| Función de onda | Función que contiene toda la información de los electrones |
| Hartree–Fock | Método en el que cada electrón siente un campo promedio de los demás |
| Campo autoconsistente (SCF) | Procedimiento que repite el cálculo hasta que el resultado deja de cambiar |
| Correlación electrónica | Parte de la interacción entre electrones que Hartree–Fock no incluye |
| DFT | Teoría que calcula la energía a partir de la densidad electrónica |
| Funcional | Fórmula de DFT que aproxima el intercambio y la correlación (B3LYP, PBE…) |
| Conjunto base | Funciones con las que se construyen los orbitales moleculares |
| HOMO / LUMO | Orbital ocupado más alto / orbital desocupado más bajo |
| Hartree (Ha) | Unidad atómica de energía |

## Para saber más

- [Guía de usuario de PySCF](https://pyscf.org/user.html) (en inglés)
- [Basis Set Exchange](https://www.basissetexchange.org), catálogo de conjuntos base (en inglés)
- Sun, Q. et al. (2020). Recent developments in the PySCF program package. *J. Chem. Phys.*, 153, 024109.
- Szabo, A. & Ostlund, N. S. (1996). *Modern Quantum Chemistry*. Dover.
- Cramer, C. J. (2004). *Essentials of Computational Chemistry* (2.ª ed.). Wiley.
- Jensen, F. (2017). *Introduction to Computational Chemistry* (3.ª ed.). Wiley.
