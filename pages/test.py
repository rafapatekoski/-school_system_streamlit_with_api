import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv
import os
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from time import sleep
from datetime import datetime
#from bson.objectid import ObjectId

import io
from docxtpl import DocxTemplate
from pathlib import Path
from datetime import datetime
pasta_documentos = Path(_file_).parent.parent / 'documentos/'
template_path = str(pasta_documentos)+"\\declaracaotransferencia.docx"
def doc_file_creation(template_path, data):
    doc = DocxTemplate(template_path)
    doc.render(data)
    return doc

def transferencia(update_data):
    listapilotocollection.update_one({"_id": dado["_id"]}, update_data)   
    print("teste")
    sleep(2)



load_dotenv(find_dotenv())
password = os.environ.get("MONGODB_PWD")
uri = f"mongodb+srv://patekoski:{password}@aprendendo.jvltr8a.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)


# Access the database and collection
teste_db = client.testeDb
listapilotocollection = teste_db.listapiloto

# Consulte todos os documentos na coleção
listapiloto = listapilotocollection.find()

# Transforme os documentos em um DataFrame do pandas
df = pd.DataFrame(list(listapiloto))
df["select"] = False
st.data_editor(df,key="dflistapiloto")


def editar(update_data):
    # Obtenha os dados editados como uma lista de dicionários
    #db.devices.updateOne({"_id": ObjectId("6427f848b39a9135e7b7e63e")}, {"$set" :{"value": "on"}}
    listapilotocollection.update_one({"_id": dado["_id"]}, update_data)   
    print("teste")
    sleep(2)

# edicao
selected_rows = st.session_state["dflistapiloto"]["edited_rows"]
selected_rows = [int(row) for row in selected_rows if selected_rows[row]["select"]]
try:    
    dado = df.iloc[selected_rows[-1]]
    st.write(dado["_id"])
    nome = st.text_input("Nome", dado["NOME"])

    # Assuming dado["nascimento"] is a string in the format "DD/MM/YYYY"
    nascimento_str = dado["NASCIMENTO"]
    nascimento_datetime = datetime.strptime(nascimento_str, "%d/%m/%Y")

    nascimento = st.date_input("Data de Nascimento", nascimento_datetime, format="DD/MM/YYYY")
    hoje = datetime.today().date()
    hoje = hoje.strftime("%d/%m/%Y")
    hoje = str(hoje)
    transferencia_update = {
    "$set": {
        "SAIDA": hoje # Update with the desired value
    }
}
    chaves = ["responsavel", "cpf_responsavel", "nome_aluno", "RA", "serie"]
    valores = ["Primeiro Pai", "000000", nome, dado["RA"], ]
    context = dict(zip(chaves, valores))
    doc_download = doc_file_creation(template_path, context)
    bio = io.BytesIO()
    doc_download.save(bio)
    if doc_download:
        btn_baixar = st.download_button(
            label="Emitir Transferência",
            data=bio.getvalue(),
            file_name=(f"{context['nome_aluno']}_saida.docx"),
            mime="docx",
            on_click=transferencia(transferencia_update)
        )
except:
    dado = "Nenhum aluno selecionado para edição"
    st.write(dado)