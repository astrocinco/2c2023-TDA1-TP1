
# TDA1-TP1

- [TDA1-TP1](#tda1-tp1)
  - [Ejecución de archivos](#ejecución-de-archivos)
    - [solutions.py](#solutionspy)
    - [sets.py](#setspy)
  - [Gráficos y análisis](#gráficos-y-análisis)

## Ejecución de archivos

### solutions.py

    python3 solutions.py [filename] --FLAGS

- Recibe como **primer parámetro** la ruta de un archivo con el dataset a pronar.
- Recibe como **segundo parámetro** el método para resolver el problema con dicho dataset.

        -a # solución alternativa (ordenar de menor a mayor según el tiempo de Scaloni)
        -r # solución aleatoria (devuelve un ordenamiento aleatorio de set)
        -b # solución por fuerza bruta (compara todas las permutaciones y devuelve la mejor)
        
        default: nuestra propuesta de solución (ordenar de mayor a menor según el tiempo de los ayudantes)

### sets.py

    python3 sets.py [n]

Crea un archivo en casos_prueba con una cantidad n de elementos aleatorios

## Gráficos y análisis

Dentro de la jupyter notebook **solutions_graphic_analisis.ipynb** se encuentra la ejecución de todas las funciones auxiliares para la obtención de los gráficos y resultados del análisis de los sets. No se requiere ejecutar, unicamente se encuentra para una mejor comprensión de lo que se realizó.
