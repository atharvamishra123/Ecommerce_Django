from django.shortcuts import render
from django.contrib.auth import logout
# from loginsignup.views import logout
import json

selected_product = []
util_list = []

selected_product_dict = {}


# def check_cart(view_function):
#     def wrapper_function(request, *args, **kwargs):
#         if not selected_product_dict:
#             logout(request)
#         else:
#
#     return wrapper_function
