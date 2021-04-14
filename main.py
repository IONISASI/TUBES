def datas_from_csv(csv):
    with open(csv, "r") as f:
        raw_lines = f.readlines()
    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
    lines.pop(0)
    datas = [convert_line_to_data(line) for line in lines]
    return datas


def konso(array, element):
    array += [element]


def splits(string, delimiter):
    array = []
    substring = ''
    for i in string:
        if (i != delimiter):
            substring += i
        else:
            konso(array, substring)
            substring = ''
    konso(array, substring)
    return array


def convert_line_to_data(line):
    raw_arr = splits(line, ';')
    arr_data = [data.strip() for data in raw_arr]
    return arr_data


def username_unik(username):
    datas = datas_from_csv("user.csv")
    cek_unik = True
    for arr_data in datas:
        if(arr_data[1] == username):
            cek_unik = False
    return cek_unik


def CariIndex(csv):
    datas = datas_from_csv(csv)
    idx = 1
    for arr_data in datas:
        idx += 1
    return str(idx)


def register():  # F01:register
    nama = input("Masukkan nama: ").strip()
    username = input("Masukkan username: ").strip()
    if (username_unik(username)):
        password = input("Masukkan password: ").strip()
        alamat = input("Masukkan alamat: ").strip()
        userID = CariIndex("user.csv")
        user = ";".join(
            [userID, username, nama, alamat, password, "user"]) + "\n"
        with open('user.csv', 'a') as f:
            f.write(user)
        print(f"User {username} telah berhasil register ke dalam Kantong Ajaib")
    else:
        print("\nMaaf, username sudah diambil :(\n")


def verifikasi(username, password):  # Fungsi untuk F02:login untuk verifikasi
    datas = datas_from_csv("user.csv")
    cek_valid = False
    for arr_data in datas:
        if(arr_data[1] == username):
            if(arr_data[4] == password):
                cek_valid = True
    return cek_valid


def login():  # F02:login
    username = input("Masukkan username: ").strip()
    password = input("Masukkan password: ").strip()
    if (verifikasi(username, password)):
        print(f"Halo {username}! Selamat datang di Kantong Ajaib")
    else:
        print("\nMaaf, password atau username yang Anda masukkan salah :(\n")

def load():
    namafuser=input('Masukkan Nama File User: ')
    with open(namafuser,'r') as f:
        user = reader(f)
