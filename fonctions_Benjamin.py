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
    # Create the "cleaned" folder if it doesn't exist
    cleaned_folder_path = os.path.join(os.path.dirname(__file__), output_folder)
    os.makedirs(cleaned_folder_path, exist_ok=True)

    # Get a list of all text files in the input folder
    text_files = [f for f in os.listdir(input_folder) if f.endswith('.txt')]

    for file_name in text_files:
        # Construct the input and output file paths
        input_file_path = os.path.join(input_folder, file_name)
        output_file_path = os.path.join(cleaned_folder_path, file_name)

        # Read the content of the input file and convert it to lowercase
        with open(input_file_path, 'r') as input_file:
            content = input_file.read().lower()

        # Write the lowercase content to the output file
        with open(output_file_path, 'w') as output_file:
            output_file.write(content)




