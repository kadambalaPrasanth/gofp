"""
URL configuration for gofp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from finance import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login_view,name="login"),
    path("register",views.signup,name="register"),
    path("index",views.index,name="index"),
    path("logout",views.logout_view,name="logout"),
    path("cal",views.cal,name="cal"),
    path("investment_cal",views.investment_cal,name="investment_cal"),
    path("table_data",views.top_30_schmeas,name="table_data"),
    path("build_your_portfolio",views.portfolio_view,name="portfolio"),
    path("about",views.about,name="about"),
    path("contact",views.contact,name="contact"),
    path("services",views.service,name="services"),
    path("base",views.base,name="base")
    
]
