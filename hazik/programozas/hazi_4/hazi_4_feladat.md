# 1. Mit csinál a következő program?
```
package main

import (
	"fmt"
	"reflect"
	"strings"
)

func getLetters(str string) map[string]int {
	str = strings.ReplaceAll(str, " ", "")
	str = strings.ToLower(str)
	letters := make(map[string]int)
	letter := ""

	for i := 0; i < len(str); i++ {
		letter = string(str[i])
		number, ok := letters[letter]
		if ok {
			letters[letter] = number + 1
		} else {
			letters[letter] = 1
		}
	}
	return letters
}

func isEqual(s1, s2 string) bool {
	return reflect.DeepEqual(getLetters(s1), getLetters(s2))
}

func main() {
	fmt.Println(isEqual("listen", "silent"))
	fmt.Println(isEqual("hello", "world"))
	fmt.Println(isEqual("Dormitory", "Dirty room"))
}

```
# 2. Írj egy olyan függvényt python nyelven, ami az angol ábécé szerinti sorrendben összeadja egy megadott string betűit. pl. ac => 4 (mert a = 1 + c = 3) 
#### hint: ord('a') = 97, ord('c') = 99