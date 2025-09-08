# Kysytään käyttäjältä hyttiluokka
hyttiluokka = input("Anna hyttiluokka (LUX, A, B, C): ")

# Tarkistetaan syöte if/elif/else-rakenteella
if hyttiluokka == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif hyttiluokka == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hyttiluokka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hyttiluokka == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")