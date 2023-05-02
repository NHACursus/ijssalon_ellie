# 8.12 homework assignments


# Lesson 8 question 2
def mijn_functie_1(int_a):
     int_a = int_a * int_a
     return int_a
 
# print(mijn_functie_1(12))


# Lesson 8 question 3
def mijn_functie_2(float_a):
   thislist = [0, 0, 0, 0]
   txt = str(float_a)
   x = txt.split('.', 2)
   a = int(x[0])
   b = int(x[1])
   
   if len(str(a)) > 2:
       b = b * 10

   thislist[0] = int(a + b)
   thislist[1] = int(a - b)
   thislist[2] = int(a * b)
   thislist[3] = int(a / b) 
   return thislist 

# print( mijn_functie_2((100.20)) )

