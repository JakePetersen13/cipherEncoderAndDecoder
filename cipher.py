def main():
    print("DEBUG: MAIN METHOD")
    chooseCipher(input("> Entered Desired Cipher: \nCeaser Cipher ('c') \nMono-Alphabetic Cipher ('m') \nPoly-Alphabetic Cipher ('p') \n"))
    

def chooseCipher(cipherChosen):
    match cipherChosen.lower():
        case 'c':
            print("Ceasar Cipher")
        case 'm':
            print("monoalphabetic cipher")
        case 'p':
            print("poly alphabetic cipher")
        case _:
            print("unkown")

if __name__ == "__main__":
	main()