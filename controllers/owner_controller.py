from flask import Blueprint, render_template, redirect, request, blueprints

from models.owners import Owner
import repositories.owener_repository as owner_repository

owners_blueprint = Blueprint("owners", __name__)

@owners_blueprint.route("/owners")
def owners():
    owners = owner_repository.select_all()
    return render_template("owners/index.html", owners=owners)

@owners_blueprint.route("/owners/<id>/delete", methods=["POST"])
def delete(id):
    owner_repository.delete(id)
    return redirect("/owners")