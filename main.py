import random

def get_optimal_analisis_order(teams_list):
    optimal_analisis_order = sorted(teams_list, key= lambda team:team[1], reverse=True)
    return optimal_analisis_order

def aux_get_analisis_duration(analisis_order):
    team_analisis_max_duration = 0
    scaloni_wait_time = 0
    for team in analisis_order:
        if scaloni_wait_time + team[0] + team[1] > team_analisis_max_duration:
            team_analisis_max_duration = scaloni_wait_time + team[0] + team[1]
        scaloni_wait_time += team[0]
    return team_analisis_max_duration

def make_teams_list(n_rivals):
    teams_list = []
    for i in range(n_rivals):
        teams_list.append((random.randint(0, n_rivals+10),  random.randint(0, n_rivals+10)))
    return teams_list

def get_solution_analysis(teams_list, time_expected=-1):
    print(f"Solution for a team list of {len(teams_list)} rivals")
    solution = get_optimal_analisis_order(teams_list)
    print("Optimal order is:", solution)
    print("Analysis time is:", aux_get_analisis_duration(solution))
    print(f"Time expected: {time_expected}")
    
def main():
    teams_list_test = [
            # Tuplas, primero con el tiempo de analisis de Scaloni y luego del ayudante. TODO: No hardcodear
            (1, 3),
            (5, 1),
            (4, 8),
            (4, 3),
            (1, 5),
            (2, 9),
            (2, 2),
            (2, 4),
            (1, 6),
            (6, 5),
        ]

    print("Hello world! ★★★")
    get_solution_analysis(teams_list_test)
    print("--------------------------------------------------------")
    get_solution_analysis(make_teams_list(15))

main()


""" (3, 3),
(5, 1),
(1, 8), """



""" (1, 3),
(5, 1),
(4, 8),
(4, 3),
(1, 5),
(2, 9),
(2, 2),
(2, 4),
(1, 6),
(6, 5), """