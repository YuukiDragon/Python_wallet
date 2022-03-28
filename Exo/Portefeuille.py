class Portefeuille:

    def __init__(self, valeur, devise):
        self.valeur = valeur
        self.devise = devise

#Fonction Ajout d'argent
    def ajouter (self, valeur, devise):
        if self.devise==devise:
            self.valeur=self.valeur+valeur
        else:
            print("Erreur de devise")

#Fonction retrait argent
    def retirer (self, valeur, devise):
        if self.devise==devise:
            self.valeur=self.valeur-valeur
        else:
            print("Erreur de devise")

    def __str__(self):
        return "La valeur est égale à {} et la devise est égale à {}.".format(self.valeur, self.devise)

#Creation porte monnaie
Portefeuille1 = Portefeuille(1000,"Euros")


# Ajout d'argent
Portefeuille1.ajouter(int(input("Ajouter le montant souhaité")),"Euros")

# Retrait D'argent
Portefeuille1.retirer(int(input("Retirer le montant souhaité")),"Euros")

#Affichage du porte monnaie
print(Portefeuille1)