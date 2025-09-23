from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def home():
    return f"Welcome to the Home Page! Navigate to /about or /user/<username>."

@app.route('/about')
def about():
    return "This is the about page. Our application is built using Flask."

@app.route('/user/<username>')
def show_user(username):
    return f"This is the profile page of {username}."

if __name__ == "__main__":
    app.run(debug=True)