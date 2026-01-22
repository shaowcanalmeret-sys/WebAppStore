from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .decorators import admin_required


def page(request):
    offers = Offer.objects.all()

    
    return render(request, "home.html", {"offers":offers})
@login_required(login_url='login')
def add_to_cart(request, offer_id):
    offer = get_object_or_404(Offer, id=offer_id)
    product = offer.product

    if product.stock <= 0:
        messages.error(request, "عذرا, الكمية نفذت من هذا المنتج.")
        return redirect('home')

    cart = request.session.get('cart', [])
    cart.append(offer.id)
    request.session['cart'] = cart

    product.stock -= 1
    product.save()

    messages.success(request, "تمت اضافة المنتج الى السلة")
    return redirect('home')






def about(request):
    return render(request, "about.html")

def offers(request):
    offers = Offer.objects.all()
    
    return render(request, "offers.html", {"offers": offers})
@admin_required
def add_offer(request):
    offer=Offer.objects.all()
    form=OfferForm()
    if request.method == 'POST':
        form=OfferForm(request.POST)
        if form.is_valid():
            form.save()
          
            return redirect('offers')
            messages.success(request,'تم الاضافة')

        else:  

            form=OfferForm() 
    return render(request, 'add_offer.html', {'form':form}) 
@admin_required
def edit_offer(request,of_id):
    offer=Offer.objects.get(id=of_id)
    form=OfferForm(instance=offer)
    if request.method =='POST':
        form=OfferForm(request.POST,instance=offer)
        if form.is_valid():
            form.save()
            messages.success(request,'تم التعديل')
            return redirect('offers')
        else:
            form=OfferForm(instance=offer)


    return render(request, 'edit_offer.html' ,{'form':form})   
@admin_required
def delete_offer(request,of_id):
    offer=Offer.objects.get(id=of_id)
    if request.method == 'POST':
        offer.delete()
        return redirect('offers')   

    return render(request, 'delete_offer.html', {'offer':offer})          




def products(request):
   
    products = Product.objects.all()
    context={
        
        'all_products':products
    }
   
    return render(request, "products.html", context)
@admin_required
def add_products(request):
    categories=Category.objects.all()
    if request.method =='POST':
     name=request.POST.get('name')
     image=request.FILES.get('image')
     description=request.POST.get('description') 
     category_id=request.POST.get('category') 
     category = Category.objects.get(id=category_id) 
     price=request.POST.get('price')
     stock=request.POST.get('stock')
     created_at=request.POST.get('created_at')
     product=Product.objects.create(name=name, description=description, category=category, price=price,
      stock=stock, created_at=created_at, image=image)


    return render(request, 'admin_product_add.html',{'all_categories':categories})
@admin_required
def edit_product(request,prod_id):
    prod=get_object_or_404(Product,id=prod_id)
    categories=Category.objects.all()
    if request.method == 'POST':
        
        prod.name=request.POST.get("name")
        if request.FILES.get("image"):
            prod.image = request.FILES.get("image")
        prod.description=request.POST.get("description")
        category_id = request.POST.get("category")
        if category_id and category_id.isdigit():
            prod.category_id = int(category_id)
        prod.price=request.POST.get("price")
        prod.stock=request.POST.get("stock") or 0

        prod.save()


        return redirect('products')

    return render(request, "admin_product_edit.html", {'product':prod, 'all_categories':categories})  
@admin_required
def delete_product(request,prod_id):
    product=Product.objects.get(id=prod_id)
    if request.method == 'POST':
        product.delete()
        return redirect('products')   

    return render(request, 'delete_product.html', {'product':product})    

      
def category(request):

    cate= Category.objects.all()
    context={

        "all_categories":cate

    }
    return render(request, "category.html", context) 
@admin_required
def add_category(request):
    
    form=CategoryForm()
    if request.method == 'POST':
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'تم الاضافة')
            return redirect('category')

        else:  

            form=CategoryForm() 
    return render(request, 'add_offer.html', {'form':form})  
@admin_required
def edit_category(request,cate_id):

    cate=Category.objects.get(id=cate_id)
    form=CategoryForm(instance=cate)
    if request.method =='POST':
        form=CategoryForm(request.POST,instance=cate)
        if form.is_valid():
            form.save()
            messages.success(request,'تم التعديل')
            return redirect('category')
        else:
            form=CategoryForm(instance=cate)


    return render(request, 'edit_category.html' ,{'form':form})  

@admin_required
def delete_category(request,cate_id):
    cate=Category.objects.get(id=cate_id)
    if request.method == 'POST':
        cate.delete()
        return redirect('category')   

    return render(request, 'delete_category.html', {'category':cate})             

def contact(request):
    return render(request, "contact.html")   





def signUp(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['username']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.set_password(form.cleaned_data['password'])

            user.save()
            messages.success(request, 'تم انشاء الحساب بنجاح')
            return redirect('login')

    return render(request, 'signup.html', {'form':form})     


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password) 
        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
                messages.error(request, 'بيانات الدخول غير صحيحة')    
    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')    