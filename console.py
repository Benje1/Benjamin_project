import pdb


from models.pet import Pet
from models.vet import Vet
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository

vet_repository.delete_all()
pet_repository.delete_all()

vet1 = Vet('Fred', 'Pears')
vet_repository.save(vet1)

wilbur = Pet('Wilbur', '2020-07-16', 'Hamster', 'Betty', 'Antibiotics', vet1.id)
pet_repository.save(wilbur)

# wilbur.owner_details = "Lizzie"
# wilbur.type = "Syrian Hamster"
# pet_repository.update(wilbur)

# vet1.last_name = "apples"
# vet1.first_name = 'Fred'
# vet_repository.update(vet1)

# what_vet = pet_repository.vet(wilbur)
# print(what_vet.__dict__)

# pets = pet_repository.select_all()
# for pet in pets:
#     print(pet.__dict__)
pdb.set_trace()