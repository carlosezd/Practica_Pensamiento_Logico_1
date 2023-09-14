
s = 0
m = 0
h = 0
  
    
while h < 24:
    print(f'{h}:{m}:{s}')
    s += 1
    if s == 60:
        s = 0
        m += 1
    if m == 60:
        m = 0
        h += 1




    