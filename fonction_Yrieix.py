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