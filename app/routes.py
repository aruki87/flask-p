from flask import render_template, flash, redirect, url_for
from app import app
from app import db
from app.forms import LoginForm, RegistrationForm, JoinIzlet
from flask_login import current_user, login_user, login_required
from app.models import User, Izlet, IzletUser
from flask_login import logout_user
from flask import request
from werkzeug.urls import url_parse
from datetime import datetime
from app.forms import EditProfileForm, StvoriIzletForm, EditIzlet



@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/user/<username>')
@login_required
def user(username):

    user = User.query.filter_by(username=username).first_or_404()
    izleti = Izlet.query.filter_by(creator = current_user)
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts, izleti=izleti)


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        #current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        current_user.picture = form.picture.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile',
                           form=form)

@app.route('/stvori_izlet', methods=['GET', 'POST'])
def stvori_izlet():
    #if not current_user.is_authenticated:
        #return redirect(url_for('login'))
    form = StvoriIzletForm()
    if form.validate_on_submit():
        izlet = Izlet(name=form.name.data, description=form.description.data, location=form.location.data, transport=form.transport.data, begin=form.begin.data, end=form.end.data,picture=form.picture.data, cost=form.cost.data, creator=current_user)
        db.session.add(izlet)
        db.session.commit()
        flash('Cestitamo, stvorili ste izlet')
        return redirect(url_for('index'))
    return render_template('stvori_izlet.html', title='Stvori izlet', form=form)



@app.route('/svi_izleti')
def svi_izleti():
    izlet = Izlet.query.all()
    return render_template('svi_izleti.html', izlet=izlet)


@app.route('/izlet/<name>', methods=['GET', 'POST'])
@login_required
def izlet(name):
    form = JoinIzlet()
    izlet = Izlet.query.filter_by(name=name).first_or_404()
    izletuser = IzletUser.query.filter_by(izlet_id=izlet.id)
    useri = []
    isAlready = False
    for x in izletuser:
        useri.append(User.query.filter_by(id=x.user_id).first()) 
    if form.validate_on_submit():
        isIzletUser = IzletUser.query.filter_by(user_id=current_user.id)
        for x in isIzletUser:
            if x.izlet_id is izlet.id:
                isAlready = True
        if not isAlready :
                izletUser= IzletUser(user_id=current_user.id, izlet_id= izlet.id)
                db.session.add(izletUser)
                db.session.commit()
                flash('Cestitamo, pridruzili ste se izletu')
                return redirect(url_for('svi_izleti'))
    return render_template('izlet.html', izlet=izlet, form=form, useri=useri )



@app.route('/svi_useri')
def svi_useri():
    useri = User.query.all()

    return render_template('svi_useri.html', useri=useri)


@app.route('/edit_izlet/<id>', methods=['GET', 'POST'])
def edit_izlet(id):
    form = EditIzlet()
    izlet = Izlet.query.filter_by(id=id).first_or_404()
    if form.validate_on_submit():
        izlet.name = form.name.data;
        izlet.description = form.description.data;
        izlet.location = form.location.data;
        izlet.transport = form.transport.data;
        izlet.end = form.end.data;
        izlet.picture = form.picture.data;
        izlet.cost = form.cost.data;
        izlet.lat = form.lat.data;
        izlet.lng = form.lng.data;
        db.session.commit()
        return redirect(url_for('svi_izleti'))
    return render_template('edit_izlet.html', title='Izmjeni izlet', form=form, izlet=izlet)