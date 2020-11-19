from django.db import models


class Pet(models.Model):
    PET_TYPES = (
        ('Dog', 'dog'),
        ('Cat', 'cat'),
        ('Parrot', 'parrot'),
        ('UNKNOWN', 'unknown'),
    )
    type = models.CharField(max_length=7, choices=PET_TYPES, default='UNKNOWN')
    name = models.CharField(max_length=6, blank=False)
    age = models.IntegerField(blank=False)
    description = models.TextField(blank=False)
    image_url = models.ImageField(upload_to='images')

    def __str__(self):
        return f'{self.id}, {self.type}, {self.name}'

    class Meta:
        ordering = ['id']


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    test = models.CharField(max_length=2, blank=True)
