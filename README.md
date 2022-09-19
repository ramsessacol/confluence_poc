# confluence_poc
Apenas uma marotagem com a api do confluence


## Configuração

Usei um arquivo json para manter alguns dados. Por isso é preciso criar um arquivo com o nome `dados_config.json` com a seguinte estrutura:
``
{
    "confluence_url": "",
    "username_confluence": "",
    "espaco": "",
    "pagina": "",
    "token": "",
    "titulo": ""
}
``
## Para executar o projeto > 

Esse projeto usa poetry para gerenciar as dependencias.

1) `poetry install`
2) `poetry run python3 criar_pagina.py`