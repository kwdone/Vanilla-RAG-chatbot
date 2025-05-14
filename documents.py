import os
import pandas as pd
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from config import NUTRITION_DATA_PATH

def load_documents(df=None):
    kaggle_docs = []
    if df is not None:
        for _, row in df.iterrows():
            text = (
                f"Food: {row['Food']}\n"
                f"Measure: {row['Measure']} ({row['Grams']}g)\n"
                f"Calories: {row['Calories']} kcal\n"
                f"Protein: {row['Protein']} g\n"
                f"Fat: {row['Fat']} g (Saturated: {row['Sat.Fat']} g)\n"
                f"Fiber: {row['Fiber']} g\n"
                f"Carbs: {row['Carbs']} g\n"
                f"Category: {row['Category']}"
            )
            kaggle_docs.append(Document(page_content=text, metadata={"source": "kaggle"}))

    loader = DirectoryLoader(NUTRITION_DATA_PATH, glob="*.txt", loader_cls=TextLoader)
    my_docs = loader.load()

    docs = my_docs + kaggle_docs
    for doc in docs:
        doc.metadata["topic"] = "nutrition"

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return splitter.split_documents(docs)
