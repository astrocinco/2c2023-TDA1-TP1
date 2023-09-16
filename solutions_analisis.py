import solutions
import sets
import graph

import time as t
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


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
    

def solution_analysis(teams_list, solution_method=solutions.get_optimal_analisis_order):
    solution = solution_method(teams_list)
    solution_time_duration = solutions.get_analisis_duration(solution)
    return (solution, solution_time_duration)
    
def dataframe_append(df, row):
    df_aux = pd.DataFrame(data=row, index=[df.shape[0]])
    return pd.concat([df, df_aux])
    
def catedra_data_sets_analysis(test_files):
    results = pd.DataFrame()
    for file in test_files:
        
        teams_list = sets.get_data_set_from_txt(file)
        solution_duration = sets.get_optimal_time_from_txt(len(teams_list))
        (solution, optimal_duration ) = solution_analysis(teams_list)
        (solution, alternative_duration) = solution_analysis(teams_list, solutions.get_alternative_analisis_order)
        (solution, ramdom_duration) = solution_analysis(teams_list, solutions.get_random_analisis_order)
        
        durations_row = {"n": len(teams_list), "solution": solution_duration, "optimal": optimal_duration, "alternative": alternative_duration, "random": ramdom_duration}
        results = dataframe_append(results, durations_row)
    
    return results

def homemade_data_sets_analysis(test_files):
    duration_results = pd.DataFrame()
    execution_time_results = pd.DataFrame()  
    discrepancies = []

    for file in test_files:
        teams_list = sets.get_data_set_from_txt(file)
        
        optimal_initial_time = t.time()
        (optimal_sol, optimal_duration) = solution_analysis(teams_list)
        
        optimal_final_time = t.time()
        
        (brute_force_sol, brute_force_duration) = solution_analysis(teams_list, solution_method=solutions.get_brute_force_analisis_order)
        brute_force_final_time = t.time()
        
        (solution, alternative_duration) = solution_analysis(teams_list, solutions.get_alternative_analisis_order)
        (solution, ramdom_duration) = solution_analysis(teams_list, solutions.get_random_analisis_order)
        
        duration_row = {"n": len(teams_list), "optimal": optimal_duration, "brute_force": brute_force_duration, "alternative": alternative_duration, "ramdom": ramdom_duration}
        duration_results = dataframe_append(duration_results, duration_row)
        
        optimal_time = (optimal_final_time - optimal_initial_time)*1000
        brute_force_time = (brute_force_final_time - optimal_final_time)*1000
        time_row = {"n": len(teams_list), "optimal": optimal_time, "brute_force": brute_force_time }
        execution_time_results = dataframe_append(execution_time_results, time_row)
        
        if((optimal_sol != brute_force_sol)):
            discrepancies.append({'optimal': optimal_sol, 'brute_force': brute_force_sol})
    
            
    return (duration_results, execution_time_results, discrepancies)
    
def all_data_sets_analysis():
    catedra_test_files=['3-elem.txt','10-elem.txt','100-elem.txt','10000-elem.txt']
    catedra_test_path = ["./casos_prueba_catedra/"+ file for file in catedra_test_files] 
    
    catedra_duration_results = catedra_data_sets_analysis(catedra_test_path)
    
    test_files=[str(n) + '-elem.txt' for n in range(3, 11)]
    test_path = ["./casos_prueba/"+ file for file in test_files] 
    
    (homemade_durations_results, homemade_execution_time_results, brute_force_discrepancies) = homemade_data_sets_analysis(test_path)
    
    ''''
    print(catedra_duration_results)
    print(homemade_durations_results)
    print(homemade_execution_time_results)
    print(brute_force_discrepancies)
    '''
    
    #title="Algoritmo propio - Duracion maxima: " + str(optimal_duration)
    #graph.make_graph_from_analisis_order(optimal_sol)
    #title="Algoritmo fuerza bruta - Duracion maxima: " + str(brute_force_duration)
    #graph.make_graph_from_analisis_order(brute_force_sol)
    

if __name__ == "__main__":
   all_data_sets_analysis()