from django.core.mail import send_mail

def send_test_email():
    send_mail(
        'test',
        'here is a test email',
        'adam@adamth.com',
        ['adam@adamth.com',],
    )
