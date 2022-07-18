from flask import Blueprint, blueprints, redirect, render_template, request
from controllers.owner_controller import owners

from models.pet import Pet
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository
import repositories.owener_repository as owner_repository

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
    owners = owner_repository.select_all()
    return render_template("/pets/new.html", vets=vets, owners=owners)

@pets_blueprint.route("/pets", methods=["POST"])
def create():
    name = request.form['name']
    dob = request.form['dob']
    type = request.form['type']
    owner_id = request.form['owner.id']
    treatment = request.form['treatment']
    vet_id = request.form['vet.id']
    pet = Pet(name, dob, type, owner_id, treatment, vet_id)
    pet_repository.save(pet)
    return redirect("/pets")

@pets_blueprint.route("/pets/<id>")
def show(id):
    pet = pet_repository.select(id)
    owner = owner_repository.select(pet.owner_id)
    vet = vet_repository.select(pet.vet_id)
    return render_template("/pets/show.html", pet=pet, owner=owner, vet=vet)

@pets_blueprint.route("/pets/<id>/edit")
def edit(id):
    pet = pet_repository.select(id)
    vets = vet_repository.select_all()
    owners = owner_repository.select_all()
    return render_template("/pets/edit.html", pet=pet, vets=vets, owners=owners)

@pets_blueprint.route("/pets/<id>/edit", methods=["POST"])
def update(id):
    pet = pet_repository.select(id)
    pet.name = request.form['name']
    pet.dob = request.form['dob']
    pet.type = request.form['type']
    pet.owner_id = request.form['owner.id']
    pet.treatment = request.form['treatment']
    pet.vet_id = request.form['vet_id']
    pet_repository.update(pet)
    return redirect(f"/pets/{id}")

@pets_blueprint.route("/pets/<id>/treatment_edit")
def treatment_edit(id):
    pet = pet_repository.select(id)
    return render_template("/pets/treatment_edit.html", pet=pet)

@pets_blueprint.route("/pets/<id>/treatment_edit", methods=["POST"])
def update_treatment(id):
    pet = pet_repository.select(id)
    pet.treatment = request.form['treatment']
    pet_repository.update(pet)
    return redirect(f"/pets/{id}")