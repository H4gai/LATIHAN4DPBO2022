class Job():
#kelas yang digunakan untuk mengimplementasikan job
#atribut job
	
    companyname = ""
    position = ""   	#type disk
    NIP = 0   #NIP
    
    def __init__(self, companyname= "", position ="", NIP = 0):
    #costructor
        self.companyname = companyname
        self.position = position
        self.NIP = NIP
	
	#mengeset nilai position
    def setposition(self, position):
        self.position = position
    
    #mengeset nilai companyname
    def setconame(self, companyname):
        self.companyname = companyname
	
	#mengeset nilai NIP
    def setNIP(self, NIP):
        self.NIP = NIP
	
    #mengembalikan nilai companyname
    def getconame(self):
        return self.companyname
     
	#mengembalikan nilai position
    def getposition(self):
        return self.position
	
	#mengembalikan nilai NIP
    def getNIP(self):
        return self.NIP	
        
    #menampilkan data
    def Displayjob(self):
        print("Company Name     : " + str(self.companyname))
        print("NIP              : " + str(self.NIP))
        print("Position         : " + str(self.position))
        