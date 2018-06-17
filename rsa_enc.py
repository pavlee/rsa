import sys

BLOK_CIFRE = 300
BLOK_KARAKTERI = BLOK_CIFRE // 3
plaintext = ""
sifrovani_text = ""

def encrypt(plaintext, key):
    
    ascii_plaintext = bytes(plaintext, "ASCII")

    # Tekst se lomi na blokove duzine najvise BLOK_KARAKTERI chara
    # Svaki char je predstavljen pomocu trocifrenog broja
    
    blokovi = []
    for i, chars in enumerate(ascii_plaintext[::BLOK_KARAKTERI]):
        start = BLOK_KARAKTERI * i
        end = BLOK_KARAKTERI * (i + 1)
        blokovi.append(ascii_plaintext[start:end])

    enkriptovani_blokovi = []
    for blok in blokovi:
        broj_plaintext = 0
        for i, char in enumerate(list(blok)[::-1]): # lista se reversuje i pocinjemo od nizih cifara
            broj_plaintext += (char * 10**(i*3))

        enkriptovani_blokovi.append(pow(broj_plaintext, key[0], key[1]))

    # Pad each block to BLOK_CIFRE
    sifrovani_text = ""
    for blok in enkriptovani_blokovi:
        sifrovani_text += str(blok).rjust(BLOK_CIFRE, "0")
    return sifrovani_text

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Validni argumenti programa su x, N, e")
        quit()

    xprim = encrypt(str(sys.argv[1]), (int(sys.argv[3]), int(sys.argv[2])))
    print("\nRezultat: \n\n{}".format(xprim))