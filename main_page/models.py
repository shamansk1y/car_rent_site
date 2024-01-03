from django.db import models
from .utils import get_file_name
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils import timezone

class Hiro(models.Model):

    title = models.CharField(max_length=50, verbose_name="Назва слайду")
    position = models.SmallIntegerField(unique=True, verbose_name="Позиція")
    back_image = models.ImageField(upload_to=get_file_name, verbose_name="Фонове зображення")
    is_visible = models.BooleanField(default=True, verbose_name="Видимість")
    h_1 = models.CharField(max_length=250, blank=True, verbose_name="Заголовок")
    desc = models.TextField(max_length=500, blank=True, verbose_name="Опис")

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('position',)
        verbose_name_plural = 'Слайдер'


class About(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    is_visible = models.BooleanField(default=True, verbose_name="Видимість")
    image = models.ImageField(upload_to=get_file_name, verbose_name="Зображення")


    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Про нас'


class Services(models.Model):
    title = models.CharField(max_length=255)
    servise_1 = models.CharField(max_length=255, verbose_name="Сервіс 1 Заголовок")
    serv_1_desc = models.TextField(max_length=500, verbose_name="Сервіс 1 Опис")
    servise_2 = models.CharField(max_length=255, verbose_name="Сервіс 2 Заголовок")
    serv_2_desc = models.TextField(max_length=500, verbose_name="Сервіс 2 Опис")
    servise_3 = models.CharField(max_length=255, verbose_name="Сервіс 3 Заголовок")
    serv_3_desc = models.TextField(max_length=500, verbose_name="Сервіс 3 Опис")
    servise_4 = models.CharField(max_length=255, verbose_name="Сервіс 4 Заголовок")
    serv_4_desc = models.TextField(max_length=500, verbose_name="Сервіс 4 Опис")

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Наші сервіси'



class Testimonial(models.Model):

    name = models.CharField(max_length=50, verbose_name="Повне ім'я")
    profession = models.TextField(max_length=50, verbose_name="Посада")
    position = models.SmallIntegerField(unique=True, verbose_name="Позиція")
    is_visible = models.BooleanField(default=True, verbose_name="Видимість")
    image = models.ImageField(upload_to=get_file_name, blank=True, verbose_name="Фото")
    desc = models.TextField(max_length=500, verbose_name="Текст", blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position',)
        verbose_name_plural = 'Відгуки'


class Car(models.Model):
    title = models.CharField(max_length=75, verbose_name="Модель авто")
    manufacturer = models.CharField(max_length=75, verbose_name="Виробник")
    data = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Дата випуску')
    image = models.ImageField(upload_to=get_file_name, blank=True, verbose_name="Фото")
    position = models.SmallIntegerField(unique=True, verbose_name="Позиція")
    is_visible = models.BooleanField(default=True, verbose_name="Видимість")
    desc = models.TextField(max_length=2000, verbose_name="Опис", blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ціна День')
    price_hour = models.DecimalField(max_digits=10, decimal_places=2, default=10, verbose_name='Ціна Година')
    price_month = models.DecimalField(max_digits=10, decimal_places=2, default=995, verbose_name='Ціна Місяць')
    mileage = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Пробіг')
    TRANSMISSION_CHOICES = [
        ('M', 'Manual'),
        ('A', 'Automatic'),
    ]
    transmission = models.CharField(max_length=1, choices=TRANSMISSION_CHOICES, blank=True, default='A',
                                              verbose_name='Коробка передач')
    SEATS_CHOICES = [
        ('5', '5 Adults'),
        ('4', '4 Adults'),
        ('3', '3 Adults'),
        ('2', '2 Adults'),
    ]
    seats = models.CharField(max_length=1, choices=SEATS_CHOICES, blank=True, default='5',
                                              verbose_name='Кількість місць')
    LUGGAGE_CHOICES = [
        ('5', '5 Bags'),
        ('4', '4 Bags'),
        ('3', '3 Bags'),
        ('2', '2 Bags'),
    ]
    luggage = models.CharField(max_length=1, choices=LUGGAGE_CHOICES, blank=True, default='4',
                                              verbose_name='Кількість багажних місць')
    FUEL_CHOICES = [
        ('D', 'Diesel'),
        ('G', 'Gas'),
        ('H', 'Hybrid'),
        ('E', 'Electric'),
    ]
    fuel = models.CharField(max_length=1, choices=FUEL_CHOICES, blank=True, default='G',
                                              verbose_name='Паливо')

    airconditions = models.BooleanField(default=False, verbose_name='Airconditions')
    child = models.BooleanField(default=False, verbose_name='Child Seat')
    gps = models.BooleanField(default=False, verbose_name='GPS')
    luggage_f = models.BooleanField(default=False, verbose_name='Luggage')
    music = models.BooleanField(default=False, verbose_name='Music')

    seat_belt = models.BooleanField(default=False, verbose_name='Seat Belt')
    sleeping_bed = models.BooleanField(default=False, verbose_name='Sleeping Bed')
    water = models.BooleanField(default=False, verbose_name='Water')
    bluetooth = models.BooleanField(default=False, verbose_name='Bluetooth')
    onboard_computer = models.BooleanField(default=False, verbose_name='Onboard computer')

    audio = models.BooleanField(default=False, verbose_name='Audio input')
    long_term_trips = models.BooleanField(default=False, verbose_name='Long Term Trips')
    car_kit = models.BooleanField(default=False, verbose_name='Car Kit')
    remote_central_locking = models.BooleanField(default=False, verbose_name='Remote central locking')
    climate_control = models.BooleanField(default=False, verbose_name='Climate control')



    def __str__(self):
        return f'{self.manufacturer} {self.title} {self.data}'

    def get_absolute_url(self):
        return reverse('main_page:car_single', kwargs={'id': self.id})

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Автомобілі'

class Experience(models.Model):

    experienced = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Років роботи')
    total_cars = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Кількість авто')
    happy_costomers = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Задоволених клієнтів')
    total_mileage = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Загальний пробіг')

    def __str__(self):
        return f'{self.experienced}'

    class Meta:
        ordering = ('experienced',)
        verbose_name_plural = 'Наш досвід'



class Contacts(models.Model):

    address = models.CharField(max_length=70, verbose_name="Адреса")
    phone_1 = models.CharField(blank=True, max_length=50, verbose_name="Телефон 1")
    phone_2 = models.CharField(blank=True, max_length=50, verbose_name="Телефон 2")
    email = models.CharField(max_length=50, verbose_name="Пошта ")

    twi_url = models.URLField(blank=True, verbose_name="Посилання на facebook", default='https://www.x.com/')
    fb_url = models.URLField(blank=True, verbose_name="Посилання на youtube", default='https://www.facebook.com/')
    inst_url = models.URLField(blank=True, verbose_name="Посилання на instagram", default='https://www.instagram.com/')


    def __str__(self):
        return f'{self.address}'

    class Meta:
        ordering = ('address',)
        verbose_name_plural = 'Контакти'


class ContactUs(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(max_length=250, blank=True)
    subject = models.CharField(max_length=50)

    date = models.DateField(auto_now_add=True)
    date_processing = models.DateField(auto_now=True)
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}: {self.email}'

    class Meta:
        ordering = ('-date',)
        verbose_name_plural = "Зворотній зв'язок"


class Booking(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    pick_up_location = models.CharField(max_length=100)
    drop_off_location = models.CharField(max_length=100)
    pick_up_date = models.DateField()
    drop_off_date = models.DateField()


    def __str__(self):
        return f'{self.pick_up_date}: {self.car} - {self.pick_up_location}'

    class Meta:
        ordering = ('-pick_up_date',)
        verbose_name_plural = "Бронь"


class Review(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    product = models.ForeignKey(Car, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    date = models.DateTimeField(default=timezone.now)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-date',)
        verbose_name_plural = "Відгуки"