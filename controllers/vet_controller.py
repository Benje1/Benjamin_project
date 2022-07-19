from flask import Blueprint, blueprints, redirect, render_template, request

from models.vet import Vet
import repositories.vet_repository as vet_repository
import repositories.pet_repository as pet_repository

vets_blueprint = Blueprint("vets", __name__)

# index
@vets_blueprint.route("/vets")
def vets():
    vets = vet_repository.select_all()
    return render_template("vets/index.html", vets=vets)

@vets_blueprint.route("/vets/<id>/delete", methods=["POST"])
def delete(id):
    vet_repository.delete(id)
    return redirect("/vets")

@vets_blueprint.route("/vets/new")
def new():
    return render_template("/vets/new.html")

@vets_blueprint.route("/vets", methods=["POST"])
def create():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    vet = Vet(first_name, last_name)
    vet_repository.save(vet)
    return redirect("/vets")

@vets_blueprint.route("/vets/<id>")
def show(id):
    vet = vet_repository.select(id)
    pets = pet_repository.select_by_vet(vet.id)
    return render_template("/vets/show.html", vet=vet, pets=pets)

@vets_blueprint.route("/vets/<id>/edit")
def edit(id):
    vet = vet_repository.select(id)
    return render_template("/vets/edit.html", vet=vet)

@vets_blueprint.route("/vets/<id>/edit", methods=["POST"])
def update(id):
    vet = vet_repository.select(id)
    vet.first_name = request.form['first_name']
    vet.last_name = request.form['last_name']
    vet_repository.update(vet)
    return redirect(f"/vets/{id}")