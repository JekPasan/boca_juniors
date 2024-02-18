from django.db import models
    

def rating_validator(val):
    if not type(val) == type(1):
        val = int(val)
    if val >= 10:
        return 10
    elif val <= 0:
        return 0
    return val
    

class Aliment(models.Model):
    nume = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[rating_validator])

    def __str__(self):
        return self.nume
