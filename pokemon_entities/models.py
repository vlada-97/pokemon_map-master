from urllib import request
from django.db import models


class Pokemon(models.Model):
    text = models.TextField('Описание', blank=True)
    title = models.CharField('Название', max_length=200, blank=True)
    photo = models.ImageField('Изображение покемона', blank=True)
    title_en = models.CharField(
        'Название (англ.)', max_length=200, blank=True)
    title_jp = models.CharField(
        'Название (яп.)', max_length=200, blank=True)
    id = models.AutoField(primary_key=True)
    previous_evolution = models.ForeignKey(
        "Pokemon",
        on_delete=models.SET_NULL,
        verbose_name='Предыдущая эволюция',
        null=True,
        blank=True,
        related_name="next_evolutions",
    )


    def __str__(self):
        return f'{self.title}'
    
    
    class Meta:
        verbose_name = 'Тип покемона'
        verbose_name_plural = 'Типы покемонов'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon, on_delete=models.CASCADE,verbose_name='Модель покемона', blank=True, null=True)
    lat = models.FloatField('Широта')
    lon = models.FloatField('Долгота')
    appeared_at = models.DateTimeField('Время появления')
    disappeared_at = models.DateTimeField('Время исчезновения')
    level = models.IntegerField('Уровень',null=True, blank=True)
    health = models.IntegerField('Здоровье',null=True, blank=True)
    strength = models.IntegerField('Атака',null=True, blank=True)
    defence = models.IntegerField('Защита',null=True, blank=True)
    stamina = models.IntegerField('Выносливость',null=True, blank=True)
    
    def __str__(self):
        return f'{self.pokemon}: {self.lat}, {self.lon}'
    
    
    class Meta:
        verbose_name = 'Покемон'
        verbose_name_plural = 'Покемоны'
