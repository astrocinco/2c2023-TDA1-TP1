import solutions
import sets

import timeit
import pandas as pd

# Obtiene la solución del analsis y su duracion total, dado un arregla con la informacion por video
# y la funcion de dicho metodo (por default se realiza con nuestra propuesta de solucion)
def solution_analysis(teams_list, solution_method=solutions.get_optimal_analisis_order):
    solution = solution_method(teams_list)
    solution_time_duration = solutions.get_analisis_duration(solution)
    return (solution, solution_time_duration)

#Dado un dataframe agrega un fila de informacion en el index indicado (cantidad de datos del dataframe)
def dataframe_append(df, idx, row):
    df_aux = pd.DataFrame(data=row, index=[idx])
    return pd.concat([df, df_aux])

# Devuelve un dataframe con la duracion total de los datasets de la catedra, obtendida por diferentes metodos 
# (solucion dada por la catedra, nuestra propuesta, una propuesta alternativa, una solucion aleatoria)
def catedra_data_sets_analysis(test_files):
    results = pd.DataFrame()
    for file in test_files:
        
        teams_list = sets.get_data_set_from_txt(file)
        solution_duration = sets.get_optimal_time_from_txt(len(teams_list))
        (solution, optimal_duration ) = solution_analysis(teams_list)
        (solution, alternative_duration) = solution_analysis(teams_list, solutions.get_alternative_analisis_order)
        (solution, ramdom_duration) = solution_analysis(teams_list, solutions.get_random_analisis_order)
        
        durations_row = {"solution": solution_duration, "our_proposal": optimal_duration, "alternative": alternative_duration, "random": ramdom_duration}
        results = dataframe_append(results, len(teams_list), durations_row)
    
    return results

# Devuelve 3 dataframe provenientes del analisis de nuestros datasets propios:
#   durations_results: DataFrame de duraciones totales obtenidas por diferentes metodos 
# (los mismos que catedra_data_sets_analysis incluyendo una solucion por fuerza bruta).
#   execution time_results: Dataframe con el tiempo de ejecución de nuestra propuesta de solucion y de fuerza bruta.
#   discrepancies: un vector de soluciones diferentes pero de misma duracion, obtenidas por nuestra propuesta de solucion y por fuerza bruta.
def homemade_data_sets_analysis(test_files):
    duration_results = pd.DataFrame()
    execution_time_results = pd.DataFrame()  
    discrepancies = []

    for file in test_files:
        teams_list = sets.get_data_set_from_txt(file)
    
        (optimal_sol, optimal_duration) = solution_analysis(teams_list)
        (brute_force_sol, brute_force_duration) = solution_analysis(teams_list, solution_method=solutions.get_brute_force_analisis_order)
        (solution, alternative_duration) = solution_analysis(teams_list, solutions.get_alternative_analisis_order)
        (solution, ramdom_duration) = solution_analysis(teams_list, solutions.get_random_analisis_order)
        
        duration_row = {"our_proposal": optimal_duration, "brute_force": brute_force_duration, "alternative": alternative_duration, "random": ramdom_duration}
        duration_results = dataframe_append(duration_results, len(teams_list) ,duration_row)
        
        optimal_time = timeit.timeit(lambda: solution_analysis(teams_list), number=100) * 1000
        brute_force_time = timeit.timeit(lambda: solution_analysis(teams_list, solution_method=solutions.get_brute_force_analisis_order), number=100) * 1000
        
        time_row = {"our_proposal": optimal_time, "brute_force": brute_force_time }
        execution_time_results = dataframe_append(execution_time_results, len(teams_list), time_row)
        
        if((optimal_sol != brute_force_sol)):
            discrepancies.append({'our_proposal': optimal_sol, 'brute_force': brute_force_sol})
    
            
    return (duration_results, execution_time_results, discrepancies)

# Dado un metodo para resolver el problema, 
# devuelve un dataframe con un promedio del tiempo que demora para obtener la solución de una cantidad incremental de datasets
# max: cantidad de datasets incrementales
# rep: repeticiones a promediar
# size: tamanio de cada operacion a repetir 
def get_execution_time(method, max, rep, size):
    df_time = pd.DataFrame()
    for n_elements in range(2, max):
        time = 0
        for i in range(1, rep):
            aux_list = sets.get_random_teams_list(n_elements)
            time += timeit.timeit(lambda: method(aux_list), number=size)
        time = time / rep
        
        aux_df = pd.DataFrame({"time": time*1000}, index=[n_elements])
        df_time = pd.concat([df_time, aux_df])
    return df_time