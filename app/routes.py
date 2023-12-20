from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, db, login_manager
from app.models import User, Miner, Buyer, Investor, Message
from app.forms import RegistrationForm, LoginForm

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Frontend Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        role = form.role.data

        hashed_password = generate_password_hash(password, method='sha256')

        new_user = User(username=username, email=email, password=hashed_password, role=role)
        db.session.add(new_user)
        db.session.commit()

        if role == 'miner':
            new_miner = Miner(user_id=new_user.id)
            db.session.add(new_miner)
        elif role == 'buyer':
            new_buyer = Buyer(user_id=new_user.id)
            db.session.add(new_buyer)
        elif role == 'investor':
            new_investor = Investor(user_id=new_user.id)
            db.session.add(new_investor)

        db.session.commit()

        flash('Registration successful! Please login.')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Login successful!')
            return redirect(url_for('dashboard'))

    return render_template('login.html', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout successful!')
    return redirect(url_for('index'))

# API Routes
@app.route('/api/listings', methods=['GET', 'POST'])
@login_required
def listings():
    if request.method == 'GET':
        # Logic to retrieve listings
        return render_template('listings.html', listings=get_listings())

    elif request.method == 'POST':
        # Logic to create new listing
        flash('Listing created successfully!')
        return redirect(url_for('listings'))

@app.route('/api/messages', methods=['GET', 'POST'])
@login_required
def messages():
    if request.method == 'GET':
        # Logic to retrieve messages
        return render_template('messages.html', messages=get_messages())

    elif request.method == 'POST':
        # Logic to send a new message
        flash('Message sent successfully!')
        return redirect(url_for('messages'))
