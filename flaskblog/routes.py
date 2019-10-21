import os
import secrets
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm
from flaskblog.models import User
from flask_login import login_user, current_user, logout_user, login_required
from datetime import date
from flaskblog.graph import graph1,graph2,graph3,graph4,graph5,graph6,graph7,graph8,graph9,graph10,graph11,recommend





today=date.today()



posts = [

    {
        'author': 'Chahak Agrawal',
        'title': ' Amount of Orders Distribution graph',
        'content': 'image' ,
        'date_posted': today.strftime("%d/%m/%Y"),
        
    },
    {
        'author': 'Pavan Bhatt',
        'title': 'Order Amounts by Days ',
        'content': 'image',
        'date_posted': today.strftime("%d/%m/%Y"),
        

    },

     {
        'author': 'Chahak Agrawal',
        'title': 'Order Amounts by Hour ',
        'content': 'image',
        'date_posted': today.strftime("%d/%m/%Y"),
        

    },
    {
        'author': 'Pavan Bhatt',
        'title': 'Number of Orders per Days Since Last Purchase ',
        'content': 'image',
        'date_posted': today.strftime("%d/%m/%Y"),
        

    },
 {
        'author': 'Chahak Agrawal',
        'title': 'Amount of Items Per Order',
        'content': 'image',
        'date_posted': today.strftime("%d/%m/%Y"),
        

    },
{
        'author': 'Pavan Bhatt',
        'title': 'Reorder Ratio Per Department',
        'content': 'image',
        'date_posted': today.strftime("%d/%m/%Y"),
        

    },
    {
        'author': 'Chahak Agrawal',
        'title': 'Add To Cart Order vs. Reorder Ratio',
        'content': 'image',
        'date_posted': today.strftime("%d/%m/%Y"),
        

    },
    {
        'author': 'Pavan Bhatt',
        'title': 'Best Selling Products',
        'content': 'image',
        'date_posted': today.strftime("%d/%m/%Y"),
        

    },
    {
        'author': 'Chahak Agrawal',
        'title': 'Top Reordered Products',
        'content': 'image',
        'date_posted': today.strftime("%d/%m/%Y"),
        
    },
    {
        'author': 'Pavan Bhatt',
        'title': 'Number of products in each department',
        'content': 'image',
        'date_posted': today.strftime("%d/%m/%Y"),
        

    },
    {
        'author': 'Chahak Agrawal',
        'title': 'Most common buying choice.',
        'content': 'image',
        'date_posted': today.strftime("%d/%m/%Y"),
            

    },
    {

        'author': 'Pavan Bhatt',
        'title': 'Recommendation',
        'content': 'image',
        'date_posted': today.strftime("%d/%m/%Y"),

    },

       {
       'author': 'Pavan Bhatt',
        'title': 'Order Info',
        'content': 'There are 3421083 orders in total.'
                    'There are 3214874 orders that are prior.'
                    'There are 131209 orders that are in train set.'
                    'There are 75000 orders that are in test set.',
        'date_posted': today.strftime("%d/%m/%Y"),
    
    },



    {
       'author': 'Pavan Bhatt',
        'title': 'Number of users',
        'content':'  There are 206209 unique customer in total.'
                    'There are 131209 customers in the train set.'
                    'There are 75000 customers in the test set.' ,
        'date_posted': today.strftime("%d/%m/%Y"),
        

    },


    {
       'author': 'Pavan Bhatt',
        'title': 'Tranaction  Info',
        'content':  'There are 3346083 order transactions .' ,
        'date_posted': today.strftime("%d/%m/%Y"),
        

    },


    {
       'author': 'Pavan Bhatt',
        'title': 'Products Info',
        'content': '19955360 products have reordered before .'
                    ' There are 33819106 grocery products ordered .'
                    'There are 49685 unique products.'
                    '13863746 products haven’t reordered before.'
                    '0.59 have reordered before .'  
                    '0.41 haven’t reordered before.',
        'date_posted': today.strftime("%d/%m/%Y"),
        

    },


    {
       'author': 'Pavan Bhatt',
        'title': 'Reorder Info',
        'content': 'dairy eggs has the most reorder ratio per department.'
                     'personal care has the least reorder ratio per department.'
                    ' milk aisle has the highest reorder ratio per aisle.'
                    'spices seasonings has the least reorder ratio per aisle.',
        'date_posted': today.strftime("%d/%m/%Y"),
        

    }
]



@app.route("/<title>", methods=['GET', 'POST','STATIC'])
    
def graph(title): 
    amount=graph1();
    order=graph2();
    hour=graph3();
    dslp=graph4();();
    aoi=graph5();
    ropd=graph6();
    cart=graph7();
    bsp=graph8();
    trp=graph9();
    nop=graph10();
    common=graph11();


    rec=recommend();


    
    if title==' Amount of Orders Distribution graph':
        return render_template('graph.html', graph1=amount, posts=posts)
    elif title=='Order Amounts by Days':
        return render_template('graph.html', graph1=order, posts=posts)

    elif title=='Order Amounts by Hour':
        return render_template('graph.html', graph1=hour, posts=posts)
    elif title=='Number of Orders per Days Since Last Purchase':
        return render_template('graph.html', graph1=dslp, posts=posts)
    elif title=='Amount of Items Per Order':
        return render_template('graph.html', graph1=aoi, posts=posts)
    elif title=='Reorder Ratio Per Department':
        return render_template('graph.html', graph1=ropd, posts=posts)
    elif title=='Add To Cart Order vs. Reorder Ratio':
        return render_template('graph.html', graph1=cart, posts=posts)
    elif title=='Best Selling Products':
        return render_template('graph.html', graph1=bsp, posts=posts)
    elif title=='Top Reordered Products':
        return render_template('graph.html', graph1=trp, posts=posts)
    elif title=='Number of products in each department':
        return render_template('graph.html', graph1=nop, posts=posts)
    elif title=='Most common buying choice.':
        return render_template('graph.html', graph1=common, posts=posts)
    elif title=='Recommendation':
        return render_template('Recommend.html', df=rec, posts=posts)    



@app.route("/", methods=['GET', 'POST','STATIC'])
def first_page():
    return render_template('first_page.html')

@app.route("/home", methods=['GET', 'POST','STATIC'])
def home():
    return render_template('home.html', posts=posts)  

@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('first_page'))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)


   