# pip install matplotlib
# pip install pandas

import matplotlib.pyplot as plt
import pandas as pd
import solutions_analisis
import sets


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

    dataFrame = pd.DataFrame(
        {
            "Tiempo hasta comenzar": scaloni_sum_from_order,
            "Tiempo de Scaloni": scaloni_from_order,
            "Tiempo de asistente": ayudante_from_order,
        }
    )
    
    plt.style.use('ggplot')
    dataFrame.plot.bar(stacked=True, color=['whitesmoke', 'skyblue', 'steelblue'])
    plt.title(title)
    plt.xlabel("Videos")
    plt.ylabel("Duración")
    #plt.ylim([0, 12]) #Para poder comparar entre gráficos, fijar el alto del eje Y
    plt.show()


# Correr con:
#make_graph_from_analisis_order(solutions_analisis.get_optimal_order_from_txt("./casos_prueba_catedra/10-elem.txt"))
#make_graph_from_analisis_order([(1, 8), (5, 1), (3, 3),])
#make_graph_from_analisis_order([ [3,6],[2,5],[4,1], ]) 