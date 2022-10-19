from flask import Flask, render_template
from dotenv import load_dotenv
load_dotenv()
from app.config.database import database
app = Flask(__name__)

database.initialize(app)
database.createTables(app)

from app.routes.restaurant import restaurant

app.register_blueprint(restaurant, url_prefix='/restaurant')

@app.route('/')
def home():
  return render_template('index.html')


if __name__ == '__main__':
  app.run(debug=True)


