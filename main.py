import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
  model="gemini-2.0-flash",
  contents = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
)

print(response.text)



def main():
    print("Hello from ai-agent!")


if __name__ == "__main__":
    main()
