'''factory pattern'''

class Dog:
    
    
    def __init__(self, name):
        self._name = name
        
    def speak(self):
        return 'woof'
        

class Cat:
    
    
    def __init__(self, name):
        self._name = name
        
    def speak(self):
        return 'meow'


def get_pet(pet='dog'):
    
    pets = dict(dog=Dog('Hope'), cat=Cat('Peace'))
    
    return pets[pet]
    
    

dog = get_pet('dog')

print dog.speak()

cat = get_pet('cat')

print cat.speak()