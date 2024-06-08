import openai

def generate_text(prompt, model_engine):
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
    # Get the generated text
    generated_text = completions.choices[0].text
    # Save the text in a file
    with open("generated_text.txt", "w") as file:
        file.write(generated_text.strip())
    print("The Text Has Been Generated Successfully!")
    return generated_text