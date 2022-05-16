
from flask import render_template,request,redirect,url_for,request,flash,abort

from app.models import User,Blog, Comment,Subscriber
from . import main
# from ..requests import get_quotes
from flask_login import current_user, login_required
from ..models import User,Blog,Comment,Subscriber
from .forms import BlogForm,CommentForm
from flask_login import login_required,current_user
from ..email import mail_message

import secrets
import os
@main.route('/')
def index():
  
    
    blogs = Blog.query.order_by(Blog.date_created.desc()).all()    
    return render_template("index.html",blog = blogs)

@main.route('/create_blog', methods = ['POST','GET'])

def new_blog():
    subscribers = Subscriber.query.all()
    form = BlogForm()
    if form.validate_on_submit():
        title = form.title.data
        blog = form.blog.data
        category = form.category.data
        user_id = current_user
        new_blog_object = Blog(blog=blog,user_id=current_user._get_current_object().id,category=category,title=title)
        new_blog_object.save_b()
        for subscriber in subscribers:
            mail_message("New Blog Post","email/new_blog",subscriber.email,blog=blog)
        return redirect(url_for('main.index'))
        
    return render_template('create_blog.html', form = form)

@main.route('/comment/<int:blog_id>', methods = ['POST','GET'])

def comment(blog_id):

    form = CommentForm()
    blog = Blog.query.get(blog_id)
    all_comments = Comment.query.filter_by(blog_id = blog_id).all()
    if form.validate_on_submit():
        comment = form.comment.data 
        blog_id = blog_id
        user_id = current_user
        new_comment = Comment(comment = comment,user_id = user_id,blog_id = blog_id)
 

        title = f'{blog.title} comment'
        return redirect(url_for('main.index', blog_id = blog_id))
    return render_template('comment.html', form =form, blog = blog,all_comments=all_comments)

@main.route('/subscribe',methods = ['POST','GET'])
def subscribe():
    email = request.form.get('subscriber')
    new_subscriber = Subscriber(email = email)
    new_subscriber.save_subscriber()
    mail_message("Subscribed to Norah's Blog","email/welcome_subscriber",new_subscriber.email,new_subscriber=new_subscriber)
    flash('Sucessfuly subscribed')
    return redirect(url_for('main.index'))

@main.route('/blog/<blog_id>/delete', methods = ['POST'])
@login_required
def delete_post(blog_id):
    blog = Blog.query.get(blog_id)
    if blog.user != current_user:
        abort(403)
    blog.delete()
    flash("You have deleted your Blog succesfully!")
    return redirect(url_for('main.index'))