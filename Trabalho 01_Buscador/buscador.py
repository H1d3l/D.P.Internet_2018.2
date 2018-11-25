from bs4 import BeautifulSoup
import requests,re

class Buscador:
    
    def __init__(self,keyword,url,deth):
        self.keyword = keyword
        self.url = url
        self.deth = deth

    def search_word(self):
        words = []
        links = []
        try:
            response = requests.get(self.url)
        except Exception as erro:
            print('Erro de Conexão')
            response = None

        soup = BeautifulSoup(response.text,'html.parser')
        temp = soup.find_all(string = re.compile(self.keyword))
        
        if self.deth == 0:                
            for i in temp:
                temp1 = i.find(self.keyword)
                words.append(i[temp1-10:len(self.keyword)+temp1+10])
            return words
        elif self.deth>0:
            for i in soup.find_all('a'):
                links.append(i.get('href'))
                





                
p = Buscador('Hildebrando','https://pt.wikipedia.org/wiki/Hildebrando_Pascoal',0)
print(p.search_word())