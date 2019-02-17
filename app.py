from flask import Flask
from flask_restful import Api, Resource, reqparse
import random

app = Flask(__name__)
api = Api(app)

users = [
    {
        "name": "Driver1",
        "full_name": "Harold",
        "rating": 5,
        "coordinates": (45.382364, -75.695791),
        "car_model": "Ford Mustang",
        "electric_car": False,
        "picture": "https://i.imgflip.com/122vae.jpg",
        "phone_number": "111-111-1111"
    },
    {
        "name": "Driver2",
        "full_name": "John Doe",
        "rating": 3,
        "coordinates": (45.400909, -75.699903),
        "car_model": "Tesla Model 3",
        "electric_car": True,
        "picture": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTGGGqbW9-gUJAOpv4dSXm_Scl3PaLnvXeycOcznmYKV_vbf98Xiw",
        "phone_number": "222-222-2222"
    },
    {
        "name": "Driver3",
        "full_name": "Carleton",
        "rating": 4,
        "coordinates": (45.337995, -75.726191),
        "car_model": "Toyota Corolla",
        "electric_car": False,
        "picture": "https://www.1310news.com/wp-content/blogs.dir/sites/4/2016/12/01/carleton-u-logo.jpg",
        "phone_number": "333-333-3333"
    }
]

class User(Resource):

    def get(self, name):
        for user in users:
            if (name == user["name"]):
                return user, 200
        return "User not found", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("rating")
        args = parser.parse_args()

        for user in users:
            if (name == user["name"]):
                return "User with name {} already exists".format(name), 400

        user = {
            "name": name,
            "rating": args["rating"]
        }
        users.append(user)
        return user, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("rating")
        args = parser.parse_args()

        for user in users:
            if (name == user["name"]):
                user["rating"] = args["rating"]
                return user, 200

        user = {
            "name": name,
            "rating": args["rating"]
        }
        users.append(user)
        return user, 201

    def delete(self, name):
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted.".format(name), 200

class UserList(Resource):
    def get(self):
        return users, 200


class UserRandom(Resource):
    def get(self):
        return random.choice(users), 200



api.add_resource(User, "/user/<string:name>")
api.add_resource(UserList, "/users")
api.add_resource(UserRandom, "/random_user")

app.run(debug=True)


