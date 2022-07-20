from flask import Flask, render_template, redirect, request, Blueprint
import repositories.in_care_repository as in_care_repository
import repositories.pet_repository as pet_repository

in_care_blueprint = Blueprint("in_care", __name__)

@in_care_blueprint.route("/in_care/new")
def new():
    pets = pet_repository.select_all()
    intaken = in_care_repository.select_all()
    for pet in pets:
        for animal in intaken:
            if animal.pet_id == pet.id:
                pets.remove(pet)
    return render_template("/in_care/new.html", pets=pets)

@in_care_blueprint.route("/in_care", methods=["POST"])
def create():
    pet_id = request.form['pet_id']
    date_of_intake = request.form['date_of_intake']
    in_care_repository.intake(pet_id, date_of_intake)
    return redirect("/pets")

@in_care_blueprint.route("/in_care/<id>/delete", methods=["POST"])
def delete(id):
    in_care_repository.delete(id)
    return redirect("/pets")

