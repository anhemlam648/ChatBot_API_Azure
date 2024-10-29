import requests
import os 
os.environ['AZURE_OPENAI_ENDPOINT'] = 'YourEnpointService'
os.environ['AZURE_OPENAI_API_KEY'] = 'YourApiKeyService' 
enpoint = os.getenv("AZURE_OPENAI_ENDPOINT") + 'openai/deployments/gpt-4/completions?api-version=2024-04-09'
api_key = os.getenv("AZURE_OPENAI_API_KEY")
headers = {
    'Authorization': f'Nghia {os.getenv('AZURE_OPENAI_API_KEY')}',
    'content-type': 'application/json'                         
}
model = 'gpt-4',
messager = [
    {"role": "system", "content": "You are a helpful assistant."},

    {"role": "user", "content": "Knock knock."},
],
response = requests.post(enpoint,headers=headers,json=messager)
print(response.status_code,response.json())
