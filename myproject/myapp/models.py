from django.db import models
from django.utils.timezone import now
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
MONTHS = models.IntegerChoices('Miesiace', 'Styczen Luty Marzec Kwiecien Maj Czerwiec Lipiec Sierpien Wrzesien Pazdziernik Listopad Grudzien')
PLCIE = models.IntegerChoices('PLEC', 'Kobieta Męzczyzna Inne')


SHIRT_SIZES = (
    ("S", "Small"),
    ("M", "Medium "),
    ("L", "Large")
)

class Team(models.Model):
    name = models.CharField(max_length=60)
    country = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.name}'

class Person(models.Model):
    name = models.CharField(max_length=60)
    pseudonim = models.CharField(max_length=80, default="")
    shirt_size = models.CharField(max_length=1, choices = SHIRT_SIZES, default = SHIRT_SIZES)
    month_added = models.IntegerField(choices = MONTHS.choices, default = MONTHS.choices[0][0])
    team = models.ForeignKey(Team, null = True, blank = True, on_delete=models.SET_NULL)

def __str__(self):
    return f"Person : {self.name}, dodana w {self.month_added}, o rozmiarze koszuli {self.shirt_size}." 
    


class Osoba(models.Model):
    PLEC_CHOICES = (
        ("K", "Kobieta"),
        ("M", "Męzczyzna "),
        ("I", "Inne")
    )

    imie = models.CharField(max_length=40, blank = False, null = False)
    nazwisko = models.CharField(max_length=60, blank = False, null = False )
    plec = models.IntegerField(choices = PLCIE.choices, default = PLCIE.choices[2][0])
    stanowisko = models.ForeignKey('Stanowisko', on_delete = models.CASCADE)
    data_dodania = models.DateField(default = date.today, blank = False, null = False)
    wlasciciel = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    
    def __str__(self):
        return f'{self.imie} {self.nazwisko}'
    
    class Meta:
        ordering = ["nazwisko"]
        permissions =[
            ("view_person_other_owner", "pozwla zobaczyc modele Osoba innych wlascicieli"),
        ]

        



class Stanowisko(models.Model):
    nazwa = models.CharField(max_length=100)
    opis = models.TextField(blank=True)

    def __str__(self):
        return self.nazwa


    
    
    