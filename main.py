from fonction_Yrieix import *
from fonctions_Benjamin import *

speeches = ["Nomination_Chirac1.txt", "Nomination_Chirac2.txt", "Nomination_Giscard dEstaing.txt",
            "Nomination_Hollande.txt", "Nomination_Macron.txt", "Nomination_Mitterrand1.txt",
            "Nomination_Mitterrand2.txt", "Nomination_Sarkozy.txt"]

cleaned_speeches = ["Cleaned_Nomination_Chirac1.txt", "Cleaned_Nomination_Chirac2.txt",
                    "Cleaned_Nomination_Giscard dEstaing.txt", "Cleaned_Nomination_Hollande.txt",
                    "Cleaned_Nomination_Macron.txt", "Cleaned_Nomination_Mitterrand1.txt",
                    "Cleaned_Nomination_Mitterrand2.txt", "Cleaned_Nomination_Sarkozy.txt"]

directory ='cleaned'

last_name = []

#Give last name
for i in speeches:
    last_name.append(extract_name_president(i))

#Associate Names
full_name = associating_names(last_name)
for i in full_name:
    print(i)

#Lower case
if __name__ == "__main__":
    input_folder = "speeches"
    output_folder = "cleaned"
    convert_to_lowercase_and_save(input_folder, output_folder)


#Remove ponctuation
for i in cleaned_speeches:
    remove_ponctuation(i)
print()
print("Conversion to lowercase and saving completed.")
print()


#TF
for i in cleaned_speeches:
    TF(i)

#IDF
IDF(directory)

#TF_IDF
TF_IDF(directory)
'''print(matrice_result)'''
'''print(TF_IDF_values)'''


#Features
matrice_result = TF_IDF(directory)

#Nonimportant
print(TF_IDF_nonimportant_value(matrice_result))

#Hightest value
print(TF_IDF_highest_value(matrice_result))

eco(directory)

print("They are",All_said(matrice_result))