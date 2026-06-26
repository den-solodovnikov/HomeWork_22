from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Наименование кагории",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание категории",
        help_text="Введите описание категории",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ("name",)


class Product(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Наименование продукта",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        verbose_name="Описание продукта",
        help_text="Введите описание продукта",
        null=True,
        blank=True,
    )
    image = models.ImageField(
        upload_to="images/",
        verbose_name="Фото продукта",
        help_text="Загрузите фото продукта",
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        related_name="products",
    )
    price = models.FloatField(
        verbose_name="Цена товара",
        help_text="Введите цену товара",
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Введите дату создания",
        null=True,
        blank=True,
    )
    updated_at = models.DateField(
        auto_now=True,
        verbose_name="Дата последнего изменения",
        help_text="Введите дату изменения",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ("name", "created_at")


class Contact(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Имя",
        help_text="Введите имя"
    )
    phone = models.CharField(
        max_length=20,
        verbose_name="Телефон",
        help_text="Введите телефон",
        null=True,
        blank=True,
    )
    message = models.TextField(
        verbose_name="Сообщение",
        help_text="Введите ваше сообщение"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        ordering = ('name',)
