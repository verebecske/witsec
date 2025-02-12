# Mit csinál a következő parancs?
1. sed -i 's/ 000/k/g' orszagok.md
2. cat orszagok.md | grep -v "ország" | wc -l 
3. awk -F\| '{ print $2 }' orszagok.md 

# Írj olyan parancsot ami:
4. kiírja azokat az országokat, aminek pontosan '57 000' a GDP/fő-je
5. eltávolítja a file nevű file-t ha létezik
