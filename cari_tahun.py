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

def cari_tahun(tahun):
    datas = datas_from_csv("gadget.csv")
    for arr_data in datas:
        if(arr_data[5] == tahun):
            print("Nama: " + arr_data[1])
            print("Deskripsi: " + arr_data[2])
            print("Jumlah: " + arr_data[3] + " buah")
            print("Rarity: " + arr_data[4])
            print("Tahun Ditemukan: " + arr_data[5] + "\n")

tahun = input("Masukkan tahun: ")
print("\nHasil pencarian: \n")
cari_tahun(tahun)
