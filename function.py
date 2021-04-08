def konso(array,element):
    array += [element]

def splits(string):
    array = []
    substring = ''
    for i in string:
        if (i != ","):
            substring += i
        else:
            konso(array,substring)
            substring = ''
    konso(array,substring)
    return array

def convert_line_to_data(line):
    raw_arr = splits(line)
    raw_arr = [data.strip() for data in raw_arr]
    return raw_arr

def conver_array_to_real_values(arr_data):
    arr_cpy = arr_data[:]
    for i in range(3):
        if(i==0):
            arr_cpy[i] = int(arr_cpy[i])
        elif(i == 2):
            arr_cpy[i] = float(arr_cpy[i])
    return arr_cpy

def modify_datas(idx,col,value):
    datas[idx][col] = value


def convert_datas_to_string():
  string_data = ",".join(header) + "\n"
  for arr_data in datas:
    arr_data_all_string = [str(var) for var in arr_data]
    string_data += ",".join(arr_data_all_string)
    string_data += "\n"
  return string_data

def username_unik(username):
    with open('user.csv','r') as f:
        cek_unik = True
        txt_raw = f.readlines()
        txt = [raw_line.replace("\n", "") for raw_line in txt_raw]
        raw_header = txt.pop(0)
        for line in txt:
            list_line = splits(line)
            if(list_line[1] == username):
                cek_unik = False
        return cek_unik
