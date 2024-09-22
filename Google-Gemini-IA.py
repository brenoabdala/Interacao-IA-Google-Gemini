import google.generativeai as genai


question = input('How can I help?')
question = str(question)
 
#API Google
GOOGLE_API_KEY = ""
genai.configure(api_key=GOOGLE_API_KEY)

#Modelo Usado
model = genai.GenerativeModel('gemini-pro')

#Define o Timeout
response = model.generate_content(question,
                                request_options={"timeout": 300})

#Resposta
resposta = response.text    
print(resposta)