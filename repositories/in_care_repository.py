from db.run_sql import run_sql
from models.in_care import In_care

def intake(pet_id, date_of_intake):
    sql = "INSERT INTO in_care (pet_id, date_of_intake) VALUES (%S, %S)"
    vallues = [pet_id, date_of_intake]

def select_all():
    intake = []
    sql = "SELECT * FROM in_care JOIN pets ON in_care.pet_id = pets.id"
    results = run_sql(sql)
    for row in results:
        in_care = In_care(row['name'], row['date_of_intake'], row['type_of_animal'], row['treatment'], row['id'])
        intake.append(in_care)
    return intake

def delete(id):
    sql = "DELETE FROM in_care WHERE id = %s"
    values = [id]
    run_sql(sql, values)