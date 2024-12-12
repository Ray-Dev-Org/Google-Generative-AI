from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

genai.configure(api_key="AIzaSyB-viAp1X-7pJv0vzbCLMJQ0jB-hYZyrxA")

@app.route('/generate-content', methods=['POST'])
def generate_content():
    data = request.get_json()
    user_message = data.get("message")

    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        system_instruction="The chatbot should only answer about information assurance and security...",
    )

    chat_session = model.start_chat(history=[])

    response = chat_session.send_message(user_message)

    return jsonify({"response": response.text})

if __name__ == "__main__":
    app.run(debug=True)
