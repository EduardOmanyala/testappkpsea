from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMessage, send_mail
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from billing.models import PaymentDetails, PaymentInfo
from . import models
from core.models import QuizCategory, MyResults, QuizQuestion, UserSubmittedAnswer, Progress


# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return render(request, 'core/home.html')
    
@login_required
def maths(request):
    paydata = PaymentInfo.objects.filter(user=request.user)
    test1 = MyResults.objects.filter(user=request.user, subject="Maths Test One").order_by('-id')[:1]
    test2 = MyResults.objects.filter(user=request.user, subject="Maths Test Two").order_by('-id')[:1]
    test3 = MyResults.objects.filter(user=request.user, subject="Maths Test Three").order_by('-id')[:1]
    test4 = MyResults.objects.filter(user=request.user, subject="Maths Test Four").order_by('-id')[:1]
    test5 = MyResults.objects.filter(user=request.user, subject="Maths Test Five").order_by('-id')[:1]
    test6 = MyResults.objects.filter(user=request.user, subject="Maths Test Six").order_by('-id')[:1]
    test7 = MyResults.objects.filter(user=request.user, subject="Maths Test Seven").order_by('-id')[:1]
    test8 = MyResults.objects.filter(user=request.user, subject="Maths Test Eight").order_by('-id')[:1]
    test9 = MyResults.objects.filter(user=request.user, subject="Maths Test Nine").order_by('-id')[:1]
    test10 = MyResults.objects.filter(user=request.user, subject="Maths Test Ten").order_by('-id')[:1]
    return render(request, 'core/maths.html',
                  {'paydata':paydata,
                    'test1':test1,
                    'test2':test2,
                    'test3':test3,
                    'test4':test4,
                    'test5':test5,
                    'test6':test6,
                    'test7':test7,
                    'test8':test8,
                    'test9':test9,
                    'test10':test10
                    })

@login_required
def kiswahili(request):
    paydata = PaymentInfo.objects.filter(user=request.user)
    test1 = MyResults.objects.filter(user=request.user, subject="Kiswahili Test One").order_by('-id')[:1]
    test2 = MyResults.objects.filter(user=request.user, subject="Kiswahili Test Two").order_by('-id')[:1]
    test3 = MyResults.objects.filter(user=request.user, subject="Kiswahili Test Three").order_by('-id')[:1]
    test4 = MyResults.objects.filter(user=request.user, subject="Kiswahili Test Four").order_by('-id')[:1]
    test5 = MyResults.objects.filter(user=request.user, subject="Kiswahili Test Five").order_by('-id')[:1]
    test6 = MyResults.objects.filter(user=request.user, subject="Kiswahili Test Six").order_by('-id')[:1]
    test7 = MyResults.objects.filter(user=request.user, subject="Kiswahili Test Seven").order_by('-id')[:1]
    test8 = MyResults.objects.filter(user=request.user, subject="Kiswahili Test Eight").order_by('-id')[:1]
    test9 = MyResults.objects.filter(user=request.user, subject="Kiswahili Test Nine").order_by('-id')[:1]
    test10 = MyResults.objects.filter(user=request.user, subject="Kiswahili Test Ten").order_by('-id')[:1]
    return render(request, 'core/kiswahili.html',
                  {'paydata':paydata,
                    'test1':test1,
                    'test2':test2,
                    'test3':test3,
                    'test4':test4,
                    'test5':test5,
                    'test6':test6,
                    'test7':test7,
                    'test8':test8,
                    'test9':test9,
                    'test10':test10
                    })

@login_required
def english(request):
    paydata = PaymentInfo.objects.filter(user=request.user)
    test1 = MyResults.objects.filter(user=request.user, subject="English Test One").order_by('-id')[:1]
    test2 = MyResults.objects.filter(user=request.user, subject="English Test Two").order_by('-id')[:1]
    test3 = MyResults.objects.filter(user=request.user, subject="English Test Three").order_by('-id')[:1]
    test4 = MyResults.objects.filter(user=request.user, subject="English Test Four").order_by('-id')[:1]
    test5 = MyResults.objects.filter(user=request.user, subject="English Test Five").order_by('-id')[:1]
    test6 = MyResults.objects.filter(user=request.user, subject="English Test Six").order_by('-id')[:1]
    test7 = MyResults.objects.filter(user=request.user, subject="English Test Seven").order_by('-id')[:1]
    test8 = MyResults.objects.filter(user=request.user, subject="English Test Eight").order_by('-id')[:1]
    test9 = MyResults.objects.filter(user=request.user, subject="English Test Nine").order_by('-id')[:1]
    test10 = MyResults.objects.filter(user=request.user, subject="English Test Ten").order_by('-id')[:1]
    return render(request, 'core/english.html',
                  {'paydata':paydata,
                    'test1':test1,
                    'test2':test2,
                    'test3':test3,
                    'test4':test4,
                    'test5':test5,
                    'test6':test6,
                    'test7':test7,
                    'test8':test8,
                    'test9':test9,
                    'test10':test10
                    })

@login_required
def science(request):
    paydata = PaymentInfo.objects.filter(user=request.user)
    test1 = MyResults.objects.filter(user=request.user, subject="Intergrated Science Test One").order_by('-id')[:1]
    test2 = MyResults.objects.filter(user=request.user, subject="Intergrated Science Test Two").order_by('-id')[:1]
    test3 = MyResults.objects.filter(user=request.user, subject="Intergrated Science Test Three").order_by('-id')[:1]
    test4 = MyResults.objects.filter(user=request.user, subject="Intergrated Science Test Four").order_by('-id')[:1]
    test5 = MyResults.objects.filter(user=request.user, subject="Intergrated Science Test Five").order_by('-id')[:1]
    test6 = MyResults.objects.filter(user=request.user, subject="Intergrated Science Test Six").order_by('-id')[:1]
    test7 = MyResults.objects.filter(user=request.user, subject="Intergrated Science Test Seven").order_by('-id')[:1]
    test8 = MyResults.objects.filter(user=request.user, subject="Intergrated Science Test Eight").order_by('-id')[:1]
    test9 = MyResults.objects.filter(user=request.user, subject="Intergrated Science Test Nine").order_by('-id')[:1]
    test10 = MyResults.objects.filter(user=request.user, subject="Intergrated Science Test Ten").order_by('-id')[:1]
    return render(request, 'core/science.html',
                  {'paydata':paydata,
                    'test1':test1,
                    'test2':test2,
                    'test3':test3,
                    'test4':test4,
                    'test5':test5,
                    'test6':test6,
                    'test7':test7,
                    'test8':test8,
                    'test9':test9,
                    'test10':test10
                    })

@login_required
def social(request):
    paydata = PaymentInfo.objects.filter(user=request.user)
    test1 = MyResults.objects.filter(user=request.user, subject="Creative Arts Test One").order_by('-id')[:1]
    test2 = MyResults.objects.filter(user=request.user, subject="Creative Arts Test Two").order_by('-id')[:1]
    test3 = MyResults.objects.filter(user=request.user, subject="Creative Arts Test Three").order_by('-id')[:1]
    test4 = MyResults.objects.filter(user=request.user, subject="Creative Arts Test Four").order_by('-id')[:1]
    test5 = MyResults.objects.filter(user=request.user, subject="Creative Arts Test Five").order_by('-id')[:1]
    test6 = MyResults.objects.filter(user=request.user, subject="Creative Arts Test Six").order_by('-id')[:1]
    test7 = MyResults.objects.filter(user=request.user, subject="Creative Arts Test Seven").order_by('-id')[:1]
    test8 = MyResults.objects.filter(user=request.user, subject="Creative Arts Test Eight").order_by('-id')[:1]
    test9 = MyResults.objects.filter(user=request.user, subject="Creative Arts Test Nine").order_by('-id')[:1]
    test10 = MyResults.objects.filter(user=request.user, subject="Creative Arts Test Ten").order_by('-id')[:1]
    return render(request, 'core/social.html',
                  {'paydata':paydata,
                    'test1':test1,
                    'test2':test2,
                    'test3':test3,
                    'test4':test4,
                    'test5':test5,
                    'test6':test6,
                    'test7':test7,
                    'test8':test8,
                    'test9':test9,
                    'test10':test10
                    })


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account Created for {email}, you can now login')
            html_template = 'core/welcomemail.html'
            html_message = render_to_string(html_template)
            subject = 'Welcome to Testprep!'
            email_from = 'Testprep@testprepken.com'
            recipient_list = [email]
            message = EmailMessage(subject, html_message,
                                   email_from, recipient_list)
            message.content_subtype = 'html'
            message.send(fail_silently=True)
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'core/register.html', {'form':form})




def categories(request):
    catData = models.QuizCategory.objects.all()
    return render(request, 'core/all-category.html', {'data':catData})

@login_required
def free_category_questions(request, cat_id):
    #paydata = PaymentConfirm.objects.filter(user=request.user)
    #if not paydata:
        #return redirect('make-a-payment')
    #else:
    category = QuizCategory.objects.get(id=cat_id)
    question = QuizQuestion.objects.filter(category=category).order_by('id').first()
    return render(request, 'core/questionslist.html', {'question':question, 'category':category})


@login_required
def category_questions(request, cat_id):
    paydata = PaymentInfo.objects.filter(user=request.user)
    if not paydata:
        return redirect('make-a-payment')
    else:
        category = QuizCategory.objects.get(id=cat_id)
        question = QuizQuestion.objects.filter(category=category).order_by('id').first()
        return render(request, 'core/questionslist.html', {'question':question, 'category':category})

@login_required
def submit_answer(request, cat_id, quest_id):
    if request.method=='POST':
        category = QuizCategory.objects.get(id=cat_id)
        questions1 = QuizQuestion.objects.all()
        question = questions1.filter(category=category,id__gt=quest_id).exclude(id=quest_id).order_by('id').first()

        quest = QuizQuestion.objects.get(id=quest_id)
        user = request.user
        answer = request.POST['answer']
        UserSubmittedAnswer.objects.create(user=user, question=quest, right_answer=answer)
        if question:
            return render(request, 'core/questionslist.html', {'question':question, 'category':category})
        else:
            result = UserSubmittedAnswer.objects.filter(user=request.user)
           
            
            score = 0
            percentage = 0
            for row in result:
                if row.question.right_opt == row.right_answer:
                    score+=1
            percentage = (score*100)/result.count()
            subject = UserSubmittedAnswer.objects.filter(user=request.user).first()
            subjectcat = subject.question.category
            MyResults.objects.create(user=user, percentage=percentage, subject=subjectcat)
            Progress.objects.create(user=user, percentage=percentage, category=category)
            UserSubmittedAnswer.objects.filter(user=request.user).delete()
            return render(request, 'core/results.html', {'result':result, 'score':score, 'percentage':percentage}) 
    else:
        return HttpResponse('Method not allowed!!')
    
@login_required
def stoptest(request):
    UserSubmittedAnswer.objects.filter(user=request.user).delete()
    return redirect('dashboard')



@login_required
def myresults(request):
    myresults = MyResults.objects.filter(user=request.user).order_by('-id')[:70]
    return render(request, 'core/userscores.html', {'myresults':myresults})

@login_required
def profile(request):
    return render(request, 'core/profile.html')



from usermanager.models import EmailVerification
@login_required
def dashboard(request):
    datum = EmailVerification.objects.filter(user=request.user)
    return render(request, 'core/subjects.html', {'datum': datum})


# @login_required
# def dashboaord(request):
#     paydata = PaymentDetails.objects.filter(user=request.user)
#     test1 = MyResults.objects.filter(user=request.user, subject="Kiswahili Test One").order_by('-id')[:1]
#     test2 = MyResults.objects.filter(user=request.user, subject="Test Two").order_by('-id')[:1]
#     test3 = MyResults.objects.filter(user=request.user, subject="Test Three").order_by('-id')[:1]
#     test4 = MyResults.objects.filter(user=request.user, subject="Test Four").order_by('-id')[:1]
#     test5 = MyResults.objects.filter(user=request.user, subject="Test Five").order_by('-id')[:1]
#     test6 = MyResults.objects.filter(user=request.user, subject="Test Six").order_by('-id')[:1]
#     test7 = MyResults.objects.filter(user=request.user, subject="Test Seven").order_by('-id')[:1]
#     test8 = MyResults.objects.filter(user=request.user, subject="Test Eight").order_by('-id')[:1]
#     test9 = MyResults.objects.filter(user=request.user, subject="Test Nine").order_by('-id')[:1]
#     test10 = MyResults.objects.filter(user=request.user, subject="Test Ten").order_by('-id')[:1]
#     return render(request, 
#                   'core/newdashboard.html',
#                    {'paydata':paydata,
#                     'test1':test1,
#                     'test2':test2,
#                     'test3':test3,
#                     'test4':test4,
#                     'test5':test5,
#                     'test6':test6,
#                     'test7':test7,
#                     'test8':test8,
#                     'test9':test9,
#                     'test10':test10
#                     })


def about(request):
    return render(request, 'core/about.html')

def contactus(request):
    return render(request, 'core/contactus.html')


def mailtest1(request):
    send_mail('Using SparkPost with Django123', 'This is a message from Django using SparkPost!123', 'Testprep@testprepken.com',
    ['reuben.omanyala22@gmail.com'], fail_silently=True)
    return render(request, 'core/about.html')


def welcomemail(request):
    return render(request, 'core/welcomemail.html')



import random
def questionListMaths(request):
    mathslistone = list(QuizQuestion.objects.filter(category=19).order_by('-id'))
    mathslisttwo = list(QuizQuestion.objects.filter(category=20).order_by('-id'))
    mathslisthree = list(QuizQuestion.objects.filter(category=21).order_by('-id'))
    datum = mathslistone + mathslisttwo + mathslisthree
    items = random.sample(datum, 15)
    return render(request, 'core/mathsquestionlist.html', {'items': items})