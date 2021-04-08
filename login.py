def datas_from_csv(csv):
    with open(csv,"r") as f:
        raw_lines = f.readlines()
    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
    lines.pop(0)
    datas = [convert_line_to_data(line) for line in lines]
    return datas

def konso(array,element):
    array += [element]

def splits(string):
    array = []
    substring = ''
    for i in string:
        if (i != ";"):
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

def validasi(username, password):
    datas = datas_from_csv("user.csv")
    cek_valid = False
    for arr_data in datas:
        if(arr_data[1] == username):
            if(arr_data[4] == password):
                cek_valid = True
    return cek_valid

while True:
    username = input("Masukkan username: ").strip()
    password = input("Masukkan password: ").strip()
    if (validasi(username, password)):
        break
    else:
        print("Maaf, password atau username yang dimasukkan salah :(")
print(f"Halo {username}! Selamat datang di Kantong Ajaib")
