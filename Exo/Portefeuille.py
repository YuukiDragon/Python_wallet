class Portefeuille:

    def __init__(self, valeur, devise):
        self.valeur = valeur
        self.devise = devise


#Creation porte monnaie
Portefeuille1 = Portefeuille(100,"Euros")


# Créer un porte-monnai
Portefeuille1.ajouter(int(input("Ajouter le montant souhaité")),"euros")
