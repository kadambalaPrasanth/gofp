from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
import json
from django.contrib.auth.hashers import make_password
import pandas as pd
from django.contrib import messages
from .models import *
# Create your views here.
from django.contrib.auth.models import User
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("services")
        else:
                return redirect("login")
    else:
         return render(request,"login.html")
    
def logout_view(request):
     logout(request)
     return redirect("login")

def index(request):
     return render(request,"index.html")

def signup(request):
     if request.method=="POST":
        first_name=request.POST["fullName"]
        username=request.POST["username"]
        email=request.POST["email"]
        phone=request.POST["phoneNumber"]
        password=request.POST["password"]
        hashed_password = make_password(password)  # hash the password
        user=User(username=username,email=email,password=hashed_password,first_name=first_name)
        user.save()
        return redirect("login")

     return render(request,"register.html")


def cal(request):
     return render(request,"cal.html")
def investment_cal(request):
     return render(request,"investment_cal.html")

def top_30_schmeas(request):
     with open("finance/top_30_schemes.json") as f:
          data=json.load(f)
     return render(request,"table_data.html",{"data":data})

def portfolio_view(request):
     if request.method=="POST":
          name=request.POST["Name"]
          price=request.POST["Price"]
          qnt=request.POST["qnt"]
          category=request.POST["type"]
          amount=request.POST["amount"]
          user=request.user
          if portfolio.objects.filter(user=user,schema_name=name).exists():
               return redirect("portfolio")
          else:
               portfolio_value = int(qnt) * float(price)
               if portfolio_value > float(amount):
                    messages.error(request, "You don't have enough investment to add this schema.")
                    return redirect("portfolio")
               Portfolio=portfolio(user=user,schema_name=name,qnt=qnt,price=price,category=category,investment=amount)
               Portfolio.save()
               messages.success(request, "Schema added successfully!")
               return redirect("portfolio")
          
     else:
          user = request.user
          portfolios = portfolio.objects.filter(user=user)
          large_cap_data = pd.read_excel('finance/large_cap.xlsx').values.tolist()
          small_cap_data = pd.read_excel('finance/small_cap.xlsx').values.tolist()
          mid_cap_data = pd.read_excel('finance/mid_cap.xlsx').values.tolist()
          return render(request,"portfolio.html",{"large_cdata":large_cap_data,"small_cdata":small_cap_data,"mid_cdata":mid_cap_data,'portfolios': portfolios})

def contact(request):
     return render(request,"contact.html")

def about(request):
     return render(request,"about.html")

def service(request):
     return render(request,"services.html")

def base(request):
     return render(request,"base.html")