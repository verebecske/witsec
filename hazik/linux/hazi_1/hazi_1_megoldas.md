# Megoldások
1. kilistázza a nevek közül azokat, ami K-val vagy S-sel kezdődnek és a-ra végződnek
2. létrehoz egy zeros.txt file-t amiben 1*100 byte 0-t tesz
3. `touch f3.txt`
4. `mkdir -p m1/m2`
5. `file hazi_1_5`

+1: 
`cat nevek.txt | nl | grep "[lL]i" | head -3 | tail -1`
vagy
`nl nevek.txt | grep -i li | head -3 | tail -1`