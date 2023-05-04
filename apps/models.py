import uuid

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Model, ForeignKey, CharField, ImageField, UUIDField, TextField, CASCADE, ManyToManyField, \
    FloatField
from django.utils.text import slugify


class Branch(Model):
    name = CharField(max_length=55)

    class Meta:
        verbose_name = 'Filial'
        verbose_name_plural = 'Filiallar'

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Branch.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = self._get_unique_slug()
        if force_update is True:
            self.name = slugify(self.name)
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)

    def __str__(self):
        return self.name


class Category(Model):
    name = CharField(max_length=55)

    class Meta:
        verbose_name = "Bo'lim"
        verbose_name_plural = "Bo'limlar"

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Category.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = self._get_unique_slug()
        if force_update is True:
            self.name = slugify(self.name)
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)

    def __str__(self):
        return self.name


class Tag(Model):
    name = CharField(max_length=125)

    class Meta:
        verbose_name = 'Hashtag'
        verbose_name_plural = 'Hashtaglar'

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Tag.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = self._get_unique_slug()
        if force_update is True:
            self.name = slugify(self.name)
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)

    def __str__(self):
        return self.name


class Blog(Model):
    title = CharField(max_length=55)
    text = TextField()
    image = ImageField(upload_to='blogs/%Y/%m/%d')
    category = ForeignKey('apps.Category', CASCADE)
    branch = ForeignKey('apps.Branch', CASCADE, null=True, blank=True)
    tag = ManyToManyField('apps.Tag')
    author = ForeignKey('user.User', CASCADE)
    rating = FloatField(
        validators=[
            MaxValueValidator(5, 'Should be 5'),
            MinValueValidator(1, 'Should be 1')
        ]
    )

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Bloglar'

    def __str__(self):
        return self.title

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Blog.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = self._get_unique_slug()
        if force_update is True:
            self.title = slugify(self.title)
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)
