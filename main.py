from flask import Flask, render_template, request, redirect, url_for
import json
import os

frontend_template = os.path.join(os.path.dirname(__file__), './../frontend')
app = Flask(__name__, template_folder = frontend_template)


# Функция для чтения данных из JSON файла
def read_json_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

# Функция для записи данных в JSON файл
def write_json_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

@app.route('/')
def indexTemplate():
    return render_template('index.html')

@app.route('/create-user', methods = ["POST"])
def createUser():
    name = request.form['name']
    email = request.form['email']

    data = read_json_file('db.json')
    data.append({'name': name, 'email': email})

    write_json_file('db.json', data)

    return redirect(url_for('indexTemplate'))



if __name__ == '__main__':
    app.run(debug=True)