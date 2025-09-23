from flask import Flask, render_template

app = Flask(__name__)
username = "JohnDoe"

@app.route('/')
def home():
    return render_template('index.html', username = username)

if __name__ == '__main__':
    app.run(debug=True)