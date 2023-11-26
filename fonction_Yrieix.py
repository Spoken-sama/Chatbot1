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


def TF_IDF_highest_value_word(dico):
    highest_value = 0.0
    final_val = 0
    nom_president = ""
    all_president_who_say_the_word = ""
    for i,j in dico.items():
        if i == "nation" :
            for k in range(len(j)):
                if j[k] > highest_value:
                    highest_value = j[k]
                    final_val = k
                if j[k] != 0.0 and j[k] != 0:
                    if k == 0 or k == 1:
                        all_president_who_say_the_word += "Chirac, "
                    elif k == 2:
                        all_president_who_say_the_word += "Giscard dEstaing, "
                    elif k == 3:
                        all_president_who_say_the_word += "Hollande, "
                    elif k == 4:
                        all_president_who_say_the_word += "Macron, "
                    elif k == 5 or k == 6:
                        all_president_who_say_the_word += "Mitterrand, "
                    elif k == 7:
                        all_president_who_say_the_word += "Sarkozy, "
    if final_val == 0 or final_val == 1:
        nom_president = "Chirac"
    elif final_val == 2:
        nom_president = "Giscard dEstaing"
    elif final_val == 3:
        nom_president = "Hollande"
    elif final_val == 4:
        nom_president = "Macron"
    elif final_val == 5 or final_val == 6:
        nom_president = "Mitterrand"
    elif final_val == 7:
        nom_president = "Sarkozy"
    return f"the presidents who said nation are {all_president_who_say_the_word}and the president who repeated it the most times is {nom_president}"

def TF_IDF_most_word_repeat(dico,president):
    val = []
    if president == "Chirac":
        val = [0,1]
    elif president == "Giscard dEstaing":
        val = [2]
    elif president == "Hollande":
        val = [3]
    elif president == "Macron":
        val = [4]
    elif president == "Mitterrand":
        val = [5,6]
    elif president == "Sarkozy":
        val = [7]
    highest_value = 0.0
    final_val = 0
    most_repeated_word = ""
    for i,j in dico.items():
        for k in val:
            if j[k] > highest_value:
                highest_value = j[k]
                final_val = k
                most_repeated_word = i

    return f"The most repeated word by President {president} is '{most_repeated_word}'"

