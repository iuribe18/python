# python
python exercises


# Dictionary
¿Qué es un diccionario Python y para qué sirve?
Un diccionario en Python es una estructura de datos que permite almacenar cualquier tipo de información, desde cadenas de texto o caracteres hasta números enteros, con decimales, listas e incluso otros diccionarios. Al igual que sucede con un diccionario de lengua, los datos se encuentran ordenados utilizando una clave única para cada uno de ellos, lo que permite localizar cada uno de los datos de una forma muy rápida.

# OOP
Class: A blueprint for creating objects. A class defines a set of attributes and methods that the created objects will have.
Clase: Es una plantilla para crear objetos (instancias de la clase). Define un conjunto de atributos y métodos que los objetos creados a partir de la clase tendrán.
```bash
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
```
Object: An instance of a class. Objects have attributes (data) and methods (functions) defined by their class.
Objeto: Es una instancia de una clase. Una clase es un molde, y el objeto es una cosa concreta creada a partir de ese molde. Clase Coche, objeto "un coche rojo".
```bash
    my_car = Car('Toyota', 'Corolla', 2020)

```
Method: A function defined inside a class. Methods operate on instances of the class (objects).
```bash
  class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def start_engine(self):
        print(f'The engine of the {self.make} {self.model} is now running')
```
Attribute: A variable that is bound to an instance of a class. Attributes hold data related to the object.
```bash
  my_car.make  # 'Toyota'
```
Inheritance: A mechanism where one class (child or subclass) inherits attributes and methods from another class (parent or superclass).
```bash
  class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size
```
Encapsulation: The bundling of data and methods that operate on the data within one unit (class). It restricts direct access to some of the object's components, which is known as data hiding.
```bash
class Car:
    def __init__(self, make, model, year):
        self._make = make  # protected attribute
        self.__model = model  # private attribute
        self.year = year
```
Polymorphism: The ability to present the same interface for different underlying data types. It allows objects of different classes to be treated as objects of a common superclass.
```bash
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def make_animal_speak(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()

make_animal_speak(dog)  # Outputs: Woof!
make_animal_speak(cat)  # Outputs: Meow!

```
Abstraction: The concept of hiding the complex implementation details and showing only the necessary features of an object. It is achieved through abstract classes and interfaces.
```bash
    from abc import ABC, abstractmethod

    class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    class Dog(Animal):
    def sound(self):
        return "Woof!"

```

A constructor in Python is a special method that is automatically called when an object of a class is created. It is used to initialize the object's attributes and perform any setup necessary for the object. In Python, the constructor method is defined by the __init__ method.

Here’s a more detailed explanation:
Constructor (__init__ Method)
Definition: The __init__ method is a special method in Python classes. It is called when an instance (object) of the class is created. The purpose of the __init__ method is to initialize the object's attributes with the values provided during object creation.

Syntax:
```bash
class ClassName:
    def __init__(self, parameters):
        # Initialization code
        self.attribute1 = value1
        self.attribute2 = value2
        # more initialization code
```
Example:
```bash
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

my_car = Car('Toyota', 'Corolla', 2020)
print(my_car.make)  # Outputs: Toyota
print(my_car.model)  # Outputs: Corolla
print(my_car.year)  # Outputs: 2020
```

The Car class has a constructor method __init__ that takes three parameters: make, model, and year.
When my_car = Car('Toyota', 'Corolla', 2020) is executed, the __init__ method is called with the arguments 'Toyota', 'Corolla', and 2020.
Inside the __init__ method, the object's attributes self.make, self.model, and self.year are initialized with these values.
Key Points:
Automatic Invocation: The __init__ method is automatically called when a new object of the class is created.
Initialization: It is mainly used to initialize the attributes of the class with the provided values or with default values.
Self Parameter: The first parameter of the __init__ method is always self, which refers to the instance being created. This allows the method to access and set the attributes of the object.
By using constructors, you can ensure that every object of the class starts with a well-defined state, making your code more robust and easier to understand.