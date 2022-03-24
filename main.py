from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SECRET_KEY'] = 'generous'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Restaurant.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restaurant_name = db.Column(db.String(100), nullable=False)
    restaurant_location = db.Column(db.String(100), nullable=False)


# db.create_all()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/all')
def all_restaurants():
    restaurants = db.session.query(Restaurant).all()
    return render_template('restaurants.html', restaurants=restaurants)


@app.route('/search', methods=['GET'])
def one_restaurant():
    # to be worked on
    if request.method == 'GET':
        user_input = request.args.get('loc')
        queried_rest = db.session.query(Restaurant).filter_by(restaurant_name=user_input).first()
        resta_name =queried_rest.restaurant_name
        rest_id = queried_rest.id
        rest_location = queried_rest.restaurant_location
        response = {
            "Id": rest_id,
            "restaurant name": resta_name,
            "Restaurant Location": rest_location,
        }
        return response
    return render_template('restaurants.html')


if __name__ == '__main__':
    app.run(debug=True)
