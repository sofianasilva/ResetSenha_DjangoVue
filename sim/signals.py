from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail
from django.conf import settings

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    reset_url = f"http://localhost:5173/reset-password/{reset_password_token.key}/"

    send_mail(
        "Password Reset for Crediation portal account",
        f"Open the link to reset your password: {reset_url}",
        settings.DEFAULT_FROM_EMAIL,
        [reset_password_token.user.email],
    )
