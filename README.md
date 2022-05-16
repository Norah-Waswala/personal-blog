# personal-blog
## Author
Norah Waswala
## User Story
As a user, I would like to view the blog posts on the site
As a user, I would like to comment on blog posts
As a user, I would like to view the most recent posts
As a user, I would like to an email alert when a new post is made by joining a subscription.
As a user, I would like to see random quotes on the site
As a writer, I would like to sign in to the blog.
As a writer, I would also like to create a blog from the application.
As a writer, I would like to delete comments that I find insulting or degrading.
As a writer, I would like to update or delete blogs I have created.
## BDD
Load the page	On page load	Get all blogs, Select between signup and login
Select SignUp	Email,Username,Password	Redirect to login
Select Login	Username and password	Redirect to page with blogs that have been posted by writes and be able to subscribe to the blog
Select comment button	Comment	Form that you input your comment
Click on submit		Redirect to all comments tamplate with your comment and other comments
Subscription	Email Address	Flash message "Succesfully subsbribed to D-Blog"
## Development Installation
Clone the repository at https://github.com/Norah-Waswala/personal-blog.git
Move to the folder and install requirements
cd personal-blog
pip install -r requirements.txt
Exporting Configurations
export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
### Running the application
python manage.py server
Testing the application
python manage.py test
Open the application on your browser 127.0.0.1:5000.

## Technology used
Python3.8
Flask
Heroku
## Contact Information

License
[MIT] License:
Copyright (c)  2020 Norah Waswala
