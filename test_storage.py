#!user/bin/python3
"""test db storage."""
import models
from models.user import User
from models.city import City



inst = User()
print(inst)
inst.save()
print("Done")

