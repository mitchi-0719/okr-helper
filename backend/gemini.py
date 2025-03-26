from google import genai
import env


GEMINI_API_KEY = env.load_env("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)
model = "gemini-2.0-flash"


async def objectives(contents: list[str]) -> str:
    response = client.models.generate_content(model=model, contents=contents)
    return response.text


async def key_results(contents: list[str]) -> str:
    response = client.models.generate_content(model=model, contents=contents)
    return response.text
