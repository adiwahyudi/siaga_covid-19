#Server side
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import pandas as pd
import numpy as np
import random
from datetime import timedelta, datetime

#Read Data
df_nik = pd.read_csv('data_nik.csv')
df_penjemput = pd.read_csv('data_penjemput.csv')

#Change to 1D List
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

def report(nik, nama):
    response = dict()
    if validate_nik(nik):
        total_pickup = random.randint(3,6)
        penjemput = list_pickup(total_pickup)
        penjemput = ', '.join(penjemput)
        time = time_pickup()
        
        response['status'] = "success"
        response['message'] = "Akan dijemput pada " + str(time) + " oleh " + str(penjemput)
    else :
        response['status'] = "failed"
        response['message'] = "Gagal bro"

    return response