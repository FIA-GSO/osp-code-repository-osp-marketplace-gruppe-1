from flask import Flask, request, render_template
from flask import session, redirect
from service.userService import UserService
from repository.userRepository import UserRepository

app = Flask(__name__)
app.secret_key = b'adasdadsgitosjtosjtehprthspi'

userService = UserService()
userRepository = UserRepository()

@app.route("/", methods=['GET'])
def index():
    user = userService.getUser()

    return render_template('index.html', user = user)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login/login.html')
    else:
        email = request.form.get('email')
        password = request.form.get('password')

        if userService.loginUser(email, password):
            return redirect('/')
        return render_template('login/login.html')

@app.route("/logout", methods=['GET'])
def logout():
    userService.logoutUser()
    return redirect('/')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('registration/registration.html')

    company = request.form['company']
    email = request.form['email']
    password = request.form['password']

    userService.registerUser(
        email,
        company,
        1,
        0,
        password
    )

    return render_template('registration/process-registration.html')

if __name__ == '__main__':
    app.run(port=4000, debug=True)
