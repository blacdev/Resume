from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
# Create your views here.



def contactPage(request):
    form = ContactForm()
    if request.method == "POST":

        form = ContactForm(request.POST)

        if form.is_valid():
            forms = form.save()
            messages.success(request, "Enquiry sent!")
        return redirect("contact")
    context = {"form": form}
    return render(request, "index.html", context)
