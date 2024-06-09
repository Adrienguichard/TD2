from random import randint
from random import choice
class Polnq :
    def __init__(self, n, q, coeffs) :
        self._coeffs = coeffs
        self._n = n
        self._q = q
        self._degre = self.get_deg()
        assert(len(self._coeffs) == n)
        for i in range(n):
            assert(self._coeffs[i]>= 0)
            assert(self._coeffs[i] < q)

    def get_deg(self):
        m = "-inf"
        for i in range(len(self._coeffs)):
            if self._coeffs[i]!= 0:
                m = i
        self.degre = m
        return m

    def __str__(self):
        s = ""
        for i in range(self._degre, 0, -1):
            if self._coeffs[i] != 0:
                s += f"{self._coeffs[i]} X**{i}"
                if i != 1 or (i == 1 and self._coeffs[0] != 0):
                    s += " + "
        if self._coeffs[0] != 0:
            s += f"{self._coeffs[0]}"
        return s

    def add(self, other):
        assert(self._n == other._n)
        assert(self._q == other._q)
        N = self._n
        Q = self._q
        add_coeffs = [0 for i in range(N)]
        for i in range(N):
            add_coeffs[i] = self._coeffs[i] + other._coeffs[i]
        for i in range(N):
            if add_coeffs[i] >= Q or add_coeffs[i] < 0 :
                add_coeffs[i] = add_coeffs[i] % Q
        return Polnq(N, Q, add_coeffs)

    def mult(self, other):
        assert(self._n == other._n)
        assert(self._q == other._q)
        N = self._n
        Q = self._q
        mult_coeffs = [0 for i in range(2*N)]
        for i in range (N):
            for j in range(N):
                mult_coeffs[i+j] = mult_coeffs[i+j] + self._coeffs[i]*other._coeffs[j]
        for p in range(N, 2*N):
            if mult_coeffs[p] != 0:
                mult_coeffs[p % N] = (-1)**(p//N)*mult_coeffs[p] + mult_coeffs[p % N]
                mult_coeffs[p] = 0
        mult_coeffs = mult_coeffs[ : N]
        for p in range(N):
            if mult_coeffs[p] >= Q or mult_coeffs[p] < 0:
                    mult_coeffs[p] = mult_coeffs[p] % Q
        return Polnq(N, Q, mult_coeffs)


    def scalar(self, c):
        N = self._n
        Q = self._q
        sc_coeffs = [0 for i in range(N)]
        for i in range (N):
            sc_coeffs[i] = self._coeffs[i] * c
        for i in range(N):
            if sc_coeffs[i] >= Q or sc_coeffs[i] < 0 :
                sc_coeffs[i] = sc_coeffs[i] % Q
        return Polnq(N, Q, sc_coeffs)

    def rescale(self, R):
        N = self._n
        Q = self._q
        rs_coeffs = self._coeffs
        for i in range(N):
            if rs_coeffs[i] >= R  :
                rs_coeffs[i] = rs_coeffs[i] % R
        return Polnq(N, R, rs_coeffs)

    def fscalar(self,r,alpha):
        N = self._n
        fscalar_coeffs = [0 for i in range(N)]
        for i in range(N):
            fscalar_coeffs[i] = round(self._coeffs[i]*alpha)%r
        return fscalar_coeffs #lorsque je veux retourner l'objet (qui devrait être dans Z_r[x]/(x^n+1) et pas uniquement les coeffs j'ai une erreur dans la fonction get deg ligne 23 : "'str' object cannot be interpreted as an integer"...

    def chiffrement(self, other, another):
        p = self
        a = other
        b = another
        assert(a._n == b._n == p._n)
        n = p._n
        t = p._q
        q = a._q
        delta = q // t
        sp = (p.scalar(delta)).rescale(q)
        u = gen_uniform_random(q, n, 0, 1)
        e1 = gen_uniform_random(q, n, -1, 1)
        c1 = ((b.mult(u)).add(e1)).add(sp)
        e2 = gen_uniform_random(q, n, -1, 1)
        c2 = (a.mult(u)).add(e2)
        return c1, c2


def gen_uniform_random(q, n, a, b):
    gur_coeffs = [0 for i in range(n)]
    for i in range(n):
        gur_coeffs[i] = randint(a, b)
        if gur_coeffs[i] < 0 or gur_coeffs[i] >= q :
            gur_coeffs[i] = gur_coeffs[i] % q
    return  Polnq(n, q, gur_coeffs) #parfois des erreurs rares lorsque je run : "'str' object cannot be interpreted as an integer"

def keys(n,q):
    sk = gen_uniform_random(q, n, 0, 1)
    a = gen_uniform_random(q, n, 0, q - 1)
    e_coeffs = [0 for i in range(n)]
    for i in range(n):
        e_coeffs[i] = choice([0,1,q -1 ])
    e= Polnq(n, q, e_coeffs)
    b1 = (a.mult(sk))
    b2 = b1.add(e)
    b = b2.scalar(-1)
    return sk, a, e, b








a = Polnq(2, 3, [1, 2])
b = Polnq(2, 3, [0, 2])
p = Polnq(2, 4, [1, 3])
print(a.add(b))
print(a.mult(b))
print(a.scalar(2))
print(a.rescale(2))
print(a.fscalar(2, 1))
print(gen_uniform_random(8,2,35,339))
print(keys(2, 3))
print(p.chiffrement(a, b))