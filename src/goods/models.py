from django.db import models

# Create your models here.

class Categories(models.Model):
    name = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="Название"
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True,
        null=True,
        verbose_name="URL address"
    )

    class Meta:
        # by default name app + class name.
        # example: app goods + class categories = goods_categories
        db_table = "category"
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name + ': ' + str(self.pk)

class Products(models.Model):
    name = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="Название"
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True,
        null=True,
        verbose_name="URL address"
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True
    )
    image = models.ImageField(
        verbose_name="Изображение",
        upload_to="goods_images",
        blank=True,
        null=True
    )
    price = models.DecimalField(
        verbose_name="Цена",
        default=0.00,
        max_digits=7,
        decimal_places=2
    )
    discount = models.DecimalField(
        verbose_name="Скидка в процентах",
        default=0.00,
        max_digits=7,
        decimal_places=2
    )
    quantity = models.PositiveIntegerField(
        verbose_name="Количество",
        default=0
    )
    category = models.ForeignKey(
        to=Categories,
        on_delete=models.CASCADE
    )

    class Meta:
        # by default name app + class name.
        # example: app goods + class categories = goods_categories
        db_table = "product"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.slug + ': ' + str(self.pk)

    def display_id(self):
        return f"{self.id:05}"

    def sell_price(self):
        if self.discount:
            return round(self.price - (self.price * self.discount / 100), 2)

        return self.price
