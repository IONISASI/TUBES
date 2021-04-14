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

def id_beda(itemID):
    cek_id = True
    if(id_valid(itemID)):
        if(itemID[0] == 'G'):
            datas = datas_from_csv("gadget.csv")
        elif(itemID[0] == 'C'):
            datas = datas_from_csv("consumable.csv")
        for arr_data in datas:
            if(arr_data[0] == itemID):
                cek_id = False
        return cek_id
    else:
        cek_id = False
        return cek_id

def id_valid(itemID):
    cek_valid = True
    if(itemID[0] != 'C' and itemID[0] != 'G'):
        cek_valid = False
    return cek_valid

def rarity_valid(rarity):
    cek_valid = True
    rarity_list = ['S','A','B','C']
    if not rarity in rarity_list:
        cek_valid = False
    return cek_valid

while True:
    itemID = input("Masukkan ID: ").strip()
    if(id_valid(itemID) and id_beda(itemID)):
        break
    else:
        if not (id_valid(itemID)):
            print("Gagal menambahkan item karena ID tidak valid.")
        elif not (id_beda(itemID)):
            print("Gagal menambahkan item karena ID sudah ada.")

nama = input("Masukan Nama: ").strip()
deskripsi = input("Masukan Deskripsi: ").strip()
jumlah = str(input("Masukan Jumlah: "))
while True:
    rarity = input("Masukan Rarity: ")
    if(rarity_valid(rarity)):
        break
    else:
        print("Input rarity tidak valid!")

if(itemID[0]=='G'):
    tahun = input("Masukan tahun ditemukan: ")
    item = ";".join([itemID, nama, deskripsi, jumlah, rarity, tahun]) + "\n"
    with open('gadget.csv','a') as f:
        f.write(item)

else: #itemID[0]=='C'
    item = ";".join([itemID, nama, deskripsi, jumlah, rarity]) + "\n"
    with open('consumable.csv','a') as f:
        f.write(item)
print("Item berhasil ditambahkan ke database.")
