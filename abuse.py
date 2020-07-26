#!/usr/bin/python3

import json
import requests
import sys, getopt
import time

def getInfo(ip):
    APIKEY="INSERTAPIKEY"
    url='https://api.abuseipdb.com/api/v2/check'
    headers={'Key':APIKEY,'Accept':'application/json'}
    payload={'ipAddress':ip,'maxAgeInDays':'90'}
    r = requests.get(url,params=payload,headers=headers)
    ip_get=r.json()['data']['ipAddress']
    whitelist=r.json()['data']['isWhitelisted']
    score=r.json()['data']['abuseConfidenceScore']
    countrycode=r.json()['data']['countryCode']
    totalreports=r.json()['data']['totalReports']
    lastreported=r.json()['data']['lastReportedAt']
    if whitelist == False:
        res="IP: "+ip_get+"\n\t- Score: "+str(score)+"\n\t- Whitelisted: "+str(whitelist)+"\n\t- Country Code: "+countrycode+"\n\t- Total Reports: "+str(totalreports)+"\n\t- Last time reported: "+lastreported[:lastreported.find("T")]+""
    elif whitelist == True:
        res="IP: "+ip_get+" is whitelisted."
    else:
        res="IP: "+ip_get+" there was a problem."
    print(res)

def help():
    print("\nFor a single IP:\n\tabuse.py -i <ip>\nFor a file:\n\tabuse.py -f <file>\n")
    sys.exit()

def main(argv):
   ip = ''
   fileips = ''
   try:
      opts, args = getopt.getopt(argv,"hi:f:")
   except getopt.GetoptError:
      help()
      sys.exit(2)
   if len(opts) < 1:
       help()
   else:
       for opt, arg in opts:
          if opt == '-h':
             help()
          elif opt == "-i":
             getInfo(arg)
             sys.exit()
          elif opt == "-f":
             with open(arg,"r") as fileips:
                 for ip in fileips:
                     getInfo(ip)
                     time.sleep(2)
             sys.exit()
          else:
             help()

if __name__ == "__main__":
   main(sys.argv[1:])
