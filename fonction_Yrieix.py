import os


def extract_name_president(name):
    president_name = name[11:]
    if ("1" in president_name) or ("2" in president_name):
        president_last_name = president_name[:-5]
    else:
        president_last_name = president_name[:-4]
    return president_last_name



'''def remove_ponctuation(text):
    os.chdir('Cleaned')
    with open(text,"w") as t :
        line = t.readline()
        while line != "":
            for char in line:
                if (char>="!" and char<="/") or (char>=":" and char<="?") or (char>="[" and char<="`") or (char>="{" and char<="~") :
                    char = " "
            line = f.readline()
    os.chdir('..')'''