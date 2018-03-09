import pickle
class CarRecord:
    def __init__(self):
        self.VehicleID = ""
        self.Registration = ""
        self.DateOfRegistration = None
        self.EngineSize = 0
        self.PurchasePrice = 0.0
ThisCar1 = CarRecord()
ThisCar2 = CarRecord()
ThisCar3 = CarRecord()
ThisCar4 = CarRecord()
ThisCar5 = CarRecord()
ThisCar1.EngineSize = 2500
ThisCar2.EngineSize = 2000
ThisCar3.EngineSize = 2300
ThisCar4.EngineSize = 2400
ThisCar5.EngineSize = 2100
ThisCar = [ThisCar1, ThisCar2, ThisCar3, ThisCar4, ThisCar5]
CarFile = open('Cars.DAT','wb')
for i in range(len(ThisCar)):
    pickle.dump(ThisCar[i],CarFile)
CarFile.close()

CarFile = open('Cars.DAT','rb')
Car = []
for i in range(5):
    Car.append(pickle.load(CarFile))
for i in range(5):
    print(Car[i].EngineSize)

CarFile.close()