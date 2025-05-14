from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    images = [
        {'filename': 'mars1.png'},
        {'filename': 'mars2.png'},
        {'filename': 'mars3.png'},
        {'filename': 'mars4.png'}
    ]
    return render_template('index.html', images=images)

if __name__ == '__main__':
    app.run(debug=True)