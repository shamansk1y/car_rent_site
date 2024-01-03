from django.contrib import admin
from main_page.models import Hiro, About, Services, Testimonial, Car, Experience, Contacts, ContactUs, Booking, Review


@admin.register(Hiro)
class HiroAdmin(admin.ModelAdmin):
    model = Hiro
    list_editable = ['title', 'position', 'is_visible', 'h_1', 'desc', 'back_image']
    list_display = ['title', 'position', 'is_visible', 'h_1', 'desc', 'back_image']
    list_display_links = None

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    model = About
    list_editable = ['title', 'content', 'image', 'is_visible']
    list_display = ['title', 'content', 'image', 'is_visible']
    list_display_links = None


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    model = Services
    list_editable = ['title', 'servise_1', 'serv_1_desc', 'servise_2', 'serv_2_desc', 'servise_3', 'serv_3_desc',
                     'servise_4', 'serv_4_desc']
    list_display = ['title', 'servise_1', 'serv_1_desc', 'servise_2', 'serv_2_desc', 'servise_3', 'serv_3_desc',
                     'servise_4', 'serv_4_desc']
    list_display_links = None


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    model = Testimonial
    list_editable = ['name', 'position', 'is_visible', 'profession', 'image', 'desc']
    list_display = ['name', 'position', 'is_visible', 'profession', 'image', 'desc']
    list_display_links = None


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    model = Car
    list_editable = ['title', 'manufacturer', 'data', 'image', 'position', 'is_visible', 'desc', 'price', 'mileage',
                     'transmission', 'seats', 'luggage', 'fuel', 'airconditions', 'child', 'gps', 'luggage_f',
                     'music', 'seat_belt', 'sleeping_bed', 'water', 'bluetooth', 'onboard_computer', 'audio',
                     'long_term_trips', 'car_kit', 'remote_central_locking', 'climate_control']
    list_display = ['id', 'title', 'manufacturer', 'data', 'image', 'position', 'is_visible', 'desc', 'price', 'mileage',
                    'transmission', 'seats', 'luggage', 'fuel', 'airconditions', 'child', 'gps', 'luggage_f',
                    'music', 'seat_belt', 'sleeping_bed', 'water', 'bluetooth', 'onboard_computer', 'audio',
                    'long_term_trips', 'car_kit', 'remote_central_locking', 'climate_control']
    list_display_links = ['id']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    model = Experience
    list_editable = ['experienced', 'total_cars', 'happy_costomers', 'total_mileage']
    list_display = ['experienced', 'total_cars', 'happy_costomers', 'total_mileage']
    list_display_links = None


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    model = Contacts
    list_editable = ['address', 'phone_1', 'phone_2', 'email']
    list_display = ['address', 'phone_1', 'phone_2', 'email']
    list_display_links = None


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    model = ContactUs
    list_editable = ['name', 'email', 'subject', 'message', 'is_processed']
    list_display = ['name', 'email', 'subject', 'message', 'date', 'date_processing', 'is_processed']
    list_display_links = None


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['car', 'pick_up_location', 'drop_off_location', 'pick_up_date', 'drop_off_date']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_editable = ['email', 'message', 'product', 'date', 'is_approved']
    list_display = ['name', 'email', 'message', 'product', 'date', 'is_approved']