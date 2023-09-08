DATA_SET_FILE_PATH = "casos_prueba_catedra/"


def get_data_set_from_txt(file):
    data_set = []
    file = DATA_SET_FILE_PATH + file
    i=0
    for line in open(file):
        if i!=0:
            aux_list = line.split(",")
            tupla = (int(aux_list[0]), int(aux_list[1].rstrip()))
            data_set.append(tupla)
        i+=1
    
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

#def main(teams_list = []):
 #   teams_list = [
        # Tuplas, primero con el tiempo de analisis de Scaloni y luego del ayudante. TODO: No hardcodear
  #      (1, 3),
   #     (5, 1),
    #    (4, 8),
     #   (4, 3),
      #  (1, 5),
       # (2, 9),
       # (2, 2),
       # (2, 4),
       # (1, 6),
       # (6, 5),
    #]
    #return get_optimal_analisis_order(teams_list)

def main():

    teams_list = get_data_set_from_txt('10000-elem.txt')
    
    return get_optimal_analisis_order(teams_list)


print("Hello world! ★★★")
optimal_order = main()
print(aux_get_analisis_duration(optimal_order))




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