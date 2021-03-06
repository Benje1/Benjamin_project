from operator import imod
from db.run_sql import run_sql
from models.owners import Owner
from models.pet import Pet
from models.vet import Vet
import repositories.vet_repository as vet_repository
import repositories.owener_repository as owner_repository

def save(pet):
    sql = """INSERT INTO pets (name, date_of_birth, type_of_animal, owner_id, treatment, vet_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"""
    values = [pet.name, pet.dob, pet.type, pet.owner_id, pet.treatment, pet.vet_id]
    results = run_sql(sql, values)
    id = results[0]['id']
    pet.id = id

def select_all():
    pets = []
    sql = "SELECT * FROM pets ORDER BY id"
    results = run_sql(sql)
    for row in results:
        pet = Pet(row['name'], row['date_of_birth'], row['type_of_animal'], row['owner_id'], row['treatment'], row['vet_id'], row['id'])
        pets.append(pet)
    return pets
# SELECT * FROM pets JOIN owners ON pets.owner_id = owners.id

def select(id):
    pet = None
    sql = "SELECT * FROM pets WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
    pet = Pet(result['name'], result['date_of_birth'], result['type_of_animal'], result['owner_id'], result['treatment'], result['vet_id'], result['id'])
    return pet

def delete_all():
    sql = "DELETE FROM pets"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM pets WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(pet):
    sql = "UPDATE pets SET (name, date_of_birth, type_of_animal, owner_id, treatment, vet_id) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [pet.name, pet.dob, pet.type, pet.owner_id, pet.treatment, pet.vet_id, pet.id]
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

def delete_by_owner(owner_id):
    sql = "DELETE FROM pets WHERE owner_id = %s"
    values = [owner_id]
    run_sql(sql, values)

def select_by_owner(owner_id):
    pets = []
    sql = "SELECT * FROM pets WHERE owner_id = %s"
    values = [owner_id]
    results = run_sql(sql, values)
    for row in results:
        pet = Pet(row['name'], row['date_of_birth'], row['type_of_animal'], row['owner_id'], row['treatment'], row['vet_id'], row['id'])
        pets.append(pet)
    return pets

def select_by_vet(vet_id):
    pets = []
    sql = "SELECT * FROM pets WHERE vet_id = %s"
    values = [vet_id]
    results = run_sql(sql, values)
    for row in results:
        pet = Pet(row['name'], row['date_of_birth'], row['type_of_animal'], row['owner_id'], row['treatment'], row['vet_id'], row['id'])
        pets.append(pet)
    return pets