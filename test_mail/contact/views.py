from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.template.loader import render_to_string
def index(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email=form.cleaned_data['email']
            content = form.cleaned_data['content']
            html = render_to_string('emails/contactform.html',{
                'name': name,
                'email': email,
                'content': content
            })
            send_mail("The contact form subject", "This is the message", "klno90@yahoo.com",['khunlinnaingoo90@gmail.com'], html_message=html)
            return redirect('index')
        
    else:
        form = ContactForm()
    return render(request, 'contact/index.html',{
        'form': form
    })
