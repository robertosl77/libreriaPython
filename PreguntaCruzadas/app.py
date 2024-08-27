from flask import Flask, request, render_template, jsonify
import pandas as pd
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        data = process_excel(file_path)
        return jsonify(data)
    return jsonify({'error': 'File upload failed'})

def process_excel(file_path):
    df = pd.read_excel(file_path)
    questions = []
    answers = []
    current_question = None
    
    for index, row in df.iterrows():
        if not row[0].startswith('>'):
            current_question = {'text': row[0], 'id': f'q{len(questions)}', 'answers': [], 'status': 'unseen'}
            questions.append(current_question)
        else:
            if current_question:
                answer = {'text': row[0][1:].strip(), 'id': f'a{len(answers)}', 'questionId': current_question['id']}
                current_question['answers'].append(answer)
                answers.append(answer)
    
    return {'questions': questions, 'answers': answers}

if __name__ == '__main__':
    app.run(debug=True)
