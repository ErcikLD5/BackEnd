from django.db import models

# Create your models here.

class Topic(models.Model):
    #Definir los campos que tiene la tabla
    top_name = models.CharField(max_length=100, unique=True)

    #Representa el registro como cadena de texto
    def __str__(self):
        return self.top_name
    
class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) #Llave foranea (nombre_tabla, metodo_de_eliminación)
    name = models.CharField(max_length = 100, unique = True)
    url = models.URLField(unique = True)

    def __str__(self):
        return self.name
    
class AccessRecord(models.Model):
    webname = models.ForeignKey(Webpage, on_delete = models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date) #Función str: Convierte fecha en cadena de texto

class Los_tres_mosqueteros(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField(unique = True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.email