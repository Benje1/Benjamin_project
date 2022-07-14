import pdb

from models.pet import Pet
from models.vet import Vet
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository

vet1 = Vet("Javier")
vet_repository.save(vet1)
wilbur = Pet("Wilbur", 16_07_2020, "Hamster", "Nimoo", "Antibiotics", vet1)
pet_repository.save(wilbur)

pdb.set_trace()