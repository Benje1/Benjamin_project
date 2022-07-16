from unittest import result
from db.run_sql import run_sql
from models.pet import Pet
from models.vet import Vet
import repositories.vet_repository as vet_repository

def save(pet):
    sql = """INSERT INTO pets (name, date_of_birth, type_of_animal, owner_details, treatment, vet_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"""
    values = [pet.name, pet.dob, pet.type, pet.owner_details, pet.treatment, pet.vet_id]
    results = run_sql(sql, values)
    id = results[0]['id']
    pet.id = id

def select_all():
    pets = []
    sql = "SELECT * FROM pets"
    results = run_sql(sql)
    for row in results:
        pet = Pet(row['name'], row['date_of_birth'], row['type_of_animal'], row['owner_details'], row['treatment'], row['vet_id'], row['id'])
        pets.append(pet)
    return pets

def select(id):
    pet = None
    sql = "SELECT * FROM pets WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
    pet = Pet(result['name'], result['date_of_birth'], result['type_of_animal'], result['owner_details'], result['treatment'], result['vet_id'], result['id'])
    return pet

def delete_all():
    sql = "DELETE FROM pets"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM pets WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(pet):
    sql = "UPDATE pets SET (name, date_of_birth, type_of_animal, owner_details, treatment, vet_id) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [pet.name, pet.dob, pet.type, pet.owner_details, pet.treatment, pet.vet_id, pet.id]
    run_sql(sql, values)

def vet(pet):
    vet = None
    sql = "SELECT first_name, last_name, vets.id FROM pets JOIN vets On vet_id = vets.id WHERE pets.id = %s"
    values = [pet.id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        vet = Vet(result['first_name'], result['last_name'], result['id'])
    return vet