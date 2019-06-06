class Config(object):
	DEBUG = False
	TESTING = False
	SECRET_KEY = '122332'

class ProductionConfig(Config):
	DATABASE_HOST = '127.0.0.1'
	USER = 'root'
	PASSWORD = ''
	DATABASE = 'flask_db'

class DevelopmentConfig(Config):
	DEBUG = True
	DATABASE_HOST = '127.0.0.1'
	USER = 'root'
	PASSWORD = ''
	DATABASE = 'flask_db'

class TestingConfig(Config):
	TESTING = True
	DATABASE_HOST = '127.0.0.1'
	USER = 'root'
	PASSWORD = ''
	DATABASE = 'flask_db'
