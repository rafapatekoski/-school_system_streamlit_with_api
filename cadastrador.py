import requests
import json
import pandas as pd
# URL para onde você deseja fazer o POST
url = 'https://apinodealuno.onrender.com/api/alunos'

def cadastrar_aluno(data):
    # Configurar o cabeçalho da requisição
    dataa = data
    headers = {
        "Content-Type": "application/json"
    }

    # Converter o dicionário em JSON
    json_data = json.dumps(dataa)
    print(json_data)
    # Fazer a requisição POST
    response = requests.post(url, data=json_data, headers=headers)
    print(response)
    # Verificar o status da resposta
    if response.status_code == 200:
        print("POST bem-sucedido!")
    else:
        print(f"Falha no POST. Código de status: {response.status_code}")
        print(response.text)
        cadastrar_aluno(dataa)

df = pd.read_csv("listapiloto2024.csv", sep=";")
# Criação dos widgets de entrada para cada variável
#nome = st.text_input("Digite seu nome")
#ra = st.text_input("Digite seu RA")
#serie = st.text_input("Digite sua série")
#sala = st.text_input("Digite o número da sala")
#nascimento = st.text_input("Digite a data de nascimento (YYYY-MM-DD)")
#laudo = st.text_input("Digite se possui laudo (Sim/Nao)")
#entrada = st.text_input("Digite a data de entrada (DD/MM/YY)")
#saida = "---"
for indice, linha in df.iterrows():
    # Acessar o valor na coluna "nome" da linha atual
    nome = linha["NOME"]
    ra = linha["RA"]
    serie = linha["SERIE"]
    sala = str(linha["SERIE"]) + linha["SALA"]
    nascimento = linha["NASCIMENTO"]
    chamada = linha["CHAMADA"]
    laudo = "não possui"
    entrada = linha["ENTRADA"]
    saida = "matriculado"
    dados = {
    "nome": nome,
    "ra": ra,
    "serie": serie,
    "sala": sala,
    "chamada": chamada,
    "nascimento": nascimento,
    "laudo": laudo,
    "entrada": entrada,
    "saida": saida
    }
    cadastrar_aluno(dados)
    