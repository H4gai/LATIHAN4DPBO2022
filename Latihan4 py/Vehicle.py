class Vehicle():
#kelas yang digunakan untuk mengimplementasikan vehicle
#atribut vehicle
	
    namevehicle = ""
    fueltype = ""   	#type disk
    maxpassengers = 0   #maxpassengers
    
    def __init__(self, namevehicle= "", fueltype ="", maxpassengers = 0):
    #costructor
        self.namevehicle = namevehicle
        self.fueltype = fueltype
        self.maxpassengers = maxpassengers
	
	#mengeset nilai fueltype
    def setfueltype(self, fueltype):
        self.fueltype = fueltype
    
    #mengeset nilai namevehicle
    def setname(self, namevehicle):
        self.namevehicle = namevehicle
	
	#mengeset nilai maxpassengers
    def setmaxpassengers(self, maxpassengers):
        self.maxpassengers = maxpassengers
	
    #mengembalikan nilai namevehicle
    def getname(self):
        return self.namevehicle
     
	#mengembalikan nilai fueltype
    def getfueltype(self):
        return self.fueltype
	
	#mengembalikan nilai maxpassengers
    def getmaxpassengers(self):
        return self.maxpassengers	