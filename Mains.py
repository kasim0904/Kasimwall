import os
from google import genai

# 1. Habee Client-ka iyadoo la isticmaalayo API Key-gaaga
client = genai.Client(api_keI")

# 2. Wac moodeelka Gemini 2.5 Flash
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents='Sidee AI Agent-ku u shaqeeyaa?',
)

# 3. Soo saar jawaabta
print(response.text)
