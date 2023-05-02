# 7.15 homework assignments question 1

from helper import decoreer

def print_aanbieding():

   # question 2

   prijzen = {
      "vanille"   : 3,    # I had to adjust this, otherwise I did not get the correct values as intended for the lesson material
      "aardbei"   : 4,
      "chocolade" : 5
   }


   # question 3
   aanbieding = prijzen["vanille"] * 0.8 
   reclame_tekst = (f"Vandaag in de aanbieding: vanille-ijs, 1 liter – slechts € {aanbieding}.")
   # print(reclame_tekst) 


   # question 5
   reclame_tekst2 = reclame_tekst[:63]
   # print(reclame_tekst2) 


   # question 6
   reclame_tekst3 = reclame_tekst2.upper()
   # print(reclame_tekst3)


   # question 7
   reclametekst4 = reclame_tekst3.split(" ")
   # print(reclametekst4)


   # question 8, 9, 10 
   for el in reclametekst4:  
      if 5 < len(el):  
         print(el.lower())
      else:   print(el) 

decoreer("Aanbieding")
 
print_aanbieding()




