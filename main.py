pseudo = input("Pseudo ? ")
rm = int(input("Rang de maitrise ? "))
warframe = input("Waframe équipé ? ")
arme = input("Arme princial ? ")
credit = int(input("Credit ? "))
platines = int(input("platine ? "))
win_credit = int(input("Credit gagner lors de la mission ? "))
new_sold = win_credit + credit

print("=== PROFIL TENNO ===")
print(f"Opérateur : {pseudo} | Rang de maitrise : {rm} | Warframe équipé : {warframe} | Arme principal : {arme} | credit actuelle : {credit} | Platines : {platines} | Nouveau solde de credits : {new_sold}")



