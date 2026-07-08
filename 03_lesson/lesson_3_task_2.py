from smartphone import Smartphone


catalog = []

catalog.append(Smartphone("Apple", "iPhone", "+79111111111"))
catalog.append(Smartphone("Samsung", "Galaxy", "+79222222222"))
catalog.append(Smartphone("Xiaomi", "Redmi", "+79333333333"))
catalog.append(Smartphone("Google", "Pixel", "+79444444444"))
catalog.append(Smartphone("Ele", "ELephone", "+79555555555"))

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
