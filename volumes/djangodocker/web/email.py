from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings

def send_email(name , body , email):
    context = {'name':name , 'body':body , 'email':email}
    email_subject = "Thanks for your review!"
    email_body = render_to_string('email_message.txt', context)

    email = EmailMessage(
        email_subject,
        email_body,
        settings.DEFAULT_FROM_EMAIL ,
        [email, ],
    )
    #raise Exception('email errir')
    return email.send(fail_silently=False)