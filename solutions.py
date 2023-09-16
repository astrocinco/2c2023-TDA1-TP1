import sys
import sets

SCALONI_INDEX = 0
ASSISTANT_INDEX = 1

from itertools import permutations

def get_brute_force_analisis_order(teams_list):
    
    all_permutations = [list(p) for p in permutations(teams_list)]
    
    permutations_durations = [get_analisis_duration(p) for p in all_permutations]
    optimal_index = permutations_durations.index(min(permutations_durations))
    
    return all_permutations[optimal_index]
    

def get_random_analisis_order(teams_list):
    from random import shuffle
    shuffle(teams_list)
    return teams_list


def get_alternative_analisis_order(teams_list):
    example_order = sorted(teams_list, key= lambda team:team[ASSISTANT_INDEX], reverse = False)
    return example_order


def get_optimal_analisis_order(teams_list):
    optimal_analisis_order = sorted(teams_list, key= lambda team:team[ASSISTANT_INDEX], reverse=True)
    return optimal_analisis_order


def get_analisis_duration(analisis_order):
    team_analisis_max_duration = 0
    scaloni_wait_time = 0
    for team in analisis_order:
        scaloni_wait_time += team[SCALONI_INDEX]
        if scaloni_wait_time + team[ASSISTANT_INDEX] > team_analisis_max_duration:
            team_analisis_max_duration = scaloni_wait_time + team[ASSISTANT_INDEX]
    return team_analisis_max_duration


'''
argv[1] -> file
arv[2] -> flag
flags:
    - -a : alternative solution
    - -r : random solution
    - -b : brute force solution
    - -o : optimal solution

'''

def determinate_method(flag):
    match flag:
        case "-a":
            return ("alternative", get_alternative_analisis_order)
        case "-r":
            return ("random", get_random_analisis_order)
        case "-b":
            return ("brute force", get_brute_force_analisis_order)
        case _:
            return ("optimal", get_optimal_analisis_order)
        
if __name__ == "__main__":
    try:
        file = sys.argv[1]
    except IndexError:
        print("ERROR")
        print("Usage: <arg1> file with information of videos, <arg2> flags for determinate method")
        sys.exit(1)
        
    try:
        flag = sys.argv[2]
    except IndexError:
        flag = ""
        
    (method_name, method) = determinate_method(flag)

    teams_list = sets.get_data_set_from_txt(file)
    analysis_order = method(teams_list)
    
    print(f"Order by {method_name} method: {analysis_order}")
    print(f"Total duration: {get_analisis_duration(analysis_order)}")
    