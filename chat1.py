import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

modelo = "gemini-2.0-flash"
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    print(f"Chave de API carregada do .env (primeiros 5 caracteres): {api_key[:5]}...")
else:
    print("Erro: A chave GOOGLE_API_KEY não foi encontrada no arquivo .env.")
   
client = genai.Client()
chat_config = types.GenerateContentConfig(system_instruction='você é um assitente pessoal, responda sempre de forma suscinta')
chat = client.chats.create(model=modelo, config=chat_config)

prompt = input('Digite algo: ')

while prompt != 'sair':
  resposta = chat.send_message(prompt)
  print('Resposta: ', resposta.text)
  print('\n')
  prompt = input('Digite algo: ')

print('até mais')