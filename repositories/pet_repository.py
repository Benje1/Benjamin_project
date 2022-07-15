from db.run_sql import run_sql
from models.pet import Pet
import repositories.vet_repository as vet_repository

def save(pet):
    sql = """INSERT INTO pets (name, date_of_birth, type_of_animal, owner_details, treatment, vet_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"""
    values = [pet.name, pet.dob, pet.type, pet.owner_details, pet.treatment, pet.vet_id]
    results = run_sql(sql, values)
    id = results[0]['id']
    pet.id = id

def select_all():
    pets = []
    sql = "SELECT * FROM vets"
    results = run_sql(sql)
    for result in results:
        vet = vet_repository.select(result["vet_id"])
        pet = Pet(result['name'], result['date_of_birth'], result['type_of_animal'], result['owner_details'], result['treatment'], vet, result['id'])
        pets.append(pet)
    return pets