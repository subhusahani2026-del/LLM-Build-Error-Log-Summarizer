
import requests

def summarize_log(log_text):

    prompt = f"""
    You are an expert software build log analyzer.

    Analyze this build log and provide:

    1. Build status
    2. Main errors
    3. Explanation of errors
    4. Possible solutions

    Build Log:
    {log_text}

    Explain everything in simple language.
    """

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.2",
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )

        response.raise_for_status()

        return response.json()["response"]

    except requests.RequestException as error:
        return f"LLM Connection Error: {error}"
