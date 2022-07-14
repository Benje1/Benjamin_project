from db.run_sql import run_sql
from models.pet import Pet

def save(pet):
    sql = """INSERT INTO pets (name, date_of_birth, type_of_animal, owner_details, treatment, vet_id) VALUES (%s, %s, %s, %s, %s, %s,) RETURNING id"""
    values = [pet.name, pet.dob, pet.type, pet.owner_details, pet.treatment, pet.vet_id]
    results = run_sql(sql, values)
    id = results[0]['id']
    pet.id = id