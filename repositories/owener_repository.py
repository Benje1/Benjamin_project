from db.run_sql import run_sql
from models.owners import Owner
from models.pet import Pet
import repositories.owener_repository as owner_repository

def save(owner):
    sql = """INSERT INTO owners (name, pet_id) VALUES (%s, %s) RETURNING *"""
    values = [owner.name, owner.pet_id]
    results = run_sql(sql, values)
    id = results[0]['id']
    owner.id = id

def select_all():
    owners = []
    sql = "SELECT * FROM owners"
    results = run_sql(sql)
    for row in results:
        owner = Owner(row['name'], row['pet_id'], row['id'])
        owners.append(owner)
    return owners

def delete(id):
    sql = "DELETE FROM owner WHERE id = %s"
    values = [id]
    run_sql(sql, values)

