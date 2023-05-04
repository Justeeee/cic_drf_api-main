from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Model, CharField, IntegerField, ForeignKey, SET_NULL, CASCADE, FloatField, EmailField, \
    SlugField
from django.utils.text import slugify


# Create your models here.
class User(Model):
    choices = (
        ("1", "Student"),
        ("2", "Admin"),
        ("3", "Journalist"),
        ("4", "Copywriter"),
    )
    slug = SlugField(unique=True, null=True, blank=True)
    nickname = CharField(max_length=255)
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    email = EmailField()
    age = IntegerField()
    branch = ForeignKey('apps.Branch', CASCADE)
    grade = IntegerField(
        validators=[
            MaxValueValidator(11, 'Should be 11'),
            MinValueValidator(1, 'Should be 1')
        ]
    )

    def __str__(self):
        return f"{self.nickname}/{self.first_name} {self.last_name}"

    def _get_unique_slug(self):
        slug = slugify(self.nickname)
        unique_slug = slug
        num = 1
        while User.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = self._get_unique_slug()
        if force_update is True:
            self.nickname = slugify(self.nickname)
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)

