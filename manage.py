from app import create_app,db
from flask_script import Manager,Server

from app.models import Subscriber, User,Comment,Blog
from  flask_migrate import Migrate, MigrateCommand
# Creating app instance
app = create_app('development')

manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command('server',Server)
manager.add_command('db',MigrateCommand)
@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User,blog = Blog, comment=Comment, subscriber=Subscriber )
@manager.command
def test():
    '''
    Run the unit tests
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=5).run(tests)


if __name__ == '__main__':
    manager.run()