import requests
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




     
def main():

    while True:
        print("1-quest01\n 2-quest02\n 3-quest03\n 0-sair"+"\n")
        menu=input("opcao: ")
        if menu == 1:
            op = raw_input("url:")
            print "statuscode:",getstatuscode(op)
            print "cabecalho:",getheaderscontentype(op)
            print "content length:",getheaderscontentlength(op)

   

main()