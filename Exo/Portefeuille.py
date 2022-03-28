class Portefeuille:

    def __init__(self, valeur, devise):
        self.valeur = valeur
        self.devise = devise

    def ajouter (self, valeur, devise):
        if self.devise==devise:
            self.valeur=self.valeur+valeur
        else:
            print("Erreur de devise")

    def __str__(self):
        return "La valeur est égale à {} et la devise est égale à {}.".format(self.valeur, self.devise)

#Creation porte monnaie
Portefeuille1 = Portefeuille(100,"Euros")


# Ajout d'argent
Portefeuille1.ajouter(int(input("Ajouter le montant souhaité")),"Euros")

#Affichage du porte monnaie
print(Portefeuille1)