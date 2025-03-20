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
        background-image: url('https://wallpaperaccess.com/full/2925320.jpg');  /* Substitua pelo link da sua imagem */
        background-size: cover;
        background-position: center;
    }

    /* Quadrado branco semi-transparente */
    .main {
        background-color: rgba(255, 255, 255, 0.9);  /* Branco com 90% de opacidade */
        padding: 1rem;
        border-radius: 10px;
        margin: 3rem auto;
        max-width: 950px;
        height: 950px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    /* Estilo dos títulos */
    h1 {
        color: #2c3e50;  /* Azul marinho */
        text-align: center;
        margin-bottom: 0.5rem;
    }

    h2 {
        color: #34495e;  /* Azul marinho mais escuro */
        text-align: center;
        margin-top: 1.5rem;
    }
    
    h3 {
        color: #34495e;  /* Azul marinho mais escuro */
        text-align: center;
        margin-top: 0.02rem;
    }

    /* Estilo dos botões */
    .stButton button {
        background-color: #3498db;  /* Azul */
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        width: 100%;
        margin-top: 1rem;
    }

    .stButton button:hover {
        background-color: #2980b9;  /* Azul mais escuro no hover */
    }

    /* Estilo do texto */
    .stMarkdown {
        color: #2c3e50;  /* Azul marinho */
        font-size: 16px;
        line-height: 1.6;
    }

    /* Rodapé */
    .footer {
        text-align: center;
        margin-top: 2rem;
        color: #7f8c8d;  /* Cinza */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Conteúdo dentro do quadrado branco
#st.markdown('<div class="main">', unsafe_allow_html=True)

# Título
st.title("Bem-vindo ao Aplicativo CQ - CAPAM")
st.subheader("Aqui você pode baixar a versão mais recente do aplicativo e seguir o tutorial para configurá-lo.")

# Tutorial
st.header("📋 Tutorial Passo a Passo")
st.markdown(
    """
    1. **Faça o download do arquivo**:
       - Clique no botão abaixo para baixar o executável do aplicativo.
    2. **Permita o download**:
       - Este aplicativo é seguro e foi desenvolvido para facilitar o seu trabalho.
    3. **Localize o executável**:
       - O arquivo baixado estará na sua pasta **"Downloads"**.
    4. **Crie um atalho**:
       - Para facilitar o acesso, crie um atalho na área de trabalho ou fixe o aplicativo na sua barra de tarefas.
    5. **Pronto para uso**:
       - Execute o aplicativo e comece a utilizá-lo!
    """
)

# Botão para baixar o executável
with open("dist/apptk.exe", "rb") as file:
    btn = st.download_button(
        label="📥 Baixar Executável",
        data=file,
        file_name="apptk.exe",
        mime="application/octet-stream",
    )

# Rodapé
st.markdown(
    """
    <div class="footer">
        <p>Desenvolvido com ❤️ por Jade Santiago</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Fechar a div do quadrado branco
st.markdown('</div>', unsafe_allow_html=True)
