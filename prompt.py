from langchain.prompts import PromptTemplate

def build_prompt_template():
    return PromptTemplate(
        input_variables=["context", "question"],
        template="""You are a helpful assistant with access to nutritional facts. Use the information from the context to answer user questions.

If the answer is not directly in the context, but you can reasonably infer it, do so.

If the context contains numeric info, use it for comparison.
If it contains general advice, use it to explain your reasoning.

You should compare the mentioned attributes among the products to give an answer on questions like: "What is the most protein rich food?"
---
Context:
{context}

Question: {question}

Answer:
"""
    )
