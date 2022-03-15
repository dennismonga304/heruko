from django.shortcuts import render, get_object_or_404
from django.db import transaction, IntegrityError
# Create your views here.

from .models import Categories, Product, CustomersContact, Commands
from .forms import ContactForm, ParagraphErrorList

def index(request):
    product = Product.objects.filter(pk=6)

    context = {
        'prod': product
    }

    return render(request, 'store/index.html', context)


def listing(request):
    product = Product.objects.filter(available=True)[:3]
    categorie = Categories.objects.all()


    context = {
        'product': product,
        'categorie': categorie

    }
    return render(request, 'store/list.html', context)


def detail(request, id_prod):

    prod = Product.objects.get(pk=id_prod)
    cat = Product.objects.filter(categorie=prod.categorie)
    context = {
        'product': prod,
        'also': cat,

    }
    if request.method == "POST":
        form = ContactForm(request.POST, error_class=ParagraphErrorList)
        if form.is_valid():

            email = form.cleaned_data['email']
            name = form.cleaned_data['name']


            # find contact customer
            try:
                with transaction.atomic():
                    contact = CustomersContact.objects.filter(email=email)
                    if not contact.exists():
                        contact = CustomersContact.objects.create(
                            name=name,
                            email=email
                        )
                    else:
                        contact = contact.first()
                    product = get_object_or_404(Product, id=id_prod)
                    booking = Commands.objects.create(
                        customers=contact,
                        product=product
                    )

                    context = {
                        'product': product,
                        'contact': contact
                    }
                    product.available =False
                    product.save()
                    return render(request, 'store/merci.html', context)
            except IntegrityError:
                form.errors['internal'] = "Une erreur interne est apparue. Merci de recommencer votre requête."



    else:
        form = ContactForm()

    context['form'] = form
    context['errors'] = form.errors.items()
    return render(request, 'store/detail.html', context)

def cataloguePrice(request):
    allCat = Categories.objects.all()
    context = {
        'catprice': allCat
    }
    return render(request, 'store/catalogue.html', context)
