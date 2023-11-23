import os


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


import os

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
            "î": "i", "ï": "i", "ù": "u", "ô": "o", "ö": "o"
        }

        new_content = ""
        for char in content:
            if char in dico_accent:
                new_content += dico_accent[char]
            else:
                new_content += char

        with open(output_file_path, "w") as output_file:
            output_file.write(new_content)



def occurrence(file_name):
    dictionary = {}
    os.chdir('Cleaned')
    with open(file_name, "r") as texte:
        for line in texte:
            for word in line.split():
                if word not in dictionary:
                    dictionary[word] = 1
                else:
                    dictionary[word] += 1
    print(dictionary)
    os.chdir('..')




