import torch
from fastapi import FastAPI

from transformers import GPT2Tokenizer, GPT2LMHeadModel

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.get("/chat")
def chat(prompt: str, temperature: float = 0.5, top_k: int = 10, top_p: float = 0.9, max_length: int = 100):
    input_ids = tokenizer.encode(prompt, return_tensors='pt')
    generated = model.generate(input_ids,
                               max_length=max_length,
                               temperature=temperature,
                               top_k=top_k,
                               top_p=top_p,
                               do_sample=True,)
    generated_text = tokenizer.decode(
        generated.tolist()[0], skip_special_tokens=True)
    return generated_text
