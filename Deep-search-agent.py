import os
from dotenv import load_dotenv
load_dotenv()
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")

print(f"Your API Key is: {LANGSMITH_API_KEY}")