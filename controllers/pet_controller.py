from flask import Blueprint, blueprints, redirect, render_template, request

from models.pet import Pet
import repositories.pet_repository as pet_repository

pets_blueprint = Blueprint("pets", __name__)

# index
@pets_blueprint.route("/pets")
def pets():
    pets = pet_repository.select_all()
    return render_template("pets/index.html", pets=pets) 