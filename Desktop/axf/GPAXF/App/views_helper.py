import hashlib

from django.core.mail import send_mail
from django.http import HttpResponse
from django.template import loader

from App.models import Cart
from GPAXF.settings import EMAIL_HOST_USER, SERVER_HOST, SERVER_PORT


def hash_str(source):
    hashlib.new("sha512", source.encode('utf-8')).hexdigest()



def send_email_activate(username, recetive, u_token):
    subject = '%s AXF Activate' % username

    from_email = EMAIL_HOST_USER
    print(from_email)
    recipient_list = [recetive,]
    message = "message"
    data = {
        'username': username,
        'activate_url': 'http://{}:{}/axf/activate?u_token={}'.format(SERVER_HOST, SERVER_PORT, u_token)
    }
    html_message = loader.get_template('user/activate.html').render(data)
    print('99999999999999')
    print(subject, message, html_message, from_email, recipient_list)

    send_mail(subject=subject, message=message, html_message=html_message, from_email=from_email, recipient_list=recipient_list)

def get_total_price():
    carts = Cart.objects.filter(c_is_select=True)
    total = 0
    for cart in carts:
        total += cart.c_goods_num * cart.c_goods.price
    return '{:.2f}'.format(total)