'''
Grammati 1

S -> 0|1|2|3|4|5|6|7|8|9|S+S|S-S

S -> S+S -> 1+S -> 1+4
S -> S+S -> S+S-S -> 1+S-S -> 1+9-S -> 1+9-7
S -> S+S -> S+S+S -> 1+S+S -> 1+4+S -> 1+4+9

Grammatik 2

S -> Z|S+S|S-S
Z -> 0|1|2|3|4|5|6|7|8|9|ZZ

S -> S+S -> S+S-S -> Z+S-S -> ZZ+S-S -> ZZ+Z-S-> ZZ+ZZ-S -> ZZ+ZZ-Z -> ZZ+ZZ-ZZ -> 1Z+ZZ-ZZ -> 12+ZZ-ZZ -> 12+3Z-ZZ -> 12+31-ZZ -> 12+31-2Z -> 12+31-29

Grammatik 2'

S -> ZS'
S' -> +ZS'|-ZS'|epsilon
Z -> DZ'
Z' -> DZ'|epsilon
D -> 0|1|2|3|4|5|6|7|8|9

Grammatik multi
S -> S + S | S - S | M   (Strichrechnung)
M -> M * M | M / M | Z | (S) (Punktrechnung)
Z -> 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9

Regel
'''



class LL1_Parser:
    def __init__(self,text):
        self.text = text
        self.pos = 0
        self.curentchar = self.text[self.pos] if self.pos < len(self.text) else 0
    def next(self):
        self.pos += 1
        self.curentchar = self.text[self.pos] if self.pos < len(self.text) else 0

    # S -> ZS'
    def S(self):
        n0 = self.Z()
        n1 = self.S_(n0)
        return n1
    # S' -> +ZS'|-ZS'|epsilon
    def S_(self,n):
        match self.curentchar:
            case "+" :
                self.next()
                n0 = self.Z()
                n1 = self.S_(n0)
                return n+n1
            case "-" :
                self.next()
                n0 = self.Z()
                n1 = self.S_(-n0)
                return n+n1
            case 0 :
                return n
            case _ :
                raise Exception( f"{self.text}\n{" "*self.pos}^\ngelesen: {self.text[self.pos]} aber +, - oder eof erwartet")
    #Z -> DZ'
    def Z(self):
        n0 = self.D()
        n1 = self.Z_(n0)
        return n1

    # Z' -> DZ'|epsilon
    def Z_(self,n):
        match self.curentchar:
            case '0':
                n0 = self.D()
                n1 = self.Z_(10*n+n0)
                return n1
            case '1':
                n0 = self.D()
                n1 = self.Z_(10*n+n0)
                return n1
            case '2':
                n0 = self.D()
                n1 = self.Z_(10*n+n0)
                return n1
            case '3':
                n0 = self.D()
                n1 = self.Z_(10*n+n0)
                return n1
            case '4':
                n0 = self.D()
                n1 = self.Z_(10*n+n0)
                return n1
            case '5':
                n0 = self.D()
                n1 = self.Z_(10*n+n0)
                return n1
            case '6':
                n0 = self.D()
                n1 = self.Z_(10*n+n0)
                return n1
            case '7':
                n0 = self.D()
                n1 = self.Z_(10*n+n0)
                return n1
            case '8':
                n0 = self.D()
                n1 = self.Z_(10*n+n0)
                return n1
            case '9':
                n0 = self.D()
                n1 = self.Z_(10*n+n0)
                return n1
            case "+" :
                return n
            case "-" :
                return n
            case 0 :
                return n
            case _:
                raise Exception( f"{self.text}\n{" "*self.pos}^\ngelesen: {self.text[self.pos]} aber +, -, 0-9 erwartet")
            
        
    # D -> 0|1|2|3|4|5|6|7|8|9
    def D(self):
        match self.curentchar:
            case '0':
                self.next()
                return 0
            case '1':
                self.next()
                return 1
            case '2':
                self.next()
                return 2
            case '3':
                self.next()
                return 3
            case '4':
                self.next()
                return 4
            case '5':
                self.next()
                return 5
            case '6':
                self.next()
                return 6
            case '7':
                self.next()
                return 7
            case '8':
                self.next()
                return 8
            case '9':
                self.next()
                return 9
            case _ :
                raise Exception( f"{self.text}\n{" "*self.pos}^\ngelesen: {self.text[self.pos]} aber 0-9 erwartet")


try:
    p = LL1_Parser('13-66666+14')
    print(p.S())
except Exception as ex: 
    print(ex)   
