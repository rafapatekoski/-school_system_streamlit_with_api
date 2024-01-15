import streamlit as st
import requests
import pandas as pd
from st_pages import Page, Section, add_page_title, show_pages

# Specify what pages should be shown in the sidebar, and what their titles 
# and icons should be
show_pages([
    Page("app.py", "Home"),
    Page("pages/listapiloto.py", "Lista Píloto"),
    Page("pages/editar.py", "Editar Aluno"),
    Page("pages/post.py", "Matricular Aluno"),
    Page("pages/fichadoaluno.py", "Ficha do Aluno")
])
# URL para onde você deseja fazer o GET
url = 'https://apinodealuno.onrender.com/api/alunos'

# Faz a requisição GET
response = requests.get(url)


# Verifica se a requisição foi bem-sucedida (código de status 200)
if response.status_code == 200:
    dados = response.json()
    st.session_state["df"] = pd.DataFrame(dados)
    df = st.session_state["df"]
    st.write("Seja bem-vindo ao Projeto Alcantara")
    numero_de_linhas = df.shape[0]
    alunos_matriculados = df[df['saida'] == 'matriculado']
    matriculas_totais = df.groupby("sala").size().reset_index(name='matriculas_totais')
# Contar o número de alunos matriculados por sala
    matriculas_ativas = alunos_matriculados.groupby('sala').size().reset_index(name='matriculas_ativas')
    st.write(f"Temos {numero_de_linhas} alunos registrados")
    #df_final = pd.merge(matriculas_totais, matriculas_ativas, on='sala')
    df_final = pd.merge(matriculas_totais, matriculas_ativas, on='sala', how='outer')
    df_final.fillna(0, inplace=True)
    df_final["transferidos"] = df_final["matriculas_totais"] - df_final["matriculas_ativas"]
    st.dataframe(df_final)
    print('GET bem-sucedido!')
else:
    print('Erro no GET. Código de status:', response.status_code)

