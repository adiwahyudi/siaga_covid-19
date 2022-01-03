from tkinter import *
import tkinter.messagebox as messagebox
import xmlrpc.client
s = xmlrpc.client.ServerProxy('http://26.122.77.13:8008')

root = Tk()

root.title('Tugas Besar Sistem Pararel dan Terdistribusi')
root.geometry("500x500")
# Label Title on GUI
label_title = Label(root,text="  Form Laporan \n Tertular COVID-19",width=18,font=("bold", 20),)
label_title.place(x=90,y=50)

# Label and Text Fields NIK
label_nik = Label(root, text="NIK : ",width=20,font=("bold", 10),anchor="w")
label_nik.place(x=110,y=150)
nik_input = StringVar(root)
tf_nik = Entry(root,textvariable=nik_input)
tf_nik.place(x=240,y=150)   

# Label and Text Fields Nama Pelapor
label_nama_pelapor = Label(root, text="Nama Pelapor : ",width=20,font=("bold", 10),anchor="w")
label_nama_pelapor.place(x=110,y=180)
tf_nama_pelapor = Entry(root)
tf_nama_pelapor.place(x=240,y=180)

# Label and Text Fields Nama Terduga
label_nama_terduga = Label(root, text="Nama Terduga : ",width=20,font=("bold", 10),anchor="w")
label_nama_terduga.place(x=110,y=210)
tf_nama_terduga = Entry(root)
tf_nama_terduga.place(x=240,y=210)

# Label and Text Fields Alamat Terduga
label_alamat_terduga = Label(root, text="Alamat Terduga : ",width=20,font=("bold", 10),anchor="w")
label_alamat_terduga.place(x=110,y=240)
tf_alamat_terduga = Entry(root)
tf_alamat_terduga.place(x=240,y=240)

# Label and Text Fields Gejala Terduga
label_gejala_terduga = Label(root, text="Gejala Terduga : ",width=20,font=("bold", 10),anchor="w")
label_gejala_terduga.place(x=110,y=270)
tf_gejala_terduga = Entry(root)
tf_gejala_terduga.place(x=240,y=270)


# Get Value
val_nama_pelapor = tf_nama_pelapor.get()
val_nama_terduga = tf_nama_terduga.get()
val_alamat_terduga = tf_alamat_terduga.get()
val_gejala_terduga = tf_gejala_terduga.get()


def submit():
    val_nik = tf_nik.get()
    if s.report(val_nik)['status'] == "Success":
        messagebox.showinfo(title=s.report(val_nik)['status'],message=s.report(val_nik)['message'])
    else:
        messagebox.showinfo(title=s.report(val_nik)['status'],message=s.report(val_nik)['message'])
        
Button(root, text='Submit',bg="green",fg='white', command=submit).place(x=225,y=310)

root.mainloop()