class ZooEntity():
    def __init__(self,name):
        self.name= name
        
    def Display(self):
        print 'Name : ',self.name
        
class Human(ZooEntity):
    def __init__(self,name,age):
        ZooEntity.__init__(self,name)
        self.age =age
        
    def Display(self):
        ZooEntity.Display(self)
        print 'Age: ',self.age

class Workers(Human):
    def __init__(self,name, age,job_type,salary):
        Human.__init__(self, name, age)
        self.job_type=job_type
        self.salary=salary
    def Display(self):
        Human.Display(self)
        print 'Job: ',self.job_type
        print 'salary: ',self.salary
class Visitors(Human):
    def __init__(self,name,age,purpose):
        Human.__init__(self, name, age)
        self.purpose=purpose
    def Display(self):
        Human.Display(self)
        print 'Purpose of Visit: ',self.purpose
        
class Animals(ZooEntity):
    def __init__(self,name,age,gender,origin,habitat,feed):
        ZooEntity.__init__(self, name)
        self.age=age
        self.gender=gender
        self.origin=origin
        self.habitat=habitat
        self.feed=feed
        
    def Display(self):
        ZooEntity.Display(self)
        print 'Age:' ,self.age
        print 'Gender: ',self.gender
        print 'Origin: ',self.origin
        print 'Habitat: ',self.habitat
        print 'Food: ',self.feed
        
class Mammals(Animals):
    def __init__(self,name,age,gender,origin,habitat,feed,vertebrates):
        Animals.__init__(self,name,age,gender,origin,habitat,feed)
        self.vertebrates=vertebrates
    def Display(self):
        Animals.Display(self)
        print 'Vertebrate: ',self.vertebrates
        
        
       
class Asset(ZooEntity):
    def __init__(self,name,purpose,number_item):
        ZooEntity.__init__(self,name)
        self.purpose=purpose
        self.number_item=number_item
    def Display(self):
        ZooEntity.Display(self)
        print 'Purpose: ',self.purpose
        print 'Number:',self.number_item
        
import datetime
class Vehicles(Asset):
 
    def __init__(self,name,purpose,number_item,date_bought=0,date_serviced=0):
        Asset.__init__(self, name, purpose, number_item)
        self.date_bought=date_bought
        self.date_serviced=date_serviced
    
    def Display(self):
        Asset.Display(self)
        print 'Date Purchased: ',self.date_bought
        print 'Last Serviced Date: ',self.date_serviced 
               
class Infrastructure(Asset):
    def __init__(self,name,purpose,number_item,date_built):
        Asset.__init__(self, name, purpose, number_item)
        self.date_built=date_built
        
    def __str__(self):
        Asset.Display(self)
        return self.date_built
    
class Equipments(Asset):
    def __init__(self,name,purpose,number_item,date_bought=0):
        Asset.__init__(self, name, purpose, number_item)
        self.date_bought=date_bought
        
    def __str__(self):
        Asset.Display(self)
        return self.date_bought


#data

zooVistor = Visitors('moses',12,'School Trip')
print zooVistor

print

Zoo=ZooEntity("Accra")
Zoo.Display()
print

worker=Workers("Mr Kwame",35,"Manager",1000)
worker.Display()
print

vistor=Visitors("Jean Can",15,"School Trip")
vistor.Display()

print

animal=Mammals("Loin",5,"Male","East Africa","Land","Meat","Yes")
animal.Display()
print

pen1=Infrastructure("Lion Pen","House Lion A",1,datetime.date(2012,1,1,))
pen1.Display()




