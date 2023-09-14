
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

# ---
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
# ---

def run_from_txt_data_set(txt_data):
    teams_list = get_data_set_from_txt(txt_data)
    return get_optimal_analisis_order(teams_list)


def main(txt_data):
    optimal_order = run_from_txt_data_set(txt_data)
    print("Optimal order is:", optimal_order)
    print("Analisis time is:", aux_get_analisis_duration(optimal_order))


if __name__ == "__main__":
   main("3 elem.txt")
