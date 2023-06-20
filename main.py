import os
import openai
import tiktoken
from dotenv import load_dotenv, find_dotenv
from openai.error import APIError, RateLimitError

from examples.example1 import example1
from examples.example2 import example2
from examples.example3 import example3
from examples.example4 import example4

_ = load_dotenv(find_dotenv())  # read local .env file

openai.api_key = os.environ["OPENAI_API_KEY"]

try:
    example1(openai)
    example2(openai)
    example3(openai)
    example4(openai)
except RateLimitError as e:
    msg = "Rate limit exceeded. Please try again later."
except APIError as e:
    msg = ("An error occurred while accessing the OpenAI API:", str(e))
print(msg)
