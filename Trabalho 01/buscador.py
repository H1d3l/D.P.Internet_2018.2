from bs4 import BeautifulSoup
import requests,re

class Buscador:
    
    def __init__(self,keyword):
        self.keyword = keyword

    def search_word(self,url):
        words = []
        try:
            response = requests.get(url)
        except Exception as erro:
            print('Erro de Conexão')
            response = None
        soup = BeautifulSoup(response.text,'html.parser')
        temp = soup.find_all(string = re.compile(self.keyword))
        for i in temp:
            temp1 = i.find(self.keyword)
            words.append(i[temp1-10:len(self.keyword)+temp1+10])
        return words


    def search_all(self,url,deth):
        links = []
        if deth == 0:
            return self.search_word(url)
        
        #if deth>0:


                

p = Buscador('Hildebrando')
print(p.search_all('https://pt.wikipedia.org/wiki/Hildebrando_Pascoal',0))