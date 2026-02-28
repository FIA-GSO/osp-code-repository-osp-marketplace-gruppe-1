from flask import Flask, request, render_template, url_for
from flask import session, redirect
import jinja_partials

from repository.eventRepository import EventRepository
from service.eventService import EventService
from service.userService import UserService
from service.eventService import EventService
from service.boothService import BoothService
from service.lectureService import LectureService
from repository.userRepository import UserRepository
from service.validatorService import ValidatorService

app = Flask(__name__)
jinja_partials.register_extensions(app)
app.secret_key = b'adasdadsgitosjtosjtehprthspi'

userService = UserService()
userRepository = UserRepository()
eventService = EventService()
eventRepository = EventRepository()
boothService = BoothService()
lectureService = LectureService()
validatorService = ValidatorService()

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        user = userService.getUser()
        if not user:
            return render_template('index.html')

        return redirect((url_for('dashboard')))

    email = request.form.get('email')
    password = request.form.get('password')

    userService.loginUser(email, password)

    return redirect((url_for('dashboard')))

@app.route("/logout", methods=['GET'])
def logout():
    userService.logoutUser()
    return redirect((url_for('index')))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('registration/registration.html')

    company = request.form['company']
    email = request.form['email']
    password = request.form['password']

    if userService.registerUser(company, email, password):
        return render_template('registration/process-registration.html', error = 0)

    return render_template('registration/process-registration.html', error = 1)

@app.route('/events', methods=['GET', 'POST'])
def events():
    user_role = userService.getRoleOfUser()
    if user_role == userService.ORGANISATIONSTEAM:
        events = eventRepository.getAll()

        if request.method == 'POST':
            date = request.form.get('date')
            eventService.registerEvent(date)

        return render_template('events/events.html', events = events, request = request.method)

    return redirect((url_for('index')))

@app.route('/events/delete/<int:uid>', methods=['GET'])
def delete_eventEvent(uid: int):
    user_role = userService.getRoleOfUser()
    if user_role == userService.ORGANISATIONSTEAM:
        if uid and eventRepository.getById(uid):
            eventRepository.deleteById(uid)
            return redirect((url_for('events')))

    return redirect((url_for('index')))

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
    return redirect((url_for('index')))

@app.route('/events/edit/<int:uid>', methods=['GET', 'POST'])
def edit_event(uid: int):
    user_role = userService.getRoleOfUser()
    if user_role == userService.ORGANISATIONSTEAM:
        if uid and eventRepository.getById(uid):
            if request.method == 'POST':
                uid = request.form.get('uid')
                date = request.form.get('date')
                eventService.updateEvent(uid, date)
                return redirect((url_for('events')))

            event = eventRepository.getById(uid)
            return render_template('events/edit-event.html', event = event)

@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    if request.method == 'GET':
        user = userService.getUser()
        if userService.getRoleOfUser() == userService.ORGANISATIONSTEAM:
            return render_template('dashboards/organisationsteam/dashboard.html', user = user)
    return redirect((url_for('index')))

@app.route("/booths", methods=['GET'])
def booths():
    if request.method == 'GET':
        user = userService.getUser()
        if userService.getRoleOfUser() == userService.ORGANISATIONSTEAM:
            events = eventService.getCurrentEvents()
            for event in events:
                uid = event.get('uid')
                eventBooths = boothService.getBoothRegestrationsForEvent(uid)
            return render_template('dashboards/organisationsteam/boothList.html', user = user, events = events, eventBooths = eventBooths)
    return redirect((url_for('index')))

@app.route("/booths/reject/<int:uid>", methods=['POST'])
def boothsReject(uid: int):
    if userService.getRoleOfUser() == userService.ORGANISATIONSTEAM:
        boothService.rejectBoothRegistration(uid)
        return redirect((url_for('booths')))
    return redirect((url_for('index')))

@app.route("/booths/accept/<int:uid>", methods=['POST'])
def boothsAccept(uid: int):
    if userService.getRoleOfUser() == userService.ORGANISATIONSTEAM:
        boothService.acceptBoothRegistration(uid)
        return redirect((url_for('booths')))
    return redirect((url_for('index')))

@app.route("/lectures", methods=['GET'])
def lectures():
    if request.method == 'GET':
        user = userService.getUser()
        if userService.getRoleOfUser() == userService.ORGANISATIONSTEAM:
            eventLectures = {}
            events = eventService.getCurrentEvents()
            for event in events:
                uid = event.get('uid')
                eventLectures[uid] = lectureService.getTechnicalLectureRegestrationsForEvent(uid)
            return render_template('dashboards/organisationsteam/boothList.html', user = user, events = events, eventLectures = eventLectures)
    return redirect((url_for('index')))

@app.route("/lectures/reject/<int:uid>", methods=['POST'])
def lecturesReject(uid: int):
    if userService.getRoleOfUser() == userService.ORGANISATIONSTEAM:
        lectureService.rejectLectureRegistration(uid)
        return redirect((url_for('lectures')))
    return redirect((url_for('index')))

@app.route("/lectures/accept/<int:uid>", methods=['POST'])
def lecturesAccept(uid: int):
    if userService.getRoleOfUser() == userService.ORGANISATIONSTEAM:
        lectureService.acceptLectureRegistration(uid)
        return redirect((url_for('lectures')))
    return redirect((url_for('index')))

if __name__ == '__main__':
    app.run(port=4000, debug=True)
