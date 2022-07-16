from flask import Blueprint, blueprints, redirect, render_template, request

from models.vet import Vet
import repositories.vet_repository as vet_repository

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