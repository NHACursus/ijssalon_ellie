
def decoreer( tekst = "" ):
   # tekst = "header"
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()
    return None


def fooi_pp(bedrag = int, personen = int):
 
  try:         
        bedrag_pp = bedrag / personen    
  except:         
        bedrag_pp = "??"    
  return f"Het bedrag per persoon is {bedrag_pp} euro"
 
''' 
 b = int(input("Welk bedrag zit er in de fooienpot? "))
 p = int(input("Over hoeveel mensen moet de pot verdeeld worden? "))
 print( fooi_pp(b, p) )
'''

# Lesson 10 question 1
def onderstreep(tekst = ""):
      uit = []
      uit.append(tekst)
      uit.append(len(tekst) * "=")   
      return uit

# 10.11 homework assignments question 1
def som(dict):
  i = 0
  for item in dict:  
       i = i + (dict[item])
  return i

'''
def som(dict):
     i = 0
     for k, v in dict.items():  
      i = i + v

      return i
     
'''
