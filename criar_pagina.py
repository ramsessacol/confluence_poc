import json
from turtle import st
from atlassian import Confluence

with open('dados_config.json') as input_file:
    json_stuff = json.loads(input_file.read())

url_confluence=json_stuff["confluence_url"]
username_confluence=json_stuff["username_confluence"]
espaco_confluence=json_stuff["espaco"]
token_confluence=json_stuff["token"]
titulo_maroto=json_stuff["titulo"]

try:
    confluence = Confluence(url=url_confluence,username=username_confluence,password=token_confluence,cloud=True)
except Exception as deu_ruim:
    print("ops, acho que a cagada comeu aqui " + url_confluence)
    print(deu_ruim)

print("########################################################################")
print ("Validando se o espaco está certo : " + espaco_confluence)

status=confluence.get_space(espaco_confluence, expand='description.plain,homepage')
#status=confluence.get_page_by_id(espaco_confluence)
print(status)
if "StatusCode" in status:
    if status["StatusCode"] == 401:
        print("Preciso rever, pq não eh isso" + espaco_confluence)
    else:
        print("Piorou, erro que nem eu sabia que existia")
        print(status["StatusCode"])
        print(status)
        exit(8)
else:
    print("Opa, parece que tamo indo " + espaco_confluence + " Nome " + status["name"])

print("########################################################################")
tituloPagina =  titulo_maroto
status1= confluence.create_page(space=espaco_confluence, title=tituloPagina, \
             body='<strong>Acho que consegui</strong>!')
if "id" in status1:
    print(status)
    print("Feito consagrado, consegui : " + str(status1["id"]) + " titulo : \"" + status1["title"] + "\" no espaco : " + status1["space"]["name"])
else:
    print("Preciso rever, pq não eh isso" + espaco_confluence)
    print(status1)
    exit()