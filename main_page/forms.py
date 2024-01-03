from .models import ContactUs, Booking, Car, Review
from django import forms

class ContactUsForm(forms.ModelForm):
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'type': "text",
                'class': "form-control",
                'placeholder': "Your Name",
            }))

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'type': "text",
                'class': "form-control",
                'placeholder': "Your Email",
            }))

    subject = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'type': "text",
                'class': "form-control",
                'placeholder': "Subject",
            }))


    message = forms.CharField(
        max_length=300,
        widget=forms.Textarea(
            attrs={
                'name': "",
                'id': "",
                'cols': "30",
                'rows': "7",
                'class': "form-control",
                'placeholder': "Message",
            }))

    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'subject', 'message']


class BookingForm(forms.ModelForm):
    pick_up_location = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'type': "text",
                'class': "form-control",
                'placeholder': "City, Airport, Station, etc",
            }))

    drop_off_location = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'type': "text",
                'class': "form-control",
                'placeholder': "City, Airport, Station, etc",
            }))

    car = forms.ModelChoiceField(
        queryset=Car.objects.all(),
        empty_label="Select Car",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    pick_up_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'book_pick_date',
                'placeholder': 'Date',
            }
        )
    )

    drop_off_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'book_off_date',
                'placeholder': 'Date',
            }
        )
    )
    class Meta:
        model = Booking
        fields = ['car', 'pick_up_location', 'drop_off_location', 'pick_up_date', 'drop_off_date']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'name', 'email', 'message']

    name = forms.CharField(label="Ім'я", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Ваше ім'я"}))
    email = forms.EmailField(label='Еmail', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваш email'}))
    message = forms.CharField(label='Коментар', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Ваш відгук'}))