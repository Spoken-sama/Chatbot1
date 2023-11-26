import os
import math
from fonction_Yrieix import *

cleaned_speeches = ["Cleaned_Nomination_Chirac1.txt", "Cleaned_Nomination_Chirac2.txt",
                    "Cleaned_Nomination_Giscard dEstaing.txt", "Cleaned_Nomination_Hollande.txt",
                    "Cleaned_Nomination_Macron.txt", "Cleaned_Nomination_Mitterrand1.txt",
                    "Cleaned_Nomination_Mitterrand2.txt", "Cleaned_Nomination_Sarkozy.txt"]

def associating_names(name):
    pre_full_name=[]
    full_names=[]
    dico=["Jaques","Chirac","Valéry","Giscard","François","Hollande","Emmanuel","Macron","François","Mitterrand","Nicolas","Sarkozy"]
    for i in range (len(name)):
        for j in range (len(dico)):
            if name[i]==dico[j]:
                pre_full_name.append(dico[j-1]+" "+name[i])
    for i in pre_full_name:
        if i not in full_names:
            full_names.append(i)
    return full_names

def convert_to_lowercase_and_save(input_folder, output_folder):
    cleaned_folder_path = os.path.join(os.path.dirname(__file__), output_folder)
    os.makedirs(cleaned_folder_path, exist_ok=True)

    text_files = [f for f in os.listdir(input_folder) if f.endswith('.txt')]

    for file_name in text_files:
        input_file_path = os.path.join(input_folder, file_name)
        file_name="Cleaned_"+file_name
        output_file_path = os.path.join(cleaned_folder_path, file_name)

        with open(input_file_path, 'r') as input_file:
            content = input_file.read().lower()

        dico_accent = {
            "é": "e", "è": "e", "ê": "e", "ë": "e", "à": "a", "â": "a", "ä": "a",
            "î": "i", "ï": "i", "ù": "u","û":"u", "ô": "o", "ö": "o","ç": "c","œ":"oe"
        }

        new_content = ""
        for char in content:
            if char in dico_accent:
                new_content += dico_accent[char]
            else:
                new_content += char

        with open(output_file_path, "w") as output_file:
            output_file.write(new_content)


def TF(file_name):
    dico_occ = {}
    doc = file_name.split(" ")
    for word in doc:
        if word[-1:] == "\n":
            word = word[:-1]
        if word != "":
            if word not in dico_occ.keys():
                dico_occ[word] = 1
            else:
                dico_occ[word] += 1
    '''print(dico_occ)'''
    return dico_occ

def IDF(directory):
    file_names = cleaned_speeches
    nb_files = len(file_names)
    final_dictio = {}
    finals_word_list = []

    os.chdir('cleaned')
    for i in range(nb_files):
        list_word_file = []
        with open( file_names[i], "r", encoding="UTF-8") as f:
            for lines in f:
                list_line = lines.split(" ")
                for word in list_line:
                    if word[-1:] == "\n":
                        word = word[:-1]
                    if word != "":
                        if word not in file_names:
                            list_word_file.append(word)
        finals_word_list.append(list_word_file)

    for i in range(len(finals_word_list)):
        for k in range(len(finals_word_list[i])):
            if finals_word_list[i][k] not in final_dictio.keys():
                apparition = 1
                for j in range(-1 + i, (-nb_files) + i, -1):
                    if finals_word_list[i][k] in finals_word_list[j]:
                        apparition += 1
                        finals_word_list[j].remove(finals_word_list[i][k])
                final_dictio[finals_word_list[i][k]] = math.log(nb_files / apparition)
    '''print(final_dictio)'''
    os.chdir('..')
    return final_dictio

def TF_IDF(directory):
    idf_dictio = IDF(directory)
    file_names = cleaned_speeches
    nb_files = len(file_names)
    matrice = {}
    os.chdir('cleaned')

    for word in idf_dictio.keys():
        matrice[word] = []

    for i in range(nb_files):
        with open(file_names[i], "r", encoding="UTF-8") as f:
            dico_tf = {}
            for lines in f :
                dico_temp = TF(lines)
                for word in dico_temp.keys():
                    if word not in dico_tf.keys():
                        dico_tf[word] = dico_temp[word]
                    else:
                        dico_tf[word] += dico_temp[word]
            dico_tf_idf = {}

            for word in dico_tf.keys() :
                word_TF_IDF = dico_tf[word]*idf_dictio[word]
                dico_tf_idf[word] = word_TF_IDF

            for word2 in idf_dictio.keys():
                if word2 not in dico_tf_idf.keys():
                    matrice[word2].append(0)
                else:
                    matrice[word2].append(dico_tf_idf[word2])
    os.chdir('..')
    '''print(matrice)'''
    return matrice

def eco(directory):
    os.chdir(directory)
    president=[]
    file_names = cleaned_speeches
    cpt=0
    counter=[]
    for i in range (8):
        with open(file_names[i], "r") as texte:
            for lines in texte:
                list_line = lines.split(" ")
                for word in list_line:
                    if word=="climat" or word=="écologie":
                        president.append(file_names[i])
                    else:
                        cpt=cpt+1
            counter.append(cpt)
    lowest = min(counter)
    for i in range (len(counter)):
        if counter[i]<=lowest:
            x=president[i]
        mx= x.split("_")
    for words in mx:
        if words!="Cleaned" and words!="Nomination" and words!="txt":
            wordn=words
    wordf = wordn.replace(".txt","")
    print("First president to speak of climat or écology is", wordf)
    return president

def All_said(dico):
    list_all_said_words = []
    for i in dico.items() :
        cpt = 0
        for j in i[1] :
            if j >= 0.0 :
                cpt += 1
        if cpt == 8 :
            if i[0] not in TF_IDF_nonimportant_value(dico):
                list_all_said_words.append(i[0])
    print("There is ",len(list_all_said_words) , "words said by all president")
    return list_all_said_words