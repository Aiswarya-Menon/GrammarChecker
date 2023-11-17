from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv

load_dotenv()
baseUrl = os.getenv('BASE_URL')
app = Flask(__name__)

# Set your ChatGPT API key here
openai.api_key = os.getenv('OPENAI_API_KEY')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/check_grammar', methods=['POST'])
def check_grammar():
    text_to_check = request.form['text_to_check']

    # Call ChatGPT API to modify the content and get error-free text
    corrected_text = modify_text(text_to_check)

    return {'corrected_text': corrected_text}


def modify_text(text):
    # Implement your logic to modify the text using ChatGPT
    # This is a placeholder and you should replace it with your actual implementation
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="modify the given text to generate a grammar and spelling errors free:" + text,
        max_tokens=150
    )
    corrected_text = response['choices'][0]['text'].strip()

    return corrected_text


if __name__ == '__main__':
    app.run(debug=True)
