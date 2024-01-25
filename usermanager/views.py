from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.core.mail import EmailMessage, send_mail
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from custom_user.models import User
from core.models import QuizQuestion
from usermanager.models import EmailVerification
# Create your views here.

def questionListAll(request):
    return render(request, 'usermanager/questionListNoAuth.html')

import random
def questionListEnglish(request):
    mathslistone = list(QuizQuestion.objects.filter(category=23).order_by('-id'))
    mathslisttwo = list(QuizQuestion.objects.filter(category=6).order_by('-id'))
    mathslisthree = list(QuizQuestion.objects.filter(category=4).order_by('-id'))
    datum = mathslistone + mathslisttwo + mathslisthree
    items = random.sample(datum, 15)
    return render(request, 'usermanager/englishquestionlist.html', {'items': items})


def questionListScience(request):
    mathslistone = list(QuizQuestion.objects.filter(category=30).order_by('-id'))
    mathslisttwo = list(QuizQuestion.objects.filter(category=31).order_by('-id'))
    mathslisthree = list(QuizQuestion.objects.filter(category=11).order_by('-id'))
    datum = mathslistone + mathslisttwo + mathslisthree
    items = random.sample(datum, 15)
    return render(request, 'usermanager/sciencequestionlist.html', {'items': items})

def questionListSocial(request):
    mathslistone = list(QuizQuestion.objects.filter(category=15).order_by('-id'))
    mathslisttwo = list(QuizQuestion.objects.filter(category=16).order_by('-id'))
    mathslisthree = list(QuizQuestion.objects.filter(category=17).order_by('-id'))
    datum = mathslistone + mathslisttwo + mathslisthree
    items = random.sample(datum, 15)
    return render(request, 'usermanager/socialquestionlist.html', {'items': items})

def questionListKiswahili(request):
    mathslistone = list(QuizQuestion.objects.filter(category=2).order_by('-id'))
    mathslisttwo = list(QuizQuestion.objects.filter(category=25).order_by('-id'))
    mathslisthree = list(QuizQuestion.objects.filter(category=36).order_by('-id'))
    datum = mathslistone + mathslisttwo + mathslisthree
    items = random.sample(datum, 15)
    return render(request, 'usermanager/kiswahiliquestionlist.html', {'items': items})

@login_required
def verifyEmail(request):
    datum = EmailVerification.objects.filter(user=request.user)
    if not datum:
        user_id = request.user.id
        user_email = request.user.email
        user_name = request.user.first_name
        verify_url = 'http://127.0.0.1:8000/confirm/verify_email/iLdxMr8pCW0p57u0/68yhz2uu/{0}/$2y$10$Oixfkm5gRoCjlmHRgDVB5Z0T2RQ/'.format(user_id)
        email = 'bestessays001@gmail.com'
        html_template = 'usermanager/verify_mail.html'
        html_message = render_to_string(html_template, {'verify_url': verify_url, 'user_name': user_name})
        subject = 'Verify your Email'
        email_from = 'Testprep@testprepken.com'
        recipient_list = [email]
        message = EmailMessage(subject, html_message,
                            email_from, recipient_list)
        message.content_subtype = 'html'
        message.send(fail_silently=True)
        messages.success(request, f'A verification Email has been sent to email provided on sign up.')
        return redirect('blank_404')
    else:
        messages.success(request, f'Email already verified')
        return redirect('blank_404')



def EmailVerificationComplete(request, id):
    user_id = User.objects.get(id=id)
    checkvar = EmailVerification.objects.filter(user=user_id)
    if not checkvar:
        datum = EmailVerification(
                user=user_id,
                verification_status='verified',
        )
        datum.save()
        return render(request, 'usermanager/emailverificationcomplete.html')
    else:
        messages.success(request, f'Email already verified')
        return redirect('blank_404')

def blank(request):
    return render(request, 'usermanager/blank.html')

