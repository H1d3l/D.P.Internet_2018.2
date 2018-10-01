from bs4 import BeautifulSoup
import requests,re

class Buscador:
    
    def __init__(self,keyword,url,deth):
        self.keyword = keyword
        self.url = url
        self.deth = deth

    def conexion(self):
        try:
            response = requests.get(self.url)
        except Exception as erro:
            print('Erro de Conexão'+self.url)
            response = None
        soup = BeautifulSoup(response.text,'html.parser')
        return soup

    


    def search_word(self):
        words = []
        word = self.conexion()
        temp = word.find_all(string = re.compile(self.keyword))
        for i in temp:
            temp1 = i.find(self.keyword)
            words.append(i[temp1-10:len(self.keyword)+temp1+10])
        return words


    def search_all(self):
        links = []
        if self.deth == 0:
            return self.search_word()
        if self.deth>0:
            temp = self.conexion()
            link = temp.find_all('a')
            for i in link:
                temp = i.get('href')
                if temp!=None:
                    links.append(temp)
            return links

                


p = Buscador('Palmeiras','https://www.uol.com.br/',1)
print(p.search_word())