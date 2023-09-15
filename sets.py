import sys
import random

def get_optimal_time_from_txt(n_elements):
    file= './casos_prueba_catedra/Tiempos optimos.txt'
    optimal_value = 0
    
    with open(file,'r') as o_file:
        o_file.readline()
        for line in o_file:
            aux_line = line.replace(':', '').replace('\n', '').split(" ")
            if(int(aux_line[0]) == n_elements):
                optimal_value = int(aux_line[2])
                
    return optimal_value  


def get_data_set_from_txt(file):
    data_set = []
    with open(file,'r') as o_file:
        o_file.readline()
        for line in o_file:
            aux_list = line.split(",")
            l_tuple = (int(aux_list[0]), int(aux_list[1].rstrip()))
            data_set.append(l_tuple)
    return data_set


def get_random_teams_list(n_rivals):
    teams_list = []
    for i in range(n_rivals):
        teams_list.append((random.randint(1, n_rivals+10),  random.randint(1, n_rivals+10)))
    return teams_list


def write_data_set_file(path, teams_list):
    file = path + str(len(teams_list)) + "-elem.txt"
    with open(file,'w') as o_file:
        o_file.write("S_i,A_i" + "\n")
        for team in teams_list:
            o_file.write(str(team[0]) + "," + str(team[1]) + "\n")


def create_random_file_from_arg():
    random_teams_list = get_random_teams_list(int(sys.argv[1]))
    write_data_set_file("./casos_prueba/", random_teams_list)

if __name__ == "__main__":
    create_random_file_from_arg()