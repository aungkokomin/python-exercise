from flask import Flask, render_template, request, redirect
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Handle POST request for login
    if request.method == 'POST':
        # Sanitize the username input to prevent XSS
        username = request.form['username'].replace("<", "&lt;").replace(">", "&gt;")
        password = request.form['password']
        stored_hashed_password = generate_password_hash("securepassword")
        if check_password_hash(stored_hashed_password, password):
            return redirect(f"/home/{username}")
        else:
            return redirect('/login')

    # For GET request, render the login form
    return render_template('login.html')

@app.route('/home/<username>')
def home(username):
    return f"Welcome, {username}!"

if __name__ == '__main__':
    app.run(debug=True)