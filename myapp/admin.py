from django.contrib import admin
from .models import Service, ServiceDetail, Product, ProductDetail, Client, Career, Job, Subscription, Blog, Information, Carousal, BlogDetail, Project, Testimonial

class ServiceDetailAdmin(admin.StackedInline):
    model = ServiceDetail
    extra = 1

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    inlines = [ServiceDetailAdmin]
    class Meta:
       model = Service

class ProductDetailAdmin(admin.StackedInline):
    model = ProductDetail
    extra = 1
 
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductDetailAdmin]
    class Meta:
       model = Product

class BlogDetailAdmin(admin.StackedInline):
    model = BlogDetail
    extra = 1
    
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    inlines = [BlogDetailAdmin]
    class Meta:
       model = Blog

admin.site.register(Career)
admin.site.register(Job)
admin.site.register(Subscription)
admin.site.register(Information)
admin.site.register(Carousal)
admin.site.register(Project)
admin.site.register(Testimonial)
admin.site.register(Client)