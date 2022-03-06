from Vehicle import Vehicle

class Airplane(Vehicle):
#kelas yang digunakan untuk mengimplementasikan Airplane
#atribut Airplane
	
    type = ""       #type Airplane
    WingsLength = 0    #WingsLength
    age = 0		#price
	
    def __init__(self, type ="", WingsLength = 0, age = 0):
	#costructor
        self.type = type
        self.WingsLength = WingsLength
        self.age = age
	
	  #mengeset nilai type
    def settype(self, type):
        self.type = type
	
	  #mengeset nilai WingsLength
    def setWingsLength(self, WingsLength):
        self.WingsLength = WingsLength
	
	  #mengeset nilai price
    def setage(self, age):
        self.age = age
     
	  #mengembalikan nilai type
    def gettype(self):
        return self.type
	
	  #mengembalikan nilai WingsLength
    def getWingsLength(self):
        return self.WingsLength

	  #mengembalikan nilai price
    def getage(self):
        return self.age
    
    def move(self):
        print("The " + self.namevehicle + " Can Moving.")

	
	