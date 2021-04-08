import csv
from csv import reader

def load():
    namafuser=input('Masukkan Nama File User: ')
    with open(namafuser,'r') as read_obj:
        user = reader(read_obj)
    namafdaftarwahana=input('Masukkan Nama File User: ')
    with open(namafdaftarwahana,'r') as read_obj:
        daftarwahana = reader(read_obj)
    namafpembeliantiket=input('Masukkan Nama File User: ')
    with open(namafpembeliantiket,'r') as read_obj:
        pembeliantiket = reader(read_obj)
    namafgunatiket=input('Masukkan Nama File User: ')
    with open(namafgunatiket,'r') as read_obj:
        gunatiket = reader(read_obj)
    namafpemiliktiket=input('Masukkan Nama File User: ')
    with open(namafpemiliktiket,'r') as read_obj:
        pemiliktiket = reader(read_obj)
    namafrefundtiket=input('Masukkan Nama File User: ')
    with open(namafrefundtiket,'r') as read_obj:
        refundtiket = reader(read_obj)
    namafkritiksaran=input('Masukkan Nama File User: ')
    with open(namafkritiksaran,'r') as read_obj:
        kritiksaran = reader(read_obj)
