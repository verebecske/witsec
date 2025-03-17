# 1. Mit csinál a következő program?
A program go nyelven írodott, ahol a main-nél kezdődik a program végrehajtása. 
A fmt.Println függvény kiírja amit paraméterül kap, így jutunk el a isEqual nevű függvényhez, aminek két string paramétere van. 
Az isEqual függvény beül meghívja a getLetters függvényt mind a két kapott string-re és összehasonlítja azok eredményét.
A getLetters függvény egy string-et vár, amiből először eltávolítja a felesleges szóközöket, majd kisbetűssé teszi. Ezután végigiterál a kapott string-en és egy map típusba (ami olyan mint a python dict) összegyűjíti hogy melyik betűből mennyi szerepel a kapott szóban vagy szövegben majd végül ezt adja vissza a függvény visszatérési értékekét. 
Ha röviden összegezni akarjuk a program működését, megnézi hogy két string anagramma-e.


# 2. Írj egy olyan függvényt python nyelven, ami az angol ábécé szerinti sorrendben összeadja egy megadott string betűit. pl. ac => 4 (mert a = 1 + c = 3) 
#### hint: ord('a') = 97, ord('c') = 99
```
def alphabetic_value(word: str) -> int:
    word = word.lower()
    value = 0
    for letter in word:
        value += ord(letter) - 96
    return value
```
