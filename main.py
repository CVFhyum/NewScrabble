from termcolor import colored as cl
from random import randint as ri, choice
from time import sleep as s

# 'word' is a string.
# 'idx' is a list containing two values (8a -> [8,1]) and usually refers to the index of the first letter in the word.
# 'direc' is a character, h(orizontal) or v(ertical).

class Board:

    def __init__(self):
        self.board = [["  ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"],
                     [" 1",s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15],
                     [" 2",s16,s17,s18,s19,s20,s21,s22,s23,s24,s25,s26,s27,s28,s29,s30],
                     [" 3",s31,s32,s33,s34,s35,s36,s37,s38,s39,s40,s41,s42,s43,s44,s45],
                     [" 4",s46,s47,s48,s49,s50,s51,s52,s53,s54,s55,s56,s57,s58,s59,s60],
                     [" 5",s61,s62,s63,s64,s65,s66,s67,s68,s69,s70,s71,s72,s73,s74,s75],
                     [" 6",s76,s77,s78,s79,s80,s81,s82,s83,s84,s85,s86,s87,s88,s89,s90],
                     [" 7",s91,s92,s93,s94,s95,s96,s97,s98,s99,s100,s101,s102,s103,s104,s105],
                     [" 8",s106,s107,s108,s109,s110,s111,s112,s113,s114,s115,s116,s117,s118,s119,s120],
                     [" 9",s121,s122,s123,s124,s125,s126,s127,s128,s129,s130,s131,s132,s133,s134,s135],
                     ["10",s136,s137,s138,s139,s140,s141,s142,s143,s144,s145,s146,s147,s148,s149,s150],
                     ["11",s151,s152,s153,s154,s155,s156,s157,s158,s159,s160,s161,s162,s163,s164,s165],
                     ["12",s166,s167,s168,s169,s170,s171,s172,s173,s174,s175,s176,s177,s178,s179,s180],
                     ["13",s181,s182,s183,s184,s185,s186,s187,s188,s189,s190,s191,s192,s193,s194,s195],
                     ["14",s196,s197,s198,s199,s200,s201,s202,s203,s204,s205,s206,s207,s208,s209,s210],
                     ["15",s211,s212,s213,s214,s215,s216,s217,s218,s219,s220,s221,s222,s223,s224,s225]]
        Board.colourBoard(self)
        self.words = [] # List of words on the board, all being objects of class 'Word'.

    def __str__(self):
        string = ""
        for i in range(len(self.board)):
            for ii in self.board[i]:
                string += f"{ii} "
            string += "\n"
        return string

    def colourBoard(self):
        # Middle Tile
        self.board[8][8] = cl("★", "red")

        # Double Word Tiles
        for i in range(1, 16):
            if i in [2, 3, 4, 5, 11, 12, 13, 14]:
                self.board[i][i] = cl(char, "red")
        for i in [[2, 14], [3, 13], [4, 12], [5, 11]]:
            self.board[i[0]][i[1]] = cl(char, "red")
            self.board[i[1]][i[0]] = cl(char, "red")

        # Triple Word Tiles
        for i in range(0, 15, 7):
            self.board[1][1 + i] = cl(char, "magenta", attrs=["bold"])
            self.board[15][1 + i] = cl(char, "magenta", attrs=["bold"])
        for i in range(1, 16, 14):
            self.board[8][i] = cl(char, "magenta", attrs=["bold"])

        # Double Letter Tiles
        for i in range(4, 13, 8):
            self.board[1][i] = cl(char, "cyan")
            self.board[15][i] = cl(char, "cyan")
        for i in range(3, 14, 2):
            if i in [5, 11]:
                continue
            self.board[7][i] = cl(char, "cyan")
            self.board[9][i] = cl(char, "cyan")
            self.board[i][7] = cl(char, "cyan")
            self.board[i][9] = cl(char, "cyan")
        for i in range(1, 16, 7):
            self.board[4][i] = cl(char, "cyan")
            self.board[12][i] = cl(char, "cyan")

        # Triple Letter Tiles
        for i in range(6, 11, 4):
            self.board[2][i] = cl(char, "blue", attrs=["bold"])
            self.board[14][i] = cl(char, "blue", attrs=["bold"])
        for i in range(2, 15, 4):
            self.board[6][i] = cl(char, "blue", attrs=["bold"])
            self.board[10][i] = cl(char, "blue", attrs=["bold"])

    def canPlaceWord(self,word,idx,direc):
        pass
        # TODO: after finishing word class

    def placeWord(self,word,idx,direc):
        self.words.append(Word(word,idx,direc))
        if direc == 'h':
            for i in word:
                self.board[idx[0]][idx[1]] = cl(i.upper(),'yellow',attrs=['bold'])
                idx[1] += 1
        if direc == 'v':
            for i in word:
                self.board[idx[0]][idx[1]] = cl(i.upper(),'yellow',attrs=['bold'])
                idx[0] += 1


    def isTileTaken(self,idx):
        if self.board[idx[0]][idx[1]] not in coloured and self.board[idx[0]][idx[1]] != char:
            return True
        return False


class Word:
    def __init__(self, word, idx, direc):
        self.word = word.upper()
        self.idx = []
        self.direc = direc
        if direc == 'h':
            for i in range(len(word)):
                self.idx.append([idx[0],idx[1]+i])
        if direc == 'v':
            for i in range(len(word)):
                self.idx.append([idx[0]+i,idx[1]])

        wordsObj[self.word] = self





class Player:

    def __init__(self, name, number, colour):
        self.name = name
        self.number = number
        self.colour = colour
        self.letters = []
        self.points = 0
        self.curword = ""
        self.curidx = ""
        self.curdirec = ""

    def __str__(self):
        return f"""{cl(f"Player {self.number} - {cl(self.name,attrs=['bold','underline'])}",'red')}\n""" \
               f"Your letters are: {', '.join([letterpointSub[x] for x in self.letters])}"

    def refillLetters(self):
        for i in range(0, 7-len(self.letters)):
            s(0.01)
            ran = choice(letterFreq)
            self.letters.append(ran)
            del letterFreq[self.letters.index(ran)]

    def canPlayWord(self):
        def LettersCheck():
            curwordL = [char for char in self.curword]
            letterscopy = self.letters.copy()
            for i in curwordL:
                if i in letterscopy:
                    curwordL.remove(i)
                    letterscopy.remove(i)
                else:
                    return False
            return True
        def DictCheck():
            with open('dict.txt', 'r') as f:
                for i in f:
                    i = i.replace("\n", '')
                    i = i.upper()
                    if self.curword == i:
                        return True
                return False

        return LettersCheck() and DictCheck()

    def canPlayIndex(self):
        pass
        # TODO










char = '□'
coloured = [cl('★','red'),cl(char,'red'),cl(char,'magenta',attrs=['bold']),cl(char,'cyan'),cl(char,'blue')]
commands = ["*help","*key","*rules"]


s1 = s2 = s3 = s4 = s5 = s6 = s7 = s8 = s9 = s10 = s11 = s12 = s13 = s14 = s15 = s16 = s17 = s18 = s19 = s20 \
    = s21 = s22 = s23 = s24 = s25 = s26 = s27 = s28 = s29 = s30 = s31 = s32 = s33 = s34 = s35 = s36 = s37 = s38 = s39 = s40 \
    = s41 = s42 = s43 = s44 = s45 = s46 = s47 = s48 = s49 = s50 = s51 = s52 = s53 = s54 = s55 = s56 = s57 = s58 = s59 = s60 \
    = s61 = s62 = s63 = s64 = s65 = s66 = s67 = s68 = s69 = s70 = s71 = s72 = s73 = s74 = s75 = s76 = s77 = s78 = s79 = s80 \
    = s81 = s82 = s83 = s84 = s85 = s86 = s87 = s88 = s89 = s90 = s91 = s92 = s93 = s94 = s95 = s96 = s97 = s98 = s99 = s100 \
    = s101 = s102 = s103 = s104 = s105 = s106 = s107 = s108 = s109 = s110 = s111 = s112 = s113 = s114 = s115 = s116 = s117 = s118 = s119 = s120 \
    = s121 = s122 = s123 = s124 = s125 = s126 = s127 = s128 = s129 = s130 = s131 = s132 = s133 = s134 = s135 = s136 = s137 = s138 = s139 = s140 \
    = s141 = s142 = s143 = s144 = s145 = s146 = s147 = s148 = s149 = s150 = s151 = s152 = s153 = s154 = s155 = s156 = s157 = s158 = s159 = s160 \
    = s161 = s162 = s163 = s164 = s165 = s166 = s167 = s168 = s169 = s170 = s171 = s172 = s173 = s174 = s175 = s176 = s177 = s178 = s179 = s180 \
    = s181 = s182 = s183 = s184 = s185 = s186 = s187 = s188 = s189 = s190 = s191 = s192 = s193 = s194 = s195 = s196 = s197 = s198 = s199 = s200 \
    = s201 = s202 = s203 = s204 = s205 = s206 = s207 = s208 = s209 = s210 = s211 = s212 = s213 = s214 = s215 = s216 = s217 = s218 = s219 = s220 \
    = s221 = s222 = s223 = s224 = s225 = char

# Conversion from 'Word' object value to the actual object
wordsObj = {

}

# The frequency of each letter
letterFreq = ['A','A','A','A','A','A','A','A',
              'B','B',
              'C','C',
              'D','D','D','D',
              'E','E','E','E','E','E','E','E','E','E','E','E',
              'F','F',
              'G','G','G',
              'H','H',
              'I','I','I','I','I','I','I','I','I',
              'J',
              'K',
              'L','L','L','L',
              'M','M',
              'N','N','N','N','N','N',
              'O','O','O','O','O','O','O','O',
              'P','P',
              'Q',
              'R','R','R','R','R','R',
              'S','S','S','S',
              'T','T','T','T','T','T',
              'U','U','U','U',
              'V','V',
              'W','W',
              'X',
              'Y','Y',
              'Z']

# The points each letter awards
letterPoint = {
    "A": 1,
    "B": 3,
    "C": 3,
    "D": 2,
    "E": 1,
    "F": 4,
    "G": 2,
    "H": 4,
    "I": 1,
    "J": 8,
    "K": 5,
    "L": 1,
    "M": 3,
    "N": 1,
    "O": 1,
    "P": 3,
    "Q": 10,
    "R": 1,
    "S": 1,
    "T": 1,
    "U": 1,
    "V": 4,
    "W": 4,
    "X": 8,
    "Y": 4,
    "Z": 10
}

# Conversion of regular letter to letter with it's point value in subscript.
letterpointSub = {
    "A": "A₁",
    "B": "B₃",
    "C": "C₃",
    "D": "D₂",
    "E": "E₁",
    "F": "F₄",
    "G": "G₂",
    "H": "H₄",
    "I": "I₁",
    "J": "J₈",
    "K": "K₅",
    "L": "L₁",
    "M": "M₃",
    "N": "N₁",
    "O": "O₁",
    "P": "P₃",
    "Q": "Q₁₀",
    "R": "R₁",
    "S": "S₁",
    "T": "T₁",
    "U": "U₁",
    "V": "V₄",
    "W": "W₄",
    "X": "X₈",
    "Y": "Y₄",
    "Z": "Z₁₀"
}

# Number to Letter converter for indexing
letToNum = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15
}
# Letter to Number converter for indexing
numToLet = {
    1: "A",
    2: "B",
    3: "C",
    4: "D",
    5: "E",
    6: "F",
    7: "G",
    8: "H",
    9: "I",
    10: "J",
    11: "K",
    12: "L",
    13: "M",
    14: "N",
    15: "O",
}

# Conversion from tiles to extra points awarded
tiles = {
    cl('★','red'): ['word',2],
    cl(char,'red'): ['word',2],
    cl(char,'magenta',attrs=['bold']): ['word',3],
    cl(char,'cyan'): ['letter',2],
    '\x1b[1m\x1b[34m□\x1b[0m': ['letter',3]
}


# [PRINT] Rules
def rules():
    print(cl("Scrabble Rules",attrs=['underline']))
    s(2)
    print("There are two players. Each one gets a set of 7 letters.")
    s(1)
    print("The players take turns to place words on the board to try and accumulate the most points as possible.")
    s(2)
    print("Each letter has a point value next to it, which shows how many points it will give if played.")
    s(2)
    print("Different letters have different frequencies.")
    s(2)
    print("For example, E is a common letter so there are twelve E tiles.")
    s(2)
    print("However, Z is a rare letter so there is only one Z tile.")
    s(2)
    print("The rarer a letter is, the more points it grants.")
    s(1.5)
    print(
        "Player 1, on the first turn, must play their word in a place where one letter of the word is on the middle star.")
    s(3)
    print("After this, all players must place their words so they connect with other words already on the board.")
    s(3)
    print("For example, the word 'FLOOR' is on the board.")
    s(1.5)
    print("You are trying to place the word 'LOVE'.")
    s(1.5)
    print("You need to place this word in a way such that the L in 'FLOOR' starts your word, 'LOVE'")
    s(2)
    print("Therefore, you'd need to sacrifice placing your L tile to be able to place the word.")
    s(1.5)


# [PRINT] Key for the coloured tiles
def key():
    print(cl("Key:",attrs=['underline']))
    print(f"{cl('★','red')} - Double Word Middle Tile (First move needs to have one letter in congruence with it.)")
    print(f"{cl(char,'red')} - Double Word Tile (Doubles your points for the word)")
    print(f"{cl(char,'magenta',attrs=['bold'])} - Triple Word Tile (Triples your points for the word)")
    print(f"{cl(char,'cyan')} - Double Letter Tile (Doubles the points for the letter that is on it)")
    print(f"{cl(char,'blue')} - Triple Letter Tile (Triples the points for the letter that is on it)")


# [PRINT] Commands process
def command(inp):
    if inp == "*help":
        pass
    elif inp == "*key":
        key()
    elif inp == "*rules":
        rules()


# [CALC] Checking a word against the dictionary
def dict(word):
    valid = False
    with open('dict.txt','r') as f:
        for i in f:
            i = i.replace("\n",'')
            if word == i:
                return True
        if not valid:
            return False


# [CALC] Checks the longest word that can be made with the letters in the given list
def checkwords(list):
    maxlen = 0
    maxword = ''
    with open("dict.txt","r") as f:
        for i in f:
            i = i.replace("\n",'')
            i = i.upper()
            wordL = [x for x in i]
            listcopy = list.copy()
            for ii in list:
                if ii in wordL:
                    listcopy.remove(ii)
                    wordL.remove(ii)
                    if len(wordL) == 0:
                        if len(i) > maxlen:
                            maxlen = len(i)
                            maxword = i
        return maxword

def multPrint(*toprint):
    for i in toprint:
        print(i)

# [CALC] Converts a number/letter index to number/number




p1 = Player("Yuval", "1", "red")
board = Board()
print(board)

board.placeWord("Hello",[8,6],'h')
multPrint(board,
          board.words,
          board.words[0].idx,
          wordsObj)

board.placeWord("love",[4,14],'v')
multPrint(board,
          board.words,
          board.words[1].idx,
          wordsObj)

# while True:
#     p1.refillLetters()
#     print(p1)
#     print(checkwords(p1.letters))
#     p1.curword = input("Word: ").upper()
#     print(p1.curword)
#     print(p1.canPlayWord())








