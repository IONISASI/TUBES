import os
s = input()
if s=='save':
    a = input("masukkan nama folder: ")
if __name__ == "__main__":
    for (a) in os.walk('a', topdown = True):
        print ("saving...")
        print ('data Anda telah tersimpan pada folder', a)
else:
    print("data Anda tidak tersimpan")

