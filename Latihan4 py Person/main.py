from Person import Person
from Job import Job
from Driver import Driver

#instalasi Objek dan mengisi data menggunakan setter
#get nilai yang ada pada objek data keseluruhan
#Person
print("--- data Person ---")
print("-----------------------------")
d1 = Person()
d1.setname("Benjamin")
d1.setgender("Male")
d1.setNIK(10001)
d1.Displayperson()
print("=====================")

d2 = Person()
d2.setname("Thomas")
d2.setgender("Male")
d2.setNIK(10012)
d2.Displayperson()
print("=====================")

d3 = Person()
d3.setname("Albertt")
d3.setgender("Male")
d3.setNIK(10123)
d3.Displayperson()
print("=====================")

d4 = Person()
d4.setname("Vior")
d4.setgender("Female")
d4.setNIK(11234)
d4.Displayperson()
print("=====================")

d5 = Person()
d5.setname("Gabriela")
d5.setgender("Female")
d5.setNIK(12345)
d5.Displayperson()
print("=====================")


print("")
print("--- data Job ---")
print("-----------------------------")

#Job
s1 = Job()
s1.setconame("Onic Esports")
s1.setNIP("40001")
s1.setposition("Brand Ambassador")
s1.Displayjob()
print("=====================")

s2 = Job()
s2.setconame("Evos Esport")
s2.setposition("Owner")
s2.setNIP(43001)
s2.Displayjob()
print("=====================")

s3 = Job()
s3.setconame("RRQ Esport")
s3.setposition("Head Manager")
s3.setNIP(43201)
s3.Displayjob()
print("=====================")


s4 = Job()
s4.setconame("Bigetron Esport")
s4.setposition("Player talent")
s4.setNIP(43211)
s4.Displayjob()
print("=====================")

s5 = Job()
s5.setconame("Alter Ego")
s5.setposition("Coach")
s5.setNIP(43210)
s5.Displayjob()
print("=====================")

print("")
print("--- data Driver ---")
print("-----------------------------")
a1 = Driver()
a1.setname("XINNN")
a1.setgender("Male")
a1.setNIK(10009)
a1.setconame("Akulaku")
a1.setNIP("40009")
a1.setposition("Staff")
a1.setlisenceid(111)
a1.setactive(2023)
a1.setvehicletype("bus")
a1.Displayperson()
a1.Displayjob()
a1.Display()
print("=====================")

a2 = Driver()
a2.setname("REKT")
a2.setgender("Male")
a2.setNIK(10008)
a2.setconame("GOTAKSI")
a2.setNIP("40008")
a2.setposition("Senior Staff")
a2.setlisenceid(222)
a2.setactive(2024)
a2.setvehicletype("CAR")
a2.Displayperson()
a2.Displayjob()
a2.Display()
print("=====================")

a3 = Driver()
a3.setname("Vivian")
a3.setgender("Female")
a3.setNIK(10007)
a3.setconame("Grak")
a3.setNIP("40007")
a3.setposition("Junior Staff")
a3.setlisenceid(333)
a3.setactive(2022)
a3.setvehicletype("Motorcycle")
a3.Displayperson()
a3.Displayjob()
a3.Display()
print("=====================")

a4 = Driver()
a4.setname("Lemon")
a4.setgender("Male")
a4.setNIK(10006)
a4.setconame("Anteraja")
a4.setNIP("40005")
a4.setposition("manager")
a4.setlisenceid(444)
a4.setactive(2025)
a4.setvehicletype("Airplane")
a4.Displayperson()
a4.Displayjob()
a4.Display()
print("=====================")

a5 = Driver()
a5.setname("Fanny")
a5.setgender("Female")
a5.setNIK(10002)
a5.setconame("Jajalanan")
a5.setNIP("40003")
a5.setposition("Owner")
a5.setlisenceid(555)
a5.setactive(2024)
a5.setvehicletype("Ship")
a5.Displayperson()
a5.Displayjob()
a5.Display()
print("=====================")













