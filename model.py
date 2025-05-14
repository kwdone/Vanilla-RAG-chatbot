from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
from langchain_community.llms import HuggingFacePipeline

def load_local_llm(model_id="google/flan-t5-large"):
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_id)

    pipe = pipeline(
        "text2text-generation",
        model=model,
        tokenizer=tokenizer,
        max_length=1024,
        do_sample=False,
        temperature=0.3,
        min_length=50,
        top_p=0.7,
        top_k=10,
        repetition_penalty=2.5,
    )

    return HuggingFacePipeline(pipeline=pipe)
