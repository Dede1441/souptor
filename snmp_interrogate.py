import sys
import json
import requests
import time
import datetime
from pprint import pprint
from jsonmerge import merge
from pysnmp.entity.rfc3413.oneliner import cmdgen
from os import environ

URL_APP = environ.get("URL_APP")
TOKEN_APP = environ.get("TOKEN_APP")

def interrogation_api_list() :
    headers = { 'Accept': 'application/json', 'Authorization' : f'Token {TOKEN_APP}'    }

    url = f'{URL_APP}/api/services'
    print(url)
    call = requests.get(url ,headers=headers)

    list_equipements=call.json()

    return(list_equipements)


def interrogation_equipmt(ip,port,oid,community) :
    #oid load '1.3.6.1.4.1.2021.10.1.3.1'

    auth = cmdgen.CommunityData(community)

    cmdGen = cmdgen.CommandGenerator()

    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
        auth,
        cmdgen.UdpTransportTarget((ip,port)),
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

    if len(list_equipements) != 0:
        for equipement in list_equipements :
            print(equipement)

            oid=equipement['identifier']
            ip=equipement['ip']
            community=equipement['community']
            id=equipement['id']
            port=equipement['port']

            url=f'{URL_APP}/api/transaction/{id}/'
            headers = { 'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization' : f'Token {TOKEN_APP}'    }

            valeurs_snmp['value']=interrogation_equipmt(ip,port,oid,community)

            if not valeurs_snmp['value'] or valeurs_snmp['value'] is None:
                valeurs_snmp['value']='error'

            else:
                print(valeurs_snmp['value'])

            try:
                requests.post(url , data=json.dumps(valeurs_snmp), headers=headers)

            except:
                print('error')

    return()

while True:
    list_equipements = interrogation_api_list()
    result_envoie = envoi_donnees(list_equipements)
    time.sleep(60)