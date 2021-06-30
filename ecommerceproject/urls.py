"""ecommerceproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from products.views import (home_page_view,
                            product_sub,
                            add_to_cart,
                            cart,
                            place_order,
                            clear)

from loginsignup.views import (signup_view,
                               login_view,
                               user_profile_view,
                               user_logout)

urlpatterns = [
                  path('admin/', admin.site.urls, name='admin'),
                  path('home/', home_page_view, name='homepage'),
                  path('sub/<int:id>', product_sub, name='product_sub'),

                  # urls regarding user registration and login and logout
                  path('signup/', signup_view, name='signup'),
                  path('login/', login_view, name='login'),
                  path('userprofile/', user_profile_view, name='userprofile'),
                  path('logout/', user_logout, name='userlogout'),
                  path('clear/', clear, name="clear"),
                  # urls regarding placing order
                  path('addtocart/<int:c_id>/<int:p_id>', add_to_cart, name="cart"),
                  path('cart/', cart, name="usercart"),
                  path('placeorder/<int:c_id>', place_order, name="placeorder")
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# <!-- <a href="{% url 'relatedproducts' id=x.id %}"><img src="{{x.pic.url}}'><img src="{{x.pic.url}}" alt="" class="card-img-top" height="200px"></a>
# <img src="{{x.pic.url}}" alt="" class="card-img-top" height="200px">-->
