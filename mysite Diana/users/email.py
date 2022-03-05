from django.core.mail import send_mail


def email():
    subject = 'Mail subject'
    message = 'Mail body'
    email_from = 'from@mysite.com'
    recipient_list = ['dianasiminabarbu@gmail.com']
    send_mail(subject, message, email_from, recipient_list)
