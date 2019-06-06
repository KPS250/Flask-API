from flask import Flask, jsonify,request, Response
import pymysql
import jwt, datetime
from functools import wraps
from database import Database

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

print(app.config['DATABASE_HOST'])

db = Database(app.config['DATABASE_HOST'],app.config['USER'],app.config['PASSWORD'],app.config['DATABASE'])

def token_required(f):
	@wraps(f)
	def wrapper(*args, **kwargs):
		token = request.args.get('token')
		try:
			jwt.decode(token, app.config['SECRET_KEY'])
			return f(*args, **kwargs)
		except:
			return jsonify({'error': 'Need a valid Token'}), 401
	return wrapper

@app.route('/login')
def getToken():
	expiration_date = datetime.datetime.utcnow() + datetime.timedelta(seconds=100)
	token = jwt.encode({'exp': expiration_date, 'id': 1}, app.config['SECRET_KEY'], algorithm='HS256')
	return token

@app.route('/verify')
@token_required
def verifyToken():
	return jsonify('Hello')

@app.route('/')
def getPlaces():
	data = db.read(None)
	return jsonify(data)

@app.route('/<int:id>')
def getPlaceWithId(id):
	data = db.read(id)
	return jsonify(data)

@app.route('/', methods=['POST'])
def insertPlace():
	requestData = request.get_json()
	data = db.insert(requestData)
	return jsonify(data)

@app.route('/<int:id>', methods=['DELETE'])
def deletePlace(id):
	data = db.delete(id)
	return jsonify(data)

@app.route('/<int:id>', methods=['PUT'])
def updatePlace(id):
	requestData = request.get_json()
	data = db.update(id, requestData)
	return jsonify(data)

app.run(port=5000)