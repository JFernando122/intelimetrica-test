from flask import Blueprint, request, jsonify, make_response
import uuid
from shapely import wkb
from marshmallow import ValidationError
from app.validation.statistics import StatsValidation
from app.validation.restaurant import RestuarantValidation
from app.models.restaurant import Restaurant
from app.config.database import database

restaurant = Blueprint('restaurant', __name__)

@restaurant.route('/', methods=['POST'])
def createRestaurant():
  data = request.get_json()
  id = uuid.uuid4()
  try:
    validatedData = RestuarantValidation().load(data)
  except ValidationError as error:
    errorMessage = RestuarantValidation().proccessErrorMessage(error)
    return make_response(jsonify({"message": errorMessage}), 400)

  newRestaurant = Restaurant(
    id = id,
    rating= validatedData['rating'],
    name= validatedData['name'],
    site= validatedData['site'],
    email= validatedData['email'],
    phone= validatedData['phone'],
    street= validatedData['street'],
    city= validatedData['city'],
    state= validatedData['state'],
    lat= validatedData['lat'],
    lng= validatedData['lng']
  )

  database.db.session.add(newRestaurant)
  database.db.session.commit()

  return make_response(jsonify({ "message": "User created Succesfully"}), 201)

@restaurant.route('/', methods=['GET'])
def getRestaurants():
  restaurants = Restaurant.query.filter()

  output = []
  for restaurant in restaurants:
    point = wkb.loads(bytes(restaurant.location.data))
    output.append({
      "id": restaurant.id,
      "rating": restaurant.rating,
      "name": restaurant.name,
      "site": restaurant.site,
      "email": restaurant.email,
      "phone": restaurant.phone,
      "street": restaurant.street,
      "city": restaurant.city,
      "state": restaurant.state,
      "lat": point.x,
      "lng": point.y
    })

  return jsonify({
    "count": len(output),
    "restaurants": output
  })

@restaurant.route('/<restaurant_id>', methods=['GET'])
def getRestaurant(restaurant_id):
  restaurant = Restaurant.query.filter_by(id=restaurant_id).first()

  if not restaurant:
    return make_response(jsonify({ "message": 'id doesnt correspond to a restaurant' }), 404)

  point = wkb.loads(bytes(restaurant.location.data))
  data = {
      "id": restaurant.id,
      "rating": restaurant.rating,
      "name": restaurant.name,
      "site": restaurant.site,
      "email": restaurant.email,
      "phone": restaurant.phone,
      "street": restaurant.street,
      "city": restaurant.city,
      "state": restaurant.state,
      "lat": point.x,
      "lng": point.y
    }
  return jsonify({ 'restaurant': data })

@restaurant.route('/<restaurant_id>', methods=['PUT'])
def updateRestaurant(restaurant_id):
  data = request.get_json()
  try:
    RestuarantValidation().load(data, partial=True)
  except ValidationError as error:
    errorMessage = RestuarantValidation().proccessErrorMessage(error)
    return make_response(jsonify({"message": errorMessage}), 400)


  restaurant = Restaurant.query.filter_by(id=restaurant_id).update(data)
  database.db.session.commit()

  if not restaurant:
    return make_response(jsonify({ "message": 'id doesnt correspond to a restaurant' }), 404)

  return jsonify(data)

@restaurant.route('/<restaurant_id>', methods=['DELETE'])
def deleteRestaurant(restaurant_id):
  restaurant = Restaurant.query.filter_by(id=restaurant_id).first()

  if not restaurant:
    return make_response(jsonify({ "message": 'id doesnt correspond to a restaurant' }), 404)

  print(restaurant)
  database.db.session.delete(restaurant)
  database.db.session.commit()

  return jsonify({ "message": "Restaurant deleted successfully" })

@restaurant.route('/statistics', methods=["GET"])
def getInRadius():
  args = request.args

  try:
    validatedArgs = StatsValidation().load(args)
  except ValidationError as error:
    errorMessage = StatsValidation().proccessErrorMessage(error)
    return make_response(jsonify({ "message": errorMessage }), 400)


  result = database.db.session.execute("SELECT count(id) as count, avg(rating) as avg, stddev(rating) as std FROM restaurant r WHERE ST_DWITHIN(r.location, ST_GeographyFromText('POINT(%s %s)'),%s);" % (args["latitude"], args["longitude"], args["radius"]))

  output = {}

  for row in result:
    output = {
      "count": row.count,
      "avg": row.avg,
      "std": row.std
    }

  return jsonify(output)