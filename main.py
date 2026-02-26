from flask import Flask, request, render_template
from flask import session, redirect

from repository.eventRepository import EventRepository
from service.eventService import EventService
from service.userService import UserService
from service.eventService import EventService
from repository.userRepository import UserRepository
from service.validatorService import ValidatorService

app = Flask(__name__)
app.secret_key = b'adasdadsgitosjtosjtehprthspi'

userService = UserService()
userRepository = UserRepository()
eventService = EventService()
eventRepository = EventRepository()
validatorService = ValidatorService()

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        user = userService.getUser()
        return render_template('index.html', user = user, userService=userService)

    return redirect('/')


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
        password
    )

    return render_template('registration/process-registration.html')

@app.route('/events', methods=['GET', 'POST'])
def events():
    user_role = userService.getRoleOfUser()
    if user_role == userService.ORGANISATIONSTEAM:
        events = eventRepository.getAll()

        if request.method == 'POST':
            date = request.form.get('date')
            eventService.registerEvent(date)

        return render_template('events/events.html', events = events, request = request.method)

    return redirect('/')

@app.route('/events/delete/<int:uid>', methods=['GET'])
def delete(uid: int):
    user_role = userService.getRoleOfUser()
    if user_role == userService.ORGANISATIONSTEAM:
        if uid and eventRepository.getById(uid):
            eventRepository.deleteById(uid)
            return redirect('/events')

    return redirect('/')

@app.route('/tagderausbildung/register', methods=['GET', 'POST'])
def tagderausbildungRegister():
    if request.method == 'GET':
        events = eventService.getCurrentEvents()
        return render_template('tagderausbildung/register.html', events=events)
    
    errors = {}
    validatorService.validateRegisterForEventForm(request.form, errors)
    if errors:
        events = eventService.getCurrentEvents()
        return render_template('tagderausbildung/register.html', events=events, errors=errors)

    eventService.registerForEvent(request.form)


if __name__ == '__main__':
    app.run(port=4000, debug=True)
