from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential
from flask import Flask, jsonify, request
from flask_cors import CORS
import os

os.environ['AZURE_OPENAI_API_KEY'] = 'YourApiKeyService'
os.environ['AZURE_OPENAI_ENDPOINT'] = 'YourEnpointService'
os.environ['AZURE_OPENAI_API_DEPLOYNAME'] = 'YourDeployName'
os.environ['AZURE_OPENAI_API_VERSION'] = 'For example 2024-04-09'

app = Flask(__name__)
CORS(app)
# Get Token
# token_provider = get_bearer_token_provider(
#     DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
# )

# api_version = "2024-07-01-preview"
# endpoint = "https://my-resource.openai.azure.com"

# client = AzureOpenAI(
#     api_version=api_version,
#     azure_endpoint=endpoint,
#     azure_ad_token_provider=token_provider,
# )

#API KEY
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
    api_version="2024-07-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

@app.route('/chatapi', methods=['POST'])
def chatAPP():
    data = request.get_json()
    prompt = data.get('prompt')

    if not prompt:
        return jsonify({"error": "Prompt is required."}), 400

    chat_messages = [
        {"role": "user", "content": prompt},
        {"role": "system", "content": "You are an experienced assistant of Elekta. You know the products of Monaco very well. You can answer any questions about Elekta and Monaco."}
    ]

    try:
        response = client.chat.completions.create(
            model=os.environ['AZURE_OPENAI_API_DEPLOYNAME'],
            messages=chat_messages
        )
        response_content = response.choices[0].message.content.strip()  
        # response_content = response['choices'][0]['message']['content'].strip() 
        return jsonify({"response": response_content}), 200
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)


