from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField('имя пользователя', max_length=30)
    last_name = models.CharField('фамилия пользователя', max_length=30)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    @property
    def full_name(self):
        return f"{self.name} {self.last_name}"

    def __str__(self):
        return self.email


class Post(models.Model):
    author = models.ForeignKey("CustomUser", on_delete=models.SET_NULL,
                               related_name="posts", null=True)
    tags = models.ManyToManyField("Tag", blank=True, related_name="posts")
    title = models.CharField('заголовок', max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    body = models.TextField('пост', blank=True, db_index=True)
    date_pub = models.DateTimeField('дата публикациии', auto_now_add=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})


class Tag(models.Model):
    title = models.CharField('заголовок тэга', max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'тэг'
        verbose_name_plural = 'тэги'
