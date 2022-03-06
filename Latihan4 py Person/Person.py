class Person():
#kelas yang digunakan untuk mengimplementasikan person
#atribut person
	
    nameperson = ""
    gender = ""   	#type disk
    NIK = 0   #NIK
    
    def __init__(self, nameperson= "", gender ="", NIK = 0):
    #costructor
        self.nameperson = nameperson
        self.gender = gender
        self.NIK = NIK
	
	#mengeset nilai gender
    def setgender(self, gender):
        self.gender = gender
    
    #mengeset nilai nameperson
    def setname(self, nameperson):
        self.nameperson = nameperson
	
	#mengeset nilai NIK
    def setNIK(self, NIK):
        self.NIK = NIK
	
    #mengembalikan nilai nameperson
    def getname(self):
        return self.nameperson
     
	#mengembalikan nilai gender
    def getgender(self):
        return self.gender
	
	#mengembalikan nilai NIK
    def getNIK(self):
        return self.NIK	
        
    #menampilkan data
    def Displayperson(self):
        print("Name             : " + str(self.nameperson))
        print("NIK              : " + str(self.NIK))
        print("Gender           : " + str(self.gender))
        