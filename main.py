from flask import Flask, request, render_template, url_for, jsonify
from flask import session, redirect
import jinja_partials

from repository.eventRepository import EventRepository
from repository.statusRepository import StatusRepository
from service.eventService import EventService
from service.userService import UserService
from service.eventService import EventService
from service.boothService import BoothService
from repository.boothRepository import BoothRepository
from service.lectureService import LectureService
from repository.lectureRepository import LectureRepository
from repository.userRepository import UserRepository
from service.validatorService import ValidatorService
from service.notificationService import NotificationService

app = Flask(__name__)
jinja_partials.register_extensions(app)
app.secret_key = b'adasdadsgitosjtosjtehprthspi'

userService = UserService()
userRepository = UserRepository()
eventService = EventService()
eventRepository = EventRepository()
boothService = BoothService()
boothRepository = BoothRepository()
lectureService = LectureService()
lectureRepository = LectureRepository()
validatorService = ValidatorService()
notificationService = NotificationService()
statusRepository = StatusRepository()

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        user = userService.getUser()
        if not user:
            return render_template('index.html')

        return redirect((url_for('dashboard')))

    email = request.form.get('email')
    password = request.form.get('password')

    if userService.loginUser(email, password):
        return redirect((url_for('dashboard')))

    return render_template('index.html', error = 1)

@app.route('/change-password', methods=['GET'])
def change_password():
    return render_template('login/change-password.html')

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
        if request.method == 'POST':
            name = request.form.get('name')
            date = request.form.get('date')
            slots = int(request.form.get('slots'))
            eventService.registerEvent(name, date, slots)

        events = eventService.getAll()

        return render_template('events/events.html', events = events, request = request.method)

    return redirect((url_for('index')))

@app.route('/events/delete/<int:uid>', methods=['GET'])
def delete_event(uid: int):
    user_role = userService.getRoleOfUser()
    if user_role == userService.ORGANISATIONSTEAM:
        if uid and eventService.getById(uid):
            eventService.deleteById(uid)
            return redirect((url_for('events')))

    return redirect((url_for('index')))

@app.route('/vocationalfair/register', methods=['GET', 'POST'])
def vocationalfairRegister():
    if request.method == 'GET':
        events = eventService.getCurrentEvents()
        return render_template('vocationalFair/register.html', events=events)
    
    errors = {}
    validatorService.validateRegisterForEventForm(request.form, errors)
    if errors:
        events = eventService.getCurrentEvents()
        return render_template('vocationalFair/register.html', events=events, errors=errors)

    eventService.registerForEvent(request.form)
    return redirect((url_for('dashboard')))

@app.route('/events/edit/<int:uid>', methods=['GET', 'POST'])
def edit_event(uid: int):
    user_role = userService.getRoleOfUser()
    if user_role == userService.ORGANISATIONSTEAM:
        if uid and eventRepository.getById(uid):
            if request.method == 'POST':
                uid = int(request.form.get('uid'))
                name = request.form.get('name')
                date = request.form.get('date')
                slots = int(request.form.get('slots'))
                eventService.updateEvent(uid, name, date, slots)
                return redirect((url_for('events')))

            event = eventRepository.getById(uid)[0]
            return render_template('events/edit-event.html', event = event)

@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    if request.method == 'GET':
        user = userService.getUser()
        if userService.getRoleOfUser() == userService.ORGANISATIONSTEAM:
            return render_template('dashboards/organisationsteam/dashboard.html')
        elif userService.getRoleOfUser() == userService.LEHRER:
            return render_template('dashboards/lehrer/dashboard.html')
        elif userService.getRoleOfUser() == userService.AUSBILDUNGSBETRIEB:
            return render_template('dashboards/ausbildungsbetrieb/dashboard.html', userUid = userService.getUserUid())
    return redirect((url_for('index')))

@app.route("/donations", methods=['GET'])
def donations():
    donating_users = userService.getDonatingUser()

    return render_template('dashboards/organisationsteam/donationList.html', donating_users = donating_users)

@app.route("/booths", methods=['GET'])
def booths():
    if request.method == 'GET':
        user = userService.getAllUser()
        user_list = {u['uid']: u for u in user}
        status = statusRepository.getAll()
        status_list = {s['uid']: s for s in status}

        if userService.getRoleOfUser() == userService.ORGANISATIONSTEAM:
            events = eventService.getCurrentEvents()
            eventBooths = {}
            for event in events:
                uid = event.get('uid')
                eventBooths[uid] = boothService.getBoothRegestrationsForEvent(uid)
            return render_template('dashboards/organisationsteam/boothList.html', user = user_list, events = events, eventBooths = eventBooths, status = status_list)
    return redirect((url_for('index')))

@app.route("/api/booths", methods=['POST'])
def boothsApi():
    data = request.get_json(silent=True)
    if not data or userService.getRoleOfUser() != userService.ORGANISATIONSTEAM:
        return jsonify(), 400
    elif data['action'] == 'accept':
        boothService.acceptBoothRegistration(int(data['uid']))
    elif data['action'] == 'reject':
        boothService.rejectBoothRegistration(int(data['uid']))
    return jsonify(boothService.getBoothById(int(data['uid']))), 200

@app.route("/lectures", methods=['GET'])
def lectures():
    if request.method == 'GET':
        user = userService.getAllUser()
        user_list = {u['uid']: u for u in user}
        status = statusRepository.getAll()
        status_list = {s['uid']: s for s in status}

        if userService.getRoleOfUser() == userService.ORGANISATIONSTEAM:
            eventLectures = {}
            events = eventService.getCurrentEvents()
            for event in events:
                uid = event.get('uid')
                eventLectures[uid] = lectureService.getTechnicalLectureRegestrationsForEvent(uid)

            return render_template('dashboards/organisationsteam/lectureList.html', user = user_list, events = events, eventLectures = eventLectures, status = status_list)
    return redirect((url_for('index')))

@app.route("/api/lectures", methods=['POST'])
def lecturesApi():
    data = request.get_json(silent=True)
    if not data or userService.getRoleOfUser() != userService.ORGANISATIONSTEAM:
        return jsonify({'data': data}), 400
    elif data['action'] == 'accept':
        lectureService.acceptLectureRegistration(int(data['uid']))
    elif data['action'] == 'reject':
        lectureService.rejectLectureRegistration(int(data['uid']))
    return jsonify(lectureService.getLectureById(int(data['uid']))), 200

@app.route("/vocationalfair/registrations/<int:userUid>", methods=['GET'])
def vocationalfairRegistrations(userUid: int):
    if request.method == 'GET':
        user = userService.getUser()
        if userService.getRoleOfUser() == userService.AUSBILDUNGSBETRIEB and userService.getUserUid() == userUid:

            status = statusRepository.getAll()
            status_list = {s['uid']: s for s in status}

            booths = boothService.getBoothRegistrationsForUser(userService.getUserUid())
            boothsWithDate = []
            for booth in booths:
                booth['date'] = eventService.getById(booth['event'])[0]['date']
                boothsWithDate.append(booth)
            
            lectures = lectureService.getlectureRegistrationsForUser(userService.getUserUid())
            lecturesWithDate = []
            for lecture in lectures:
                lecture['date'] = eventService.getById(lecture['event'])[0]['date']
                lecturesWithDate.append(lecture)

            return render_template('dashboards/ausbildungsbetrieb/registrations.html', user = user, boothsWithDate = boothsWithDate, lecturesWithDate = lecturesWithDate, status_list = status_list)
    return redirect((url_for('index')))

@app.route("/booth/edit/<int:boothUid>", methods=['GET', 'POST'])
def editBooth(boothUid: int):
    if userService.getRoleOfUser() == userService.AUSBILDUNGSBETRIEB and userService.getUserUid() == boothRepository.getById(boothUid)[0]['user']:
        if request.method == 'GET':
            booth = boothRepository.getById(boothUid)[0]
            return render_template('dashboards/ausbildungsbetrieb/editBooth.html', booth = booth)

        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        telephone = request.form.get('telephone')
        note = request.form.get('note')
        table_count = request.form.get('table_count')
        chair_count = request.form.get('chair_count')
        boothService.updateBooth(boothUid, first_name, last_name, email, telephone, note, table_count, chair_count, boothService.STATUS_IN_PROGRESS)

        return redirect((url_for('vocationalfairRegistrations', userUid = userService.getUserUid())))
    return redirect((url_for('index')))

@app.route("/lecture/edit/<int:lectureUid>", methods=['GET', 'POST'])
def editLecture(lectureUid: int):
    if userService.getRoleOfUser() == userService.AUSBILDUNGSBETRIEB and userService.getUserUid() == lectureRepository.getById(lectureUid)[0]['user']:
        if request.method == 'GET':
            lecture = lectureRepository.getById(lectureUid)[0]
            return render_template('dashboards/ausbildungsbetrieb/editLecture.html', lecture = lecture)

        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        telephone = request.form.get('telephone')
        note = request.form.get('note')
        topic = request.form.get('topic')
        duration = request.form.get('duration')
        lectureService.updateLecture(lectureUid, first_name, last_name, email, telephone, note, topic, duration, LectureService.STATUS_IN_PROGRESS)

        return redirect((url_for('vocationalfairRegistrations', userUid = userService.getUserUid())))
    return redirect((url_for('index')))

@app.route("/lecture/delete/<int:lectureUid>", methods=['GET'])
def deleteLecture(lectureUid: int):
    if userService.getRoleOfUser() == userService.AUSBILDUNGSBETRIEB and userService.getUserUid() == lectureRepository.getById(lectureUid)[0]['user']:
        if request.method == 'GET':
            lectureService.deleteLecture(lectureUid)
            return redirect((url_for('vocationalfairRegistrations', userUid = userService.getUserUid())))
    return redirect((url_for('index')))

@app.route("/booth/delete/<int:boothUid>", methods=['GET'])
def deleteBooth(boothUid: int):
    if userService.getRoleOfUser() == userService.AUSBILDUNGSBETRIEB and userService.getUserUid() == boothRepository.getById(boothUid)[0]['user']:
        if request.method == 'GET':
            boothService.deleteBooth(boothUid)
            return redirect((url_for('vocationalfairRegistrations', userUid = userService.getUserUid())))
    return redirect((url_for('index')))

@app.route("/notifications", methods=['GET'])
def notifications():
    if userService.getRoleOfUser() == userService.AUSBILDUNGSBETRIEB:
        if request.method == 'GET':
            notifications = notificationService.getNotificationByUser(userService.getUserUid())
            return render_template('dashboards/ausbildungsbetrieb/notification.html', notifications = notifications)
    return redirect((url_for('index')))

if __name__ == '__main__':
    app.run(port=4000, debug=True)
