import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def ask_local_api(question, model="gemini-1.5-flash"):
    url = "http://localhost:8000/gemini-chat-completion"
    
    data = {
        "model": model,
        "contents": [
            {
                "role": "user",
                "parts": [
                    {
                        "text": question
                    }
                ]
            }
        ],
        "generationConfig": {
            "temperature": 1,
            "topK": 40,
            "topP": 0.95,
            "maxOutputTokens": 8192,
            "responseMimeType": "text/plain"
        }
    }
    
    response = requests.post(url, json=data)
    
    if response.status_code == 200:
        try:
            return response.json()['candidates'][0]['content']['parts'][0]['text']
        except KeyError:
            return "Error parsing response"
    else:
        return f"Error: {response.status_code} - {response.text}"

def main():
    print("Local FastAPI Gemini Test (Type 'quit' to exit)")
    print("Available models: gemini-1.5-flash, gemini-pro, gemini-pro-vision")
    print("-" * 50)
    
    # Ask for model name once at the start
    model = input("\nEnter model name (press Enter for default 'gemini-1.5-flash'): ").strip()
    if not model:
        model = "gemini-1.5-flash"
    
    while True:
        question = input("\nEnter your question: ")
        if question.lower() == 'quit':
            break
            
        print("\nGemini's response:")
        print("-" * 20)
        response = ask_local_api(question, model)
        print(response)
        print("-" * 50)

if __name__ == "__main__":
    main()
