from fastapi import FastAPI
from pydantic import BaseModel
from googletrans import Translator
import uuid

app = FastAPI()
translator = Translator()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all domains (or replace with your domain)
    allow_credentials=True,
    allow_methods=["*"],  # allow POST, OPTIONS, GET, PUT, DELETE
    allow_headers=["*"],  # allow all headers
)

class TranslateData(BaseModel):
    text: str
    target_lang: str
    

@app.post("/translate")
def translate_text(data: TranslateData):
    translated = translator.translate(data.text, dest=data.target_lang)

    return {
        "original_text": data.text,
        "translated_text": translated.text,
        "language": data.target_lang,
        
        "translation_id": str(uuid.uuid4())  # unique ID
    }
