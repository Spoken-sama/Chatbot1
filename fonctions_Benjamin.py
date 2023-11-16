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


'''def undercase (file_name)'''