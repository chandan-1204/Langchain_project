from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()


model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
prompt="My name is chandan, what is capital of india?"

result=model.invoke(prompt)
print(result.content)