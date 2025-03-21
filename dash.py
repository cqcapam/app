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
        background-image: url('https://ayurvedasalud.com/wp-content/uploads/2019/02/hd-wallpaper-macro-splash-67843-1024x678.jpg');
        background-size: cover;
        background-position: center;
    }
    .main {
        background-color: rgba(255, 255, 255, 0.95); /* Fundo branco */
        padding: 2rem;
        border-radius: 10px;
        margin: 2rem auto;
        max-width: 800px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        min-height: 500px;
    }
    h1, h2, p {
        color: black !important; /* Texto preto */
        text-align: center;
        font-weight: bold;
    }
    ol, ul, li {
        color: black !important; /* Texto preto */
        text-align: left;  /* Alinha o texto à esquerda */
        font-size: 14px;  /* Tamanho da fonte menor */
        font-weight: bold;
    }
    .button-container {
        text-align: center; /* Centraliza o botão */
        margin-top: 20px;
    }
    .custom-button {
        background-color: #007BFF; /* Azul */
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        font-weight: bold;
        cursor: pointer;
    }
    .custom-button:hover {
        background-color: #0056b3;
    }
    .footer {
        text-align: center;
        margin-top: 2rem;
        color: black !important; /* Texto preto */
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

# Link direto do Google Drive
download_link = "https://drive.google.com/uc?export=download&id=1WqNoQVPCMeJHQqy3N55Voi5uXjd6dxKy"

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
        <div class="button-container">
            <button class="custom-button" onclick="showWarning()">📥 Baixar Executável</button>
        </div>
        <div class="footer">
            <p>Desenvolvido com ❤️ por Jade Santiago</p>
        </div>
    </div>

    <script>
        function showWarning() {
            if (confirm("O Google Drive pode exibir um aviso de segurança ao baixar arquivos grandes. Clique em 'Estou Ciente' para continuar.")) {
                window.open('{download_link}', '_blank');
            }
        }
    </script>
""", unsafe_allow_html=True)
