import requests
"""response = requests.get('http://www.google.com')
print(response.status_code)
print(response.headers['content-type'])
print(response.headers['content-length'])
"""
def quest01(self, url):
    response = requests.get(url)
    return response.status_code
    
def main():
    menu = "1-quest01\n 2-quest02\n 3-quest03\n 0-sair"
    while True:
        print(menu)
        menu=input("opcao: ")
        if menu == 1:
            print(quest01)
        if menu == "0":
            break
   

main()