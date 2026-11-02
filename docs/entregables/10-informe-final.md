---
title: "Sesión 10 · Informe final"
sidebar_label: "10 · Informe final"
description: "Montaje del informe reproducible con registro de entorno, verificación del portafolio y presentación de cinco minutos."
sidebar_position: 11
slug: informe-final
---

# Sesión 10 · Informe final

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pesco13/Python-para-Quimica/blob/main/notebooks/11_Informe_reproducible.ipynb)

**Objetivo.** Convertir los nueve entregables anteriores en un informe único y reproducible sobre su familia de compuestos, y presentarlo en cinco minutos.

**Duración.** 2 horas.

| Tiempo | Qué se hace |
|---|---|
| 0:00 – 0:30 | Estructura de carpetas, registro del entorno, estilo común de figuras |
| 0:30 – 0:50 | Cómo se escribe una sección de métodos reproducible |
| 0:50 – 1:00 | Pausa |
| 1:00 – 1:35 | Montaje del informe |
| 1:35 – 2:00 | Presentaciones de cinco minutos |

## Antes de la sesión

- Tenga los nueve entregables anteriores accesibles en su Drive.
- Decida cuál es **el resultado principal** de su trabajo: el número que pondría en el resumen si solo pudiera poner uno.

## Paso a paso del entregable

1. Cree la estructura de carpetas `datos/`, `resultados/` y `resultados/figuras/`, y copie en ellas lo que produjo durante el curso.
2. Renombre todas las figuras con el formato `figNN_nombre.png` y renumere en el orden en que aparecen en el informe.
3. Aplique el estilo común de figuras y **regenere** las figuras principales con él, para que las nueve no parezcan de nueve autores distintos.
4. Ejecute la celda de registro del entorno y guarde `entorno.txt`.
5. Rellene la plantilla del informe: resumen, introducción, métodos, resultados, discusión, conclusiones, referencias y anexo.
6. Escriba la sección de métodos siguiendo la regla de las cuatro preguntas: qué datos, qué se les hizo, con qué herramienta y con qué parámetros.
7. Ponga pie a todas las figuras y tablas, numerados, diciendo qué muestran y con qué n.
8. Complete la lista `ESPERADOS` con sus diez archivos y ejecute la verificación del portafolio. No entregue hasta que no falte ninguno.
9. Escriba un `README.md` que explique qué hay en cada carpeta y en qué orden se ejecuta todo.
10. Prepare tres diapositivas, o tres celdas, para su presentación: qué le tocó, qué encontró, qué no pudo concluir.

## Criterios de aceptación

- [ ] El informe tiene las nueve secciones de la plantilla, todas con contenido propio.
- [ ] El resumen incluye el resultado principal **con su incertidumbre**.
- [ ] Todas las figuras tienen pie numerado y comparten el mismo estilo.
- [ ] `entorno.txt` está presente y corresponde a la ejecución entregada.
- [ ] La verificación del portafolio corre y no reporta archivos faltantes.
- [ ] La sección de métodos permitiría a otra persona repetir el trabajo sin preguntarle nada.

## Entrega

Carpeta completa en Drive, compartida con permiso de lectura, más el enlace al notebook `S10_Apellido_Nombre.ipynb`. **Este entregable vale el doble** que los anteriores.

## La presentación de cinco minutos

Tres minutos de exposición y dos de preguntas. Una estructura que funciona:

1. **Treinta segundos:** qué familia le tocó y por qué tiene interés químico.
2. **Un minuto:** el resultado experimental, la concentración o la energía de activación, con su incertidumbre y una figura.
3. **Un minuto:** lo que aprendió de la estructura de sus compuestos, con el mapa del espacio químico o los descriptores.
4. **Treinta segundos:** una cosa que no pudo concluir y qué haría falta para concluirla.

Ese último punto es el que más se valora. Reconocer los límites de un resultado es la parte del oficio que más tarda en aprenderse.

## Errores que van a aparecer

**El notebook no corre tras reiniciar** · Hay celdas que dependen de variables definidas en otro notebook. Todo lo que el informe necesita debe estar en el informe, o cargarse desde un archivo de `datos/`.

**Las figuras se ven distintas entre sí** · No regeneró las antiguas con el estilo común. Vuelva al paso 3.

**Las rutas no existen en otra máquina** · Usó rutas absolutas del tipo `/content/drive/MiUnidad/...`. Use rutas relativas a la carpeta del informe.

**El resumen no tiene ningún número** · Un resumen sin resultado cuantitativo no es un resumen. Ponga el valor principal con su unidad y su incertidumbre.

