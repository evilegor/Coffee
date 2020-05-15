import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Configuration(object):
	"""docstring for Configuration"""
	DEBUG = True
	SECRET_KEY = 'adadadadadadadadadad'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
