from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from vendedoras.models import Representantes

@receiver(post_save, sender=Representantes)
def enviar_email_boas_vindas(sender, instance, created, **kwargs):
    print('Signal disparado - tentando enviar e-mail')
    if created:
        send_mail(
            subject='Cadastro Consultora!',
            message=f'Olá Hevelyn,{instance.nome},acabou de se inscrever para fazer parte da sua equipe!',
            from_email='hevelyn.semijoias@gmail.com',
            # recipient_list=[instance.email],1
            recipient_list=['caiocezar2807@gmail.com'],
            fail_silently=False,
        )
    else:
        print('### Falhou ###')