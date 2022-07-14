DROP TABLE IF EXISTS pets
DROP TABLE IF EXISTS vets

CREATE TABLE vets {
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
}

CREATE TABLE pets {
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    date_of_birth DATE,
    type_of_animal VARCHAR(255),
    owner_details VARCHAR(255),
    treatment TEXT,
    vet_id INT NOT NULL REFERENCES vet(id) ON DELETE CASCADE
}

CREATE TABLE owner {
    id SERIAL PRIMARY KEY
    name VARCHAR(255)
}