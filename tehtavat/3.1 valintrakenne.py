
alamitta = 37

#kysytään käyttäjältä kuhan pituus
pituus = float(input("Anna kuhan pituus (cm): "))
if pituus < alamitta:
    puuttuu = alamitta - pituus
    print(f"Kuha alamittainen. Laske kuha takaisin jarveen!")
    print(f"Kuha on {puuttuu} cm liian lyhyt.")
else:
    print("Kuha on sallitun kokoinen. Voit pitää sen.")