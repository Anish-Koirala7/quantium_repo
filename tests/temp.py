class Car():
    def __init__(self, model: str, brand: str):
     
        self.model=model                            
        self.brand=brand
    # @property
    # def set_property(self, model, brand, no_wheels):
    #      self.wheels = no_wheels
        
    def run_engine(self):
        print("The car model is" + self.model)
        print("Engine is starting")


    def move_car(self):  
        print("Moving the car")


car1=Car("T24-10","tesla") #instance 
car2=Car("M24-9912","Mercedes")
car3= Car(1234, "tesla")

"""Car model, brand



car object----> (car_instance, t24, tesla ---> car1
car1.run_engine()
run_engine(car1)
 print("The car model is" + car1.model)


"""

print(car1.model)
# car1.set_property()
car1.run_engine() # car1.run_engine(car1)
car1.move_car()
car3.run_engine()

