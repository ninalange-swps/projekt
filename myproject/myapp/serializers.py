from rest_framework import serializers
from .models import Person, Team, MONTHS, SHIRT_SIZES, Stanowisko, Osoba


class PersonSerializer(serializers.Serializer):

    # pole tylko do odczytu, tutaj dla id działa też autoincrement
    id = serializers.IntegerField(read_only=True)

    # pole wymagane
    name = serializers.CharField(required=True)

    # pole mapowane z klasy modelu, z podaniem wartości domyślnych
    # zwróć uwagę na zapisywaną wartość do bazy dla default={wybór}[0] oraz default={wybór}[0][0]
    # w pliku models.py SHIRT_SIZES oraz MONTHS zostały wyniesione jako stałe do poziomu zmiennych skryptu
    # (nie wewnątrz modelu)
    shirt_size = serializers.ChoiceField(choices=SHIRT_SIZES, default=SHIRT_SIZES[0][0])
    miesiac_dodania = serializers.ChoiceField(choices=MONTHS.choices, default=MONTHS.choices[0][0])

    # odzwierciedlenie pola w postaci klucza obcego
    # przy dodawaniu nowego obiektu możemy odwołać się do istniejącego poprzez inicjalizację nowego obiektu
    # np. team=Team({id}) lub wcześniejszym stworzeniu nowej instancji tej klasy
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())

    # przesłonięcie metody create() z klasy serializers.Serializer
    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    # przesłonięcie metody update() z klasy serializers.Serializer
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.shirt_size = validated_data.get('shirt_size', instance.shirt_size)
        instance.miesiac_dodania = validated_data.get('miesiac_dodania', instance.miesiac_dodania)
        instance.team = validated_data.get('team', instance.team)
        instance.save()
        return instance


# class PersonModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         # musimy wskazać klasę modelu
#         model = Person
#         # definiując poniższe pole możemy określić listę właściwości modelu,
#         # które chcemy serializować
#         fields = ['id', 'name', 'miesiac_dodania', 'shirt_size', 'team']
#         # definicja pola modelu tylko do odczytu
#         read_only_fields = ['id']



class StanowiskoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stanowisko
        fields = '__all__'

    def create(self, validated_data):
        return Stanowisko.objects.create(**validated_data)  

    def update(self, intance, validated_data):
        instance.nazwa = validatd_data.get('nazwa', instance.nazwa)
        instance.opis = validated_|data.get('opis', instance.opis)
        instance.save()
        return instance


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'country']
        read_only_fields = ['id']



class OsobaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Osoba
        fields = ['id', 'imie', 'nazwisko', 'plec', 'stanowisko', 'data_dodania']
        read_only_fields = ['id', 'data_dodania']



