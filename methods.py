#methods are functions that are defined inside a class
class Car:
    def __init__(self,carname):
        self.name=carname

    #Mutator method
    def set_make(self,carname):
        self.name=carname

    #Accessor method
    def get_make(self):
        return self.name
    
mycar=Car('Ford')
#get current value
print(mycar.get_make())
#value modified
mycar.set_make('Suzuki')
print(mycar.get_make())
