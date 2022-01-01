from os import walk
import os
import pickle


try:
    with open("saves.pkl", "rb") as file:
        files_list = pickle.load(file)
except FileNotFoundError:
    files_list = []

flag=True
for path, _, names in walk('C:\\'):
    for i in range(len(names)):
        if names[i] in files_list:
            continue
        else:
            print("Nowy plik: ", end='')
            files_list.append(names[i])
            print(names[i], " w ", path)
            flag = False

with open('saves.pkl', 'wb') as file:
    pickle.dump(files_list, file)

if flag:
    print("Brak nowych plików.")
   