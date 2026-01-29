from flask import Flask, request, render_template, send_file
from flask import session, redirect, url_for

app = Flask(__name__)
app.secret_key = b'adasdadsgitosjtosjtehprthspi'


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('login/login.html')
    else:
        email = request.form.get('email')
        password = request.form.get('password')
        # todo: add processing of login
        return redirect('/')

if __name__ == '__main__':
    app.run(port=4000, debug=True)
