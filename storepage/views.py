from django.shortcuts import render, redirect
from storepage.forms import OrderCreationForm, OrderDetailsForm
from storepage.models import Order, OrderFiles
from datetime import timedelta
#import datetime
from datetime import datetime, timezone

# Create your views here.
def createOrder(request):
    if request.method == "POST":
        form = OrderCreationForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('order_detail', obj.id)
        else:
            form = OrderCreationForm()
    context = {'form': OrderCreationForm()}
    return render(request, 'storepage/createOrder.html', context)


def OrderDetail(request, id):
    order = Order.objects.get(id=id)
    orderinfo = OrderFiles.objects.filter(order=order)
    form = OrderDetailsForm()
    # for obj in order:
    order_hours = int(order.hours)
    order_days = int(order.days)
    deadline = order.created_at + timedelta(days=order_days, hours=order_hours)
    time_now = datetime.now(timezone.utc)
    time_left = deadline - time_now
    cost = int(order.pages) * 300
    words = int(order.pages) * 275
    if request.method == "POST":
        form = OrderDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.order = order
            obj.save()
            return redirect('order_detail', order.id)
        else:
            form = OrderDetailsForm()
    return render(request, 'storepage/OrderDetail.html', {'order':order, 'form':form, 'time_left':time_left, 'orderinfo':orderinfo, 'cost':cost, 'words':words})
    #return render(request, 'storepage/OrderDetail.html', {'order':order, 'time_left':time_left})


def mainpage(request):
    return render(request, 'storepage/mainpage.html')


def OrderUpdate(request, id):
     order = Order.objects.get(id=id)
     if request.method == 'POST':
         form = OrderCreationForm(request.POST, instance=order)
         if form.is_valid():
             form.save()
             return redirect('order_detail', order.id)
     else:
         form = OrderCreationForm(instance=order)
     return render(request, 'storepage/createOrder.html',  {'form': form})





        
