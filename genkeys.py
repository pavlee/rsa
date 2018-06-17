import math
import fractions
import random as rand

DEFAULT_CERTAINTY = 10 # 1 in 2**VAL chance of false prime

def is_prime(x, certainty=DEFAULT_CERTAINTY):
    
    if x % 2 != 1: return False

    odd_factor = x - 1
    powers_two = 0
    while odd_factor % 2 == 0:
        powers_two += 1
        odd_factor = (x - 1) // 2**powers_two

    def confirmed_composite_by(test):
        for _ in range(powers_two - 1):
            test = pow(test, 2, x)
            if test == x - 1: return False
            if test == 1: return True
        return True

    for _ in range(certainty):
        witness_maybe = rand.randint(2, x - 2)
        test = pow(witness_maybe, odd_factor, x)

        if test == 1 or test == x - 1: continue
        if confirmed_composite_by(test):
            # log.debug("is_prime:CONFIRMED COMPOSITE:" + str(x))
            # log.debug("is_prime:CONFIRMED COMPOSITE BY:" + str(test))
            return False

    # log.debug("is_prime:PROBABLE PRIME:" + str(x))
    return True

def prost_broj():
    
    veliki_broj = rand.randint(6*10**149, (10**150)-1)
    # veliki_broj = rand.getrandbits(512)
    if veliki_broj % 2 == 0: veliki_broj -= 1

    while not is_prime(veliki_broj) and veliki_broj < 10**150:
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
    """Returns the multiplicative d of a, mod (mod)."""
    assert fractions.gcd(a, mod) == 1

    def obrnuti_euklidov(a, b):
        """Returns the solution (x, y) to [ax + by = gcd(a, b)].

        Credit to page 937 of the textbook.
        """
        if b == 0:
            return (1, 0)
        else:
            x_, y_ = obrnuti_euklidov(b, a % b)
            x, y = y_, x_ - (a // b) * y_
            return (x, y)

    d = obrnuti_euklidov(a, mod)[0] % mod
    return d

def generisi_kljuceve():
    
    """
    if passphrase != None:
        rand.seed(passphrase)
    """
    pq = (prost_broj(), prost_broj())
    moduo = pq[0] * pq[1]
    eksponent = get_eksponent(fi(pq))
    d = get_d(eksponent, fi(pq))

    # assert pq[0] < eksponent and pq[1] < eksponent
    # assert math.floor(math.log10(moduo)) + 1 == 300
    # assert fi(pq) % 2 == 0
    # assert eksponent < moduo

    return [(d, moduo), (eksponent, moduo)]
    
if __name__ == "__main__":
	privkey, pubkey = generisi_kljuceve()
	print("\n##########################################################")
	print("#                  IZGENERISANI KLJUCEVI                 #")
	print("##########################################################\n")
	print("---- PRIVATNI KLJUC(d, N)\n\nd = {}\n\nN = {}".format(privkey[0], privkey[1]))
	print()
	print("---- JAVNI KLJUC(e, N)\n\ne = {}\n\nN = {}".format(pubkey[0], pubkey[1]))