'''
### Principle of OOP ###

    ### 4 Major principles ###

    1. Abstraction; 
        
        * It provides you with a simple interface to the clients, where the clients can interact 
          with class objects and call methods defined in the interface.
        
        * It abstracts the complexity of internal classes with an interface so that the client need
          not be aware of internal implementations.
    
        ** example, internal details of the Adder class are abstracted with the add() method
        
        class Adder:
            
            def __init__(self):
                self.sum = 0
                
            def add(self, value):
                self.sum += value
                
        # main
        
        acc = Adder()
        
        for el in range(99):
            acc.add(el)
            
        print 'total : %s' % (str(acc.sum))
    
    2. Inheritance; 
    
        * Inheritance indicates that one class derives (most of its) functionally from the parent class.Inheritance
        
        * Inheritance is described as an option to reuse functionality defined in the base class
          and allow independent extensions of the original software implementation.and
          
        * Inheritance creates hierarchy via the relationships among objects of different classes.
          Python, unlike Jaca, supports multiple inheritance (inheriting from multiple base classes.)
          
        ** multiple inheritance exmaple      
          
            Sedan   Truck
                \   /
                 SUV.get_options() , get_engine()
        
    
        
        
        ** The Python supports multiple inheritance
    3. Polymorphism;
    
        * Polymorphism can be of two types:
            
            * An object provides different implementations of the method based on input parameters
            
            * The same interface can be used by objects of different types
            
        * In Python, polymorphism is a feature built-in for the language. For example, the + operator
          can act on two integers to add them or can work with strings to concatenate them
          
        ** The Python is already has polymorphism
        
        ** In the example, Strings, Tuples, or Lists can all be accessed with an integer index. 
           This shows how Python demonstrates polymorphism in built-in types:
           
           a = 'JK'
           b = (1,2,3)
           c = [1,2,3,4,5]
           print a[1], b[0], c[2]
    
    4. Encapsulation; 
    
        * An object's behavior is kept hidden from the outside world or objects keep their state 
          information private.Python
          
        * Clients can't change the object's internal state by directly acting on them; rather,
          clients request the object by sending messages. Based on thetype of requests, objects may respond
          by changing their internal state using special memeber functions such as get and set.by
          
        * In Python, the concept of encapsulate (data and method hiding) is not implicit, as it doesn't have
          keywords such as public, private, and protected (in languages such as C++ or Java) that are required
          to support encapsulation. Of course, accessibility can be made private by prefixing __ in the
          variable or function name.
          
          
        ** Python doesn't provide keywords such as public, private, protected
        ** '__' use this as prefix of function name and variable name
        
    
    ### Composition ###
    
        * It is a way to combine objects or classes into more complex data structures or software implementations
        
        * In composition, an object is used to call member functions in other modules thereby making base functionality
          available across modules without inheritance
          
        ** example, the object of class A is composited under class Based
        
        
        class A(ojbect):
            
            def a1(self):
                print 'a1'
                
        
        class B(object):
        
            def b(self):
                print 'b'
                A().a1()
                
        
        # main
        
        obj_b = B()
        obj_b.b()
'''

class Person(object):
    
    #public variable
    username = 'root'
    
    
    #private variable
    __password = 'private var'
    
    
    # constructor
    def __init__(self, name):
        self.name = name
        self.__prv_get_name()
        
        
    # member function
    def get_name(self, ):
        return self.name
        
    
    # get username
    def get_username(self, ):
        return self.username
        
    
    # get password
    def get_password(self, ):
        return self.__password
        
        
    # private member function
    def __prv_get_name(self, ):
        print '### %s' % (self.name)
        

class Car(object):
    
    car_type = '4 door car'
    
    # constructor
    def __init___(self):
        print '### %s' % ('Car declared')
        
    
    # get car type
    def get_car_type(self, ):
        return self.car_type


# Sedan
class Sedan(object):
    
    name = 'Lexus'
    options = ['Power Seat', 'Leather Set']

    
    def __init__(self, name):
        self.name = name
        
    
    def get_name(self, ):
        return self.name
        
    
    def get_options(self, ):
        return self.options
        
# Truck
class Truck(object):
    
    name = 'Toyota Sequa'
    engine = 'V8'
    
    
    def __init__(self, name):
        self.name = name
        
        
    def get_name(self, ):
        return self.name


    def get_engine(self, ):
        return self.engine

class Suv(Sedan, Truck):
    
    name = 'RX 350'
    type = 'Luxury'
    
    # constructor
    def __init__(self, name):
        self.name = name
    
    
    # get name for suv
    def get_name(self, ):
        return self.name
    

    def getType(self, ):
        return self.type


# Abstract Class Sample; abstracts the complexity, provide the simple interface to clients
import random

class Algorithm(object):
    
    # hide the complexity
    def qsort(self, li):
        if len(li) <= 0:
            return li
        
        p_adr = random.randrange(0,len(li))
        p = li[p_adr]
        l = []
        r = []
        eq = []
        
        for idx, el in enumerate(li):
            if idx == p_adr:
                continue
            else:
                if el < p:
                    l.append(el)
                elif el > p:
                    r.append(el)
                else:
                    eq.append(el)
                    
        return self.qsort(l) + eq + [p] + self.qsort(r)
        

# Composition sample
class Odd(object):
    
    def get_odd(self, li):
        temp = filter(lambda el: el % 2 != 0, li)
        return Algorithm().qsort(temp)



if __name__ == '__main__':
    
    p = Person('JK')
    suv = Suv('Armada')
    
    print '### options %s ' % (suv.get_options())
    print '### engine %s ' % (suv.get_engine())
    print '### name %s ' % (suv.get_name())
    
    li = [5,4,3,3,2,1]
    a = Algorithm()
    obj_odd = Odd()
    print '## Odd numbers from sorted list %s ' % (obj_odd.get_odd(li))
    
    