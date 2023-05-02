from algemene_functies import mijn_functie_2

# Lesson 8 question 5
def aanbieding_1(smaak, prijs, korting):
   
    a = prijs / korting  
    a = abs(a / 100 - prijs)
   
    result = (F"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {a:.2f} euro.")
    return result

# print()
# print( aanbieding_1("aardbei", 4, 0.1) )
# print()


# Lesson 8 question 6 and 7
def inkomsten_totaal(inkomsten = [], btw = float):
  a = 0
  b = 0
   
  for x in inkomsten:
      a =  a + x
  #endfor 
      b = a * btw  
  return (f"Het totaal van alle inkomsten van deze week is {a} euro, waarover {b} euro btw betaald dient te worden.")

# list_inkomsten = [220, 430, 125, 160, 205, 90, 345]
# print( inkomsten_totaal(list_inkomsten, 0.09) )
# print()


# Lesson 8 question 8
def laag_en_hoog(mijn_lijst = []):
    thislist = [0, 0]

    thislist[0] = max(mijn_lijst) 
    thislist[1] = min(mijn_lijst)
    return thislist 

# list_laag_en_hoog = [220, 430, 125, 160, 205, 90, 345]
# print( laag_en_hoog(list_laag_en_hoog) )  # '\n' 
# print()


# Lesson 8 question 9 and 10
def gemiddelde(mijn_lijst = []):
    length = len(mijn_lijst) 
    sum = sum(mijn_lijst) 
    average = sum / length 
    return (f"De gemiddelde inkomsten deze week zijn {str(average)} euro.")

# list_gemiddelde = [220, 430, 125, 160, 205, 90, 345]    
# print( gemiddelde(list_gemiddelde) )
# print()


# lesson 8 question 11
def meervoudig(invoer_lijst = []):
    return laag_en_hoog(invoer_lijst) 

# list_meervoudig = [10,5,3,2,1,2,9]
# print( meervoudig(list_meervoudig) ) 


# lesson 8 question 12 
def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer






