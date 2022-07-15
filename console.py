import pdb
import datetime

from models.pet import Pet
from models.vet import Vet
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository

vet1 = Vet("Fred", "Pears")
vet_repository.save(vet1)

wilbur = Pet("Wilbur", "2020-07-16", "Hamster", "Betty", "Antibiotics", vet1.id)
pet_repository.save(wilbur)

vet_repository.delete_all()

pdb.set_trace()