from flask import render_template,redirect,url_for,abort,request,flash
from app.main import main
from app.models import User,Blog,Comment,Subscriber
from .forms import UpdateProfile,CreateBlog,ChangeProfile
from .. import db
from app.requests import get_quotes
from flask_login import login_required,current_user
from ..email import mail_message
import secrets
import os


@main.route('/')
def index():
    quotes = get_quotes()
    blogs = Blog.query.order_by(Blog.posted.desc()).all() 
    return render_template('index.html',quote = quotes, blogs=blogs)

@main.route('/new_post', methods=['POST','GET'])
@login_required
def new_blog():
    # subscribers = Subscriber.query.all()
    form = CreateBlog()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        user_id =  current_user
        blog = Blog(title=title,content=content,user_id=current_user._get_current_object().id)
 
        blog.save()
        # for subscriber in subscribers:
        #     mail_message("New Blog Post","email/new_blog",subscriber.email,blog=blog)
        return redirect(url_for('main.index'))
        # flash('You Posted a new Blog')
    return render_template('newblog.html', form = form)
@main.route('/blog/<id>')
def blog(id):
    comments = Comment.query.filter_by(blog_id=id).all()
    blog = Blog.query.get(id)
    return render_template('blog.html',blog=blog,comments=comments)
    




@main.route('/comment/<blog_id>', methods = ['Post','GET'])
@login_required
def comment(blog_id):
    blog = Blog.query.get(blog_id)
    comment =request.form.get('newcomment')
    new_comment = Comment(comment = comment, user_id = current_user._get_current_object().id, blog_id=blog_id)
    new_comment.save()
    return redirect(url_for('main.blog',id = blog.id))



@main.route('/blog/<blog_id>/delete', methods = ['POST'])
@login_required
def delete_post(blog_id):
    blog = Blog.query.get(blog_id)
    if blog.user != current_user:
        abort(403)
    blog.delete()
    flash("You have deleted your Blog succesfully!")
    return redirect(url_for('main.index'))


@main.route('/user/<string:username>')
def user_posts(username):
    user = User.query.filter_by(username=username).first()
    
    blogs = Blog.query.filter_by(user=user).order_by(Blog.posted.desc())
    if user is None:
        abort(404)
    return render_template('profile/profile.html',blogs=blogs,user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(username):
    user = User.query.filter_by(username = username).first()
    if user is None:
        abort(404)

    form = ChangeProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)
