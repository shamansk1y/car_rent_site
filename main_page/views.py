from django.db.models import Avg, Count
from django.shortcuts import render, get_object_or_404, redirect
from .context_data import get_common_context
from .forms import ContactUsForm, BookingForm, ReviewForm
from .models import Car, Review
from django.core.paginator import Paginator

def post_request(request):

    contact_us = ContactUsForm(request.POST)
    if contact_us.is_valid():
        contact_us.save()
        return redirect('/')


def index(request):
    booking_form = BookingForm()
    if request.method == 'POST':
        booking_form = BookingForm(request.POST)

        if booking_form.is_valid():
            booking_form.save()
            return redirect('/')
    data = {'booking_form': booking_form}
    context_data = get_common_context()
    data.update(context_data)
    return render(request, 'index.html', context=data)

def cars_list(request):
    if request.method == 'POST':
        pass
        # handle_post_request(request)

    cars = Car.objects.filter(is_visible=True)
    paginator = Paginator(cars, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {
        'cars': cars,
        'page_obj': page_obj,
    }
    context_data = get_common_context()
    data.update(context_data)
    return render(request, 'cars_list.html', context=data)

def car_single(request, id):
    product = get_object_or_404(Car, id=id)
    car = get_object_or_404(Car, id=id)
    average_rating = Review.objects.aggregate(Avg('rating'))['rating__avg']
    review_app = product.review_set.filter(is_approved=True)

    rating_counts = review_app.values('rating').annotate(count=Count('rating'))
    av_rating = Review.objects.filter(product=product, is_approved=True).aggregate(Avg('rating'))['rating__avg']

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.save()
            form = ReviewForm()
    else:
        form = ReviewForm()
    data = {
        'product': product,
        'average_rating': average_rating,
        'review_app': review_app,
        'rating_counts':rating_counts,
        'av_rating': av_rating,
        'car': car,

    }
    context_data = get_common_context()
    data.update(context_data)
    data['form'] = form
    return render(request, 'car_single.html', context=data)


def about(request):
    if request.method == 'POST':
        pass
        # handle_post_request(request)
    data = {}
    context_data = get_common_context()
    data.update(context_data)
    return render(request, 'page_about.html', context=data)

def service(request):
    if request.method == 'POST':
        pass
        # handle_post_request(request)
    data = {}
    context_data = get_common_context()
    data.update(context_data)
    return render(request, 'page_service.html', context=data)


def contact(request):
    if request.method == 'POST':
        post_request(request)

    data = {}
    context_data = get_common_context()
    data.update(context_data)
    return render(request, 'page_contact.html', context=data)


def pricing(request):
    if request.method == 'POST':
        pass
        # handle_post_request(request)
    data = {}
    context_data = get_common_context()
    data.update(context_data)
    return render(request, 'page_pricing.html', context=data)


# # views.py
# from django.shortcuts import render, redirect
# from .forms import BookingForm
#
# def car_selection_view(request):
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             form.save()  # Сохранение бронирования в базе данных
#             # Дополнительные действия, например, перенаправление на страницу подтверждения
#             return redirect('confirmation_page')
#     else:
#         form = BookingForm()
#
#     return render(request, 'your_template_name.html', {'form': form})
