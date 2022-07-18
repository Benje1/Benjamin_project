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
    vet_id = request.form['vet.id']
    pet = Pet(name, dob, type, owner_details, treatment, vet_id)
    pet_repository.save(pet)
    return redirect("/pets")

@pets_blueprint.route("/pets/<id>")
def show(id):
    pet = pet_repository.select(id)
    return render_template("/pets/show.html", pet=pet)

@pets_blueprint.route("/pets/<id>/edit")
def edit(id):
    pet = pet_repository.select(id)
    vets = vet_repository.select_all()
    return render_template("/pets/edit.html", pet=pet, vets=vets)

@pets_blueprint.route("/pets/<id>", methods=["POST"])
def update(id):
    pet = pet_repository.select(id)
    pet.name = request.form['name']
    pet.dob = request.form['dob']
    pet.type = request.form['type']
    pet.owner_details = request.form['owner_details']
    pet.treatment = request.form['treatment']
    pet.vet_id = request.form['vet_id']
    pet_repository.update(pet)
    return redirect(f"/pets/{id}")
