# Code Explanation and Debugging Tool

This project is a simple web app built with Flask and OpenAI's GPT-4 API to analyze code based on user input.

## Prerequisites

- **Python 3.x**
- **Flask**: Install via `pip install flask`
- **OpenAI Python SDK**: Install via `pip install openai`
- **OpenAI API Key**: Get from [OpenAI](https://beta.openai.com/signup/)

## Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/shahinur-alam/Code-Explanation-and-Debugging-Tool.git
   cd Code-Explanation-and-Debugging-Tool
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Replace the OpenAI API key in the code:
   ```bash
   openai.api_key = 'your_openai_api_key_here'
   ```
4. Run the app:
   ```bash
   python app.py
   ```
Visit the app at http://127.0.0.1:5000/.

## Structure
- app.py: Main app logic with Flask routes and OpenAI integration.
- templates/index.html: Web form for code input and task selection.

## Usage
- Enter code and specify a task (e.g., "Review this code").
- Submit the form to get the analysis.
