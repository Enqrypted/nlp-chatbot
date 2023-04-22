from flask import Flask, request, jsonify
from chatbot import chat

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat_endpoint():
    data = request.get_json()
    input_text = data['input_text']
    output_text = chat(input_text)
    return jsonify({'response': output_text})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8085)
