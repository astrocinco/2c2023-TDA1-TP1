# pip install matplotlib
# pip install pandas

import matplotlib.pyplot as plt
import pandas as pd


#Grafica el tiempo de ejecución dado un dataframe (acepta que tenga más de un método)
def make_execution_time_graph(time_execution, title="Gráfico de tiempo de ejecución"):
    plt.style.use('ggplot')
    time_execution.plot()
    plt.title(title)
    plt.xlabel("Cantidad de elementos por set")
    plt.ylabel("Tiempo [ms]")
    plt.show()

#Dada un dataframe con las duraciones obtenidas por diferentes metodos y una columna de soluciones,
#grafica la diferencia entre las solucion y la respuesta de cada metodo 
def make_graph_for_different_method_durations(durations, solution, df_name):
    df = durations
    serie_solution = df[solution]
    df = df.drop(columns=[solution], axis=1)

    df.our_proposal = df.our_proposal - serie_solution
    df.alternative = df.alternative - serie_solution
    df.random = df.random - serie_solution

    plt.style.use('ggplot')
    df.plot.bar(stacked=False)
    plt.title("Diferencia de resultado con la respuesta óptima para " + df_name)
    plt.xlabel("Cantidad de elementos por set")
    plt.ylabel("Resultado del analisis")
    plt.yscale('log')
    plt.show()
    

# Recibe un analisis order (lista de tuplas) e imprime en pantalla su gráfico
def make_graph_from_analisis_order(analisis_order, title="Gráfico de orden óptimo"):
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
