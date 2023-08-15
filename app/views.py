from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
# Create your views here.
def home(request):
    return render(request , 'home.html')



def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            send_contact_email(form.cleaned_data)
            return redirect('contact_success')
    else:
        form = ContactForm()
    
    return render(request, 'home.html', {'form': form})

def send_contact_email(data):
    subject = 'New Contact Message'
    message = f"Name: {data['name']}\nEmail: {data['email']}\nSubject: {data['subject']}\nMessage: {data['message']}"
    from_email = 'your_email@example.com'
    recipient_list = ['admin@example.com']  
    
    send_mail(subject, message, from_email, recipient_list)

def contact_success(request):
    return render(request, 'contact_us/contact_success.html')
