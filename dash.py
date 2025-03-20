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
        background-image: url('https://www.hdwallpapers.in/thumbs/2018/splash_4k-t2.jpg');
        background-size: cover;
        background-position: center;
    }
    .main {
        background-color: rgba(0, 0, 0, 0.6);
        padding: 2rem;
        border-radius: 10px;
        margin: 2rem auto;
        max-width: 800px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        min-height: 500px;
    }
    h1, h2, p {
        color: white !important;
        text-align: center;
        font-weight: bold;
    }
    ol, ul, li {
        color: white !important;
        text-align: left;  /* Alinha o texto à esquerda */
        font-size: 14px;  /* Tamanho da fonte menor */
        font-weight: bold;
    }
    .stButton button {
        background-color: #3498db;
        color: white !important;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        width: 100%;
        margin-top: 1rem;
        font-weight: bold;
    }
    .stButton button:hover {
        background-color: #2980b9;
    }
    .footer {
        text-align: center;
        margin-top: 2rem;
        color: white !important;
        font-weight: bold;
    }
    /* Esconde a barra superior do Streamlit */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

# Conteúdo principal
title = "Tudo pronto para você!"
description = "Aqui você pode baixar a versão mais recente do aplicativo e seguir o tutorial para configurá-lo."

st.markdown(f"""
    <div class="main">
        <h1>{title}</h1>
        <p>{description}</p>
        <h2>📋 Tutorial Passo a Passo</h2>
        <ol>
            <li><strong>Faça o download do arquivo:</strong>
                <ul><li>Clique no botão abaixo para baixar o executável.</li></ul>
            </li>
            <li><strong>Permita o download:</strong>
                <ul><li>O aplicativo é seguro e facilita o seu trabalho.</li></ul>
            </li>
            <li><strong>Localize o executável:</strong>
                <ul><li>O arquivo estará na pasta "Downloads".</li></ul>
            </li>
            <li><strong>Crie um atalho:</strong>
                <ul><li>Para facilitar o acesso, crie um atalho na área de trabalho.</li></ul>
            </li>
            <li><strong>Pronto para uso:</strong>
                <ul><li>Execute o aplicativo e comece a usá-lo!</li></ul>
            </li>
        </ol>
        <a href="https://drive.google.com/uc?export=download&id=1WqNoQVPCMeJHQqy3N55Voi5uXjd6dxKy" target="_blank">
            <button class="stButton">📥 Baixar Executável</button>
        </a>
        <div class="footer">
            <p>Desenvolvido com ❤️ por Jade Santiago</p>
        </div>
    </div>
""", unsafe_allow_html=True)
