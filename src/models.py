from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Integer


db = SQLAlchemy()

class User(db.Model):
    favorites = db.relationship("Favorites")
    email = db.Column(String(100), nullable=False)
    password = db.Column(String(100), nullable=False)
    id = db.Column(Integer, primary_key=True)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
        }
    
class Favoritos(db.Model):
    id = db.Column(Integer, primary_key=True)
    planetas = db.relationship("Planetas")
    personajes = db.relationship("Personajes")

class Personajes(db.Model):
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(100))
    height = db.Column(String(100)) 
    mass = db.Column(String(100)) 
    hair_color = db.Column(String(100)) 
    eye_color = db.Column(String(100)) 
    birth_year = db.Column(String(100)) 
    gender = db.Column(String(100))
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "heigh": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color,  
            "birth_year": self.birth_year,
            "gender": self.gender,
        }
 

class Planetas(db.Model):
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(100))
    rotation_period = db.Column(String(100)) 
    orbital_period = db.Column(String(100)) 
    diameter = db.Column(String(100)) 
    climate = db.Column(String(100)) 
    gravity = db.Column(String(100)) 
    terrain = db.Column(String(100))
    surface_water = db.Column(String(100))
    population = db.Column(String(100))
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "diameter": self.diameter,
            "climate": self.climate,
            "gravity": self.gravity,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            "population": self.population,
        }