def associating_names(name):
    pre_full_name=[]
    full_names=[]
    dico=["Jaques","Chirac","Valéry","Giscard","François","Hollande","Emmanuel","Macron","François","Mitterrand","Nicolas","Sarkozy"]
    for i in range (len(name)):
        for j in range (len(dico)):
            if name[i]==dico[j]:
                prefullname.append(dico[j-1]+" "+name[i])
        if pre_full_name!=full_names:
            full_names.append(pre_full_name)
    return full_names


'''def undercase (file_name)'''