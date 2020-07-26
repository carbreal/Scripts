#!/usr/bin/python3

import json
import requests
import sys, getopt
import time
import base64

def getInfo(type_vt,id_vt):
    #ip_addresses/files
    
    try:
        APIKEY="INSERTAPIKEY"
        url='https://www.virustotal.com/api/v3/'+type_vt+'/'+id_vt
        headers={'x-apikey':APIKEY}
        r = requests.get(url,headers=headers)
        id_get=r.json()['data']['id']
        malicious=r.json()['data']['attributes']['last_analysis_stats']['malicious']
        suspicious=r.json()['data']['attributes']['last_analysis_stats']['suspicious']
        bad=malicious+suspicious
        undetected=r.json()['data']['attributes']['last_analysis_stats']['undetected']
        harmless=r.json()['data']['attributes']['last_analysis_stats']['harmless']
        good=undetected+harmless
        res="Object: "+id_get+" - "+str(bad)+"/"+str(good+bad)+""
        print(res)
    except:
        print("Not Found")

def help():
    print("\nFor a single Hash:\n\tvt.py -h <hash>\nFor a file with a hash list:\n\tvt.py -H <file>\nFor a single IP:\n\tvt.py -i <ip>\nFor a file with an ip list:\n\tvt.py -I <file>\nFor a single domain:\n\tvt.py -d <domain>\nFor a file with a domain list:\n\tvt.py -D <file>\nFor a single url:\n\tvt.py -u <url>\nFor a file with a url list:\n\tvt.py -U <file>\n")
    sys.exit()

def main(argv):
   ip = ''
   fileips = ''
   hash_vt = ''
   filehash = ''
   domain = ''
   file_dom = ''
   url = ''
   file_url = ''
   try:
      opts, args = getopt.getopt(argv,"i:I:h:H:u:U:d:D:")
   except getopt.GetoptError:
      help()
      sys.exit(2)
   if len(opts) < 1:
       help()
   else:
       for opt, arg in opts:
          if opt == "-i":
             getInfo("ip_addresses",arg)
             sys.exit()
          elif opt == "-h":
             getInfo("files",arg)
             sys.exit()
          elif opt == "-d":
             getInfo("domains",arg)
             sys.exit()
          elif opt == "-u":
             getInfo("urls",base64.b64encode(arg))
             sys.exit()
          elif opt == "-I":
             with open(arg,"r") as fileips:
                 for ip in fileips:
                     getInfo("ip_addresses",ip)
                     time.sleep(20)
             sys.exit()
          elif opt == "-H":
             with open(arg,"r") as filehash:
                 for hash_vt in filehash:
                     getInfo("files",hash_vt)
                     time.sleep(20)
             sys.exit()
          elif opt == "-D":
             with open(arg,"r") as file_dom:
                 for domain in filehash:
                     getInfo("domains",domain)
                     time.sleep(20)
             sys.exit()
          elif opt == "-U":
             with open(arg,"r") as file_url:
                 for url in filehash:
                     getInfo("urls",base64.b64encode(url))
                     time.sleep(20)
             sys.exit()
          else:
             help()

if __name__ == "__main__":
   main(sys.argv[1:])
