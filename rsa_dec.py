import sys
import math

BLOK_CIFRE = 300
BLOK_KARAKTERI = BLOK_CIFRE // 3
plaintext = ""
sifrovani_text = ""

def decrypt(sifrovani_text, key):

    # Break text into blokovi by BLOK_CIFRE
    blokovi = []
    for i, blok in enumerate(sifrovani_text[::BLOK_CIFRE]):
        start = BLOK_CIFRE * i
        end = BLOK_CIFRE * (i + 1)
        blokovi.append(sifrovani_text[start:end])

    dekriptovani_ascii_chari = []

    for blok in blokovi:
        blok_karakters = []
        dekriptovani_blok = pow(int(blok), key[0], key[1])

        dekriptovani_string = str(dekriptovani_blok)

        d_n_copy = dekriptovani_blok
        for _ in range(math.ceil(len(dekriptovani_string) / 3)):
            # Evaluate 3 digits at a time to convert to string.
            char = chr(d_n_copy % 10**3)
            d_n_copy //= 10**3
            blok_karakters.insert(0, char)

        dekriptovani_ascii_chari.extend(blok_karakters)
    dekriptovana_poruka = "".join(dekriptovani_ascii_chari)
    return dekriptovana_poruka

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Validni argumenti programa su x, N, d")
        quit()
        
    x = decrypt(str(sys.argv[1]), (int(sys.argv[3]), int(sys.argv[2])))
    print("\nRezultat: \n\n{}".format(x))