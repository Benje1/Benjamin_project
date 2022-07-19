from db.run_sql import run_sql
from models.owners import Owner
from models.pet import Pet
import repositories.owener_repository as owner_repository

def save(owner):
    sql = "INSERT INTO owners (name, contact_details) VALUES (%s, %s) RETURNING *"
    values = [owner.name, owner.contact_details]
    results = run_sql(sql, values)
    id = results[0]['id']
    owner.id = id
    return results

def select_all():
    owners = []
    sql = "SELECT * FROM owners"
    results = run_sql(sql)
    for row in results:
        owner = Owner(row['name'], row['contact_details'], row['id'])
        owners.append(owner)
    return owners

def select(id):
    owner = None
    sql = "SELECT * FROM owners WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
    owner = Owner(result['name'], result['contact_details'], result['id'])
    return owner

def delete(id):
    sql = "DELETE FROM owners WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(owner):
    sql = "UPDATE owners SET contact_details = %s WHERE id = %s"
    values = [owner.contact_details, owner.id]
    run_sql(sql, values)
