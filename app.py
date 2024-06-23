#%%
# Import necessary libraries
import os
import textwrap
import warnings
import chromadb
import pathlib
import google.generativeai as genai
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
from IPython.display import display, Markdown
import streamlit as st
from dotenv import load_dotenv
# %%
# Suppress warnings
warnings.filterwarnings('ignore', category=FutureWarning)
warnings.filterwarnings('ignore', category=UserWarning, module='torch.utils._pytree')

load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel(
    'gemini-1.5-flash',
    system_instruction=[
        """Bạn là một nhân viên giới thiệu công ty Sun. Hãy trả lời câu hỏi sau dựa trên ngữ cảnh, 
        nếu ngữ cảnh không cung cấp câu trả lời hoặc không chắc chắn hãy trả lời 
        'Tôi không biết thông tin này, tuy nhiên đoạn thông tin dưới phần tham khảo có thể có câu trả lời cho bạn!' 
        đừng cố tạo ra câu trả lời không có trong ngữ cảnh.\nNgữ cảnh: {context} \nCâu hỏi: {question}\nTrả lời:"""
    ]
)

#%%


# Configure ChromaDB client and collection
embedding_fn = SentenceTransformerEmbeddingFunction(model_name='sentence-transformers/paraphrase-multilingual-mpnet-base-v2')
chroma_client = chromadb.PersistentClient(path="db")
chroma_collection = chroma_client.get_or_create_collection("sun", embedding_function=embedding_fn)

# Function to format text as Markdown
def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Function to perform Retrieval-Augmented Generation (RAG)
def rag(query: str, n_results=5):
    res = chroma_collection.query(query_texts=[query], n_results=n_results)
    docs = res["documents"][0]
    joined_information = ';'.join([f'{doc}' for doc in docs])
    context = joined_information
    question = query
    input = f"Dựa vào một số ngữ cảnh được cho dưới đây, trả lời câu hỏi.\n\n{context}\n\nQuestion: {question}"
    response = model.generate_content(input)
    return response.text, docs

#%%
# Streamlit UI setup
st.header("Hỏi đáp về Sun*")

# Text input field
user_query = st.text_input(label="", help="Ask here to know about Sun Asterisk", placeholder="What do you want to know about Sun Asterisk?")
rag_response = ''
raw_docs = ['', '', '', '', '']

if user_query:
    rag_response, raw_docs = rag(user_query)

rag_response = '' if len(user_query) == 0 else rag_response
raw_docs = ['', '', '', '', ''] if len(user_query) == 0 else raw_docs
# Display raw information and RAG response
st.header("Raw Information")
st.text(f"Raw Response 0: {raw_docs[0]}")
st.text(f"Raw Response 1: {raw_docs[1]}")
st.text(f"Raw Response 2: {raw_docs[2]}")
st.text(f"Raw Response 3: {raw_docs[3]}")
st.text(f"Raw Response 4: {raw_docs[4]}")

st.header("RAG Response")
st.write(rag_response)