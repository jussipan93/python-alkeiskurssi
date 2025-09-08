#kysytään köyttäjän biologinen sukupuoli ja hemoglobiini
sukupuoli = input("Anna biologinen sukupuoli (nainen/mies): ").lower()
hb = int(input("Anna hemoglobiiniarvo (g/l):"))

# Tarkistetaan arvot sukupuolen perusteella
if sukupuoli == "nainen":
    if hb < 117:
        print("Hemoglobiini arvo on matala.")
    elif hb <= 175:
        print("Hemoglobiini arvo on normaali.")
    else:
        print("Hemoglobiini arvo on korkea.")
elif sukupuoli == "mies":
    if hb < 134:
        print("Hemoglobiini arvo on matala.")
    elif hb <= 195:
        print("Hemoglobiini arvo on normaali.")
    else:
        print("Hemoglobiini arvo on korkea.")
else:
    print("Virheellinen sukupuoli syote")