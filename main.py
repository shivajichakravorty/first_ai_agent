import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

response = client.models.generate_content(
  model="gemini-2.5-pro",
  contents = prompt
)

if response.usage_metadata is None:
    raise RuntimeError("Response is missing usage metadata")

usage_meta = response.usage_metadata
print(f"User prompt: {prompt}")
print(f"Prompt tokens: {usage_meta.prompt_token_count}")
print(f"Response tokens: {usage_meta.total_token_count}")
print(f"Response:\n{response.text}")



def main():
    print("Hello from ai-agent!")


if __name__ == "__main__":
    main()
