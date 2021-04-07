nama = input("Masukkan nama: ")
username = input("Masukkan username: ")
password = input("Masukkan password: ")
alamat = input("Masukkan alamat: ")



f = open("hai.csv","r")
raw_lines = f.readlines()
f.close()
lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
for line in lines:
  print(line)
