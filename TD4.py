import matplotlib.pyplot as plt

class Hashtable:
    def __init__(self, hash_function, N):
        self.__hash_function = hash_function
        self.__size = int(N)
        self.__table = [[] for k in range(self.__size)]
        self.__nb_element = 0

    def nb_element(self):
        return self.__nb_element

    def resize(self):
        self.__size *= 2
        tab = list(self.__table)
        self.__tableau = [[] for k in range(self.__size)]
        for l in tab:
            for (r,p) in l:
                self.put(r,p)

    def put(self, key : str, value) :
        index = self.__hash_function(key) % self.__size
        if self.nb_element() >= 1.2*self.__size:
            self.resize()
        if key in [k for (k,v) in self.__table[index]]:
            ind = 0
            for p in range(len(self.__table[index])):
                key2,v = self.__table[index][p]
                if key2 == key:
                    ind = p
            k,v = self.__table[index][ind]
            if v != value:
                self.__table[index][ind] = (key,value)
        else:
            self.__table[index].append((key,value))
            self.__nb_element += 1

    def __str__(self) :
        return str(self.__table)

    def get(self, key):
        index = self.__hash_function(key)%self.__size
        for (q,r) in self.__table[index]:
            if q == key:
                return r
        return None

    def repartition(self) :
        collision_size = []
        for k in self.__table:
            collision_size.append(len(k))
        x = [k for k in range(self.__size)]
        width = 5
        plt.bar(x,collision_size, width, color="blue")
        plt.title("Nombre de collisions par emplacement dans le tableau")
        plt.show()

def hash_function_naive(key):
    return sum([ord(c) for c in key])

a = Hashtable(hash_function_naive, 97)
a.put('a', 12)
a.put('bbb', 12)
a.put('aaaa', 12)
a.put('aaa', 12)
a.put('bb', 12)
print(a.get('a'))
print(a)
print(a.repartition())
