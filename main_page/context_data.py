from blog.models import Blog
from main_page.forms import ContactUsForm
from main_page.models import Hiro, Services, Testimonial, About, Car, Experience, Contacts


def get_common_context():
    return {
    'slider': Hiro.objects.get(id=1),
    'servise': Services.objects.get(id=1),
    'testimonial': Testimonial.objects.filter(is_visible=True),
    'about': About.objects.get(id=1),
    'main_page_posts': Blog.objects.filter(is_visible=True).order_by('-pub_date')[:3],
    'main_cars_list': Car.objects.filter(is_visible=True).order_by('-id')[:10],
    'experience': Experience.objects.get(id=1),
    'contacts': Contacts.objects.get(id=1),
    'contact_us': ContactUsForm(),
    'pricing_cars': Car.objects.filter(is_visible=True),
    'recomend_car': Car.objects.filter(is_visible=True).order_by('-id')[:3],
    }
