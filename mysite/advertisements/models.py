from django.db import models


# Create your models here.
class Advertisement(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=60)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    auction = models.BooleanField(help_text="Торг")
    create_ad = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'id={self.id} title={self.title}, price={self.price}'

    class Meta:
        db_table = 'advertisement'
