import re

class Human:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        self._pets_allowed = "Heyyyyyy"

    @property
    def pets_allowed(self):
        return self._pets_allowed

    @pets_allowed.setter
    def pets_allowed(self, val):
        self._pets_allowed = val


topher = Human("Topher", "Male", 20)
print(topher.pets_allowed)
topher.pets_allowed = "wahahaha"

print(topher.pets_allowed)


pattern = r"anana"

print(re.findall(pattern, "ananananababanananananananana"))

print(r"I am \r\a\w!")