#!/usr/bin/python
# Written By: Aikon Nexus
# Date: 16/3/2023
# Hours: 22:57
#github:  @coyotikon
from colorama import Fore
import hashlib

print(Fore.LIGHTYELLOW_EX+ """BEM  VINDO  AO  XBRUTEKON""")
def openFile(wordList):
    try:    
        file = open(wordList, 'r')
        return file
    except:
        print("[~]  passlist inexistente ou não presente no diretorio.")
        quit()

passwordHash = input(Fore.GREEN + '[_$_]  Escreva o Email : ')
wordList = input(Fore.RED + '[_$_]    Escreva sua lista de senhas: ')
file = openFile(wordList)

for word in file:
    print(Fore.YELLOW + '[*] Testando.. ' + word.strip('\n'))
    encodeWord = word.encode('UTF-8')
    md5Hash = hashlib.md5(encodeWord.strip()).hexdigest()

    if md5Hash == passwordHash:
        print(Fore.GREEN + '[+] Senha encontrada: ' + word)
        exit(0)
    else:
        pass

print('[-] Senha não encontrada  :(')
