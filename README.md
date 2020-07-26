# SCRIPTS  
  
A collection of some of the poorly coded scripts I use. I'll post some others I find useful.  
  
	- cswinstaller.py: check the latest windows installer version and download it:  
		Usage:  
			cswinstaller.py -i <client_id> -s <client_secret>  
	- vt.py: use the VirusTotal API to check a list of IPs/domains/hashes and return a score  
		Usage:  
			For a single Hash:  
				vt.py -h <hash>  
			For a file with a hash list:  
				vt.py -H <file>  
			For a single IP:  
				vt.py -i <ip>  
			For a file with an ip list:  
				vt.py -I <file>  
			For a single domain:  
				vt.py -d <domain>  
			For a file with a domain list:  
				vt.py -D <file>  
			For a single url:  
				vt.py -u <url>  
			For a file with a url list:  
				vt.py -U <file>  
  
	- abuse.py: use the abuseipdb API to check a list of IPs reputation  
		Usage:  
			For a single IP:  
				abuse.py -i <ip>  
			For a file:  
				abuse.py -f <file>  
			  
  
  

