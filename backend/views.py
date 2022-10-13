from django.shortcuts import render, redirect
from .models import Subscriber, Article
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    if request.method == "GET":
        context = {}
        return render(request, "index.html", context)
    else:
        email = request.POST.get("email")
        Subscriber.objects.create(email=email)
        sub = "Subscription successful"
        msg = f"Hello {email}, Thanks for subscribing us. Now you will get email"
        send_mail(sub, msg, settings.EMAIL_HOST_USER, [email], fail_silently=False)
        return redirect("/")
