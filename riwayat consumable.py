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

def consumable(id_id_pengambil,id_consumable,tanggal_peminjaman):
    csv_filename = "consumable_history.csv"
    datas = datas_from_csv(csv_filename)
    idi = len(datas)+1
    item = str(idi) + ";" + id_pengambil + ";" + id_consumable + ";" + tanggal_peminjaman + ";" + "\n"
    with open('consumable_history.csv','a') as f:
        f.write(item)


ID = input("Massukkan ID : ")
nama = input("Nama pengambil : ")
jumlah = input("Nama consumable : ")
tanggal = input("Tanggal pengambilan: ")
jumlah = input("Jumlah: ")

csv_filename = "consumable.csv"
datas = datas_from_csv(csv_filename)
for arr_data in datas:
        if arr_data[0] == ID :
            if arr_data[3] >= jumlah:
                consumable("1", ID, tanggal, jumlah)
                print(arr_data[1],"Riwayat pengembalian : ",jumlah)
            else:
                print("Tidak dikembalikan")
            break