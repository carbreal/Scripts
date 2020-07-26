#!/usr/bin/python3

import json
import requests
import sys, getopt

def getToken(client_id,client_secret):
    try:
        url='https://api.crowdstrike.com/oauth2/token'
        data_post={'client_id':client_id,'client_secret':client_secret}
        r = requests.post(url,data=data_post)
        bearer_token=r.json()['access_token']
        print("[+]Got access_token: "+bearer_token)
        return bearer_token
    except:
        print("[-]Ups! Something happened...")
        print(r.text+"\n"+r.content)
        sys.exit(1)
def getInstallerList(bearer_token):
    try:
        url='https://api.crowdstrike.com/sensors/combined/installers/v1?filter=platform:%27windows%27'
        headers={'Authorization':'Bearer '+bearer_token,'Content-Type':'application/json','Accept':'application/json'}
        r = requests.get(url,headers=headers)
        hash_installer=r.json()['resources'][0]['sha256']
        print("[+]Got hash of latest installer: "+hash_installer)
        return hash_installer
    except:
        print("[-]Ups! Something happened...")
        print(r.text+"\n"+r.content)
        sys.exit(1)

def getInstaller(hash_installer,bearer_token):
    try:
        url='https://api.crowdstrike.com/sensors/entities/download-installer/v1'
        params_get={'id':hash_installer}
        headers={'Authorization':'Bearer '+bearer_token}
        r = requests.get(url,params=params_get,headers=headers)
        open("/tmp/windowsinstaller.exe","wb").write(r.content)
        print("[+]File Downloaded")
    except:
        print("[-]Ups! Something happened...")
        print(r.text+"\n"+r.content)
        sys.exit(1)


def help():
    print("Usage:\n\tpython3 cswinstaller.py -i <client_id> -s <client_secret>\n")
    sys.exit()

def use_api(client_id,client_secret):
    token=getToken(client_id,client_secret)
    hash_ins=getInstallerList(token)
    getInstaller(hash_ins,token)
    sys.exit()

def main(argv):
    client_id = ''
    client_secret = ''
    try:
        opts, args = getopt.getopt(argv,"i:s:")
    except getopt.GetoptError:
        help()
        sys.exit(2)
    if len(opts) < 2:
        help()
    else:
        for opt, arg in opts:
           if opt == "-i":
              client_id=arg
           elif opt == "-s":
              client_secret=arg
           else:
              help()
        use_api(client_id,client_secret)

if __name__ == "__main__":
    main(sys.argv[1:])
