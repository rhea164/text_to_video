import streamlit as st
import openai
from dotenv import load_dotenv
import os
import text_generator
import video_generator

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variable
API_KEY = os.getenv('API_KEY')

# Set your OpenAI API key
openai.api_key = API_KEY

# Set the model to use
model_engine = "gpt-3.5-turbo-instruct"

def main():
    st.title("Text-to-Video Generator")

    prompt = st.text_input("Enter a topic to generate text and video")

    if st.button("Generate"):
        generated_text = text_generator.generate_text(prompt, model_engine)
        st.write("Generated Text:")
        st.write(generated_text)

        video_generator.generate_video(generated_text)

        # Display the final video
        video_file = open("final_story_video.mp4", "rb").read()
        st.video(video_file)

if __name__ == "__main__":
    main()