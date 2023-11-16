def associating_names(name):
    full_names=[]
    dico=["Jaques","Chirac","Valéry","Giscard","François","Hollande","Emmanuel","Macron","François","Mitterrand","Nicolas","Sarkozy"]
    for i in range (len(name)):
        for j in range (len(dico)):
            if name[i]==dico[j]:
                full_names.append(dico[j-1]+" "+name[i])
    return full_names







