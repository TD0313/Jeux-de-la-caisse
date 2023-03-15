# Recolter une valeur porte monnaie
wallet = int(input("Inserer une somme :"))
print ("Sur votre compte en banque vous avez :",wallet,"euros")

# crer un produit
produit = 50
print ("Le produit vaut",produit,"euros")

# Enlever le prix du produit du wallet
wallet = wallet - produit

if wallet > produit :
    print ("Produit acheté")
    print ("Il vous reste",wallet,"euros")
else :
    print ("Vous n'avez pas assez d'argent")
