from smartphone import Smartphone

catalog = []

phone1 = Smartphone("Sumsung", "K1", "+79009009090")
phone2 = Smartphone("Sumsung", "K2", "+79008008080")
phone3 = Smartphone("Sumsung", "K3", "+79007007070")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)

for phone in catalog:
    print(f"{phone.brand} - {phone.model} {phone.number}")
