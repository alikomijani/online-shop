from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
# Create your models here.


class Category(models.Model):
    slug = models.CharField(verbose_name=_(
        'Slug'), max_length=250, unique=True, db_index=True)
    name = models.CharField(verbose_name=_('Name'), max_length=250)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    slug = models.CharField(verbose_name=_(
        'Slug'), max_length=250, unique=True, db_index=True)
    name = models.CharField(verbose_name=_('Name'), max_length=250)
    description = models.TextField(verbose_name=_("Description"))
    price = models.IntegerField(verbose_name=_("Price"))
    # image = models.ImageField()
    discount = models.IntegerField(verbose_name=_("Discount"), default=0)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.name


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    text = models.TextField(verbose_name=_("Description"))
