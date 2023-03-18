from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.views.decorators.gzip import gzip_page
from .models import *
from django.conf import settings
from django.core.mail import send_mail


@gzip_page
def index(request):
    products = Product.objects.all()[:3]
    services = Service.objects.all()[:4]
    info = Information.objects.get(id=1)
    testimonial = Testimonial.objects.all()
    clients = Client.objects.all()
    cars = Carousal.objects.all()
    return render(request, 'index.html', {'products':products, 'services': services, 'information':info, 'carousals': cars, 'tag': "Salam", 'testimonial': testimonial, 'clients': clients})

def about(request):
    info = Information.objects.get(id=1)
    products = Product.objects.all()
    services = Service.objects.all()
    testimonial = Testimonial.objects.all()
    clients = Client.objects.all()
    return render(request, 'about.html', {'information':info, 'products':products, 'services': services, 'testimonial':testimonial, 'clients': clients})

def services(request):
    products = Product.objects.all()
    services = Service.objects.all()
    info = Information.objects.get(id=1)
    return render(request, 'service.html', {'products':products, 'services': services, 'information':info})

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
        text = f'''You have received a message from Burak HVAC Pvt. Ltd. website.
        Name: {name}
        Phone: {phone}
        Message: {message}'''
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['shaikharshi69@gmail.com', 'iamaladdin02@gmail.com']
        send_mail(subject=subject, message=text, from_email=email_from, recipient_list=recipient_list )
        # messages.success(request, 'Email Sent Successfully')
        return redirect('index')
    else:
        text = f'''You have received a message from Burak HVAC Pvt. Ltd. website.
        Name: {name}
        Email: {email}
        Message: {message}'''
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['shaikharshi69@gmail.com', 'iamaladdin02@gmail.com']
        send_mail(subject=subject, message=text, from_email=email_from, recipient_list=recipient_list )
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
            subject = 'Thank you for subscribing to our website.'
            text = f'''Your subscription has been confirmed!
              You are now part of our exclusive group of subscribers who will be the first to hear about our new products, services and promotions.'''
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject=subject, message=text, from_email=email_from, recipient_list=recipient_list )
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
        subject = 'You have received a resume from Burak HVAC Pvt. Ltd. website.'
        text = f'''
        Name of the candidate is {name} applying for the position of {position}. Check out his resume on https://web-production-d702.up.railway.app/admin/career
        Details of the candidate:
        Name: {name}
        Phone: {phone}
        Email: {email}
        Position: {position}
        Biodata: {about}'''
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['shaikharshi69@gmail.com', 'iamaladdin02@gmail.com']
        send_mail(subject=subject, message=text, from_email=email_from, recipient_list=recipient_list )
        return redirect('career', id=id)
    return render(request, 'career.html', {"career": car, 'information':info, 'products':products, 'services': services})

def faqs(request):
    products = Product.objects.all()
    services = Service.objects.all()
    info = Information.objects.get(id=1)
    return render(request, 'faq.html', {'information':info, 'products':products, 'services': services})