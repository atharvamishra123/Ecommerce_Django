from django.shortcuts import render, HttpResponseRedirect, redirect
from products.models import Products, Sub_Products
from loginsignup.models import CustomUsers
from loginsignup.addtocart_util import selected_product, util_list, selected_product_dict
from django.http import HttpResponse
from django.core import serializers


# Create your views here.
def home_page_view(request, *args, **kwargs):
    querysets_male = Products.objects.filter(gender='male')
    querysets_female = Products.objects.filter(gender='female')
    context = {
        "object_list_male": querysets_male,
        "object_list_female": querysets_female
    }
    return render(request, "homepage.html", context)


def product_sub(request, id):
    var = Products.objects.get(id=id)
    querysets = Sub_Products.objects.filter(product=var)
    context = {
        "object_list": querysets
    }
    return render(request, "subproducts.html", context)


def add_to_cart(request, c_id, p_id):
    user = CustomUsers.objects.get(id=c_id)
    product = Sub_Products.objects.get(id=p_id)
    util_list.append(product)
    selected_product_dict[user] = util_list
    return redirect('/home/')


def cart(request):
    return render(request, "cart.html", {})


def place_order(request, c_id):
    # print(selected_product)
    user = CustomUsers.objects.get(id=c_id)
    for var in selected_product_dict[user]:
        product = Sub_Products.objects.get(id=var.id)
        product.user.add(user)
    util_list.clear()
    return redirect('/home/')


def clear(request):
    # print(util_list)
    # util_list.clear()
    # print(util_list)
    return HttpResponse("cleared")
