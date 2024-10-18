from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        if username and email and password:
            # Here, you would typically save the user to a database
            flash('Registration successful!', 'success')
            return redirect(url_for('register'))
        else:
            flash('Please fill in all fields!', 'danger')

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)

