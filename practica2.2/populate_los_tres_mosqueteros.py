import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','practica1.settings')

import django
django.setup()

from primera_app.models import Los_tres_mosqueteros

from faker import Faker
faker_generator = Faker()

def populate(N=5):
    for entry in range(N):
        faker_first_name = faker_generator.first_name()
        faker_last_name = faker_generator.last_name()
        faker_email = faker_generator.email()
        faker_phone_number = faker_generator.phone_number()

        #Crear registro falso
        mosqueteros = Los_tres_mosqueteros.objects.get_or_create(first_name = faker_first_name, last_name = faker_last_name, email = faker_email, phone_number = faker_phone_number)[0]

if __name__ == '__main__':
    print("Comienzo a poblar")
    populate(30)
    print("Finalizado")