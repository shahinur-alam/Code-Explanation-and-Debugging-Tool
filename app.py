import os
from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set up OpenAI API key
#openai.api_key = 'your_openai_api_key_here'
openai.api_key = 'Open API Key'


def analyze_code(code, task):
    prompt = f"{task}:\n\n{code}\n\nAnalysis:"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that analyzes code."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        code = request.form['code']
        task = request.form['task']
        analysis = analyze_code(code, task)
        return render_template('index.html', code=code, analysis=analysis, task=task)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)