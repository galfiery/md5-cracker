import hashlib

def openDictionary(path, toCrack):
    with open(path) as file:
        lines = file.readlines()
        for line in lines:
            if (crackMd5(line.replace('\n', ''), toCrack)):
                return line
        return False

def crackMd5(first, second):
    converted = hashlib.md5(first.encode())
    if (converted.hexdigest() == second):
        return True
    else:
        return False

dictionaryName = input("Inserisci il nome del file da utilizzare come dizionario: ")
if (dictionaryName and dictionaryName != ''):
    stringToCrack = input("Inserisci la stringa in formato MD5 da craccare: ")
    if (stringToCrack and stringToCrack != ''):
        result = openDictionary(dictionaryName, stringToCrack)
        if (result != False):
            print("La stringa inserita corrisponde a: " + result)
        else:
            print("La ricerca non ha fornito risultati.")
    else:
        print("La stringa da craccare non può essere vuota.")
else:
    print("Non è stato possibile accedere al file utilizzato come dizionario.")