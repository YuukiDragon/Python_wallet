class Portefeuille:

    def __init__(self, valeur, devise, valeurd, devised):
        self.valeur = valeur
        self.devise = devise
        self.valeurd = valeurd
        self.devised = devised

    # self.valeure = valeure
    # self.devisee = devisee

    # Fonction Ajout d'argent euro
    def ajouter(self, valeur, devise):
        if self.devise == devise:
            self.valeur = self.valeur + valeur
        else:
            print("Erreur de devise")

    # Fonction retrait argent euro
    def retirer(self, valeur, devise):
        if self.devise == devise:
            self.valeur = self.valeur - valeur
        else:
            print("Erreur de devise")

    # Fonction Ajout d'argent dollar
    def ajouterd(self, valeurd, devised):
        if self.devised == devised:
            self.valeurd = self.valeurd + valeurd
        else:
            print("Erreur de devise")

    # Fonction retrait argent dollar
    def retirerd(self, valeurd, devised):
        if self.devised == devised:
            self.valeurd = self.valeurd - valeurd
        else:
            print("Erreur de devise")

    def __str__(self):
        return "Votre portefeuille contient {} {} et {} {}.".format(self.valeur, self.devise, self.valeurd, self.devised)


# Creation porte monnaie
Portefeuille1 = Portefeuille(1000, "Euros", 250, "Dollar")

# Ajout d'argent
Portefeuille1.ajouter(int(input("Ajouter le montant souhaité")), "Euros")

# Retrait D'argent
Portefeuille1.retirer(int(input("Retirer le montant souhaité")), "Euros")

# Ajout d'argent
Portefeuille1.ajouterd(int(input("Ajouter le montant souhaité")), "Dollar")

# Retrait D'argent
Portefeuille1.retirerd(int(input("Retirer le montant souhaité")), "Dollar")

# Affichage du porte monnaie
print(Portefeuille1)

