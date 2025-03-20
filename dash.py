# dashboard.py
import streamlit as st

# Configurações da página
st.set_page_config(
    page_title="Aplicativo CQ - CAPAM",
    page_icon="📥",
    layout="centered",
)

# CSS personalizado para estilizar o dashboard
st.markdown(
    """
    <style>
    /* Fundo com a imagem de capa */
    .stApp {
        background-image: url('https://www.hdwallpapers.in/thumbs/2018/splash_4k-t2.jpg');  /* Substitua pelo link da sua imagem */
        background-size: cover;
        background-position: center;
    }

    /* Quadrado preto semi-transparente */
    .main {
        background-color: rgba(0, 0, 0, 0.5);  /* Preto com 50% de opacidade */
        padding: 2rem;
        border-radius: 10px;
        margin: 2rem auto;
        max-width: 800px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        min-height: 500px;  /* Altura mínima de 500 pixels */
        position: relative;  /* Permite sobrepor elementos */
        z-index: 1;  /* Define a ordem de sobreposição */
    }

    /* Estilo dos títulos */
    h1 {
        color: white !important;  /* Texto branco */
        text-align: center;
        margin-bottom: 1.5rem;
        font-weight: bold;  /* Negrito */
    }

    h2 {
        color: white !important;  /* Texto branco */
        margin-top: 1.5rem;
        font-weight: bold;  /* Negrito */
    }

    /* Estilo dos botões */
    .stButton button {
        background-color: #3498db;  /* Azul */
        color: white !important;  /* Texto branco */
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        width: 100%;
        margin-top: 1rem;
        font-weight: bold;  /* Negrito */
    }

    .stButton button:hover {
        background-color: #2980b9;  /* Azul mais escuro no hover */
    }

    /* Estilo do texto */
    .stMarkdown {
        color: white !important;  /* Texto branco */
        font-size: 16px;
        line-height: 1.6;
        font-weight: bold;  /* Negrito */
    }

    /* Rodapé */
    .footer {
        text-align: center;
        margin-top: 2rem;
        color: white !important;  /* Texto branco */
        font-weight: bold;  /* Negrito */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Criar um container para o quadrado preto e inserir todo o conteúdo dentro dele
st.markdown(
    """
    <div class="main">
        <h1>Bem-vindo ao Aplicativo CQ - CAPAM</h1>
        <p>Aqui você pode baixar a versão mais recente do aplicativo e seguir o tutorial para configurá-lo.</p>

        <p>📋 Tutorial Passo a Passo</p>
        <ol>
            <li><strong>Faça o download do arquivo</strong>:
                <ul>
                    <li>Clique no botão abaixo para baixar o executável do aplicativo.</li>
                </ul>
            </li>
            <li><strong>Permita o download</strong>:
                <ul>
                    <li>Este aplicativo é seguro e foi desenvolvido para facilitar o seu trabalho.</li>
                </ul>
            </li>
            <li><strong>Localize o executável</strong>:
                <ul>
                    <li>O arquivo baixado estará na sua pasta <strong>"Downloads"</strong>.</li>
                </ul>
            </li>
            <li><strong>Crie um atalho</strong>:
                <ul>
                    <li>Para facilitar o acesso, crie um atalho na área de trabalho ou fixe o aplicativo na sua barra de tarefas.</li>
                </ul>
            </li>
            <li><strong>Pronto para uso</strong>:
                <ul>
                    <li>Execute o aplicativo e comece a utilizá-lo imediatamente!</li>
                </ul>
            </li>
        </ol>

        <a href="https://drive.google.com/uc?export=download&id=SEU_ID_DO_ARQUIVO" target="_blank">
            <button style="background-color: #3498db; color: white; border-radius: 5px; padding: 10px 20px; font-size: 16px; width: 100%;">
                📥 Baixar Executável
            </button>
        </a>

        <div class="footer">
            <p>Desenvolvido com ❤️ por CAPAM - Controle de Qualidade</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,  # Permite renderizar HTML
)
