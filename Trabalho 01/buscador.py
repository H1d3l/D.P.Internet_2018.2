from bs4 import BeautifulSoup
import requests
import re

#response = requests.get('http://www.ifpi.edu.br/')
#print (response)

class Buscador:
    def __init__(self,keyword,url,deth):
        self.keyword = keyword
        self.url = url
        self.deth = deth
    
    def search(self):
        words = []
        links = []
        try:
            response = requests.get(self.url)
        except Exception as erro:
            print('Erro de Conexão'+self.url)
            response = None
        soup = BeautifulSoup(response.text,'html.parser')
        word = soup.find_all(string = re.compile(self.keyword))
        if self.deth == 0:
            for i in word:
                temp = i.find(self.keyword)
                words.append(i[temp-10:len(self.keyword)+temp+10])
            return words
        if self.deth>0:
            link = soup.find_all('a')
            for i in link:
                temp = i.get('href')
                if temp!=None:
                    links.append(temp)
            return links

                


p = Buscador('Palmeiras','https://www.uol.com.br/',1)
print(p.search())