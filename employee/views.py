from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from forms import RegistrationForm
from datetime import datetime
from models import attend, salary
import UserList


def loggedin(request):
    check =  attend.objects.filter(a_user=request.user, a_date=datetime.now().date())
    if not check:
        u = attend.objects.create(a_user=request.user, a_date=datetime.now().date(), a_time=datetime.now().time())
        u.save()
        message = 'Login Success.'
    else:
        message = 'You have already been logged in'

    return render_to_response('registration/loggedin.html',
                                  {'user': request.user, 'message': message})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register/complete')
    else:
            form = RegistrationForm()
            token = {}
            token.update(csrf(request))
            token = {'form':form }
            return render(request,'registration/registration_form.html',token)


def registration_complete(request):
    return render_to_response('registration/registration_complete.html', )


def salarydetails(request):
    thismonth = datetime.today().month
    list_paidthismonth = salary.objects.filter(s_paiddate__month=thismonth)
    message = ""
    if not list_paidthismonth:
        message = "No any in the list"
    return render_to_response('display/salary.html',{'paidthismonth':list_paidthismonth, 'message':message})


def main(request):
    return render_to_response('main.html')