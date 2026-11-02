---
title: "Cómo funcionan los entregables"
sidebar_label: "Cómo funciona"
description: "Calendario de las diez sesiones, asignación de sistemas químicos, formato de entrega, rúbrica y política de uso de asistentes de IA."
sidebar_position: 1
slug: como-funciona
---

# Cómo funcionan los entregables

El curso tiene **diez sesiones de dos horas**, dos por semana durante cinco semanas. Cada sesión termina con un archivo que usted construye con **sus propios datos** y entrega ese mismo día. No hay tareas acumuladas: lo que se hace en clase es lo que se entrega.

Los diez entregables no son ejercicios sueltos. Todos giran alrededor del mismo sistema químico, el que le toca por número de lista, y en la última sesión se juntan en un informe único. Al terminar el curso usted no tiene diez tareas: tiene un trabajo completo sobre una familia de compuestos.

## Calendario

| Semana | Sesión | Tema | Entregable |
|---|---|---|---|
| 1 | [1](./01-calculos-de-laboratorio.md) | Colab y Python básico | Hoja de cálculos de laboratorio |
| 1 | [2](./02-tablas-y-graficas.md) | Tablas y gráficas | Tabla propia y dos figuras |
| 2 | [3](./03-calibracion.md) | Curva de calibración | Concentración de la muestra con su incertidumbre |
| 2 | [4](./04-cinetica.md) | Cinética y Arrhenius | Orden de reacción y energía de activación |
| 3 | [5](./05-descriptores.md) | Descriptores con RDKit | Tabla de descriptores de su familia |
| 3 | [6](./06-pubchem.md) | Consultas a PubChem | Tabla enriquecida y registro de fallos |
| 4 | [7](./07-espacio-quimico.md) | Similitud y PCA | Mapa del espacio químico |
| 4 | [8](./08-conformeros.md) | Estructuras 3D | Análisis conformacional y archivo XYZ |
| 5 | [9](./09-calculo-cuantico.md) | Química cuántica | HOMO, LUMO y momento dipolar |
| 5 | [10](./10-informe-final.md) | Informe final | Informe reproducible y presentación |

## Su sistema químico

Todo lo que entregue sale de su número de lista. Para consultarlo:

```python
!wget -q -O generar_datos.py https://raw.githubusercontent.com/pesco13/Python-para-Quimica/main/datos/generar_datos.py
from generar_datos import mi_asignacion

print(mi_asignacion(7))   # cambie el 7 por su número
```

| N.º | Familia de compuestos | Analito de calibración | Reacción que sigue |
|---|---|---|---|
| 1 | Agroquímicos | Azul de metileno, 664 nm | Descomposición del peróxido de hidrógeno |
| 2 | Alcaloides y estimulantes | Permanganato de potasio, 525 nm | Hidrólisis del acetato de etilo en medio básico |
| 3 | Aminas y bases nitrogenadas | Dicromato de potasio, 350 nm | Decoloración del cristal violeta con NaOH |
| 4 | Aminoácidos | Complejo Fe(II)-fenantrolina, 510 nm | Reacción del tiosulfato con ácido |
| 5 | Analgésicos y antiinflamatorios | Rojo de metilo, 520 nm | Dimerización del ciclopentadieno |
| 6 | Aromas y fragancias | Anaranjado de metilo, 464 nm | Hidrólisis de la sacarosa |
| 7 | Colorantes e indicadores | Complejo Cu(II)-amoníaco, 610 nm | Yodación de la acetona |
| 8 | Compuestos de azufre | Nitrato de cobalto(II), 510 nm | Descomposición del pentóxido de dinitrógeno |
| 9 | Conservantes alimentarios | Verde de bromocresol, 616 nm | Saponificación del acetato de fenilo |
| 10 | Fenoles y antioxidantes | Cromato de potasio, 372 nm | Oxidación del yoduro por persulfato |
| 11 | Fármacos cardiovasculares | Azul de metileno, 664 nm | Descomposición del peróxido de hidrógeno |
| 12 | Haloalcanos | Permanganato de potasio, 525 nm | Hidrólisis del acetato de etilo en medio básico |
| 13 | Heterociclos | Dicromato de potasio, 350 nm | Decoloración del cristal violeta con NaOH |
| 14 | Hidrocarburos aromáticos | Complejo Fe(II)-fenantrolina, 510 nm | Reacción del tiosulfato con ácido |
| 15 | Moléculas pequeñas y gases | Rojo de metilo, 520 nm | Dimerización del ciclopentadieno |
| 16 | Monómeros de polímeros | Anaranjado de metilo, 464 nm | Hidrólisis de la sacarosa |
| 17 | Plásticos y plastificantes | Complejo Cu(II)-amoníaco, 610 nm | Yodación de la acetona |
| 18 | Polifenoles naturales | Nitrato de cobalto(II), 510 nm | Descomposición del pentóxido de dinitrógeno |
| 19 | Polioles | Verde de bromocresol, 616 nm | Saponificación del acetato de fenilo |
| 20 | Solventes apróticos | Cromato de potasio, 372 nm | Oxidación del yoduro por persulfato |
| 21 | Solventes próticos | Azul de metileno, 664 nm | Descomposición del peróxido de hidrógeno |
| 22 | Sulfonamidas | Permanganato de potasio, 525 nm | Hidrólisis del acetato de etilo en medio básico |
| 23 | Ácidos carboxílicos | Dicromato de potasio, 350 nm | Decoloración del cristal violeta con NaOH |
| 24 | Ácidos grasos | Complejo Fe(II)-fenantrolina, 510 nm | Reacción del tiosulfato con ácido |
| 25 | Ésteres de frutas | Rojo de metilo, 520 nm | Dimerización del ciclopentadieno |
| 26 | Agroquímicos | Anaranjado de metilo, 464 nm | Hidrólisis de la sacarosa |
| 27 | Alcaloides y estimulantes | Complejo Cu(II)-amoníaco, 610 nm | Yodación de la acetona |
| 28 | Aminas y bases nitrogenadas | Nitrato de cobalto(II), 510 nm | Descomposición del pentóxido de dinitrógeno |
| 29 | Aminoácidos | Verde de bromocresol, 616 nm | Saponificación del acetato de fenilo |
| 30 | Analgésicos y antiinflamatorios | Cromato de potasio, 372 nm | Oxidación del yoduro por persulfato |

![Ejemplo de los datos que recibe cada estudiante](/img/datos-por-estudiante.png)

*Tres calibraciones distintas, una por número de lista, y la serie cinética a cuatro temperaturas de uno de ellos.*

Si su número es mayor que 30, la asignación se repite cíclicamente; el generador funciona con cualquier número entero positivo.

Los datos de calibración y de cinética **se generan con su número y son distintos para cada persona**, pero siempre los mismos para usted: si vuelve a correr la celda dentro de tres semanas, obtiene exactamente los mismos valores. Dos consecuencias prácticas: no puede entregar el trabajo de otra persona, y si pierde el archivo lo recupera corriendo una celda.

## Cómo se entrega

1. Trabaje sobre su copia en Drive (*Archivo › Guardar una copia en Drive*).
2. Renombre el archivo como `S03_Apellido_Nombre.ipynb`, con el número de sesión en dos dígitos, sin espacios y sin tildes.
3. *Compartir › Acceso general › Cualquier persona con el enlace › Lector*. Sin ese paso el enlace no abre y la entrega no cuenta.
4. Suba el enlace a la tarea correspondiente en el aula virtual de la asignatura, antes de que termine la sesión. Lo que se entrega es el **enlace**, no el archivo: así el profesor ve siempre la última versión y usted no tiene que volver a exportar nada.
5. Antes de entregar, use *Entorno de ejecución › Reiniciar y ejecutar todo*. Si el notebook no corre de arriba abajo sin intervención, todavía no está listo.

Ese último punto es el que más entregas arruina. Un notebook que solo funciona si se ejecutan las celdas en cierto orden no es reproducible, y la primera línea de la rúbrica lo penaliza.

## Rúbrica

La misma para las diez sesiones. Cuatro criterios, cuatro niveles, doce puntos en total.

| Criterio | 0 · Insuficiente | 1 · En desarrollo | 2 · Competente | 3 · Destacado |
|---|---|---|---|---|
| **El código corre** | No se ejecuta o falta el enlace | Corre con errores en alguna celda | Corre de principio a fin tras reiniciar | Además incluye comprobaciones propias con `assert` |
| **Corrección química** | Resultado equivocado o sin unidades | Resultado correcto pero con unidades o cifras significativas mal | Resultado correcto, con unidades y cifras adecuadas | Además discute la incertidumbre o los supuestos del método |
| **Figuras y tablas** | Faltan o no se entienden | Presentes, sin etiquetas ni unidades | Ejes etiquetados con unidades y título informativo | Calidad de informe: 300 dpi, barras de error, anotación pertinente |
| **Interpretación** | No hay texto propio | Describe lo que hizo, no lo que significa | Explica qué significa el resultado | Relaciona con la estructura química o con lo visto en otras asignaturas |

La nota de cada sesión es la suma de los cuatro criterios sobre doce. El informe final de la sesión 10 vale el doble.

## Uso de asistentes de IA

Puede usarlos, con tres condiciones:

1. **Declárelo.** La última celda de cada entregable debe decir si usó un asistente, para qué, y qué cambió usted del resultado. Una o dos frases bastan.
2. **Entienda lo que entrega.** En clase se le puede pedir que explique cualquier línea de su notebook. Si no puede explicarla, esa parte no cuenta, aunque el resultado sea correcto.
3. **Los datos y las conclusiones son suyos.** El asistente puede ayudarle a entender un error o a recordar una función; no puede interpretar sus resultados por usted.

No declarar el uso sí es una falta. Usarlo y declararlo no resta ni un punto.

## Entregas fuera de plazo

Hasta 48 horas después: se califica sobre el 80 %, salvo que la normativa de la asignatura diga otra cosa. Más allá, solo con justificación documentada. Si durante la sesión se queda atascado, avise en el momento: es mucho más fácil desatascar un error en clase que recuperar una entrega perdida.

## Antes de la primera sesión

- Tenga una cuenta de Google activa y compruebe que puede abrir [un notebook de ejemplo](../practicas/00-bienvenida-a-colab.md) en Colab.
- Anote su número de lista.
- Traiga audífonos: parte del trabajo es leer documentación y buscar errores a su propio ritmo.
