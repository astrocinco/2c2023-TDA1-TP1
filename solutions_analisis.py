import solutions
import sets
import time
import matplotlib.pyplot as plt
import numpy as np


def compare_solutions(data_set_size, amount):
    for i in range(amount):
        teams_list = sets.get_random_teams_list(data_set_size)
        # main.get_analisis_duration(main.get_optimal_analisis_order(teams_list)) 
        duration_analisis_optimo = solutions.get_analisis_duration(solutions.get_optimal_analisis_order(teams_list))
        duration_analisis_no_optimo = solutions.get_analisis_duration(solutions.get_alternative_analisis_order(teams_list))
        duration_analisis_random = solutions.get_analisis_duration(solutions.get_random_analisis_order(teams_list))

        #print(f"OPTIMO : {analisis_optimo}, NO OPTIMO : {no_optimo}, RANDOM : {analisis_random}")
        if duration_analisis_no_optimo < duration_analisis_optimo or duration_analisis_random < duration_analisis_optimo:
            print(f"FALLó EL ANALISIS ..... OPTIMO : {duration_analisis_optimo}, NO OPTIMO : {duration_analisis_no_optimo}, RANDOM : {duration_analisis_random}. DATA SET {teams_list}")
            break
    print("todo salio bien!")


def random_graph():
    list_x=[]
    y_rand=[]
    data_size = 5
    teams_list = sets.get_random_teams_list(data_size)
    y_opt = []
    for i in range(200):
        list_x.append(i)    
        y_opt.append(solutions.get_analisis_duration(solutions.get_optimal_analisis_order(teams_list)))
        y_rand.append( solutions.get_analisis_duration(solutions.get_random_analisis_order(teams_list)))    
    fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')  # Create a figure containing a single axes.
    ax.plot(list_x,y_opt, label="optimo")
    ax.plot(list_x ,y_rand,label="random")

    ax.legend()
    plt.show()
    

def solution_analysis(teams_list, duration_expected=0, show_solution=False):
    solution = solutions.get_optimal_analisis_order(teams_list)
    solution_time = solutions.get_analisis_duration(solution)
    
    print("---")
    print(f"Solution for a team list of {len(teams_list)} rivals")
    if(show_solution): print("Optimal order is:", solution)
    print("Analysis time duration is: ", solution_time)
    if(duration_expected): print("Time expected: ", duration_expected)
    
    return (solution, solution_time, duration_expected)
    
    
def catedra_data_sets_analysis(test_files, show_solution=False):
    for file in test_files:
        teams_list = sets.get_data_set_from_txt(file)
        optimal_time_expected = sets.get_optimal_time_from_txt(len(teams_list))
        solution_analysis(teams_list, optimal_time_expected, show_solution=show_solution)
        

def confirm_all_solutions_optimal():
    print("Hello world! ★★★")
    test_files=['3-elem.txt','10-elem.txt','100-elem.txt','10000-elem.txt']
    catedra_test_files = ["./casos_prueba_catedra/"+ file for file in test_files] 
    catedra_data_sets_analysis(catedra_test_files)


if __name__ == "__main__":
   confirm_all_solutions_optimal()
