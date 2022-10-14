import sys
import json
import requests
import time
import datetime
from pprint import pprint
from jsonmerge import merge
from pysnmp.entity.rfc3413.oneliner import cmdgen



def interrogation_api_list() :
    headers = { 'Accept': 'application/json', 'Authorization' : 'Token c4bd47910dd422220be8aee15404faf907fed92e'    }
    url = "http://172.18.1.100:8001/api/service/all/"
    call = requests.get(url ,headers=headers)

    list_equipements=call.json()

    return(list_equipements)


def interrogation_equipmt(ip,oid,community) :
    #oid load '1.3.6.1.4.1.2021.10.1.3.1'

    auth = cmdgen.CommunityData(community)

    cmdGen = cmdgen.CommandGenerator()

    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
        auth,
        cmdgen.UdpTransportTarget((ip, 161)),
        cmdgen.MibVariable(oid),
        lookupMib=False,
    )

    for oid, val in varBinds:
        return(val.prettyPrint())

def envoi_donnees(list_equipements):
    valeurs_snmp={}
    now = datetime.datetime.now()

    with open('collektor.txt', 'a') as f:
            f.write('\n' + now.strftime("%Y-%m-%d %H:%M:%S"))


    for equipement in list_equipements :
        print(equipement)

        oid=equipement['identifier']
        ip=equipement['ip']
        community=equipement['community']
        id=equipement['id']

        result_loc=interrogation_equipmt(ip,oid,community)
        valeurs_snmp[id]=result_loc
        
        #print(valeurs_snmp[id])  

        with open('collektor.txt', 'a') as f:
            f.write('\n' + valeurs_snmp[id])

        #result vide/error stop avec un error code 
        #envoi en json de result_glob vers api web -> id, valeur
            #return ok
    #print(valeurs_snmp)
    return('ok')

while True:
    list_equipements = interrogation_api_list()
    result_envoie = envoi_donnees(list_equipements)
    time.sleep(60)
    #return (result_envoie)