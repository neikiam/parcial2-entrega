from django.core.mail import EmailMessage
from django.conf import settings


def send_email(to_email, subject, message, attachment_content=None, attachment_filename=None):
    try:
        email = EmailMessage(
            subject=subject,
            body=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[to_email],
        )
        
        if attachment_content and attachment_filename:
            email.attach(attachment_filename, attachment_content, 'application/pdf')
        
        email.send(fail_silently=False)
        return True
        
    except Exception as e:
        print(f"Error enviando email: {str(e)}")
        return False
