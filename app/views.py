from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.urls import reverse,reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import ListView,DetailView,DeleteView


def user_registration(request):
    FO=UserForm()
    d={'FO':FO}
    if request.method=='POST':
        FOD=UserForm(request.POST)
        if FOD.is_valid():
            NSUO=FOD.save(commit=False)
            password=FOD.cleaned_data['password']
            NSUO.set_password(password)
            NSUO.save()
            return HttpResponse('registration success')
        else:
            return HttpResponse('registration is not successful')
    return render(request,'app/user_registration.html',d)



class ListOfQuestions(ListView):
    model = DisplayQuestions
    context_object_name='QUSL'

class DetailQuestions(DetailView):
    model =DisplayQuestions
    context_object_name='QUSD'


def login_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        AUO=authenticate(username=username,password=password)
        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=username
            return HttpResponseRedirect(reverse('ListOfQuestions'))
        else:
            return render(request,'app/invalid.html')
        
    return render(request,'app/login_user.html')


@login_required
def post_questions(request):
    QUSF= DisplayQuestionsForm()
    D={'QUSF':QUSF}
    if request.method == 'POST':
        QUSFOD = DisplayQuestionsForm(request.POST)
        if  QUSFOD.is_valid():
            username=request.session['username']
            UO=User.objects.get(username=username)

            NSAQO = QUSFOD.save(commit=False)
            NSAQO.user = UO
            NSAQO.save()
            return HttpResponse('quiestion asked successfully')
        else:
            return HttpResponse('quiestion not asked successfully')
        
    return render(request,'app/post_questions.html',D)
@login_required
def answer_question(request):
    aqo = DisplayAnswersForm()
    d={'aqo':aqo}
    question = DisplayQuestions.objects.all()
    if request.method == 'POST':
        aqd= DisplayAnswersForm(request.POST)
        if aqd.is_valid():
            username=request.session['username']
            UO=User.objects.get(username=username)
            NSAQO = aqd.save(commit=False)
            NSAQO.user = UO
            NSAQO.save()
            Q=NSAQO.question
            AO=DisplayAnswers.objects.filter(question=Q)
            d1={'AO':AO}
            return  HttpResponse('Solution saved successfully')
        else:
            return HttpResponse('quiestion not asked successfully')
        
    return render(request, 'app/answer_question.html',d)

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('ListOfQuestions'))

@login_required
def likes(request):
    if request.method == 'POST':
        cb=request.POST['cb']
        AO=DisplayAnswers.objects.get(pk=cb)
        username=request.session.get('username')
        UO=User.objects.get(username=username)
        LO=Like.objects.get_or_create(answer=AO,user=UO,value='Like')[0]
        LO.save()
        return HttpResponseRedirect(reverse('ListOfQuestions'))
