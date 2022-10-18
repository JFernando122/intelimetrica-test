from flask import Flask
from dotenv import load_dotenv
load_dotenv()
from config.database import database
app = Flask(__name__)

database.initialize(app)
database.createTables(app)

from routes.restaurant import restaurant

app.register_blueprint(restaurant, url_prefix='/restaurant')
if __name__ == '__main__':
  app.run(debug=True)


