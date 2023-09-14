#  pip install matplotlib

import matplotlib.pyplot as plt
import solutions


def make_graph_from_analisis_order(analisis_order):
    def aux_generate_x_axis(length):
        lista = []
        for i in range(length):
            lista.append(str(i))
        return lista
    
    x_axis = aux_generate_x_axis(len(analisis_order))
    scaloni_sum_from_order = []
    scaloni_from_order = []
    ayudante_from_order = []

    def aux_lists_for_plot():
        scaloni_backlog = 0
        for tupla in analisis_order:
            scaloni_sum_from_order.append(scaloni_backlog)
            scaloni_from_order.append(scaloni_backlog + tupla[0])
            ayudante_from_order.append(tupla[1])
            scaloni_backlog += tupla[0]
    
    plt.title('Gráfico de orden de analisis')
    plt.xlabel('Orden')
    plt.ylabel('Tiempo')
    aux_lists_for_plot()
    
    plt.bar(x_axis, scaloni_sum_from_order, color='whitesmoke')
    plt.bar(x_axis, scaloni_from_order, bottom=scaloni_sum_from_order, color='skyblue')
    plt.bar(x_axis, ayudante_from_order, bottom=scaloni_from_order, color='steelblue')
    plt.show()


# Celeste: Scaloni
# Azul: Ayudante
make_graph_from_analisis_order(solutions.run_from_txt_data_set("3 elem.txt"))

# No funciona, pero solución está acá
# https://stackoverflow.com/questions/71654486/stacked-bar-chart-with-multiple-variables-in-python