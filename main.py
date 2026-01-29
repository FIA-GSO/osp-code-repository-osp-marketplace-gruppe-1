from flask import Flask, request, render_template, send_file
from flask import session, redirect, url_for
from repositories.userRepository import UserRepository
from utiltiy.hashUtility import HashUtility

app = Flask(__name__)
app.secret_key = b'adasdadsgitosjtosjtehprthspi'


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login/login.html')
    else:
        email = request.form.get('email')
        password = request.form.get('password')
        # todo: add processing of login
        return redirect('/')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('registration/registration.html')

    user_repository = UserRepository()
    hash_utility = HashUtility()

    company = request.form.get('company')
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    email = request.form['email']
    password = hash_utility.hash(request.form['password'])

    user_repository.insert(
        [
            {
                'company': company,
                'first_name': firstname,
                'last_name': lastname,
                'email': email,
                'password_hash': password,
                'role': 1,
                'donation': 0
            }
        ]
    )

    return render_template('registration/process-registration.html', firstname = firstname)

if __name__ == '__main__':
    app.run(port=4000, debug=True)
