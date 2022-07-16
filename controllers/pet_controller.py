from sys import dont_write_bytecode
from flask import Blueprint, blueprints, redirect, render_template, request

from models.pet import Pet
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository

pets_blueprint = Blueprint("pets", __name__)

# index
@pets_blueprint.route("/pets")
def pets():
    pets = pet_repository.select_all()
    return render_template("pets/index.html", pets=pets) 

@pets_blueprint.route("/pets/<id>/delete", methods=["POST"])
def delete(id):
    pet_repository.delete(id)
    return redirect("/pets")

@pets_blueprint.route("/pets/new")
def new():
    vets = vet_repository.select_all()
    return render_template("/pets/new.html", vets=vets)

@pets_blueprint.route("/pets", methods=["POST"])
def create():
    name = request.form['name']
    dob = request.form['dob']
    type = request.form['type']
    owner_details = request.form['owner_details']
    treatment = request.form['treatment']
    vet_id = request.form['vet_id']
    pet = Pet(name, dob, type, owner_details, treatment, vet_id)
    pet_repository.save(pet)
    return redirect("/pets")