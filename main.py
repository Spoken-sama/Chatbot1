from fonction_Yrieix import *


speeches = ["Nomination_Chirac1.txt", "Nomination_Chirac2.txt", "Nomination_Giscard dEstaing.txt",
            "Nomination_Hollande.txt", "Nomination_Macron.txt", "Nomination_Mitterrand1.txt",
            "Nomination_Mitterrand2.txt", "Nomination_Sarkozy.txt"]

last_name = []

for i in speeches :
    last_name.append(extract_name_president(i))


from fonctions_Benjamin import *
full_name = associating_names(last_name)
for i in full_name :
    print(i)