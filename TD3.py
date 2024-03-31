class Tree:
    def __init__(self, label, *children):
        self.__label = label
        self.__children = list(children)

    def label(self) :
        return self.__label

    def children (self):
        return self.__children

    def nb_children(self):
        return len(self.__children)

    def child(self, i):
        return self.__children[i]

    def is_leaf(self) :
        if self.__children == []:
            return True
        else :
            return False

    def depth(self):
        if self.is_leaf():
            return 0
        else:
            return 1 + max([i.depth() for i in self.children()])

    def __str__(self):
        if self.is_leaf():
            return self.label()
        s = f"{self.label()}("
        if self.nb_children() == 1:
            s += f"{self.child(0).__str__()})"
            return s
        else:
            n = self.nb_children()
            for p in range(0,n-1):
                s+= f"{self.child(p).__str__()},"
            s+= f"{self.child(n-1).__str__()})"
            return s

    def __eq__(self, other):
        if self.is_leaf() and other.is_leaf():
            return self.label() == other.label()
        if self.nb_children() == other.nb_children():
            if self.label == other.label:
                return self.children.__eq__(other.children)
            else :
                return False
        else : return False

    def deriv(self, var):
        if self.is_leaf():
            if var.label() == self.label():
                return Tree("1")
            else:
                return Tree("0")
        if self.label() == "+":
            return Tree(self.label(),*tuple([s.deriv(var) for s in self.children()]))
        if self.label() == "*":
            l = []
            number = 1.
            index = 0
            for s in self.children():
                if is_floatint(s.label()):
                    number *= float(s.label())
                elif s.label() == var.label():
                    index += 1
                else:
                    l.append(Tree(s.label()))
            number *= index
            if number.is_integer():
                l.append(Tree(str(int(number))))
            else:
                l.append(Tree(str(number)))
            for k in range(index-1):
                l.append(var)
            return Tree("*",*l)


a = Tree("f", Tree("a"), Tree("b"))
b = Tree("f", Tree("a"), Tree("b"))
c = Tree('+', Tree('a'), Tree('X'))
print(a.children())
print(a.nb_children())
print(a.child(0))
print(a.is_leaf())
print(a.depth())
print(a)
print(a, b)
print(Tree('+', Tree('a'), Tree('X')).deriv(Tree('X')))

