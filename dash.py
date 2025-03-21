import streamlit as st

# Configurações da página
st.set_page_config(
    page_title="Aplicativo CQ - CAPAM",
    page_icon="📥",
    layout="centered",
)

# CSS personalizado para estilizar o botão
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
        text-align: left;
        font-size: 14px;
        font-weight: bold;
    }
    .button-container {
        text-align: center; /* Centraliza o botão */
        margin-top: 20px;
    }
    .stButton button {
        background-color: #007BFF !important; /* Azul */
        color: white !important;
        border: none !important;
        border-radius: 5px !important;
        padding: 10px 20px !important;
        font-size: 16px !important;
        font-weight: bold !important;
        cursor: pointer !important;
    }
    .stButton button:hover {
        background-color: #0056b3 !important;
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
        <div class="footer">
            <p>Desenvolvido com ❤️ por Jade Santiago</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# Lógica para exibir a mensagem antes do download
if st.button("📥 Baixar Executável"):
    st.warning("O Google Drive pode exibir um aviso de segurança ao baixar arquivos grandes. Clique em 'Estou Ciente' para continuar.")
    if st.button("Estou Ciente"):
        st.markdown(f'<meta http-equiv="refresh" content="0;url={download_link}">', unsafe_allow_html=True)
