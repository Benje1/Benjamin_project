DROP TABLE IF EXISTS in_care;
DROP TABLE IF EXISTS pets;
DROP TABLE IF EXISTS owners;
DROP TABLE IF EXISTS vets;

CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);

CREATE TABLE owners (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    contact_details VARCHAR(255)
);

CREATE TABLE pets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    date_of_birth DATE,
    type_of_animal VARCHAR(255),
    owner_id INT NOT NULL REFERENCES owners(id),
    treatment TEXT,
    vet_id INT NOT NULL REFERENCES vets(id)
);


CREATE TABLE in_care (
    id SERIAL PRIMARY KEY,
    pet_id INT REFERENCES pets(id),
    date_of_intake DATE
);
