#!/usr/bin/python3
""" Test link Many-To-Many Place <> Amenity
"""
import models
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

# creation of a State
state = State(name="Texas")
state.save()

# creation of a City
city = City(state_id=state.id, name="Dallas")
city.save()

# creation of a User
user = User(
    email="john@snow.com",
    password="johnpwd",
    first_name="John",
    last_name="Snow"
)
user.save()

# creation of 2 Places
place_1 = Place(
    city_id=city.id,
    user_id=user.id,
    name="The Flats",
    description="Small smart apartment homes located downtown.",
    number_rooms=2,
    number_bathrooms=1,
    max_guest=4,
    price_by_night=150,
    latitude=37.773972,
    longitude=-122.431297
)
place_1.save()
place_2 = Place(
    city_id=city.id,
    user_id=user.id,
    name="Garden Grove",
    description="Beautiful large house with garden courtyard",
    number_rooms=4,
    number_bathrooms=4,
    max_guest=8,
    price_by_night=300,
    latitude=47.773972,
    longitude=-122.431297
)
place_2.save()
place_3 = Place(
    city_id=city.id,
    user_id=user.id,
    name="Beach Hut",
    description="Open floor hut right on the beach.",
    number_rooms=1,
    number_bathrooms=1,
    max_guest=2,
    price_by_night=100,
    latitude=57.773972,
    longitude=-122.431297
)
place_3.save()
place_4 = Place(
    city_id=city.id,
    user_id=user.id,
    name="Boat House",
    description="Boat house that floats on the lake.",
    number_rooms=3,
    number_bathrooms=2,
    max_guest=6,
    price_by_night=200,
    latitude=67.773972,
    longitude=-122.431297
)
place_4.save()

# creation of 3 various Amenity
amenity_1 = Amenity(name="Wifi")
amenity_1.save()
amenity_2 = Amenity(name="Cable")
amenity_2.save()
amenity_3 = Amenity(name="Oven")
amenity_3.save()
amenity_4 = Amenity(name="Gym")
amenity_4.save()
amenity_5 = Amenity(name="Laundry")
amenity_5.save()
amenity_6 = Amenity(name="Pool")
amenity_6.save()

# link place_1 with 4 amenities
place_1.amenities.append(amenity_1)
place_1.amenities.append(amenity_2)
place_1.amenities.append(amenity_4)
place_1.amenities.append(amenity_6)

# link place_2 with 4 amenities
place_2.amenities.append(amenity_1)
place_2.amenities.append(amenity_2)
place_2.amenities.append(amenity_3)
place_2.amenities.append(amenity_5)

# link place_3 with 2 amenities
place_3.amenities.append(amenity_3)
place_3.amenities.append(amenity_5)

# link place_4 with amenities
place_4.amenities.append(amenity_3)
place_4.amenities.append(amenity_5)

storage.save()

print("OK")
