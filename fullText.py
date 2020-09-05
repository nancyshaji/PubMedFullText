import requests 
from bs4 import BeautifulSoup 
print("PMID \t\t Full text link")
f = open("pmid.txt", "r") #opening the file with pmids
p=f.readline() #reads first id
while(p):
	url=f"https://pubmed.ncbi.nlm.nih.gov/" 
	url=url+p[:-1]#add it to link after removing the \n
	print(p[:-1],end='\t')
	#print(url) 
	# Sending HTTP request 
	req = requests.get(url) 
	data=req.text  
	# Pulling HTTP data from internet  
	soup = BeautifulSoup(data,"html.parser") 
	#print(soup)
	print(soup.find("aside", class_ = "page-sidebar").div.a.get('href'))
	p=f.readline() #read next line
	print('\n')
f.close()
