from django.db import models

# Create your models here.



CARACTERISTIK = (
    ('Avec manche', 'Avec manche'),
    ('Sans manche', 'Sans manche')
)

SPECIFIK = (
    ('Avec design', 'Avec design'),
    ('Sans design', 'Sans design')
)

class Categories(models.Model):
    reference = models.CharField('Reference', max_length=30)
    taille = models.CharField('Taille', max_length=100)
    pack_quantity = models.IntegerField('Quantité par pack')
    piece_quantity = models.IntegerField('Quantité par piece')
    price = models.FloatField('Prix')


    def __str__(self):

        return self.reference

    class Meta:
        verbose_name = "Categorie"

class Product(models.Model):

    picture = models.ImageField('Image', upload_to="img/%y")
    discription = models.TextField('Description',)
    available = models.BooleanField('Disponible', default=True)
    created_at = models.DateTimeField('Date de Creation', auto_now_add=True)
    categorie = models.ForeignKey(Categories, on_delete=models.CASCADE)
    caracterisk = models.CharField('Caracteristique', choices=CARACTERISTIK, max_length=20, default="Avec manche")
    specifik = models.CharField('Specificité', choices=SPECIFIK, max_length=20, default='Avec design')

    def __str__(self):
        return self.categorie.reference

    class Meta:
        verbose_name = "Produit"


class CustomersContact(models.Model):
    name = models.CharField('Nom', max_length=20)
    email = models.EmailField('E-mail', max_length=50)
    #phonenumber = models.CharField(max_length=15)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Client"

class Commands(models.Model):
    created_at = models.DateTimeField('Date d\'envoie', auto_now_add=True)
    contacted = models.BooleanField('Demande traitée ?', default=False)
    customers = models.ForeignKey(CustomersContact, on_delete=models.CASCADE)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.customers.name

    class Meta:
        verbose_name = "Commande"
