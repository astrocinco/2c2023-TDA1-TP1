# pip install matplotlib
# pip install pandas

import matplotlib.pyplot as plt
import pandas as pd

def make_execution_time_graph(time_execution, title="Gráfico de tiempo de ejecución"):
    plt.style.use('ggplot')
    time_execution.plot()
    plt.title(title)
    plt.xlabel("Cantidad de elementos por set")
    plt.ylabel("Tiempo [ms]")
    plt.show()

def method_difference_normalizated(df, solution, method):
    df[method] = (df[method] - solution) / df.index
    
def make_graph_for_different_method_durations(durations, solution, df_name):
    
    df = durations
    
    sol = df[solution]
    df = df.drop(columns=[solution], axis=1)

    method_difference_normalizated(df, sol, "optimal")
    method_difference_normalizated(df, sol, "alternative")
    method_difference_normalizated(df, sol, "random")

    plt.style.use('ggplot')
    df.plot.bar(stacked=False)
    plt.title("Gráfico comparativo entre diferentes métodos para " + df_name)
    plt.xlabel("Cantidad de elementos por set")
    plt.ylabel("Duración")
    plt.show()
    
def make_graph_from_analisis_order(analisis_order, title="Gráfico de orden óptimo"):
    # Recibe un analisis order (lista de tuplas) e imprime en pantalla su gráfico
    scaloni_sum_from_order = []
    scaloni_from_order = []
    ayudante_from_order = []

    scaloni_backlog = 0
    for tupla in analisis_order:
        scaloni_sum_from_order.append(scaloni_backlog)
        scaloni_from_order.append(tupla[0])
        ayudante_from_order.append(tupla[1])
        scaloni_backlog += tupla[0]

    df = pd.DataFrame(
        {
            "Tiempo hasta comenzar": scaloni_sum_from_order,
            "Tiempo de Scaloni": scaloni_from_order,
            "Tiempo de asistente": ayudante_from_order,
        }
    )
    
    plt.style.use('ggplot')
    df.plot.bar(stacked=True, color=['whitesmoke', 'skyblue', 'steelblue'])
    plt.title(title)
    plt.xlabel("Videos")
    plt.ylabel("Duración")
    plt.show()
