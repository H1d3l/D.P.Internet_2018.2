# for more information on how to install requests
# http://docs.python-requests.org/en/master/user/install/#install


'''
A Oxford Dictionaries API permite acesso fácil conteúdo de dicionário de renome mundial.
Use a documentação ao vivo abaixo para experimentar, visualizar respostas reais e explorar um número crescente
de amostras de código para ajudar você a começar.
'''

import  requests
import json
# TODO: replace with your own app_id and app_key
app_id = '60d5c52a'
app_key = '8070cb7e4f64043112fcea1470533d14'
language = 'es'
word_id = 'rojo'
url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/'  + language + '/'  + word_id.lower()
#url Normalized frequency
urlFR = 'https://od-api.oxforddictionaries.com:443/api/v1/stats/frequency/word/'  + language + '/?corpus=nmc&lemma=' + word_id.lower()
r = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})
print("code {}\n".format(r.status_code))
print("text \n" + r.text)
print("json \n" + json.dumps(r.json()))
