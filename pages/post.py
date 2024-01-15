import streamlit as st
import requests
import json

# URL para onde você deseja fazer o POST
url = 'https://apinodealuno.onrender.com/api/alunos'

def cadastrar_aluno(data):
    # Configurar o cabeçalho da requisição
    headers = {
        "Content-Type": "application/json"
    }

    # Converter o dicionário em JSON
    json_data = json.dumps(data)

    # Fazer a requisição POST
    response = requests.post(url, data=json_data, headers=headers)

    # Verificar o status da resposta
    if response.status_code == 200:
        print("POST bem-sucedido!")
    else:
        print(f"Falha no POST. Código de status: {response.status_code}")
        print(response.text)
    print(dados)

# Criação dos widgets de entrada para cada variável
nome = st.text_input("Digite seu nome")
ra = st.text_input("Digite seu RA")
serie = st.text_input("Digite sua série")
sala = st.text_input("Digite o número da sala")
chamada = st.text_input("Digite a chamada")
nascimento = st.text_input("Digite a data de nascimento (YYYY-MM-DD)")
laudo = st.text_input("Digite se possui laudo (Sim/Nao)")
entrada = st.text_input("Digite a data de entrada (DD/MM/YY)")
saida = "---"

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

# Função que será chamada quando o botão for clicado
def on_button_click():
    cadastrar_aluno(dados)

# Botão para enviar os dados
st.button("Enviar", on_click=on_button_click)
