class Car:
    def __init__(self,namecar,color,type,limitspeed=200) :
        self.namecar = namecar
        self.color = color
        self.type = type
        self.limitspeed = limitspeed
        
    def getdata(self) :  
        print(f'ยี่ห้อรถคือ  {self.namecar}  สี {self.color} รุ่น {self.type} ความเร็วสูงสุด {self.limitspeed}') 
        
        
        
car1 = Car('ford','red','mustang',250)   
car1.getdata()    