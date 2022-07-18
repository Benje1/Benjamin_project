from flask import Blueprint, render_template, redirect, request, blueprints

from models.owners import Owner
from models.pet import Pet
import repositories.owener_repository as owner_repository
import repositories.vet_repository as vet_repository
import repositories.pet_repository as pet_repository

owners_blueprint = Blueprint("owners", __name__)

@owners_blueprint.route("/owners")
def owners():
    owners = owner_repository.select_all()
    return render_template("owners/index.html", owners=owners)

@owners_blueprint.route("/owners/<id>/delete", methods=["POST"])
def delete(id):
    owner_repository.delete(id)
    pet_repository.delete_by_owner(id)
    return redirect("/owners")

@owners_blueprint.route("/owners/new")
def new():
    vets = vet_repository.select_all()
    return render_template("/owners/new.html", vets=vets)

@owners_blueprint.route("/owners", methods=["POST"])
def create():
    name = request.form['name']
    contact_details = request.form['contact_details']
    owner = Owner(name, contact_details)
    results = owner_repository.save(owner)
    id = results[0]['id']
    owner.id = id
    pet_name = request.form['pet_name']
    dob = request.form['dob']
    pet_type = request.form['type']
    treatment = request.form['treatment']
    vet_id = request.form['vet.id']
    pet = Pet(pet_name, dob, pet_type, owner.id, treatment, vet_id)
    pet_repository.save(pet)
    return redirect("/owners")

@owners_blueprint.route("/owners/<id>")
def show(id):
    owner = owner_repository.select(id)
    pets = pet_repository.select_by_owner(owner.id)
    return render_template("/owners/show.html", owner=owner, pets=pets)

@owners_blueprint.route("/owners/<id>/edit")
def edit(id):
    owner = owner_repository.select(id)
    return render_template("/owners/edit.html", owner=owner)

@owners_blueprint.route("/owners/<id>", methods=["POST"])
def update(id):
    owner = owner_repository.select(id)
    owner.contact_details = request.form['contact_details']
    owner_repository.update(owner)
    return redirect(f"/owners/{id}")