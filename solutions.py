SCALONI_INDEX = 0
ASSISTANT_INDEX = 1


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
