import uuid

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Model, ForeignKey, CharField, ImageField, UUIDField, TextField, CASCADE, ManyToManyField, \
    FloatField, SET_NULL, DateTimeField, SmallIntegerField, SlugField
from django.utils.text import slugify

from core import settings
from shared.models import BaseModel


# auto directory
def upload_directory_name(instance, filename):
    return f'blogs/{instance.blog.id}/{filename}'


# model for Branches

class Branch(BaseModel):
    name = CharField(max_length=55)
    slug = SlugField(unique=True, null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    # UNIQUE SLUG

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Branch.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    # SAVE UNIQUE SLUG

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = self._get_unique_slug()
        if force_update is True:
            self.name = slugify(self.name)
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)

    def __str__(self):
        return self.name


# model for Category

# class Category(Model):
#     name = CharField(max_length=55)
#     slug = SlugField(unique=True, null=True, blank=True)
#
#     class MPTTMeta:
#         order_insertion_by = ['name']
#
#     UNIQUE SLUG
#
#     def _get_unique_slug(self):
#         slug = slugify(self.name)
#         unique_slug = slug
#         num = 1
#         while Category.objects.filter(slug=unique_slug).exists():
#             unique_slug = '{}-{}'.format(slug, num)
#             num += 1
#         return unique_slug
#
#     SAVE UNIQUE SLUG
#
#     def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
#         self.slug = self._get_unique_slug()
#         if force_update is True:
#             self.name = slugify(self.name)
#         super().save(force_insert=False, force_update=False, using=None, update_fields=None)
#
#     # def __str__(self):
#     #     return self.name
#
#
# model for Tags

class Tag(BaseModel):
    slug = SlugField(unique=True, null=True, blank=True)
    name = CharField(max_length=125)

    class MPTTMeta:
        order_insertion_by = ['name']

    #     UNIQUE SLUG

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Tag.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    #     SAVE UNIQUE SLUG

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = self._get_unique_slug()
        if force_update is True:
            self.name = slugify(self.name)
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)

    def __str__(self):
        return self.name


# model for Blog
class Blog(BaseModel):
    slug = SlugField(unique=True, null=True, blank=True)
    title = CharField(max_length=55)
    text = TextField()

    # category = ForeignKey('apps.Category', CASCADE)
    branch = ForeignKey('apps.Branch', CASCADE, null=True, blank=True)
    tag = ManyToManyField('apps.Tag')

    author = CharField(max_length=255)

    # rating = FloatField(
    #     validators=[
    #         MaxValueValidator(5, 'Should be 5'),
    #         MinValueValidator(1, 'Should be 1')
    #     ]
    # )

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.title

    # UNIQUE SLUG
    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Blog.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    # SAVE UNIQUE SLUG

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = self._get_unique_slug()
        if force_update is True:
            self.title = slugify(self.title)
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)

        User = get_user_model()
        users = User.objects.values()
        # print(users[0]['email'])
        for i in range(users.last()['id']):
            try:
                send_mail(
                    subject=f"Check out this new article - {self.title}",
                    message=f"Hello, {users[i]['first_name']}{users[i]['last_name']}!\nBe first to check out our new article published by{self.author}!",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[users[i]['email']]
                )
            except:
                print(
                    f"Hello, {users[i]['first_name']}{users[i]['last_name']}!\nBe first to check out our new article published by{self.author}!")


# model for Blogs' images
class BlogImages(BaseModel):
    blog = ForeignKey('Blog', CASCADE)
    image = ImageField(upload_to=upload_directory_name)

    def __str__(self):
        return f'{self.blog.title} -> {self.image.name}'


# model for Blogs' comments
# class BlogComment(Model):
#     blog = ForeignKey('Blog', CASCADE)
#     headline = CharField(max_length=255)
#     text = TextField()
#     author = ForeignKey('user.User', CASCADE)
#     rate = SmallIntegerField(default=0)
#     updated_at = DateTimeField(auto_now=True)
#     created_at = DateTimeField(auto_now_add=True)
#
#
# # model for Blogs' comments
# class BlogCommentImage(Model):
#     comment = ForeignKey('BlogComment', CASCADE)
#     picture = ImageField(upload_to='comments/')


class Creators(BaseModel):
    slug = SlugField(unique=True, null=True, blank=True)
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    role = CharField(max_length=255)
    photo = ImageField(upload_to=f'creators/')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class MPTTMeta:
        order_insertion_by = ['first_name', 'last_name']

    #     UNIQUE SLUG

    def _get_unique_slug(self):
        slug = slugify(self.first_name + self.last_name)
        unique_slug = slug
        num = 1
        while Tag.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    #     SAVE UNIQUE SLUG

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = self._get_unique_slug()
        if force_update is True:
            self.name = slugify(self.first_name + self.last_name)
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)

