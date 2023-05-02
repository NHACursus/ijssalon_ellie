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
 
  
b = int(input("Welk bedrag zit er in de fooienpot? "))
p = int(input("Over hoeveel mensen moet de pot verdeeld worden? "))

print( fooi_pp(b, p) )






'''
def tryparse(divide, by):
    try:
        return True, divide / by #string, base     #int(string, base=base)
    except ValueError:
        return False, None

i = 1
while i < 6:
  print(tryparse(0,i))
  i += 1
'''


# fruits = ["apple", "banana", "cherry"]
# for x > 10:
#  print(x)


#for i < 10
#print( tryparse(0, 1))    