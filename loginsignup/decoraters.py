from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import logout
import json
from loginsignup.addtocart_util import selected_product_dict
from loginsignup.models import CustomUsers


def is_registered(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_function(request, *args, **kwargs)

    return wrapper_function


def is_logged_in(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('homepage')
        else:
            return view_function(request, *args, **kwargs)

    return wrapper_function


def is_logout(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
            redirect('homepage')
        else:
            return view_function(request, *args, **kwargs)

    return wrapper_function


def logged_in_user_profile(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            render(request, 'profilepage.html', {})
        else:
            return view_function(request, *args, **kwargs)

    return wrapper_function


# def check_cart(view_function):
#     def wrapper_function(request, *args, **kwargs):
#         if not selected_product_dict:
#             logout(request)
#         else:
#             u = request.user
#             print(u)
#             list = selected_product_dict[u]
#             print(list)
#             temp_dict = {'products': selected_product_dict[u]}
#             temp_str = json.dumps(temp_dict)
#             response = render(request)
#             response.set_cookie('products', temp_str)
#             return view_function(request, *args, **kwargs)
#
#     return wrapper_function
