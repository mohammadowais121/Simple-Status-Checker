'''
Author: Mohammad Owais
Email: mohammadowais616@gmail.com
How to use:

URLS.TXT should contain HTTP/HTTPS URLS.
python status-finder
or
python3 status-finder
'''

import requests
import os,sys
import sys



def main():
	
	print('\033[32m' + """
 ___   _         _                    ___            _            
(  _`\( )_      ( )_                /'____          ( )           
| (_(_| ,_)  _ _| ,_)_   _  ___    | (__(_) ___    _| |  __  _ __ 
`\__ \| |  /'_` | | ( ) ( /',__)   | ,__| /' _ `\/'_` |/'__`( '__)
( )_) | |_( (_| | |_| (_) \__, \   | |  | | ( ) ( (_| (  ___| |   
`\____`\__`\__,_`\__`\___/(____/   (_)  (_(_) (_`\__,_`\____(_)   
                                                                  
                                                                  """)
	print('\033[32m' +"""                                                       Coded by Mohamad Owais""")
	print("[~] URLS|Status..")
	for link in open("urls.txt","r").read().splitlines():
		try:
			r = requests.get(link, allow_redirects=True, timeout=4)
			print(link + " ["+ str(r.status_code)+ "]")
		except requests.exceptions.ConnectionError:
			print("Host Dead!")
			
			
			

if __name__=="__main__":
	main()
