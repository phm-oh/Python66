firstname = 'นายภาณุเมศ'
lastname = 'ชุมภูนท์'
age = 42
test = True
cars = ['ford','bmw','benz','volvo'] # array
mylist = ['apple',66,'phanumet'] #list
mydic = {
    'oh':6959,
    'jame':8560,
    'dev':5050,
    'mylist':[1,2,3,4]
}

print(type(firstname))
print(type(lastname))
print(type(age))
print(type(test))

print(firstname+" "+lastname+" อายุ "+str(age))
print(cars[0])
print(len(cars))  #ได้ใช้ในการนับบอท

#list
print(mylist[0])
mylist[1] = 99
print(mylist[1])
mylist.append('dexler')
print(mylist[3])
mylist.remove(99)
print(mylist)
    
for i in mylist:
    print(i)   
    
mylist2 = [1,4,6,8,7]   
mylist2.sort()  
print(mylist2)

mylist2.sort(reverse=True) 
print(mylist2)

mylist3 = ['ก','ว','ฝ','ม']
mylist3.sort()  
print(mylist3)


# Dictionary
print(type(mydic))
print(mydic)
print(mydic['oh'])

mydic['oh'] = 666
print(mydic['oh'])

# mydic['oh'] = mydic['oh']+500
mydic['oh'] += 500
print(mydic['oh'])



print(mydic.keys())
print(mydic.values())

for name,score in mydic.items():
    print(name,score)



print(mydic['mylist'])
print(mydic['mylist'][2])




