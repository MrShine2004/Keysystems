from django.db import models

class Country(models.Model):
    name = models.CharField(verbose_name="Название", max_length=100)
    kode = models.IntegerField()
    capital = models.CharField(verbose_name="Столица", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"


class Parts(models.Model):
    name = models.CharField(verbose_name="Название", max_length=100)
    manufacturer = models.CharField(verbose_name="Производитель", max_length=100)
    price = models.DecimalField(verbose_name="Цена", max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Запчасть"
        verbose_name_plural = "Запчасти"


class Car(models.Model):
    brand = models.CharField(verbose_name="Марка", max_length=100)
    model = models.CharField(verbose_name="Модель", max_length=100)
    year = models.IntegerField(verbose_name="Год производства")
    country = models.ForeignKey(Country, verbose_name="Страна производства", on_delete=models.CASCADE)
    parts = models.ManyToManyField(Parts, verbose_name="Запчасти", related_name="cars")
    image = models.ImageField(upload_to='cars/', verbose_name="Изображение", null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.model} {self.year}"

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"
