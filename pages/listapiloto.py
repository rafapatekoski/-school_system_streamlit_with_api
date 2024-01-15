import streamlit as st
import requests
import pandas as pd
from st_pages import Page, Section, add_page_title, show_pages
from streamlit_extras.switch_page_button import switch_page
from time import sleep
import io
from docxtpl import DocxTemplate
from pathlib import Path
from datetime import datetime

def paginadoaluno(dado):
    st.session_state["alunoSelecionado"] = dado
if "alunoSelecionado" not in st.session_state:
    print("siga ->")
else:
    print("não sei o que lpá sosjks")
    switch_page("Ficha do Aluno")

if "df" not in st.session_state:
    st.write("Volta para home para carregar os dados")
    sleep(1)
    switch_page("Home")
else:
    dados = st.session_state["df"]
    df = pd.DataFrame(dados)
    df.insert(0, 'select', False)
    st.data_editor(df, key="dflistapiloto")
    selected_rows = st.session_state["dflistapiloto"]["edited_rows"]
    selected_rows = [int(row) for row in selected_rows if selected_rows[row]["select"]]
    try:    
        dado = df.iloc[selected_rows[-1]]
        idselecionado = dado["_id"]
        #paginadoaluno(dado)
        st.write(f"Nome: {dado["nome"]}")
        st.button("Ir para pagina", on_click=paginadoaluno(dado))
        
        
    except:
        print('nao deu certo aqui')