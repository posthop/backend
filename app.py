from flask import Flask
from flask_restful import Api, Resource, reqparse
import random
import os

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
        "name": "Driver4",
        "full_name": "Mario",
        "rating": 3,
        "coordinates": (43.653355, -79.383120),
        "car_model": "Nissan Leaf",
        "electric_car": True,
        "picture": "https://i.imgur.com/JGNcNKm.png",
        "phone_number": "444-444-4444"
    },
    {
        "name": "Driver5",
        "full_name": "Batman",
        "rating": 5,
        "coordinates": (49.875000, -97.119636),
        "car_model": "Batmobile",
        "electric_car": True,
        "picture": "https://i.imgur.com/IY2YWY9.png",
        "phone_number": "555-555-5555"
    },
    {
        "name": "Driver6",
        "full_name": "Julia",
        "rating": 5,
        "coordinates": (43.541391, -79.666126),
        "car_model": "Audi A4",
        "electric_car": False,
        "picture": "https://i.imgur.com/kyM4fKd.png",
        "phone_number": "666-666-6666"
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

app.run(os.getenv('POSTHOP_HOST', '127.0.0.1'), debug=True)


