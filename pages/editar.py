import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
from datetime import datetime
from time import sleep
import requests
# URL para onde você deseja fazer o GET
# Verifica se a requisição foi bem-sucedida (código de status 200)
def editar(dados):

    # Dados que você deseja enviar no corpo da requisição
    data = {
    "id": idselecionado,
    "nome": nome,
    "ra": ra,
    "serie": serie,
    "sala": sala,
    "chamada": chamada,
    "nascimento": nascimento,
    "laudo": laudo,
    }
    # ID como variável
    aluno_id = data["id"]  # Substitua pelo ID desejado
    aluno_id = str(aluno_id)
    # URL para onde você deseja fazer o PUT com o ID como parte da URL
    url = f"https://apinodealuno.onrender.com/api/alunos/{aluno_id}"

    # Configurar o cabeçalho da requisição (Content-Type: application/json)
    headers = {
        "Content-Type": "application/json"
    }
    # Fazer a requisição PUT
# Fazer a requisição PUT
    response = requests.put(url, json=data, headers=headers)

    # Verificar o status da resposta
    if response.status_code == 200:
        st.success("deu certo a atualização, volte para home para atualizar")
        del st.session_state["df"]
        print("PUT bem-sucedido!")
    else:
        print(f"Falha no PUT. Código de status: {response.status_code}")
        print(response.text)
if "df" not in st.session_state:
    st.write("Volta para home para carregar os dados")
    sleep(1)
    switch_page("Home")
else:
    dados = st.session_state["df"]
    df = pd.DataFrame(dados)
    df["select"] = False
    st.data_editor(df,key="dflistapiloto")
    # edicao
    selected_rows = st.session_state["dflistapiloto"]["edited_rows"]
    selected_rows = [int(row) for row in selected_rows if selected_rows[row]["select"]]
    try:    
        dado = df.iloc[selected_rows[-1]]
        idselecionado = dado["_id"]
        nome = st.text_input("Nome:",dado["nome"])
        ra = st.text_input("Digite seu RA", dado["ra"])
        serie = st.text_input("Digite sua série", dado["serie"])
        sala = st.text_input("Digite o número da sala", dado["sala"])
        chamada = st.text_input("Digite a chamada", dado["chamada"])
        nascimento = st.text_input("Digite a data de nascimento", dado["nascimento"])
        laudo = st.text_input("Digite se possui laudo", dado["laudo"])
        hoje = datetime.today().date()
        hoje = hoje.strftime("%d/%m/%Y")
        hoje = str(hoje)
        entrada = hoje  
        def on_button_click():
            editar(dados)
# Botão para enviar os dados
        st.button("Enviar", on_click=on_button_click)
    except:
        print('...')