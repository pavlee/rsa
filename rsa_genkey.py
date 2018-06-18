import math
import fractions
import random as rand

# fermat test za proste brojeve, k - broj testova, sto je veci to je veca vjerovatnoca da je test tacan
def fermat_test(n, k):

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(k):
        a = rand.randint(1, n-1)

        if pow(a, n-1, n) != 1:
            return False
    return True

def prost_broj():
    
    veliki_broj = rand.randint(10**149, (10**150)-1)
    
    if veliki_broj % 2 == 0: veliki_broj -= 1

    while not fermat_test(veliki_broj, 100) and veliki_broj < 10**150:
        veliki_broj += 2

    if veliki_broj > 10**150:
        # Ne prelazimo granicu od 150 cifara
        veliki_broj = prost_broj()

    return veliki_broj

def fi(pq):
    return (pq[0] - 1) * (pq[1] - 1)

def get_eksponent(N_veliko):
    
    exp = rand.randint(10**160, 10**200)
    if exp % 2 == 0: exp -= 1

    while fractions.gcd(exp, N_veliko) != 1:
        exp += 2
    
    return exp

def get_d(a, mod):
    assert fractions.gcd(a, mod) == 1

    def obrnuti_euklidov(a, b):
        if b == 0:
            return (1, 0)
        else:
            xx, yy = obrnuti_euklidov(b, a % b)
            x, y = yy, xx - (a // b) * yy
            return (x, y)

    d = obrnuti_euklidov(a, mod)[0] % mod
    return d

def generisi_kljuceve():
    
    pq = (prost_broj(), prost_broj())
    moduo = pq[0] * pq[1]
    eksponent = get_eksponent(fi(pq))
    d = get_d(eksponent, fi(pq))

    return [(d, moduo), (eksponent, moduo)]

if __name__ == "__main__":
	privkey, pubkey = generisi_kljuceve()
	print("\n##########################################################")
	print("#                  IZGENERISANI KLJUCEVI                 #")
	print("##########################################################\n")
	print("---- PRIVATNI KLJUC(d, N)\n\nd = {}\n\nN = {}".format(privkey[0], privkey[1]))
	print()
	print("---- JAVNI KLJUC(e, N)\n\ne = {}\n\nN = {}".format(pubkey[0], pubkey[1]))