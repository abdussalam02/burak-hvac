from django.contrib import admin
from .models import Service, ServiceDetail, Product, ProductDetail, Client, Career, Job, Subscription, Blog, Information, Carousal, BlogDetail, Project, Testimonial

class ServiceDetailAdmin(admin.StackedInline):
    model = ServiceDetail
    extra = 1

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    inlines = [ServiceDetailAdmin]
    fields = ['title', 'image', 'image_tag', 'slug', 'description']
    readonly_fields = ['image_tag']
    class Meta:
       model = Service

class ProductDetailAdmin(admin.StackedInline):
    model = ProductDetail
    extra = 1
 
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductDetailAdmin]
    fields = ['title', 'image', 'image_tag', 'slug', 'description']
    readonly_fields = ['image_tag']
    class Meta:
       model = Product

class BlogDetailAdmin(admin.StackedInline):
    model = BlogDetail
    extra = 1
    
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    inlines = [BlogDetailAdmin]
    fields = ['title', 'image', 'image_tag', 'slug', 'description', 'posted_by']
    readonly_fields = ['image_tag']
    class Meta:
       model = Blog

@admin.register(Carousal)
class CarousalAdmin(admin.ModelAdmin):
    fields = ['heading', 'sub_heading', 'image', 'image_tag', 'video']
    readonly_fields = ['image_tag']
    class Meta:
       model = Carousal

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    fields = ['name', 'category', 'image', 'image_tag']
    readonly_fields = ['image_tag']
    class Meta:
       model = Project

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    fields = ['name', 'logo', 'image_tag']
    readonly_fields = ['image_tag']
    class Meta:
       model = Client

admin.site.register(Career)
admin.site.register(Job)
admin.site.register(Subscription)
admin.site.register(Information)
admin.site.register(Testimonial)