#Server side
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from datetime import timedelta, datetime
import pandas as pd
import numpy as np
import random

# Membaca dataset
df_nik = pd.read_csv('data_nik.csv')
df_penjemput = pd.read_csv('data_penjemput.csv')

# Ubah dari dataframe ke 1d list
df_nik = np.array(df_nik).ravel().tolist()
df_penjemput = np.array(df_penjemput).ravel().tolist()

def validate_nik(nik):
    return int(nik) in df_nik

def list_pickup(kuantitas):
    list_penjemput = []
    for i in range(kuantitas):
        list_penjemput.append(df_penjemput[random.randrange(i, 499)])
    return list_penjemput

def time_pickup():
    time = datetime.now() + timedelta(hours=4)
    time_format = time.strftime("%d-%m-%Y %H:%M:%S")

    return time_format

# Buat kelas requesthandler batasi pada path /RPC2 saja
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2')

    # Enable CORS
    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    # Add these headers to all responses
    def end_headers(self):
        self.send_header("Access-Control-Allow-Headers", 
                         "Origin, X-Requested-With, Content-Type, User-Agent, Accept")
        self.send_header("Access-Control-Allow-Origin", "*")
        SimpleXMLRPCRequestHandler.end_headers(self)

# Buat variabel port number dan ip server
PORT_NUM = 8008
IP_SERVER = '26.122.77.13'

# Buat server serta register fungsi 
with SimpleXMLRPCServer((IP_SERVER, PORT_NUM), requestHandler = RequestHandler) as server:
    server.register_introspection_functions()

    def report(nik,nama_pelapor,nama_terduga,gejala_terduga,alamat_terduga):
        response = dict()
        if validate_nik(nik):
            total_pickup = random.randint(3,6)
            penjemput = list_pickup(total_pickup)
            penjemput = ', '.join(penjemput)
            time = time_pickup()
            
            response['status'] = "Success"
            response['message'] = "Penjemputan akan dilakukan pada " + str(time) + " WIB oleh petugas sebanyak "+ str(total_pickup) + " orang dan berikut yang akan menjemput " + str(penjemput)
            
            # Save to txt file
            teks = "\nNIK Pelapor : {}\nNama Pelapor : {}\nNama Terduga : {}\nGejala Terduga : {}\nAlamat Terduga : {}\n======================================================".format(nik, nama_pelapor, nama_terduga, gejala_terduga, alamat_terduga)
            file_bio = open("report_valid.txt", "a")
            file_bio.write(teks)
            file_bio.close()
        else :
            response['status'] = "Failed"
            response['message'] = "NIK pelapor tidak valid"

            # Save to txt file
            teks = "\nNIK Pelapor : {}\nNama Pelapor : {}\nNama Terduga : {}\nGejala Terduga : {}\nAlamat Terduga : {}\n======================================================".format(nik, nama_pelapor, nama_terduga, gejala_terduga, alamat_terduga)
            file_bio = open("report_notvalid.txt", "a")
            file_bio.write(teks)
            file_bio.close()

        return response
    
    server.register_function(report,'report')
    print("Server running on port", PORT_NUM)
    server.serve_forever()