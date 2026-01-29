__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import streamlit as st
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_groq import ChatGroq  # <--- CAMBIATO IN GROQ
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings # <--- GRATIS

# --- CONFIGURAZIONE ---
st.set_page_config(page_title="AI Human Capital Mapper (Groq Edition)", layout="wide")
st.title("🧠 AI Knowledge Mapper (Powered by Groq)")
st.sidebar.info("Esercizio 2: Sistema con Groq e Local Embeddings")

# Chiediamo la chiave di Groq
groq_api_key = st.sidebar.text_input("Inserisci Groq API Key (gsk_...)", type="password")
if not groq_api_key:
    st.warning("Inserisci la chiave API di Groq per continuare. La trovi su console.groq.com")
    st.stop()

# --- MODULO 1: AGENTE ESTRATTORE (Zero Data-Entry) ---
@st.cache_resource # Per non ricaricare il modello di embedding ogni volta
def get_embeddings():
    return HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def process_document(uploaded_file, location):
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    loader = PyPDFLoader("temp.pdf")
    documents = loader.load()
    
    for doc in documents:
        doc.metadata["location"] = location
    
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    texts = text_splitter.split_documents(documents)
    
    vectorstore = Chroma.from_documents(
        documents=texts, 
        embedding=get_embeddings(),
        persist_directory="./chroma_db"
    )
    return "Competenze salvate nel database aziendale!"

# --- UI ---
st.header("📤 Caricamento Documenti")
col1, col2 = st.columns(2)
with col1:
    location = st.selectbox("Sede di provenienza", ["Milano", "Singapore", "Londra", "New York"])
    uploaded_file = st.file_uploader("Carica un PDF (CV o Report)", type="pdf")

if uploaded_file and st.button("Mappa Competenze"):
    with st.spinner("L'AI sta leggendo il documento..."):
        msg = process_document(uploaded_file, location)
        st.success(msg)

st.divider()
st.header("🔍 Ricerca Talenti Globali")
query = st.text_input("Cosa stai cercando? (es: Esperti di chimica a Singapore)")

if query:
    vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=get_embeddings())
    
    # Usiamo Llama 3 su Groq (velocissimo!)
    llm = ChatGroq(
        groq_api_key=groq_api_key, 
        model_name="llama-3.1-8b-instant",
        temperature=0.1
    )
    
    docs = vectorstore.similarity_search(query, k=3)
    
    if docs:
        context = "\n\n".join([f"Sede: {d.metadata['location']}\nContenuto: {d.page_content}" for d in docs])
        prompt = f"""Sei un assistente HR aziendale. 
        Rispondi alla domanda usando SOLO i documenti forniti.
        
        DOMANDA: {query}
        DOCUMENTI ESTRATTI:
        {context}
        """
        
        response = llm.invoke(prompt)
        st.subheader("Risposta dall'AI:")
        st.write(response.content)
        
        with st.expander("Vedi dettagli fonti"):
            for doc in docs:
                st.write(f"📍 **{doc.metadata['location']}**: {doc.page_content[:200]}...")
    else:
        st.info("Nessun dato trovato nel database.")