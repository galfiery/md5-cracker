import hashlib

messages = [
    'Inserisci il nome del file da utilizzare come dizionario: ',
    'Inserisci la stringa in formato MD5 da craccare: ',
    'La stringa inserita corrisponde a: ',
    'La ricerca non ha fornito risultati.',
    'La stringa da craccare non può essere vuota.',
    'Non è stato possibile accedere al file utilizzato come dizionario.'
]

def getMessages(index):
    return messages[index]

def openDictionary(path, toCrack):
    try:
        with open(path) as file:
            lines = file.readlines()
            for line in lines:
                if (crackMd5(line.replace('\n', ''), toCrack)):
                    return line
            return False
    except:
        return False

def crackMd5(first, second):
    converted = hashlib.md5(first.encode())
    if (converted.hexdigest() == second):
        return True
    else:
        return False

def main():
    dictionaryName = input(getMessages(0))
    if (dictionaryName and dictionaryName != ''):
        stringToCrack = input(getMessages(1))
        if (stringToCrack and stringToCrack != ''):
            result = openDictionary(dictionaryName, stringToCrack)
            if (result != False):
                print(getMessages(2) + result)
            else:
                print(getMessages(3))
        else:
            print(getMessages(4))
    else:
        print(getMessages(5))

if __name__ == '__main__':
    main()