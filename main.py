from sets import *
import time

CATEDRA_DATA_SET_FILE_PATH = "./casos_prueba_catedra/"
SCALONI_ANALYSIS = 0
ASISTENT_ANALYSIS = 1

def get_optimal_analisis_order(teams_list):
    optimal_analisis_order = sorted(teams_list, key= lambda team:team[1], reverse=True)
    return optimal_analisis_order

def aux_get_analisis_duration(analisis_order):
    team_analisis_max_duration = 0
    scaloni_wait_time = 0
    for team in analisis_order:
        scaloni_wait_time += team[SCALONI_ANALYSIS]
        if scaloni_wait_time + team[ASISTENT_ANALYSIS] > team_analisis_max_duration:
            team_analisis_max_duration = scaloni_wait_time + team[ASISTENT_ANALYSIS]
    return team_analisis_max_duration

def solution_analysis(teams_list, time_expected=0, show_solution=False):
    
    start_time = time.time()
    solution = get_optimal_analisis_order(teams_list)
    end_time = time.time()
    
    solution_time = aux_get_analisis_duration(solution)
    excecution_time = end_time - start_time
    
    print("--------------------------------------------------------")
    print(f"Solution for a team list of {len(teams_list)} rivals")
    if(show_solution): print("Optimal order is:", solution)
    print("Analysis time is: ", solution_time)
    if(time_expected): print("Time expected: ", time_expected)
    print("Execution time: ", excecution_time)
    
    return (solution, solution_time, excecution_time)
    
def catedra_data_sets_analysis(test_files, show_solution=False):
    for file in test_files:
        teams_list = get_data_set_from_txt(CATEDRA_DATA_SET_FILE_PATH, file)
        optimal_time_expected = get_optimal_time_from_txt(CATEDRA_DATA_SET_FILE_PATH, len(teams_list))
        solution_analysis(teams_list, optimal_time_expected, show_solution=show_solution)

def main():

    print("Hello world! ★★★")
    catedra_test_files=['3-elem.txt','10-elem.txt','100-elem.txt','10000-elem.txt']
    catedra_data_sets_analysis(catedra_test_files)
    solution_analysis(get_random_teams_list(15))
    
main()