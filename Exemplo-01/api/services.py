import os
from dotenv import load_dotenv, find_dotenv
import openai


load_dotenv(find_dotenv())


# Shared OpenAI client for the application
openai_client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
token = os.environ.get("API_TOKEN")
