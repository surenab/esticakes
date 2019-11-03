from django.db import models

# Create your models here.
class Cake(models.Model):
    name = models.TextField(default=None, blank=True, null=True)
    price = models.FloatField(default=0,blank=True, null=True)
    description = models.TextField(default=None, blank=True, null=True)
    long_description = models.TextField(default='All ingredients are irish.', blank=True, null=True)
    ingredients = models.TextField(default='eggs,vegetable oil, milk, caster sugar, self-raising flour, baking powder, salt, chocolate, butter, fondant', blank=True, null=True)
    image1 = models.ImageField(upload_to='static/image', max_length=100, blank = True, null=True)
    image2 = models.ImageField(upload_to='static/image', max_length=100, blank = True, null=True)
    image3 = models.ImageField(upload_to='static/image', max_length=100, blank = True, null=True)
    image4 = models.ImageField(upload_to='static/image', max_length=100, blank = True, null=True)
    video =  models.FileField(upload_to='static/image', blank = True, null=True)

    CATEGORIES = (
        ('Muffins', 'Muffins'),
        ('Fondant_Cakes', 'Fondant_Cakes'),
        ('Cookies', 'Cookies'),
        ('Cakes', 'Cakes'),
        ('Desserts', 'Desserts'),
    )
    category = models.CharField('Category', max_length=25, choices=CATEGORIES, blank=False, default='Cakes')
    class Meta:
        ordering = ('-name',)
    def __str__(self):
        return self.name+str(self.price)
