import streamlit as st

# Configurações da página
st.set_page_config(
    page_title="Aplicativo CQ - CAPAM",
    page_icon="📥",
    layout="centered",
)

# CSS personalizado para garantir que o texto fique na frente do quadrado branco
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://www.hdwallpapers.in/thumbs/2018/splash_4k-t2.jpg');
        background-size: cover;
        background-position: center;
        display: flex;
        justify-content: center;
    }
    .content-box {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 2rem;
        border-radius: 10px;
        max-width: 800px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        position: relative;
        z-index: 10;
        text-align: center;
    }
    .stMarkdown, h1, h2 {
        color: #2c3e50;
        z-index: 20;
        position: relative;
    }
    .stButton button {
        background-color: #3498db;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        width: 100%;
        margin-top: 1rem;
        border: none;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }
    .stButton button:hover {
        background-color: #2980b9;
    }
    .footer {
        text-align: center;
        margin-top: 2rem;
        color: #7f8c8d;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Criar a estrutura principal
with st.container():
    st.markdown('<div class="content-box">', unsafe_allow_html=True)
    
    # Título e descrição
    st.title("Bem-vindo ao Aplicativo CQ - CAPAM")
    st.write("Aqui você pode baixar a versão mais recente do aplicativo e seguir o tutorial para configurá-lo.")
    
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
           - Execute o aplicativo e comece a utilizá-lo imediatamente!
        """
    )
    
    # Botão de download
    st.markdown(
        """
        <a href="https://drive.google.com/uc?export=download&id=SEU_ID_DO_ARQUIVO" target="_blank">
            <button style="background-color: #3498db; color: white; border-radius: 5px; padding: 10px 20px; font-size: 16px; width: 100%; border: none;">
                📥 Baixar Executável
            </button>
        </a>
        """,
        unsafe_allow_html=True,
    )
    
    # Rodapé
    st.markdown(
        """
        <div class="footer">
            <p>Desenvolvido com ❤️ por CAPAM - Controle de Qualidade</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    # Fechar a div do quadrado branco
    st.markdown('</div>', unsafe_allow_html=True)
