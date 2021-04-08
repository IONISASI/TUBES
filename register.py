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
    arr_data = [data.strip() for data in raw_arr]
    return arr_data

def username_unik(username):
    datas = datas_from_csv("user.csv")
    cek_unik = True
    for arr_data in datas:
        if(arr_data[1] == username):
            cek_unik = False
    return cek_unik

def CariIndex():
    datas = datas_from_csv("user.csv")
    idx = 1
    for arr_data in datas:
        print(arr_data)
        idx += 1
    return str(idx)

nama = input("Masukkan nama: ").strip()
while True:
    username = input("Masukkan username: ").strip()
    if (username_unik(username)):
        break
    else:
        print("Maaf, username sudah diambil :(")

password = input("Masukkan password: ").strip()
alamat = input("Masukkan alamat: ").strip()
userId = 0
userID = CariIndex()
user = ";".join([userID, username, nama, alamat, password, "user"]) + "\n"
with open('user.csv','a') as f:
    f.write(user)
print(f"User {username} telah berhasil register ke dalam Kantong Ajaib")

