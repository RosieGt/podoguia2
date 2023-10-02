from django.db import models

# Create your models here.
class Podologo(models.Model):
    nome = models.CharField("Nome", max_length=200)
    email = models.EmailField("Email", max_length=100)
    info = models.TextField("Informações", blank=True)
    whatsapp = models.CharField("Whatsapp", max_length=15, blank=True)
    endereco = models.CharField("Endereço", max_length=200, blank=True)
    avatar = models.ImageField("Avatar", upload_to="avatares", blank=True, null=True)

    def __str__(self):
        return self.nome