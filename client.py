#Client side
import xmlrpc.client
s = xmlrpc.client.ServerProxy('http://127.0.0.1:8000')

print("Siaga COVID-19")

form_nik_pelapor = input("NIK Pelapor\t\t: ")
form_nama_pelapor = input("Nama Pelapor\t\t: ")
form_nama_terduga = input("Nama Terduga\t\t: ")
form_alamat_terduga = input("Alamat Terduga\t\t: ")
form_gejala_terduga = input("Gejala Terduga\t\t: ")

print(s.report(form_nik_pelapor))