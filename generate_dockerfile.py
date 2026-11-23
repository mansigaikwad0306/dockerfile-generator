import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2:1b"

def generate_dockerfile(language):
    prompt = (
        f"Write an optimized Dockerfile for a {language} application. "
        "Use a small official base image, install dependencies before copying the code "
        "for layer caching, run as a non-root user, and add short comments explaining "
        "each step. Output only the Dockerfile content."
    )
    response = requests.post(
        OLLAMA_URL,
        json={"model": MODEL, "prompt": prompt, "stream": False},
        timeout=300,
    )
    response.raise_for_status()
    return response.json()["response"]

if __name__ == "__main__":
    language = input("Enter programming language: ").strip()
    dockerfile = generate_dockerfile(language)
    print(dockerfile)

    with open("Dockerfile.generated", "w", encoding="utf-8") as f:
        f.write(dockerfile)
    print("Saved to Dockerfile.generated")