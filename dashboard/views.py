from django.shortcuts import render,redirect
from django.http import HttpResponse
from beautyapp.models import Citys
from beautyapp.models import Appointment
from django.contrib import messages
from beautyapp.models import Services
from beautyapp.models import Gift
from beautyapp.models import Carriers
from .models import Addstaff
from .models import Guest
from beautyapp.models import Franchisee

from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from twilio.rest import Client

# # for weasyprint
# from django.core.files.storage import FileSystemStorage
# from django.http import HttpResponse
# from django.template.loader import render_to_string

# from weasyprint import HTML


# Create your views here.
@login_required(login_url='/dashboard/admin_login/')
def dashboard(request):
        if request.user.is_superuser:
            guests = Guest.objects.all()
        else:
            city = request.user.city
            guests = Guest.objects.filter(city=city)
        return render(request,'dashboard/guest_list.html',{'guests':guests})

def guest(request):
    if request.method == 'POST':
        name = request.POST['name']
        mobileno = request.POST['mobileno']
        service = request.POST['service']
        serviceby = request.POST['serviceby']
        duration = request.POST['duration']
        timein = request.POST['timein']
        timeout = request.POST['timeout']
        totaltime = request.POST['totaltime']
        price = request.POST['price']
        paym = request.POST['paym']

        city=request.POST['city']
        city = Citys.objects.get(id=city)

        print(service)
        s = Services.objects.get(pk=service)
        a = Addstaff.objects.get(pk=serviceby)


        new_guest = Guest(gname=name,mobile=mobileno,city=city,services=s,treatment_by=a,duration=duration,time_in=timein,time_out=timeout,total_time=totaltime,price=price,payment=paym)
        new_guest.save()
        messages.success(request,' ')
        return redirect(guest)
    services = Services.objects.all()

    if request.user.is_superuser:
        staffs = Addstaff.objects.all()
    else:
        staff_city = request.user.city
        staffs = Addstaff.objects.filter(city=staff_city)

    city = Citys.objects.all()
    return render(request,'dashboard/guest.html',{'services':services,'staffs':staffs,'city':city})


# def guest_list(request):
#     guests = Guest.objects.all()
#     return render(request,'dashboard/guest_list.html',{'guests':guests})

def gdel(request,id):
    dc=Guest.objects.get(id=id)
    dc.delete()
    return redirect(dashboard)

def carriers(request):
    careers=Carriers.objects.all()


    return render(request,'dashboard/carriers.html', {'careers':careers})

def gifts(request):
    gifts = Gift.objects.all()
    return render(request,'dashboard/gifts.html',{'gifts':gifts})

def appointment(request):
    if request.user.is_superuser:
        appointment = Appointment.objects.all()
    else:
        city = request.user.city
        if city is None:
            return redirect(dashboard)
        print(city,' ----- ',city.name)
        appointment = Appointment.objects.filter(city=city).order_by('-date')

    paginator = Paginator(appointment, 5)  # 10 appointments in each page
    page = request.GET.get('page')
    try:
        appointment_list = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        appointment_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        appointment_list = paginator.page(paginator.num_pages)


    return render(request,'dashboard/appointment.html',{'appointment':appointment_list,'page': page} )
# def edit(request, id):
#     city = Citys.objects.get(id=id)
#     context = {'city': city}
#     return render(request, 'crud/edit.html', context)

def confirm_appointment(request,id):
    appointment = Appointment.objects.get(id=id)
    if request.method == 'POST':
        comments = request.POST['comments']
        mobileno = appointment.mobileno

        account_sid = 'ACf72d08db3e903a8b1c7cef4abcefd1ed'
        auth_token = 'a6373d036f80a7ccbfc32fd173883a2b'
        client = Client(account_sid, auth_token)
        message = client.messages.create(from_='+19386669137',body =comments,to ="+918356016968",)

    return HttpResponse("Msg sent to the user")

def update(request, id):
    city = Citys.objects.get(id=id)
    city.name = request.POST['name']
    city.save()
    return redirect(addcity)

def clientupdate(request, id):
    g  = Guest.objects.get(id=id)
    # g.time_in = request.POST['time_in']
    g.time_out= request.POST['time_out']
    g.total_time=request.POST['total_time']
    g.comments = request.POST['comments']
    g.save()
    return redirect(dashboard)

def modify(request, id):
    service = Services.objects.get(id=id)
    service.name = request.POST['name']

    service.save()
    return redirect(addservice)





def deletes(request,id):
    service = Services.objects.get(id=id)
    service.delete()
    # messages.success(request,('item has been deleted!'))
    return redirect(addservice)

def jobdelete(request,id):
    ca=Carriers.objects.get(id=id)
    ca.delete()
    return redirect(carriers)

def deletgift(request,id):
    g=Gift.objects.get(id=id)
    g.delete()
    return redirect(gifts)


def deleted(request,id):
    appointments=Appointment.objects.get(id=id)
    appointments.delete()
    return redirect(appointment)


def delete(request,id):
    city = Citys.objects.get(id=id)
    city.delete()
    # messages.success(request,('item has been deleted!'))
    return redirect( addcity)

def addservice(request):
    if request.method == 'POST':
        name = request.POST['name']
        service = Services(name=name)
        service.save()
        return redirect(addservice)
    else:
        context_data = {
        'service':Services.objects.all()
        }
    return render(request,'dashboard/addservices.html',context_data)


# def price(request):
#     if request.method == 'POST':
#         price = request.POST['price']
#         p = Price(price=price)
#         p.save()
#         return redirect(price)
#     else:
#         context_data = {
#         'p':Addprice.objects.all()
#         }
#     return render(request,'dashboard/price.html',context_data)


def addstaff(request):
    if request.method == 'POST':
        name = request.POST['name']
        mobileno = request.POST['mobileno']
        services=request.POST['service']
        city=request.POST['city']
        city = Citys.objects.get(id=city)
        se=Services.objects.get(id=services)
        staff=Addstaff(name=name,mobileno=mobileno,city=city,services=se)
        staff.save()
        return redirect(addstaff)
    else:
        if request.user.is_superuser:
            staff = Addstaff.objects.all()
        else:
            staff_city = request.user.city
            staff = Addstaff.objects.filter(city=staff_city)

        context_data = {
        'service':Services.objects.all(),
        'staff':staff,
        'city':Citys.objects.all()
        }
    return render(request,'dashboard/addstaff.html',context_data)

def delete_staff(request,id):
    staff = Addstaff.objects.get(id=id)
    staff.delete()

    return redirect(addstaff)

def update_staff(request, id):
    if request.method == 'POST':
        staff = Addstaff.objects.get(id=id)
        staff.name = request.POST['name']
        staff.mobileno = request.POST['mobileno']
        s = request.POST.get('service')
        service = Services.objects.get(id=s)

        service.save()
        staff.services = service

        staff.save()
        return redirect(addstaff)
    return redirect(addstaff)

def addcity(request):
    if request.method == 'POST':
        name = request.POST['name']
        city = Citys(name=name)
        city.save()
        return redirect(addcity)
    else:
        context_data = {

          'city':Citys.objects.all()


        }

    return render(request,'dashboard/addcity.html',context_data)



def admin_login(request):
    if request.method=='POST':


        register=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if register is not None:
            auth.login(request,register)
            return redirect(dashboard)
        else:
            messages.info(request,'invalid credentials')
            return redirect(admin_login)
    else:
        return render(request,'dashboard/admin_login.html')


def franch(request):
    f=Franchisee.objects.all()
    return render(request,'dashboard/franch.html', {'f':f})

def deletefranch(request, id):
    f = Franchisee.objects.get(id=id)
    f.delete()
    return redirect(franch)

def report(request):
    guests = Guest.objects.all()
    return render(request,'dashboard/report.html',{'guests':guests})


# def html_to_pdf_view(request):
#     guests = Guest.objects.all()
#     html_string = render_to_string('dashboard/report.html',{'guests':guests})

#     html = HTML(string=html_string)
#     html.write_pdf(target='/tmp/mypdf.pdf');

#     fs = FileSystemStorage('/tmp')
#     with fs.open('mypdf.pdf') as pdf:
#         response = HttpResponse(pdf, content_type='application/pdf')
#         response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
#         return response

#     return response