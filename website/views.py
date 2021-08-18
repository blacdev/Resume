from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
# from MyFooodApp.settings import EMAIL_HOST_USER
# Create your views here.
# def home(request):
#     return render(request,"index.html")


def contactPage(request):
    if request.method == "POST":

        form = ContactForm(request.POST)

        if form.is_valid():

            subject = "Make an Inquiry"
            cd = form.cleaned_data

            body = {
                "name": form.cleaned_data["name"],
                "email": form.cleaned_data["email"],
                "message": form.cleaned_data["message"],

            }

            # to join the body together
            message = "\n".join(body.values())
            try:
                send_mail(subject, message, EMAIL_HOST_USER,
                          [cd["to"]])

            # to protect the app from hackers trying to insert bad email headers
            except BadHeaderError:

                return HttpResponse("Invalid header found.")

            return redirect("home")

    form = ContactForm()
    return render(request, "index.html", {"form": form})
