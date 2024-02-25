from flask import Flask, render_template, request,url_for
import markdown2 
import os
import google.generativeai as genai


app = Flask(__name__)

api_key = os.getenv('GOOGLE_API')
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')


# List to store user messages and processed messages as tuples
message_history = []

@app.route('/')
def index():
    return render_template('index.html', message_history=message_history)

@app.route('/process_user_input', methods=['POST'])
def process_user_input():
    if request.method == 'POST':
        user_message = request.form['user_message']
        
        # Process the user message (replace this with your processing logic)
        processed_message = model.generate_content(user_message)

        processed_message = markdown2.markdown(processed_message.text)
        # Store both user message and processed message as a tuple
        message_history.append((user_message, processed_message))

        return render_template('index.html', message_history=message_history)

if __name__ == '__main__':
    app.run(debug=True)
