'''inheritance'''

class Animal(object):
    
    def speak(self):
        return ''
        
        
class Dog(Animal):
    
   
    
    def speak(self):
        return 'woof'
        
        
class Cat(Animal):
    
  
        
    def speak(self):
        return 'mew'
        

if __name__ == '__main__':
    
    
    dog = Dog()
    cat = Cat()
    
    
    print dog.speak()
    #print cat.speak()