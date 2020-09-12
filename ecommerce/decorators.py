from django.shortcuts import redirect
from django.core.paginator import Paginator
from .models import Product

#all are custom function for dry principle use

#this will help to redirect authenticated user to use website 
#unauthenticated user will be redirected to 
def unauthenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('ecommerce:appindex')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func

#will lis all categories with sub_categories from product model
def categories_with_sub_categories():
    products = Product.objects.all()
    all_categories_with_subcategories = dict()
    for product in products:
        if all_categories_with_subcategories.get(product.category) == None:
            all_categories_with_subcategories[product.category] = [product]
        else:
            sub_category_list = all_categories_with_subcategories[product.category]
            if product.sub_category not in sub_category_list:
                all_categories_with_subcategories[product.category].append(
                    product.sub_category)
    return all_categories_with_subcategories

#will handle pagination to reduce load 
def pagination_handle(request,filtered_products,num_of_objects):
    paginator = Paginator(filtered_products, num_of_objects)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj

#return cart obj to display them
def cart_handle(request):
    if request.user.is_authenticated:
        cart_obj=request.user.customer.cart
        cart=cart_obj.products.all()
        return cart
    else:
        cart=0
        return cart