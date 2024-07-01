from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class Member(models.Model):
    member_user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.member_user.username.title()

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name.title()

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Announcement(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    author = models.ForeignKey(Member, on_delete=models.CASCADE)
    dateCreation = models.DateTimeField(auto_now_add=True)
    announcementCategory = models.OneToOneField(Category, on_delete=models.CASCADE)

    def preview(self):
        return f'{self.text[0: 124]}...'

    def __str__(self):
        return f'{self.id} {self.title}'

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class AnnouncementCategory(models.Model):
    announcementThrough = models.ForeignKey(Announcement, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.categoryThrough.name.title()}/Объявление {self.announcementThrough.id}'

    class Meta:
        verbose_name = 'Категория объявления'
        verbose_name_plural = 'Категории объявлений'


class Respond(models.Model):
    author = models.ForeignKey(Member, on_delete=models.CASCADE)
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE)
    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'Отклик'
        verbose_name_plural = 'Отклики'


class Subscriber(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )
