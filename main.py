from fonction_Yrieix import *
from fonctions_Benjamin import *

speeches = ["Nomination_Chirac1.txt", "Nomination_Chirac2.txt", "Nomination_Giscard dEstaing.txt",
            "Nomination_Hollande.txt", "Nomination_Macron.txt", "Nomination_Mitterrand1.txt",
            "Nomination_Mitterrand2.txt", "Nomination_Sarkozy.txt"]

cleaned_speeches=["Cleaned_Nomination_Chirac1.txt","Cleaned_Nomination_Chirac2.txt","Cleaned_Nomination_Giscard dEstaing.txt","Cleaned_Nomination_Hollande.txt","Cleaned_Nomination_Macron.txt","Cleaned_Nomination_Mitterrand1.txt","Cleaned_Nomination_Mitterrand2.txt","Cleaned_Nomination_Sarkozy.txt"]

last_name = []

for i in speeches:
    last_name.append(extract_name_president(i))

full_name = associating_names(last_name)
for i in full_name:
    print(i)

if __name__ == "__main__":
    input_folder = "speeches"
    output_folder = "cleaned"

    convert_to_lowercase_and_save(input_folder, output_folder)

for i in cleaned_speeches:
    remove_ponctuation(i)

print("Conversion to lowercase and saving completed.")

for i in cleaned_speeches:
    occurrence(i)

total =7241