import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import tempfile


def process_pdf(pdf_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(pdf_file.getvalue())
        tmp_path = tmp_file.name

    try:
        loader = PyPDFLoader(tmp_path)
        docs = loader.load()
        if not docs:
            return None
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = text_splitter.split_documents(docs)
        embeddings = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2", model_kwargs={"device": "cpu"}
        )
        vector_store = FAISS.from_documents(chunks, embeddings)
        return vector_store
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)


def retrieve_context(vector_store, query="main topics and key concepts", k=5):
    docs = vector_store.similarity_search(query, k=k)
    context = "\n\n".join([doc.page_content for doc in docs])
    return context
