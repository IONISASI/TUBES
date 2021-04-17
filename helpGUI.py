import tkinter
window = tkinter.Tk()
window.title("HELP")

tkinter.Label(window, text = "'Perlu bantuan? (help/no)'").grid() 
def bantu():

    tkinter.Label(window, text = "register - untuk melakukan registrasi user baru").grid()
    tkinter.Label(window, text = "login - untuk melakukan login ke sistem").grid()
    tkinter.Label(window, text = "tambahitem - untuk melakukan penambahan item").grid()
    tkinter.Label(window, text = "hapus item - untuk melakukan penghapusan item").grid()
    tkinter.Label(window, text = "ubahjumlah - untuk melakukan pengubahan jumlah").grid()
tkinter.Button(window, text = "Help", command = bantu).grid()

def tidak():
    tkinter.Label(window, text = "terima kasih!").grid()
tkinter.Button(window, text = "skip", command = tidak).grid()


window.mainloop()