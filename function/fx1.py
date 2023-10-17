def cal1(name,score):
    if score >= 90:
        print('ชื่อ' + name + ' '+ 'gade A')
    elif score>= 80:
        print('ชื่อ' + name + ' '+ 'gade B') 
    elif score>= 70:
        print('ชื่อ' + name + ' '+ 'gade C')  
    elif score>= 60:
        print('ชื่อ' + name + ' '+ 'gade D')  
    else:
        print('ชื่อ' +' '+ name + ' '+'สอบตก')   
        
def cal2(name,score):
    if score >= 90:
        # result = 'ชื่อ' + name + ' '+ 'gade A'
        #  result = 'ชื่อ  {Name} gade A'.format(Name=name)
        # result = 'ชื่อ  {} ได้คะแนน {} = gade A'.format(name,score)
        result = 'ชื่อ  {1} ได้คะแนน {0} = gade A'.format(score,name)
    elif score>= 80:
        result = 'ชื่อ  {Name} gade B'.format(Name=name) 
    elif score>= 70:
        result = 'ชื่อ  {Name} gade C'.format(Name=name)
    elif score>= 60:
        result =  'ชื่อ  {Name} gade D'.format(Name=name)
    else:
        result =  'ชื่อ  {Name} สอบตก'.format(Name=name)
        
    return result                     