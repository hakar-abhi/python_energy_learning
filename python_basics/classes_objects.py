##                          Classes & Objects                         ##

class Turbine:
    category = "Turbine"

    @classmethod
    def get_category(cls):
        return cls.category

    @staticmethod
    def kw_to_mw(value):
        return value/1000

    @property
    def power_ratio(self):
        return self.power/self.rated_power
        
    def __init__(self,name,rated_power,actual_power,location):
        if rated_power <= 0:
            raise ValueError("Rated power can not be negative")
        self.name = name
        self.rated_power = rated_power
        self.power = actual_power
        self.location = location


    @property
    def power(self):
        return self._actual_power

    @power.setter
    def power(self,new_power):
        if new_power < 0:
            raise ValueError("Power can not be negative")
        self._actual_power = new_power

    def __str__(self):
        return f"Name: {self.name}, Power: {self.power} kW"
    # def capacity_factor(self):
    #     return self.actual_power/self.rated_power
    # def update_power(self,new_power):
        # if new_power < 0:
        #     raise ValueError("Power can not be negative")
        
        # self.actual_power = new_power
        # return self.actual_power
    def status(self):
        if self.power == 0:
            return "Stopped"
        elif self.power < self.rated_power:
            return "Running"
        elif self.power == self.rated_power:
            return "At rated power"
        else:
            return "Above rated power"
        
    def capacity_percentage(self):
        return (self.power/self.rated_power)*100

    def has_higher_power_than(self,other):
        if self.power > other.power:
            return True
        else:
            return False
    def has_higher_capacity_percentage_than(self,other):
        return self.capacity_percentage() > other.capacity_percentage()

    def summary(self):
        return(f"Turbine {self.name} | Rated: {self.rated_power} | Actual: {self.power} | Status: {self.status()}")
    
    def location_summary(self):
        return f"Turbine {self.name} is located in {self.location.summary()}"
# t1 = Turbine("T1", 3000, 1500)

# print(t1.power)

# t1.power = 1800
# print(t1.power)


# try:

#     t1.power = -100
# except ValueError as error:
#     print(error)



# print(t1.has_higher_power_than(t2))
# print(t2.has_higher_power_than(t1))
# print()
# print(t1.has_higher_capacity_percentage_than(t2))
# print(t2.has_higher_capacity_percentage_than(t1))
# print()
# print(t1.category)
# print(t2.category)
# print(Turbine.category)


##                                   Inheritance                         ##

# class WindTurbine(Turbine):
#     def __init__(self,name,rated_power,actual_power,blade_length):
#         super().__init__(name,rated_power,actual_power)
#         self.blade_length = blade_length
#     def summary(self):
#         result = super().summary()
#         result += f" | Blade length: {self.blade_length}"
#         return result




# wt1 = WindTurbine("WT1", 3000, 1500,65)

# print(wt1.name)
# print(wt1.status())
# print(wt1.capacity_percentage())
# print(wt1.blade_length)
# print(wt1.summary())

# class SolarPlant(Turbine):

#     def status(self):
#         if self.power == 0:
#             return "No generation"
#         if self.power < self.rated_power:
#             return "Gnerating"
#         if self.power == self.rated_power:
#             return "At maximum output"
#         else:
#             return "Above expected output"

# s1 = SolarPlant("S1",5000,2500)
# print(s1.status())
# print(s1.capacity_percentage())

# plants = [
#     Turbine("T1", 3000, 1500),
#     SolarPlant("S1", 5000, 2500)
# ]


class Location:
    def __init__(self,city,country):
        self.city = city
        self.country = country
    def summary(self):
        return f"{self.city}, {self.country}"

loc1 = Location("Berlin","Germany")
t1 = Turbine("T1",3000,1500,loc1)
# print(t1.location.city)
# print(t1.location.country)
# print(t1.location_summary())
    

# for plant in plants:
#     print(plant.name)
#     print(plant.status())
#     print(plant.capacity_percentage())

# for plant in plants:
#     if isinstance(plant,SolarPlant):
#         print("Solar object")
#     else:
#         print("Turbine object")
# print(isinstance(s1,Turbine))

# print(Turbine.get_category())
# print(t1.get_category())
# print(Turbine.kw_to_mw(1500))
# print(t1.kw_to_mw(2000))
# print(t1.power_ratio)

##                              Abstraction                          ##
from abc import ABC, abstractmethod

class EnergyAsset(ABC):

    def __init__(self,name,output):
        self.name = name
        self.output = output

    # @abstractmethod
    # def operate(self):
    #     pass

    @abstractmethod
    def get_output(self):
        pass

class SolarAsset(EnergyAsset):

    
    # def operate(self):
    #     return "Solar asset operating"

    def get_output(self):
        return self.output

class WindAsset(EnergyAsset):

    # def operate(self):
    #     return "Wind asset operating"

    def get_output(self):
        return self.output
    
assets = [WindAsset("Nordex",1500),
          SolarAsset("RWE",1800)
        ]
          

for asset in assets:
    print(asset.name)
    print(asset.get_output())
