from flask import Flask, jsonify, render_template, request, redirect, url_for
from models.cafe import Cafe, db
import random


'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db.init_app(app)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record

@app.route("/random")
def get_random_cafe():
    row_count = db.session.query(Cafe).count()
    random_row_id = random.randint(1, row_count)
    print(random_row_id)
    with app.app_context():
        random_cafe = db.get_or_404(Cafe, random_row_id)
    # The long way to create a dict to jsonify, but you'd have to repeat this
    # or similar code block in other routes.
    # cafe_data = {
    #     "id": random_cafe.id,
    #     "name": random_cafe.name,
    #     "map_url": random_cafe.map_url,
    #     "img_url": random_cafe.img_url,
    #     "location": random_cafe.location,
    #     "seats": random_cafe.seats,
    #     "has_toilet": random_cafe.has_toilet,
    #     "has_wifi": random_cafe.has_wifi,
    #     "has_sockets": random_cafe.has_sockets,
    #     "can_take_calls": random_cafe.can_take_calls,
    #     "coffee_price": random_cafe.coffee_price
    # }
    # return jsonify(
    #     cafe=cafe_data
    # )

    # Instead, create a method in the Cafe class that returns a dict.
    # See ./models/cafe.py
    return jsonify(random_cafe.to_dict())


if __name__ == '__main__':
    app.run(debug=True)
