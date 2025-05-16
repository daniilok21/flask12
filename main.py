import random
from flask import Flask, render_template, request, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandex_luceum_secret_key'
app.config['UPLOAD_FOLDER'] = 'static/images'
app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'jpeg', 'png', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/', methods=['GET', 'POST'])
def index():
    images = []
    for filename in os.listdir(app.config['UPLOAD_FOLDER']):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            images.append({
                'filename': filename,
            })

    if request.method == 'POST':
        if 'file' not in request.files:
            print('Файл не выбран')
            return redirect(request.url)

        file = request.files['file']
        if file.filename == '':
            print('Файл не выбран')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print('Файл загружен')
            return redirect(url_for('index'))

    return render_template('index.html', images=images)


@app.route('/member')
def member():
    with open('templates/crew.json', 'r', encoding='utf-8') as f:
        crew_data = json.load(f)

    random_member = random.choice(crew_data['crew'])
    return render_template('member.html', member=random_member)


if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)