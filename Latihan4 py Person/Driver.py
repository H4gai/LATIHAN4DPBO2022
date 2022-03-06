from Person import Person
from Job import Job

class Driver(Person, Job):
#kelas yang digunakan untuk mengimplementasikan Driver
#atribut Driver
	
    vehicletype = ""       #vehicletype Ship
    active = 0    #active
    lisenceid = 0		#price

    def __init__(self, vehicletype ="", active = 0, lisenceid = 0):
	#costructor
        self.vehicletype = vehicletype
        self.active = active
        self.lisenceid = lisenceid
        
	  #mengeset nilai lisenceid
    def setlisenceid(self, lisenceid):
        self.lisenceid = lisenceid	
    
	  #mengeset nilai vehicletype
    def setvehicletype(self, vehicletype):
        self.vehicletype = vehicletype
	
	  #mengeset nilai active
    def setactive(self, active):
        self.active = active
     
    #mengembalikan nilai vehicletype
    def getvehicletype(self):
        return self.vehicletype
	
	  #mengembalikan nilai active
    def getactive(self):
        return self.active

	  #mengembalikan nilai price
    def getlisenceid(self):
      return self.lisenceid
    
    def move(self):
        print(self.nameperson + " was sleeping.")
        
    #menampilkan data
    def Display(self):
        print("Lisence ID       : " + str(self.lisenceid))
        print("Active Until     : " + str(self.active))
        print("Vehicle Type     : " + str(self.vehicletype))
        