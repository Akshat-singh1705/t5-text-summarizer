#fastapi
from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import T5ForConditionalGeneration ,T5Tokenizer
import torch
import re
from fastapi.templating import Jinja2Templates  #UI part
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles


# initalize our fastapi api 
app = FastAPI(title="text summarizer APP",description="Text Summarization using T5", version ="1.0")


#model and tokenizer
model = T5ForConditionalGeneration.from_pretrained("./saved_summary_model")
tokenizer = T5Tokenizer.from_pretrained("./saved_summary_model")

# define our device
if torch.backends.mps.is_available():
    device = torch.device("mps")
elif torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

model.to(device)

# templating 
templates = Jinja2Templates(directory=".")

#Input schema for dialogue ===> string
class DialogueInput(BaseModel):
    dialogue:str
    
#clean data function
def clean_data(text):
    text= re.sub(r"\r\n"," ",text) #replacing next line space to empty space
    text = re.sub(r"\s+"," ",text) #spaces
    text = re.sub(r"<.*?>"," ",text) #html tags <bvofisbbv>
    text= text.strip().lower()

    return text

#summarization function
def summarize_dialogue(dialogue):
    dialogue= clean_data(dialogue) # clean

    #tokenize
    inputs = tokenizer(
        dialogue,
        padding = "max_length",
        max_length= 512,
        truncation=True,
        return_tensors="pt"
    ).to(device)
    
    #generating the summamry => token ids
    model.to(device)
    targets = model.generate(
        input_ids=inputs["input_ids"],
        attention_mask = inputs["attention_mask"],
        max_length=150,
        num_beams=4,  # best of 4 outputs 
        early_stopping=True
    ) 
    
    #token ids convert to summary ==> decoding
    summary = tokenizer.decode(targets[0], skip_special_tokens=True) #EOS , SEP

    return summary


# API Endpoints
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.post("/summarize/")
async def summarize(dialogue_input: DialogueInput):
    summary = summarize_dialogue(dialogue_input.dialogue)
    return {"summary":summary}