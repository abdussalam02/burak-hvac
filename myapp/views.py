from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import *
import smtplib

EMAIL = "engineerak569@gmail.com"
PASSWORD = "jueianotflghxrwv"

def index(request):
    products = Product.objects.all()[:3]
    services = Service.objects.all()[:4]
    info = Information.objects.get(id=1)
    testimonial = Testimonial.objects.all()
    cars = Carousal.objects.all()
    return render(request, 'index.html', {'products':products, 'services': services, 'information':info, 'carousals': cars, 'tag': "Salam", 'testimonial': testimonial})

def about(request):
    info = Information.objects.get(id=1)
    products = Product.objects.all()
    services = Service.objects.all()
    testimonial = Testimonial.objects.all()
    return render(request, 'about.html', {'information':info, 'products':products, 'services': services, 'testimonial':testimonial})

def services(request):
    products = Product.objects.all()
    services = Service.objects.all()
    info = Information.objects.get(id=1)
    testimonial = Testimonial.objects.all()
    return render(request, 'service.html', {'products':products, 'services': services, 'information':info, 'testimonial':testimonial})

def service_details(request, slug):
    products = Product.objects.all()
    services = Service.objects.all()
    service = Service.objects.get(slug=slug)
    details = ServiceDetail.objects.filter(service=service).all()
    info = Information.objects.get(id=1)
    return render(request, "service-details.html", {"service":service, 'products':products, 'services': services, 'details': details, 'information':info, "related_services": services.reverse()[:3]})

def products(request):
    products = Product.objects.all()
    services = Service.objects.all()
    info = Information.objects.get(id=1)
    return render(request, 'products.html', {'products':products, 'services': services, 'information':info})
    
def product_details(request, slug):
    products = Product.objects.all()
    services = Service.objects.all()
    product = Product.objects.get(slug=slug)
    data = ProductDetail.objects.filter(product=product).all()
    info = Information.objects.get(id=1)
    return render(request, 'product-details.html', {'products':products, 'services': services, 'product':product, "details":data, 'information':info, "related_products": products.reverse()[:3]})


def jobs(request):
    products = Product.objects.all()
    services = Service.objects.all()
    info = Information.objects.get(id=1)
    data = Job.objects.all()
    return render(request, 'jobs.html', {"jobs": data, 'information':info, 'products':products, 'services': services,}) 


def contact(request):
    products = Product.objects.all()
    services = Service.objects.all()
    info = Information.objects.get(id=1)
    return render(request, 'contact.html', {'information':info, 'products':products, 'services': services})


def blogs(request):
    products = Product.objects.all()
    services = Service.objects.all()
    data = Blog.objects.all()
    info = Information.objects.get(id=1)
    return render(request, "blog.html", {"blogs":data, 'information':info, 'products':products, 'services': services})


def blog_details(request, slug):
    products = Product.objects.all()
    services = Service.objects.all()
    info = Information.objects.get(id=1)
    data = Blog.objects.get(slug=slug)
    blogs = BlogDetail.objects.filter(blog=data).all()
    return render(request, "blog-details.html", {"blogs": blogs, "data":data, 'information':info, 'products':products, 'services': services})

def message(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    subject = request.POST.get('subject')
    message = request.POST.get('message')
    if phone !=  None:
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=EMAIL, password = PASSWORD)
            connection.sendmail(from_addr=EMAIL, to_addrs=['shaikharshi69@gmail.com', 'iamaladdin02@gmail.com'], msg = f'subject : {subject}\n\n Name: {name}\n Phone:{phone}\n Message:{message} ')
        # messages.success(request, 'Email Sent Successfully')
        return redirect('index')
    else:
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=EMAIL, password = PASSWORD)
            connection.sendmail(from_addr=EMAIL, to_addrs=['shaikharshi69@gmail.com', 'iamaladdin02@gmail.com'], msg = f'subject : {subject}\n\n Name: {name}\n Email:{email}\n Message:{message} ')
        # messages.success(request, 'Email Sent Successfully')
        return redirect('contact')

def projects(request):    
    products = Product.objects.all()
    services = Service.objects.all()
    info = Information.objects.get(id=1)
    data = Project.objects.all()
    return render(request, 'project.html' ,{"projects":data, 'information':info, 'products':products, 'services': services})

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            validate_email(email)
        except ValidationError as e:
            return redirect('index')

        if not Subscription.objects.filter(email=email).exists():
            Subscription(email=email).save()
            with smtplib.SMTP('smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(user=EMAIL, password = PASSWORD)
                connection.sendmail(from_addr=EMAIL, to_addrs=email, msg = f'subject : Thank you for subscribing to our website.\n\nYour subscription has been confirmed! You are now part of our exclusive group of subscribers who will be the first to hear about our new products, services and promotions.')
            # messages.success(request, 'Email Sent Successfully')
    return redirect('index')

def jobs(request):
    products = Product.objects.all()
    services = Service.objects.all()
    info = Information.objects.get(id=1)
    data = Job.objects.all()
    return render(request, 'jobs.html', {"jobs": data, 'information':info, 'products':products, 'services': services})


def careers(request, id):
    products = Product.objects.all()
    services = Service.objects.all()
    info = Information.objects.get(id=1)
    car = Job.objects.get(id=id)
    if request.method=='POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        position = request.POST.get('position')
        about = request.POST.get('about')
        resume = request.FILES.get('resume')
        data = Career(name=name, phone = phone, email=email, position=position, about=about, resume=resume )
        data.save()
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=EMAIL, password = PASSWORD)
            connection.sendmail(from_addr=EMAIL, to_addrs=['iamaladdin02@gmail.com', 'shaikharshi69@gmail.com'], msg = f'subject : you have recieved a resume.\n\n Name of the candidate is {name} applying for the position of {position}. Check out his resume on https://127.0.0.1:8000/admin/career')
        return redirect('career', id=id)
    return render(request, 'career.html', {"career": car, 'information':info, 'products':products, 'services': services})

def faqs(request):
    products = Product.objects.all()
    services = Service.objects.all()
    info = Information.objects.get(id=1)
    return render(request, 'faq.html', {'information':info, 'products':products, 'services': services})