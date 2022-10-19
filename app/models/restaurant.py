from geoalchemy2 import Column, Geography
from app.config.database import database

class Restaurant(database.db.Model):
  id = database.db.Column(database.db.String(50), primary_key=True)
  rating = database.db.Column(database.db.SmallInteger)
  name = database.db.Column(database.db.String(80))
  site = database.db.Column(database.db.String(50))
  email = database.db.Column(database.db.String(80))
  phone = database.db.Column(database.db.String(16))
  street = database.db.Column(database.db.String(80))
  city = database.db.Column(database.db.String(80))
  state = database.db.Column(database.db.String(80))
  location = Column(Geography(geometry_type='POINT'))

  def __init__(self, id, rating, name, site, email, phone, street, city, state, lat, lng):
    super().__init__()
    self.id = id
    self.rating = rating
    self.name = name
    self.site = site
    self.email = email
    self.phone = phone
    self.street = street
    self.city = city
    self.state = state
    self.location = 'POINT(%s %s)' % (lat, lng)
