from django.db import models
from froala_editor.fields import FroalaField
from .helpers import generate_slug, compress_img
from django.utils.html import mark_safe

class Information(models.Model):
    phone = models.CharField(max_length=15)
    phone_2 = models.CharField(max_length=15)
    branch = models.PositiveIntegerField(default=1)
    projects = models.PositiveIntegerField(default=1)
    clients = models.PositiveIntegerField(default=1)
    members = models.PositiveIntegerField(default=1)
    experience = models.PositiveIntegerField(default=1)
    address = models.CharField(max_length=255)
    email = models.EmailField(max_length=200)
    whatsapp = models.URLField(max_length=200)
    facebook = models.URLField(max_length=200)
    twitter = models.URLField(max_length=200)
    instagram = models.URLField(max_length=200)
    linkedin = models.URLField(max_length=200)
    
    def __str__(self) -> str:
        return str(self.email)

class Carousal(models.Model):
    heading = models.CharField(max_length=255)
    sub_heading = models.CharField(max_length=255)
    image = models.ImageField(upload_to='carousal', help_text='Upload image of size 1900 x 900')
    video = models.URLField(max_length=200)

    def save(self, *args, **kwargs):
        new_image = compress_img(self.image)
        self.image = new_image
        super(Carousal, self).save(*args, **kwargs)

    def image_tag(self):
        if self.image:    
            return mark_safe('<img src="/media/%s" width="350" height="175" style="border-radius: 10px; padding:5px; border : 2px solid grey" />' % (self.image))
        else:
            return mark_safe('<p> No preview Available </p>')

    image_tag.short_description = 'Image Preview'

    def __str__(self) -> str:
        return str(self.heading)


class Service(models.Model):
    image = models.ImageField(upload_to='service', help_text='Upload image of size 350 x 300')
    title = models.CharField(max_length=255, null=False)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    description = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        new_image = compress_img(self.image)
        self.image = new_image
        super(Service, self).save(*args, **kwargs)

    def image_tag(self):
        if self.image:    
            return mark_safe('<img src="/media/%s" width="150" height="125" style="border-radius: 10px; padding:5px; border : 2px solid grey" />' % (self.image))
        else:
            return mark_safe('<p> No preview Available </p>')

    image_tag.short_description = 'Image Preview'

    def __str__(self) -> str:
        return str(self.title)

ALIGN_IMAGE = (
    ("LEFT", "LEFT"),
    ("RIGHT", "RIGHT")
)

class ServiceDetail(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='service', help_text='Upload image of size 400 x 350')
    align_image = models.CharField(choices=ALIGN_IMAGE, max_length=10)
    heading = models.CharField(max_length=255, null=True)
    description = FroalaField()

    def save(self, *args, **kwargs):
        new_image = compress_img(self.image)
        self.image = new_image
        super(ServiceDetail, self).save(*args, **kwargs)

    def image_tag(self):
        if self.image:    
            return mark_safe('<img src="/media/%s" width="150" height="125" style="border-radius: 10px; padding:5px; border : 2px solid grey" />' % (self.image))
        else:
            return mark_safe('<p> No preview Available </p>')

    image_tag.short_description = 'Image Preview'

    def __str__(self) -> str:
        return str(self.service.title)
    

class Product(models.Model):
    image = models.ImageField(upload_to='product', help_text='Upload image of size 350 x 300')
    title = models.CharField(max_length=255, null=False)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    description = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        new_image = compress_img(self.image)
        self.image = new_image
        super(Product, self).save(*args, **kwargs)

    def image_tag(self):
        if self.image:    
            return mark_safe('<img src="/media/%s" width="150" height="125" style="border-radius: 10px; padding:5px; border : 2px solid grey" />' % (self.image))
        else:
            return mark_safe('<p> No preview Available </p>')

    image_tag.short_description = 'Image Preview'

    def __str__(self) -> str:
        return str(self.title)
    
class ProductDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product', help_text='Upload image of size 400 x 350')
    align_image = models.CharField(choices=ALIGN_IMAGE, max_length=10)
    heading = models.CharField(max_length=255, null=True)
    description = FroalaField()

    def save(self, *args, **kwargs):
        new_image = compress_img(self.image)
        self.image = new_image
        super(ProductDetail, self).save(*args, **kwargs)

    def image_tag(self):
        if self.image:    
            return mark_safe('<img src="/media/%s" width="150" height="125" style="border-radius: 10px; padding:5px; border : 2px solid grey" />' % (self.image))
        else:
            return mark_safe('<p> No preview Available </p>')

    image_tag.short_description = 'Image Preview'

    def __str__(self) -> str:
        return str(self.product.title)
    

class Career(models.Model):
    name = models.CharField(max_length=255, blank=False)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=255)
    position = models.CharField(max_length=255)
    about = models.TextField()
    resume = models.FileField(upload_to='resume')
    
    def __str__(self) -> str:
        return str(self.name)


class Job(models.Model):
    position = models.CharField(max_length=255, blank=False)
    description = models.TextField()
    type = models.CharField(max_length=255, blank=False)
    pay = models.CharField(max_length=255)

    def __str__(self) -> str:
        return str(self.position)

class Subscription(models.Model):
    email = models.EmailField(unique=True)
    
    def __str__(self) -> str:
        return str(self.email)
    
PROJECT_CATEGORY = (
    ("Testing", "Testing"),
    ("Cleaning", "Cleaning"),
    ("Repair", "Repair"),
    ("Heating", "Heating")
)

class Portfolio(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(choices=PROJECT_CATEGORY, max_length=20)
    image = models.ImageField(upload_to='projects', help_text='Upload image of size 350 x 400')

    def save(self, *args, **kwargs):
        new_image = compress_img(self.image)
        self.image = new_image
        super(Portfolio, self).save(*args, **kwargs)

    def image_tag(self):
        if self.image:    
            return mark_safe('<img src="/media/%s" width="130" height="150" style="border-radius: 10px; padding:5px; border : 2px solid grey" />' % (self.image))
        else:
            return mark_safe('<p> No preview Available </p>')

    image_tag.short_description = 'Image Preview'

    def __str__(self) -> str:
        return str(self.name)

class Blog(models.Model):
    image = models.ImageField(upload_to="blogs", null=False, help_text='Upload image of size 350 x 350')
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    description = models.TextField()
    posted_by = models.CharField(max_length=255, null=True)

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        new_image = compress_img(self.image)
        self.image = new_image
        super(Blog, self).save(*args, **kwargs)

    def image_tag(self):
        if self.image:    
            return mark_safe('<img src="/media/%s" width="150" height="125" style="border-radius: 10px; padding:5px; border : 2px solid grey" />' % (self.image))
        else:
            return mark_safe('<p> No preview Available </p>')

    image_tag.short_description = 'Image Preview'

    def __str__(self) -> str:
        return str(self.title)
    
class BlogDetail(models.Model):
    blog = models.ForeignKey(Blog, related_name="blogs", on_delete=models.CASCADE)
    writing = FroalaField()

    def __str__(self) -> str:
        return str(self.blog.title)
    
class Testimonial(models.Model):
    name = models.CharField(max_length=255, null=False)
    photo = models.ImageField(upload_to='testimonial')
    designation = models.CharField(max_length=255, null=False)
    comment = models.TextField()

    def save(self, *args, **kwargs):
        new_image = compress_img(self.photo)
        self.photo = new_image
        super(Testimonial, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return str(self.name)

class Client(models.Model):
    name = models.CharField(max_length=255, null=False)
    logo = models.ImageField(upload_to='clients', help_text='Upload image of size 150 x 40')

    def save(self, *args, **kwargs):
        new_image = compress_img(self.logo)
        self.logo = new_image
        super(Client, self).save(*args, **kwargs)

    def image_tag(self):
        if self.image:    
            return mark_safe('<img src="/media/%s" width="50" height="25" style="border-radius: 10px; padding:5px; border : 2px solid grey" />' % (self.logo))
        else:
            return mark_safe('<p> No preview Available </p>')

    image_tag.short_description = 'Image Preview'

    def __str__(self) -> str:
        return str(self.name)