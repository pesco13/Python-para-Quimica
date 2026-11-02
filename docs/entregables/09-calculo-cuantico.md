---
title: "Sesión 09 · Primer cálculo cuántico"
sidebar_label: "09 · Cálculo cuántico"
description: "Hartree-Fock y DFT con dos bases, orbitales frontera, brecha HOMO-LUMO y momento dipolar."
sidebar_position: 10
slug: calculo-cuantico
---

# Sesión 09 · Primer cálculo cuántico

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pesco13/Python-para-Quimica/blob/main/notebooks/07_Primer_calculo_cuantico_PySCF.ipynb)

**Objetivo.** Obtener la energía, los orbitales frontera y el momento dipolar de una molécula pequeña de su familia, comparando dos métodos y dos conjuntos base.

**Duración.** 2 horas.

| Tiempo | Qué se hace |
|---|---|
| 0:00 – 0:40 | Qué resuelve un cálculo de estructura electrónica, Hartree–Fock y DFT ([práctica 07](../practicas/07-primer-calculo-cuantico-pyscf.md)) |
| 0:40 – 1:05 | Conjuntos base, unidades de energía, HOMO y LUMO |
| 1:05 – 1:15 | Pausa |
| 1:15 – 1:50 | Construcción del entregable |
| 1:50 – 2:00 | Verificación y entrega |

## Antes de la sesión

- Elija de su familia la molécula **más pequeña**, de menos de quince átomos pesados. Un cálculo cuántico sobre una molécula grande no termina en una sesión de Colab.
- Tenga a mano el archivo XYZ de la sesión 8 si corresponde a esa molécula.

## Paso a paso del entregable

1. Construya la molécula en PySCF a partir de su geometría 3D. Diga cuántos electrones tiene y verifique que la multiplicidad es coherente.
2. Haga un cálculo Hartree–Fock con la base STO-3G. Reporte la energía total en hartree **y** en kJ/mol.
3. Repita con la base 6-31G(d). Compare las dos energías y explique por qué la segunda es más baja.
4. Haga un cálculo DFT con el funcional B3LYP y la base 6-31G(d). Compare con Hartree–Fock y explique qué describe el DFT que HF no.
5. Obtenga las energías del HOMO y del LUMO y la brecha entre ellos. Conviértala a eV y estime a qué longitud de onda correspondería.
6. Calcule el momento dipolar y compárelo con lo que esperaría por la estructura: dónde están los átomos electronegativos.
7. Repita el cálculo del dipolo con otra conformación de la molécula, si tiene más de una. ¿Cambia? Comente qué implica eso.
8. Arme una tabla comparativa con método, base, energía total, brecha HOMO–LUMO y tiempo de cálculo.
9. Escriba tres frases sobre qué significa que la energía baje al aumentar la base, y por qué **no** se pueden comparar energías de métodos o bases distintos.
10. Declaración de uso de IA.

## Criterios de aceptación

- [ ] Las energías se reportan en hartree y convertidas a una unidad química, con la conversión explícita en el código.
- [ ] Están los cuatro cálculos de la tabla comparativa, con su tiempo.
- [ ] La brecha HOMO–LUMO está en eV y hay una estimación de longitud de onda.
- [ ] El momento dipolar está interpretado con la estructura en la mano, no solo reportado.
- [ ] Está la advertencia sobre comparar energías de métodos distintos.

## Entrega

Archivo `S09_Apellido_Nombre.ipynb` y la tabla comparativa como CSV.

## Errores que van a aparecer

**`Electron number 9 and spin 0 are not consistent`** · Un número impar de electrones no puede tener multiplicidad de capa cerrada. Fije `spin=1` o revise la carga.

**`SCF not converged`** · El ciclo autoconsistente no encontró solución. Aumente el número máximo de iteraciones, pruebe otra geometría de partida o una base más pequeña.

**El cálculo lleva veinte minutos y no termina** · La molécula es demasiado grande para la base elegida. Baje a STO-3G o elija una molécula más pequeña: no es un fracaso, es una decisión de método, y así debe reportarse.

**La sesión de Colab se desconecta** · Guarde los resultados parciales en un CSV a medida que los obtiene, en vez de dejarlos solo en memoria.

