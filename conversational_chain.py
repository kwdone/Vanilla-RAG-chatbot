from langchain.chains import ConversationalRetrievalChain
from llm.model import load_local_llm
from llm.prompt import build_prompt_template
from vector_store.vector_store import init_vector_store

def init_conversation_chain(df=None):
    vectorstore = init_vector_store(df)
    llm = load_local_llm()
    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5}),
        return_source_documents=True,
        combine_docs_chain_kwargs={"prompt": build_prompt_template()}
    )
