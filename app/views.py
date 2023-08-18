from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
# Create your views here.
def home(request):
    return render(request , 'home.html')



def contact_us(request):
    if request.method == 'POST':
        message_name = request.POST['message_name']
        message_email = request.POST['message_email']
        message = request.POST['message']

        send_mail(
            message_name,
            message,
            message_email,
            ["impérial@gmail.com"],
        )

        return render(request, 'home.html', {'message_name': message_name , 'message_email' : message_email , 'message' : message})
    else:
        
    
     return render(request, 'home.html', {'form': form})

def send_contact_email(data):
    subject = 'New Contact Message'
    message = f"Name: {data['name']}\nEmail: {data['email']}\nSubject: {data['subject']}\nMessage: {data['message']}"
    from_email = 'your_email@example.com'
    recipient_list = ['admin@example.com']  
    
    send_mail(subject, message, from_email, recipient_list)

def contact_success(request):
    return render(request, 'contact_us/contact_success.html')
