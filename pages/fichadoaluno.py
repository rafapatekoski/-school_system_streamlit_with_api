import streamlit as st
from time import sleep
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
import io
from docxtpl import DocxTemplate
from pathlib import Path
from datetime import datetime
import requests
# URL para onde você deseja fazer o GET
# Verifica se a requisição foi bem-sucedida (código de status 200)

pasta_documentos = Path(__file__).parent.parent / 'documentos'
template_path = pasta_documentos / 'declaracaotransferencia.docx'
# Agora template_path é um objeto Path, mas você pode convertê-lo para uma string se necessário
template_path_str = str(template_path)
# Path to the Word document template
#construir download aqui
    #funcoes transferencia
def clicoubotao():
    st.write("clicou")
def transferencia():
    print('id enviado até aqui')
    hoje = datetime.today().date()
    hoje = hoje.strftime("%d/%m/%Y")
    hoje = str(hoje)
        # Dados que você deseja enviar no corpo da requisição
    data = {
            "saida": hoje
    }
        # ID como variável
    aluno_id = infoAluno["_id"] # Substitua pelo ID desejado
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
    print(response)
        # Verificar o status da resposta
    if response.status_code == 200:
        st.success("deu certo a atualização, volte para home para atualizar")
        del st.session_state["df"]
        print("PUT bem-sucedido!")
    else:
        print(f"Falha no PUT. Código de status: {response.status_code}")
        print(response.text)
def doc_file_creation(template_path, data):
    doc = DocxTemplate(template_path)
    doc.render(data)
    return doc
if "voltarHome" not in st.session_state:
    print("continue daqui")
else:
    switch_page("Home")

    
if "alunoSelecionado" not in st.session_state:
    switch_page("lista píloto")
else:
    print("Continue")
infoAluno = st.session_state["alunoSelecionado"]
st.write(f"Nome: {infoAluno["nome"]} id: {infoAluno["_id"]}")
    
sala = str(infoAluno["sala"])
sala = sala[0]
chaves = ["responsavel", "cpf_responsavel", "nome_aluno", "RA", "serie"]
valores = ["Primeiro Pai", "000000", infoAluno["nome"], infoAluno["ra"], ]
context = dict(zip(chaves, valores))
idparaenviar = []

# Atribuindo valores aos elementos
idparaenviar.append(infoAluno["_id"])      
        # Create and render the Word document
#se o aluno foi transferido
if infoAluno["saida"] == "matriculado":

    def on_button_click(id):
        print("clicou no botão")
        idparaenviar.append(True)  
        transferencia(id)
    doc_download = doc_file_creation(template_path, context)
    bio = io.BytesIO()
    doc_download.save(bio)
    if doc_download:
        btn_baixar = st.download_button(
            label="Emitir Transferência",
            data=bio.getvalue(),
            file_name=(f"{context['nome_aluno']}_saida.docx"),
            mime="docx",
            on_click=transferencia
        )
else:
    st.error(f"Aluno transferido no dia: {infoAluno['saida']}")
        # Save the document to BytesIO

del st.session_state['alunoSelecionado'] 