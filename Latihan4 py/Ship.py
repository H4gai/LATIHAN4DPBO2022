from Vehicle import Vehicle

class Ship(Vehicle):
#kelas yang digunakan untuk mengimplementasikan Ship
#atribut Ship
	
    type = ""       #type Ship
    countryOfManufacture = ""    #countryOfManufacture
    age = 0		#price

    def __init__(self, type ="", countryOfManufacture = "", age = 0):
	#costructor
        self.type = type
        self.countryOfManufacture = countryOfManufacture
        self.age = age
        
	  #mengeset nilai age
    def setage(self, age):
        self.age = age	
    
	  #mengeset nilai type
    def settype(self, type):
        self.type = type
	
	  #mengeset nilai countryOfManufacture
    def setcountryOfManufacture(self, countryOfManufacture):
        self.countryOfManufacture = countryOfManufacture
     
    #mengembalikan nilai type
    def gettype(self):
        return self.type
	
	  #mengembalikan nilai countryOfManufacture
    def getcountryOfManufacture(self):
        return self.countryOfManufacture

	  #mengembalikan nilai price
    def getage(self):
      return self.age
    
    def move(self):
        print("The " + self.namevehicle + " Can Moving.")