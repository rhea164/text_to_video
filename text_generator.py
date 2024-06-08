import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variable
API_KEY = os.getenv('API_KEY')

# Set the API key for OpenAI
openai.api_key = API_KEY

# Set the model to use
model_engine = "gpt-3.5-turbo-instruct"

# Set the prompt to generate text for
text = input("What topic do you want to write about: ")
prompt = text

print("The AI BOT is trying now to generate a new text for you...")

# Generate text using the GPT-3.5-turbo-instruct model
completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

# Print the generated text
generated_text = completions.choices[0].text

# Save the text in a file
with open("generated_text.txt", "w") as file:
    file.write(generated_text.strip())

print("The Text Has Been Generated Successfully!")


# import openai
# from api_key import API_KEY

# openai.api_key = API_KEY

# # Set the model to use
# model_engine = "gpt-3.5-turbo-instruct"

# # Set the prompt to generate text for
# text = input("What topic do you want to write about: ")
# prompt = text

# print("The AI BOT is trying now to generate a new text for you...")
# # Generate text using the GPT-3.5-turbo-instruct model
# completions = openai.Completion.create(
#     engine=model_engine,
#     prompt=prompt,
#     max_tokens=1024,
#     n=1,
#     stop=None,
#     temperature=0.5,
# )

# # Print the generated text
# generated_text = completions.choices[0].text

# # Save the text in a file
# with open("generated_text.txt", "w") as file:
#     file.write(generated_text.strip())

# print("The Text Has Been Generated Successfully!")