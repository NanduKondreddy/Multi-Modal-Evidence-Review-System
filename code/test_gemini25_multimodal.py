from google import genai
from PIL import Image
import os

img = Image.new('RGB', (100, 100), color = 'red')

from dotenv import load_dotenv
load_dotenv()

# Read keys from environment
api_key = os.getenv("GOOGLE_API_KEY", "")
keys = [k.strip() for k in api_key.split(",") if k.strip()] or [api_key]

for i, key in enumerate(keys):
    print(f"Testing Key {i+1} ({key[-10:]}):")
    client = genai.Client(api_key=key)
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=["Identify this image color:", img],
        )
        print("  SUCCESS! Response:", response.text.strip())
    except Exception as e:
        print("  FAILED:", type(e), str(e)[:150])
    print("-" * 50)
