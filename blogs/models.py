from django.core.mail import send_mail
from django.db import models
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _

from config import settings


class Blog(models.Model):
    CHOICES = [
        (True, _('Да')),
        (False, _('Нет')),
    ]

    title = models.CharField(
        max_length=150,
        verbose_name="Заголовок записи",
        help_text="Введите заголовок записи",
    )
    content = models.TextField(
        verbose_name="Содержимое",
        help_text="Введите текст",
        null=True,
        blank=True,
    )
    image = models.ImageField(
        upload_to="images/",
        verbose_name="Превью",
        help_text="Загрузите изорбражение",
        null=True,
        blank=True,
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Введите дату создания",
        null=True,
        blank=True,
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name=_("Активен"),
        help_text="Выберите значение",
        choices=CHOICES,
    )
    views_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Укажите количество просмотров",
        default=0,
    )
    is_notification_sent = models.BooleanField(
        verbose_name=_("Сообщение отправлено"),
        help_text="Выберите значение",
        default=False,
        choices=CHOICES,
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """ Переопределяем метод: Отправляем письмо на указанный e-mail при достижении 100 просмотров. """
        # Проверяем, достигли ли 100 просмотров и не отправляли ли письмо ранее
        if self.views_counter >= 100 and not self.is_notification_sent:
            print(f'{self.views_counter} достиг 100')
            try:
                send_mail(
                    subject='Поздравляем! Статья набрала 100 просмотров!',
                    message=f'Ваша статья "{self.title}" достигла отметки в 100 просмотров.',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=['densfmost01@gmail.com'],  # Ваша почта
                    fail_silently=False,
                )
                self.is_notification_sent = True
                return HttpResponse('Письмо успешно отправлено!')

            except Exception as e:
                return HttpResponse(f'Ошибка при отправке: {e}')

        super().save(*args, **kwargs)


    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
        ordering = ("title", "created_at")
