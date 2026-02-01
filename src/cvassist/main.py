import os
import requests
from dotenv import load_dotenv

load_dotenv()

def check_openrouter_connection():
    api_key = os.getenv("OPENROUTER_API_KEY")

    if not api_key:
        print("Error: OPENROUTER_API_KEY environment variable not set.")
        return False

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [{"role": "user", "content": "Hello, this is a test message."}]
    }

    print("Sending request to OpenRouter API...")
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        print("✅ Success! API is working correctly.")
        data = response.json()
        if "choices" in data and len(data["choices"]) > 0:
            message_content = data["choices"][0]["message"]["content"]
            print(f"Response from API: {message_content}")
        return True
    else:
        print(f"❌ Error: {response.status_code}")
        print(f"Response: {response.text}")
        return False

def main():
    print("Testing OpenRouter API connection...")
    success = check_openrouter_connection()

    if success:
        print("\n🎉 OpenRouter API test completed successfully!")
    else:
        print("\n💥 OpenRouter API test failed!")

if __name__ == "__main__":
    main()
