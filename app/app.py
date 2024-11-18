from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/db_name'

db = SQLAlchemy(app)

# Check the URI:
print("Database URI: ", app.config['SQLALCHEMY_DATABASE_URI'])

if __name__ == "__main__":
    app.run(debug=True)
