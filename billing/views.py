from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django_daraja.mpesa.core import MpesaClient
from django.views.decorators.csrf import csrf_exempt
import json
from billing.models import Post, Contact, PaymentDetails, PaymentUpdates, PaymentInfo, SubscriptionData
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from custom_user.models import User
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.

@login_required
def mpesarequest(request):
    cl = MpesaClient()
    #get user details
    mydata = Post.objects.filter(user=request.user).order_by('-id')[:1]
    phone_number = mydata[0]
    #print(phone_number)
    user_id = request.user.id
    #print(user_id)
    #phone_number = '0740408496'
    amount = 1
    account_reference = 'reference'
    transaction_desc = 'Description'
    callback_url = 'https://kpsea.testprepken.com/billing/callback/{0}/'.format(user_id)
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)


@login_required
def paymentflutter(request):
    user_id = request.user.id
    user_email = request.user.email
    user_name = request.user.first_name
    mydata = Post.objects.filter(user=request.user).order_by('-id')[:1]
    phone_number = mydata[0]
    callback_url = 'https://kpsea.testprepken.com/billing/callback/{0}/'.format(user_id)
    return render(request, 'billing/flutterpay.html', {'user_id':user_id, 'user_name':user_name, 'user_email':user_email, 'phone_number':phone_number, 'callback_url':callback_url})


def call_back_flutter(request, id):
    user_id = User.objects.get(id=id)
    payment = PaymentInfo(
            user=user_id,
            payment_status='400',
        )
    payment.save()
    datum = SubscriptionData(
            user=user_id,
            payment_status='400',
    )
    datum.save()
    return render(request, 'billing/paymessage.html')


def call_back_annual(request, id):
    user_id = User.objects.get(id=id)
    payment = PaymentInfo(
            user=user_id,
            payment_status='3000',
        )
    payment.save()
    datum = SubscriptionData(
            user=user_id,
            payment_status='3000',
    )
    datum.save()
    return render(request, 'billing/paymessage.html')


@csrf_exempt
def callbackurl(request, id):
    user_id = User.objects.get(id=id)
    if request.method == 'POST':
        m_body =request.body.decode('utf-8')
        mpesa_payment = json.loads(m_body)
        payment = PaymentDetails(
            phonenumber=mpesa_payment['Body']['stkCallback']['CallbackMetadata']['Item'][4]['Value'],
        	transcode=mpesa_payment['Body']['stkCallback']['CallbackMetadata']['Item'][1]['Value'],
            user=user_id,
        )
        payment.save()
        context = {
             "ResultCode": 0,
             "ResultDesc": "Accepted"
        }
        return JsonResponse(dict(context))
    


    

  
 
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['phonenumber']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['phonenumber']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False
    
class PostDetailView(DetailView):
    model = Post



class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Contact
    fields = ['phonenumber']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ContactUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Contact
    fields = ['phonenumber']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False
    
class ContactDetailView(DetailView):
    model = Contact





@login_required
def makeapayment(request):
    #user_id = request.user.id
    #callback_url = 'https://darajambili.herokuapp.com/callback/{0}/'.format(user_id)
    #print(callback_url)
    return render(request, 'billing/makepayment.html')

def pricing(request):
    return render(request, 'billing/pricing.html')

@login_required
def pricing_standard(request):
    return render(request, 'billing/pricing_standard.html')

@login_required
def pricing_corporate(request):
    return render(request, 'billing/pricing_corporate.html')

@login_required
def finpayment(request):
    mydata = Post.objects.filter(user=request.user)
    if not mydata:
        return redirect('post-create')
    else:
        blogs = Post.objects.filter(user=request.user).values_list('pk', flat=True)
        numpk = blogs[0]
        return render(request, 'billing/paydetailsconfirm.html', {'mydata':mydata, 'numpk':numpk})

@login_required
def yearlypayments(request):
    mydata = Post.objects.filter(user=request.user).order_by('-id')[:1]
    if not mydata:
        return redirect('post-create')
    else:
        blogs = Post.objects.filter(user=request.user).values_list('pk', flat=True)
        numpk = blogs[0]
        return render(request, 'billing/yearlypaydetailsconfirm.html', {'mydata':mydata, 'numpk':numpk})


@login_required
def yearlypaydetailsmpesa(request):
    return render(request, 'billing/yearlypaydetailsmpesa.html')



@login_required
def paydetailsmpesa(request):
    return render(request, 'billing/paydetailsmpesa.html')

@login_required
def processingpaymentpage(request):
    paydata = PaymentDetails.objects.filter(user=request.user)
    if not paydata:
        return render(request, 'billing/processingpaymentpage.html')
    else:
        messages.success(request, f'Payment completed successfully!')
        return redirect('dashboard')


@login_required
def proceedToGateway(request):
    user_id = request.user.id
    user_email = request.user.email
    user_name = request.user.first_name
    mydata = Post.objects.filter(user=request.user).order_by('-id')[:1]
    phone_number = mydata[0]
    callback_url = 'https://kpsea.testprepken.com/billing/callback/{0}/'.format(user_id)
    return render(request, 'billing/proceedToGateway.html', {'user_id':user_id, 'user_name':user_name, 'user_email':user_email, 'phone_number':phone_number, 'callback_url':callback_url})



@login_required
def proceedToGatewayannual(request):
    user_id = request.user.id
    user_email = request.user.email
    user_name = request.user.first_name
    mydata = Post.objects.filter(user=request.user).order_by('-id')[:1]
    phone_number = mydata[0]
    callback_url = 'https://kpsea.testprepken.com/billing/callback/{0}/'.format(user_id)
    return render(request, 'billing/proceedToGatewayannual.html', {'user_id':user_id, 'user_name':user_name, 'user_email':user_email, 'phone_number':phone_number, 'callback_url':callback_url})

@login_required
def paymentsTracker(request):
    if request.user.is_superuser:
        mydata = PaymentInfo.objects.all()
        userCount = User.objects.all().count()
        return render(request, 'billing/paymentsTracker.html', {'mydata':mydata, 'userCount':userCount})
    else:
        return redirect('dashboard')

def paymentsDelete(request, id):
    PaymentInfo.objects.filter(id=id).delete()
    return redirect('paytracker')


@login_required
def proceedToGatewaypaystack(request):
    user_id = request.user.id
    user_email = request.user.email
    user_name = request.user.first_name
    #mydata = Post.objects.filter(user=request.user).order_by('-id')[:1]
    #phone_number = mydata[0]
    callback_url = 'https://kpsea.testprepken.com/billing/payment_review/$2y$10$g/H75NWQ4eS/{0}/t3x6Jlf6fFYUptfxRsdyttm8iHjWkQU/rvyQ5CHYC/'.format(user_id)
    return render(request, 'billing/paystack.html', {'user_id':user_id, 'user_name':user_name, 'user_email':user_email, 'callback_url':callback_url})
    



@login_required
def proceedToGatewaypaystackannual(request):
    user_id = request.user.id
    user_email = request.user.email
    user_name = request.user.first_name
    #mydata = Post.objects.filter(user=request.user).order_by('-id')[:1]
    #phone_number = mydata[0]
    callback_url = 'https://kpsea.testprepken.com/billing/payment_review/$2y$10$g/H75NWJ4eS/{0}/t3x6Jlf6fFYUtriidyttm8iHjWkQDPT/rvyQ5CHYC/'.format(user_id)
    return render(request, 'billing/paystackannual.html', {'user_id':user_id, 'user_name':user_name, 'user_email':user_email, 'callback_url':callback_url})
    