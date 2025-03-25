# dashboard.py
import streamlit as st
from PIL import Image
import io

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
        background-image: url('https://wallpaperaccess.com/full/2925320.jpg');
        background-size: cover;
        background-position: center;
    }

    /* Quadrado branco semi-transparente */
    .main {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 2rem;
        border-radius: 10px;
        margin: 2rem auto;
        max-width: 950px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    /* Container da logo - centralizado e com margem */
    .logo-container {
        display: flex;
        justify-content: center;
        margin: 0 auto 1.5rem auto;
        width: 100%;
    }

    /* Estilo da logo reduzida */
    .logo-img {
        max-width: 400px;  /* Largura máxima reduzida */
        width: 100%;
        height: auto;
    }

    /* Outros estilos permanecem iguais */
    h1 {
        color: #2c3e50;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    /* ... (mantenha o resto do CSS igual) ... */
    </style>
    """,
    unsafe_allow_html=True,
)

# Conteúdo dentro do quadrado branco
with st.container():
    st.markdown('<div class="main">', unsafe_allow_html=True)
    
    # Logo - container e imagem
    st.markdown('<div class="logo-container">', unsafe_allow_html=True)
    try:
        # Carrega a imagem e redimensiona para tamanho menor
        logo = Image.open('logo.png')
        
        # Novo tamanho desejado (ajuste esses valores conforme necessário)
        new_width = 400  # Largura desejada em pixels
        ratio = new_width / float(logo.size[0])
        new_height = int(float(logo.size[1]) * float(ratio))
        
        logo = logo.resize((new_width, new_height), Image.LANCZOS)
        
        # Exibe a imagem redimensionada
        st.image(logo, use_column_width=False, width=new_width, 
                 output_format='PNG', caption='')
    
    except FileNotFoundError:
        st.warning("Logo não encontrada. Verifique o caminho do arquivo.")
    
    st.markdown('</div>', unsafe_allow_html=True)

    # Restante do conteúdo (título, tutorial, etc.)
    st.title("Bem-vindo ao Aplicativo CQ - CAPAM")
    st.subheader("Aqui você pode baixar a versão mais recente do aplicativo e seguir o tutorial para configurá-lo.")
    
    # ... (mantenha o resto do conteúdo igual) ...

    # Fechar a div do quadrado branco
    st.markdown('</div>', unsafe_allow_html=True)
