import os
import string


def extract_name_president(name):
    president_name = name[11:]
    if ("1" in president_name) or ("2" in president_name):
        president_last_name = president_name[:-5]
    else:
        president_last_name = president_name[:-4]
    return president_last_name



def remove_ponctuation(input_file):
    os.chdir('Cleaned')

    p = string.punctuation

    with open(input_file,"r") as t :
        text = t.read()
        for char in p :
            text = text.replace(char, " ")
        with open(input_file,"w") as output :
            output.write(text)

    os.chdir('..')

def TF_IDF_nonimportant_value(dico):
    list_non_important_value = []
    for i in dico.items() :
        cpt = 0
        for j in i[1] :
            if j == 0.0 :
                cpt += 1
        if cpt == 8 :
            list_non_important_value.append(i[0])
    return list_non_important_value

def TF_IDF_highest_value(dico):
    word_highest = ""
    highest_value = 0
    for i in dico.items():
        for j in i[1]:
            if j > highest_value:
                highest_value = j
                word_highest = i[0]
    return word_highest, highest_value

