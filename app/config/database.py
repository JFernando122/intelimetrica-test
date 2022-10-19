import os
from flask_sqlalchemy import SQLAlchemy


class Database:
  db = None
  __DATABASE_URI = os.environ['DATABASE_URI']
  
  def initialize(self, app):
    app.config['SQLALCHEMY_DATABASE_URI'] = self.__DATABASE_URI
    self.db = SQLAlchemy(app)

  def createTables(self, app):
    with app.app_context():
      self.db.create_all()

database = Database()