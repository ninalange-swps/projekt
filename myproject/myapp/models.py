from django.db import models

# Create your models here.

class Stanowisko(models.Model):
    nazwa = models.TextField(blank=False, null=False)
    opis = models.TextField(blank=True)

class Osoba(models.Model):
    imie = models.TextField(blank=False, null=False)
    nazwisko = models.TextField(blank=False, null=False)
    plec_wybor = (
        ("K", "Kobieta"),
        ("M", "Męczyzna "),
        ("I", "Inne")
    )
    plec = models.CharField(max_length=1, choices=plec_wybor)
    stanowisko = models.ForeignKey(Stanowisko, on_delete=models.CASCADE)

    data_dodania= models.DateField(auto_now=False, auto_now_add=True)


def __str__(self):
        return f"{self.imie} {self.nazwisko}"

class Meta:
        ordering = ['nazwisko']
