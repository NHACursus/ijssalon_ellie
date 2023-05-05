


def presenteer(dict, totaal):
    i = 0
    for item, v in dict.items():  
       print(f" {item} : {v} euro")
       # print ( dict[item] )
       # print (str((dict[item])) + (" euro"))
    pass

    print("==========================")
    print(f"totaal : {totaal}  euro")
 
    return 0


mijn_dict = {'vis' : 10, 'vlees': 25, 'overig' : 15}
totaal = 50

# presenteer(mijn_dict, totaal)