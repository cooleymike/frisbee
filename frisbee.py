class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        if self.weight > 29:
            print(self.name, 'says "WOOF WOOF"')
        else:
            print(self.name, 'says "woof woof"')

    def human_years(self):
        years = self.age * 7
        return years

    def __str__(self):
        return "I'm a dog named " + self.name

class ServiceDog(Dog):
    def __init__(self, name, age, weight, handler):
        Dog.__init__(self, name, age, weight)
        self.handler = handler
        self.is_working = True

    def walk(self):
        print(self.name, "is helping the handler", self.handler, "walk")

    def bark(self):
        if self.is_working:
            print(self.name, "I can't bark right now I'm working")
        else:
            Dog.bark(self)

class Frisbee:
    def __init__(self, color):
        self.color = color

        def __str__(self):
            return "I'm a " + self.color + "frisbee"



class FrisbeeDog(Dog):
    def __init__(self, name, age, weight):
        Dog.__init__(self, name, age, weight)
        self.frisbee = None

        def bark(self):
            if self.frisbee:
                print(self.name, "I can't right now i have a frisbee in my mouth")
            else:
                Dog.bark(self)

    def catch(self, frisbee):
        self.frisbee = frisbee
        print(self.name, "caught a", frisbee.color, "frisbee")


    def give(self):
        if self.frisbee != None:
            frisbee = self.frisbee
            self.frisbee = None
            print(self.name, "gives back", frisbee.color, "frisbee")
            return frisbee
        else:
            print(self.name, "doesn't have a ", frisbee.color, "Frisbee")
            return None

    def __str__(self):
        str= "I'm a dog named " + self.name
        if self.name != None:
            str = str + " and i have a frisbee"
        return str
            
        
#dog names can be changed to suit your needs
buddy = FrisbeeDog("Buddy", 4, 27)
rody = ServiceDog("Rody", 8, 39, "Joseph")
codie = Dog('Codie', 12, 33)
freddy = Dog('Freddie', 10, 40)
vinny = Dog('Vinny', 9, 28)
print(codie), codie.bark()
print(freddy), freddy.bark()
print(vinny), vinny.bark()
print(rody), rody.bark()
print(buddy), buddy.bark()
print(Frisbee)
