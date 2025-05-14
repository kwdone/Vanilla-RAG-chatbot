from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from vector_store.documents import load_documents

def init_vector_store(df=None):
    texts = load_documents(df)
    print(f"[DEBUG]: Loaded {len(texts)} nutrition-related chunks.")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-mpnet-base-v2",
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True}
    )
    return FAISS.from_documents(texts, embeddings)
