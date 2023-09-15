from django.shortcuts import render
from django.shortcuts import render, redirect  
from fisrtApp.forms import ProductForm  
from fisrtApp.models import Product 
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})




def emp(request):  
    if request.method == "POST":  
        form = ProductForm(request.POST, request.FILES)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/user/show')  
            except:  
                pass  
    else:  
        form = ProductForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    products = Product.objects.all()  
    return render(request,"show.html",{'products':products})  
def edit(request, id):  
    product = Product.objects.get(id=id)  
    return render(request,'edit.html', {'product':product})  
def update(request, id):  
    product = Product.objects.get(id=id)  
    form = ProductForm(request.POST, instance = product)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'product': product})  

def get_product(request, id):
        product = Product.objects.get(id=id)
        return render(request, 'one_product.html', {'one_product': product})
    

def destroy(request, id):  
    product = Product.objects.get(id=id)  
    product.delete()  
    return redirect("/user/show")