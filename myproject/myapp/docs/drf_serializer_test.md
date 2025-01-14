from myapp.models import Osoba, Stanowisko
from myapp.serializers import OsobaSerializer, StanowiskoSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# Tworzymy nowe obiekty
stanowisko = Stanowisko.objects.create(nazwa="Kierownik", opis="Zarządza tymi, co zarządzają")
osoba = Osoba.objects.create(imie="Jan", nazwisko="Malinowski", plec=2, stanowisko=stanowisko)

# Serializacja obiektu Osoba
osoba_serializer = OsobaSerializer(osoba)
print(osoba_serializer.data)

# Serializacja do JSON
osoba_json = JSONRenderer().render(osoba_serializer.data)

import io

# Deserializacja z JSON
stream = io.BytesIO(osoba_json)
data = JSONParser().parse(stream)
deserializer = OsobaSerializer(data=data)

# Walidacja danych
print(deserializer.is_valid())
print(deserializer.errors)

# Błędne dane
invalid_data = {'imie': 'Adam', 'nazwisko': 'Nowak', 'plec': 'kobieta', 'stanowisko': stanowisko.id}
invalid_serializer = OsobaSerializer(data=invalid_data)
print(invalid_serializer.is_valid())
print(invalid_serializer.errors)

# Zapis do bazy danych
if deserializer.is_valid():
    deserializer.save()

# Serializacja obiektu Stanowisko
stanowisko_serializer = StanowiskoSerializer(stanowisko)
print(stanowisko_serializer.data)

# Serializacja do JSON
stanowisko_json = JSONRenderer().render(stanowisko_serializer.data)
print(stanowisko_json)

# Deserializacja
stream = io.BytesIO(stanowisko_json)
data = JSONParser().parse(stream)

deserializer = StanowiskoSerializer(data=data)

print(deserializer.is_valid())

if deserializer.is_valid():
    deserializer.save()