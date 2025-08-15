from transformers import pipeline

def text_to_art(prompt: str, max_length: int = 60) -> str:
    generator = pipeline("text-generation", model="gpt2")
    return generator(prompt, max_length=max_length)[0]["generated_text"]

if __name__ == "__main__":
    print(text_to_art("Uma paisagem tranquila para reduzir a ansiedade"))
