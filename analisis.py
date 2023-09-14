import main as m
import matplotlib.pyplot as plt
import numpy as np

def random_case(teams_list):
    from random import shuffle
    shuffle(teams_list)

    return teams_list

def counter_example(teams_list):
    example_order = sorted(teams_list, key= lambda team:team[1], reverse = False)

    return example_order

def compare_solutions(data_set_size, amount):
    
    for i in range(amount):
        teams_list = m.make_teams_list(data_set_size)
        m.aux_get_analisis_duration(m.get_optimal_analisis_order(teams_list))
        analisis_optimo = m.aux_get_analisis_duration(m.get_optimal_analisis_order(teams_list))
        no_optimo = m.aux_get_analisis_duration(counter_example(teams_list))
        analisis_random = m.aux_get_analisis_duration(random_case(teams_list))
        print(f"OPTIMO : {analisis_optimo}, NO OPTIMO : {no_optimo}, RANDOM : {analisis_random}")
        if no_optimo < analisis_optimo or analisis_random < analisis_optimo:
            print(f"FALLó EL ANALISIS ..... OPTIMO : {analisis_optimo}, NO OPTIMO : {no_optimo}, RANDOM : {analisis_random}. DATA SET {teams_list}")
            break
    print("todo salio bien!")



# Idea para grafico: comparo el valor optimo con, probablemente, todos los ordenamientos posibles
def random_graph():

    x=[]
    y_rand=[]
    data_size = 5
    teams_list = m.make_teams_list(data_size)
    y_opt = []
    for i in range(200):
        x.append(i)    
        y_opt.append(m.aux_get_analisis_duration(m.get_optimal_analisis_order(teams_list)))
        y_rand.append( m.aux_get_analisis_duration(random_case(teams_list)))    
    fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')  # Create a figure containing a single axes.
    ax.plot(x,y_opt, label="optimo")
    ax.plot(x ,y_rand,label="random")

    ax.legend()

    plt.show()

random_graph()
