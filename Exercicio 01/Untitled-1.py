import requests
from PIL import Image
from StringIO import StringIO

#response = requests.get('http://www.google.com')

def getstatuscode(url):
    response = requests.get(url)
    return response.status_code

def getheaderscontentype(url):
    response = requests.get(url) 
    return response.headers['content-type']

def getheaderscontentlength(url):
    response = requests.get(url) 
    return response.headers['content-length']

def getimage(url):
    response = requests.get(url)
    i = Image.open(StringIO(response.content))
    i.save("flower.jpg")
    return i.show()   

#getimage("https://conteudo.imguol.com.br/c/noticias/35/2018/09/22/22set2018---o-candidato-do-pt-fernando-haddad-caminhada-no-centro-do-recife-acompanhado-da-sua-vice-manuela-davila-pcdob-do-senador-humberto-costa-e-do-candidato-a-reeleicao-ao-governo-1537637710639_615x300.jpg")
     
def main():

    while True:
        print("1-quest01\n 2-quest02\n 3-quest03\n 0-sair"+"\n")
        menu=input("opcao: ")
        if menu == 1:
            op = raw_input("url:")
            print "statuscode:",getstatuscode(op)
            print "cabecalho:",getheaderscontentype(op)
            print "content length:",getheaderscontentlength(op)
        elif menu == 2:
            op = raw_input("url:")
            getimage(op)

   

main()