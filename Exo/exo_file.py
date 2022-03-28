print("Hello")
dollar = 1000
euro = 95
yen = 96401
portemonnaie = "vous avez " +str(dollar) +" dollars, " + str(euro) +" euros, "+"et " + str(yen) + ' yens.'

print(str(portemonnaie))
print("-------------------------------------------------------------------------------------------")
dollar = dollar + 10
print("vous avez recu 10 dollars")
euro = euro + 50
print("vous avez recu 50 euros")
yen = yen - 5000
print("vous avez perdu 5000 yens")
portemonnaie = "vous avez " +str(dollar) +" dollar, " + str(euro) +" euro, "+"et " + str(yen) + ' yen.'
print(str(portemonnaie))
print("-------------------------------------------------------------------------------------------")
if euro <= 0:
    print('vous etes ruiné !Ils vous restent aucun euro.')
else:
    print ('ils vous restent de l\'argent dans le portemonnaie euro.')
if yen <= 0:
    print('vous etes ruiné ! Ils vous restent aucun yen.')
else:
    print('ils vous restent de l\'argent dans le portemonnaie yen.')
if dollar <= 0:
    print('vous etes ruiné ! Ils vous restent aucun dollar.')
else:
    print ('ils vous restent de l\'argent dans le portemonnaie dollar.')
print("-------------------------------------------------------------------------------------------")
#reponseyen = input("Voulez-vous retirer des yen ? [oui/non] ")
#reponseyen = reponseyen.strip().lower()
#if reponseyen.startswith('oui'):
 #   print("OK. Sans problème. Combien souhaitez vous retirer ? ")
#  retraityen = input()
#else :reponseyen.startswith('non')
#print("OK. Sans problème")
#print("Au revoir")
#yen2 = yen - retraityen
#portemonnaie = "vous avez "+ str(yen2) + ' yen.'
#print(str(portemonnaie))










#comptage du portefeuille
#if euro <= 0:
 #   print('vous etes ruiné !Ils vous restent aucun euro.')
#else:
 #   print ('ils vous restent de l\'argent dans le portemonnaie euro.')
#if yen <= 0:
 #   print('vous etes ruiné ! Ils vous restent aucun yen.')
#else:
 #   print('ils vous restent de l\'argent dans le portemonnaie yen.')
#if dollar <= 0:
 #   print('vous etes ruiné ! Ils vous restent aucun dollar.')
#else:
 #   print ('ils vous restent de l\'argent dans le portemonnaie dollar.')
#print("-------------------------------------------------------------------------------------------")



#def = nom fonction comme un verbe