
DATA_SET_FILE_PATH = "casos_prueba_catedra/"

def get_data_set_from_txt(file : str) -> tuple : 
    data_set = []
    file = DATA_SET_FILE_PATH + file

    with open(file,'r') as o_file:
        o_file.readline() # quito la primera linea de encabezado
        for line in o_file:
            aux_list = line.split(",")
            l_tuple = (int(aux_list[0]), int(aux_list[1].rstrip()))
            data_set.append(l_tuple)
    return data_set


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

def main():
    teams_list = get_data_set_from_txt('3 elemen.txt')
    return get_optimal_analisis_order(teams_list)

print("Hello world! ★★★")
optimal_order = main()
print("Optimal order is:", optimal_order)
print("Analisis time is:", aux_get_analisis_duration(main()))



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
