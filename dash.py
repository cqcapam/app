import streamlit as st

# Configurações da página
st.set_page_config(
    page_title="Aplicativo CQ - CAPAM",
    page_icon="📥",
    layout="centered",
)

# CSS personalizado
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://images.unsplash.com/photo-1619252584172-a83a949b6efd?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');
        background-size: cover;
        background-position: center;
    }
    .main {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 2rem;
        border-radius: 10px;
        margin: 2rem auto;
        max-width: 800px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        min-height: 500px;        
    }
    h1, h2, p {
        color: black !important;
        text-align: center;
        font-weight: bold;
    }
    ol, ul, li {
        color: black !important;
        text-align: left;
        font-size: 14px;
    }
    .button-container {
        text-align: center;
        margin-top: 20px;
    }
    .stButton button {
        background-color: #3498db;
        color: white !important;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        font-weight: bold;
    }
    .stButton button:hover {
        background-color: #2980b9;
    }
    .footer {
        text-align: center;
        margin-top: 2rem;
        color: black !important;
        font-weight: bold;
    }
    .logo-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 20px;
    }
    
    /* Esconde a barra superior do Streamlit */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)


# Exibir a logo centralizada
# Exibir a logo centralizada
col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')
    
with col2:
    st.image("logo.png", width=250)

with col3:
    st.write(' ')

# Conteúdo principal
title = "Tudo pronto para você!"
description = "Aqui você pode baixar a versão mais recente do aplicativo e seguir o tutorial para configurá-lo."

download_link = "https://drive.google.com/uc?export=download&id=1WqNoQVPCMeJHQqy3N55Voi5uXjd6dxKy"

st.markdown("""
    <div class="main">
        <h1>{}</h1>
        <p>{}</p>
        <h2>📋 Tutorial Passo a Passo</h2>
        <ol>
            <li><strong>Faça o download do arquivo:</strong>
                <ul>Clique no botão abaixo para baixar o executável.</ul>
            </li>
            <li><strong>Permita o download:</strong>
                <ul>O aplicativo é seguro e facilita o seu trabalho.</ul>
            </li>
            <li><strong>Localize o executável:</strong>
                <ul>O arquivo estará na pasta "Downloads".</ul>
            </li>
            <li><strong>Crie um atalho:</strong>
                <ul>Para facilitar o acesso, crie um atalho na área de trabalho.</ul>
            </li>
            <li><strong>Pronto para uso:</strong>
                <ul>Execute o aplicativo e comece a usá-lo!</ul>
            </li>
        </ol>
        <div class="button-container">
            <a href="{}" target="_blank">
                <button class="stButton">📥 Baixar Executável</button>
            </a>
        </div>
        <div class="footer">
            <p>Desenvolvido com ❤️ por Jade Santiago</p>
        </div>
    </div>
""".format(title, description, download_link), unsafe_allow_html=True)

# Mensagem de aviso sobre o Google Drive
st.warning("O Google Drive pode exibir um aviso de segurança ao baixar arquivos grandes. Clique em 'Fazer Download mesmo assim' para continuar.")
