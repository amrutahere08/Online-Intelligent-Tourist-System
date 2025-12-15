from django.shortcuts import render,redirect
from django.urls import reverse
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from touristapp.models import UserRegistration
from touristapp.models import UserLogin
from touristapp.models import BookInfo
from touristapp.models import CustomerInfo
from touristapp.models import FeedBackInfo
from touristapp.models import PaymentInfo
from touristapp.models import PlaceInfo
from touristapp.models import RouteInfo
from touristapp.models import VehicleInfo
from touristapp.models import UploadImage
from touristapp.models import ResortInfo
from touristapp.models import OtpCode

import datetime
import smtplib
import random
from django.core.files.storage import FileSystemStorage
import os
from tourist_db.settings import BASE_DIR




def index(request):
    return render(request,'index1.html')

def admin_home(request):
    return render(request,'admin_home.html')

def user_home(request):
    return render(request,'user_home.html')

def mainindex(request):
    return render(request,'index1.html')

def reg(request):
    if request.method=="POST":
        name=request.POST.get('t1','')
        city = request.POST.get('t2', '')
        address = request.POST.get('t3', '')
        email = request.POST.get('t4', '')
        contact = request.POST.get('t5', '')
        UserRegistration.objects.create(name=name,city=city,address=address,email=email,contact=contact)
    return render(request,'reg.html')

def login(request):
    if request.method=="POST":
        username =request.POST.get('t1','')
        request.session['username']=username
        password = request.POST.get('t2','')
        ucheck=UserLogin.objects.filter(username=username).count()
        if ucheck>=1:
            udata=UserLogin.objects.get(username=username)
            upass=udata.password
            utype=udata.utype
            if password==upass:
                if utype=="admin":
                    return render(request,'admin_home.html')
                if utype=="user":
                    return render(request,'user_home.html')
                if utype=="agency":
                    return render(request,'agency_home.html')
            else:
                return render(request, 'index1.html',{'msg':'invalid password'})
        else:
            return render(request, 'index1.html', {'msg': 'invalid username'})
    return render(request,'index1.html')

def reg_view(request):
    userdict=UserRegistration.objects.all()
    return render(request,'reg_view.html',{'userdict':userdict})

def bookinfo(request,pk):
    username=request.session['username']
    udata=ResortInfo.objects.get(id=pk)
    package_type=udata.package_type
    package_amount=udata.charges
    now=datetime.datetime.now()
    book_date=now.strftime("%Y-%m-%d")
    book_time=now.strftime("%X")
    if request.method=="POST":
        customer_id=request.POST.get('t1','')
        package_type= request.POST.get('t2', '')
        package_amount = request.POST.get('t3', '')
        book_date = request.POST.get('t4', '')
        book_time = request.POST.get('t5', '')
        no_of_members = request.POST.get('t6', '')
        total = request.POST.get('t7', '')
        BookInfo.objects.create(customer_id=customer_id,package_type=package_type,package_amount=package_amount,book_date=book_date,book_time=book_time,no_of_members=no_of_members,total=total,status='pending')
        userdict=ResortInfo.objects.all()
        return redirect('/resortinfo_view_c/',userdict='userdict')
    return render(request,'bookinfo.html',{'custid':username,'book_date':book_date,'book_time':book_time,'package_type':package_type,'package_amount':package_amount})

def bookinfo_view(request):
    userdict=BookInfo.objects.all()
    return render(request,'bookinfo_view.html',{'userdict':userdict})

def bookinfo_view_u(request):
    username=request.session['username']
    userdict=BookInfo.objects.filter(customer_id=username).values()
    return render(request,'bookinfo_view_u.html',{'userdict':userdict})

def bookinfo_del(request,pk):
    rid=BookInfo.objects.get(id=pk)
    rid.delete()
    userdict=BookInfo.objects.all()
    return render(request,'bookinfo_view_u.html',{'userdict':userdict})

def bookinfo_update(request,pk):
    userdict=BookInfo.objects.filter(id=pk).update(status='Accepted')
    base_url=reverse('bookinfo_view')
    userdict=BookInfo.objects.all()
    return redirect(base_url,userdict=userdict)



def bookinfo_db(request):
    if request.method=="POST":
        id=request.POST.get('id')
        customer_id=request.POST.get('t1','')
        package_type= request.POST.get('t2', '')
        package_amount = request.POST.get('t3', '')
        book_date = request.POST.get('t4', '')
        book_time = request.POST.get('t5', '')
        no_of_members = request.POST.get('t6', '')
        total = request.POST.get('t7', '')
        status = request.POST.get('t8', '')
        BookInfo.objects.filter(id=id).update(customer_id=customer_id,package_type=package_type,package_amount=package_amount,book_date=book_date,book_time=book_time,no_of_members=no_of_members,total=total,status=status)
        userdict=BookInfo.objects.all()
    return render(request,'bookinfo_view.html',{'userdict':userdict})


def customerinfo(request):
    if request.method=="POST" and request.FILES['myfile']:
        customer_name=request.POST.get('t2','')
        aadhar_no=request.POST.get('t3','')
        myfile = request.FILES['myfile']
        address = request.POST.get('t4', '')
        contact_no = request.POST.get('t5', '')
        email = request.POST.get('t6', '')
        password=request.POST.get('t7','')
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        pat = os.path.join(BASE_DIR, '/media/'+filename)
        CustomerInfo.objects.create(customer_name=customer_name,aadhar_no=aadhar_no,upload_aadhar_copy=myfile,address=address,contact_no=contact_no,email=email)
        UserLogin.objects.create(username=email,password=password,utype='user')
        return render(request,'index1.html')
    return render(request,'index1.html')


def customerinfo_view(request):
    userdict=CustomerInfo.objects.all()
    return render(request,'customerinfo_view.html',{'userdict':userdict})

def customerinfo_del(request,pk):
    rid=CustomerInfo.objects.get(id=pk)
    rid.delete()
    userdict=CustomerInfo.objects.all()
    return redirect('/customerinfo_view/',userdict='userdict')
    #return render(request,'customerinfo_view.html',{'userdict':userdict})

def customerinfo_update(request,pk):
    userdict=CustomerInfo.objects.filter(id=pk).values()
    return render(request,'customerinfo_edit.html',{'userdict':userdict})

def customerinfo_db(request):
    if request.method=="POST":
        id=request.POST.get('id')
        customer_name=request.POST.get('t2','')
        aadhar_no=request.POST.get('t3','')
        address = request.POST.get('t5', '')
        contact_no = request.POST.get('t6', '')
        email = request.POST.get('t7', '')
        CustomerInfo.objects.filter(id=id).update(customer_name=customer_name,aadhar_no=aadhar_no,address=address,contact_no=contact_no,email=email)
        return render(request, 'index.html')
        userdict = CustomerInfo.objects.all()
    return render(request, 'customerinfo_view.html',{'userdict': userdict})


def feedbackinfo(request):
    username=request.session['username']
    if request.method=="POST":
        customer_id = request.POST.get('t1', '')
        about_service = request.POST.get('t2', '')
        about_facilities = request.POST.get('t3', '')
        comments = request.POST.get('t4', '')
        FeedBackInfo.objects.create(customer_id=customer_id,about_service=about_service,about_facilities=about_facilities,comments=comments)
    return render(request,'feedbackinfo.html',{'username':username})

def feedbackinfo_view(request):
    userdict=FeedBackInfo.objects.all()
    return render(request,'feedbackinfo_view.html',{'userdict':userdict})

def feedbackinfo_del(request,pk):
    rid=FeedBackInfo.objects.get(id=pk)
    rid.delete()
    userdict=FeedBackInfo.objects.all()
    return render(request,'feedbackinfo_view.html',{'userdict':userdict})

def feedbackinfo_update(request,pk):
    userdict=FeedBackInfo.objects.filter(id=pk).values()
    return render(request,'feedbackinfo_edit.html',{'userdict':userdict})

def feedbackinfo_db(request):
    if request.method=="POST":
        id = request.POST.get('id')
        customer_id = request.POST.get('t1', '')
        about_service = request.POST.get('t2', '')
        about_facilities = request.POST.get('t3', '')
        comments = request.POST.get('t4', '')
        FeedBackInfo.objects.filter(id=id).update(customer_id=customer_id,about_service=about_service,about_facilities=about_facilities,comments=comments)
        userdict = FeedBackInfo.objects.all()
    return render(request,'feedbackinfo_view.html',{'userdict': userdict})


def paymentinfo(request,pk):
    udata=BookInfo.objects.get(id=pk)
    userid=udata.customer_id
    amount=udata.total
    if request.method=="POST":
        customer_id = request.POST.get('t1', '')
        amount = request.POST.get('t2', '')
        advance_payment = request.POST.get('t3', '')
        balance = request.POST.get('t4', '')
        BookInfo.objects.filter(id=pk).update(pay_status='paid')
        PaymentInfo.objects.create(customer_id=customer_id,amount=amount,advance_payment=advance_payment,balance=balance,payment_mode='online',payment_status='paid')
        return render(request,'payment2.html',{'amount':advance_payment})
    return render(request,'paymentinfo.html',{'userid':userid,'amount':amount})

def paymentinfo_view(request):
    userdict=PaymentInfo.objects.all()
    return render(request,'paymentinfo_view.html',{'userdict':userdict})

def paymentinfo_del(request,pk):
    rid=PaymentInfo.objects.get(id=pk)
    rid.delete()
    userdict=PaymentInfo.objects.all()
    return render(request,'paymentinfo_view.html',{'userdict':userdict})

def paymentinfo_update(request,pk):
    userdict=PaymentInfo.objects.filter(id=pk).values()
    return render(request,'paymentinfo_edit.html',{'userdict':userdict})

def paymentinfo_db(request):
    if request.method=="POST":
        id = request.POST.get('id')
        customer_id = request.POST.get('t1', '')
        amount = request.POST.get('t2', '')
        advance_payment = request.POST.get('t3', '')
        balance = request.POST.get('t4', '')
        payment_mode = request.POST.get('t5', '')
        payment_status = request.POST.get('t6', '')
        PaymentInfo.objects.filter(id=id).update(customer_id=customer_id,amount=amount,advance_payment=advance_payment,balance=balance,payment_mode=payment_mode,payment_status=payment_status)
        userdict = PaymentInfo.objects.all()
    return render(request, 'paymentinfo_view.html',{'userdict': userdict})

def placeinfo(request):
    now=datetime.datetime.now()
    year=now.strftime("%Y")
    if request.method=="POST" and request.FILES['myfile']:
        tourist_spot = request.POST.get('t2', '')
        climate = request.POST.get('t3', '')
        max_temp = request.POST.get('t4', '')
        min_temp = request.POST.get('t5', '')
        avg_rain_fall = request.POST.get('t6', '')
        population = request.POST.get('t7', '')
        languages = request.POST.get('t8', '')
        best_time_to_visit = request.POST.get('t9', '')
        clothing = request.POST.get('t10', '')
        visiting_places = request.POST.get('t11', '')
        total_cost = request.POST.get('t12', '')
        offer_cost = request.POST.get('t13', '')
        facilities = request.POST.get('t14', '')
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        pat = os.path.join(BASE_DIR, '/media/' + filename)
        PlaceInfo.objects.create(tourist_spot=tourist_spot,climate=climate,max_temp=max_temp,min_temp=min_temp,avg_rain_fall=avg_rain_fall,population=population,languages=languages,best_time_to_visit=best_time_to_visit,clothing=clothing,visiting_places=visiting_places,total_cost=total_cost,offer_cost=offer_cost,facilities=facilities,place_photo=myfile,year=year)
        return render(request, 'placeinfo.html')
    return render(request,'placeinfo.html')

def placeinfo_view(request):
    userdict=PlaceInfo.objects.all()
    return render(request,'placeinfo_view.html',{'userdict':userdict})

def placeinfo_del(request,pk):
    rid=PlaceInfo.objects.get(id=pk)
    rid.delete()
    userdict=PlaceInfo.objects.all()
    return redirect('/placeinfo_view/',userdict='userdict')
    #return render(request,'placeinfo_view.html',{'userdict':userdict})

def placeinfo_update(request,pk):
    userdict=PlaceInfo.objects.filter(id=pk).values()
    return render(request,'placeinfo_edit.html',{'userdict':userdict})

def placeinfo_db(request):
    if request.method=="POST":
        id = request.POST.get('id')
        tourist_spot = request.POST.get('t2', '')
        climate = request.POST.get('t3', '')
        max_temp = request.POST.get('t4', '')
        min_temp = request.POST.get('t5', '')
        avg_rain_fall = request.POST.get('t6', '')
        population = request.POST.get('t7', '')
        languages = request.POST.get('t8', '')
        best_time_to_visit = request.POST.get('t9', '')
        clothing = request.POST.get('t10', '')
        visiting_places = request.POST.get('t11', '')
        total_cost = request.POST.get('t12', '')
        offer_cost = request.POST.get('t13', '')
        facilities = request.POST.get('t14', '')
        PlaceInfo.objects.filter(id=id).update(place_id=id,tourist_spot=tourist_spot,climate=climate,max_temp=max_temp,min_temp=min_temp,avg_rain_fall=avg_rain_fall,population=population,languages=languages,best_time_to_visit=best_time_to_visit,clothing=clothing,visiting_places=visiting_places,total_cost=total_cost,offer_cost=offer_cost,facilities=facilities)
        userdict = PlaceInfo.objects.all()
        return render(request, 'placeinfo_view.html',{'userdict':userdict})




def routeinfo(request,pk):
    uid=PlaceInfo.objects.get(id=pk)
    if request.method=="POST":
        place_id = request.POST.get('t1', '')
        transport_type = request.POST.get('t2', '')
        from_place = request.POST.get('t3', '')
        destination = request.POST.get('t4', '')
        via = request.POST.get('t5', '')
        no_of_km = request.POST.get('t6', '')
        remarks = request.POST.get('t7', '')
        RouteInfo.objects.create(place_id=place_id,transport_type=transport_type,from_place=from_place,destination=destination,via=via,no_of_km=no_of_km,remarks=remarks)
    return render(request,'routeinfo.html',{'id':pk})

def routeinfo_view(request,pk):
    userdict=RouteInfo.objects.filter(place_id=pk).values()
    return render(request,'routeinfo_view2.html',{'userdict':userdict})

def routeinfo_del(request,pk):
    rid=RouteInfo.objects.get(id=pk)
    rid.delete()
    userdict=RouteInfo.objects.all()
    return render(request,'routeinfo_view.html',{'userdict':userdict})

def routeinfo_update(request,pk):
    userdict=RouteInfo.objects.filter(id=pk).values()
    return render(request,'routeinfo_edit.html',{'userdict':userdict})

def routeinfo_db(request):
    if request.method=="POST":
        id = request.POST.get('id')
        place_id = request.POST.get('t1', '')
        transport_type = request.POST.get('t2', '')
        from_place = request.POST.get('t3', '')
        destination = request.POST.get('t4', '')
        via = request.POST.get('t5', '')
        no_of_km = request.POST.get('t6', '')
        remarks = request.POST.get('t7', '')
        RouteInfo.objects.filter(id=id).update(place_id=place_id,transport_type=transport_type,from_place=from_place,destination=destination,via=via,no_of_km=no_of_km,remarks=remarks)
        userdict = RouteInfo.objects.all()
    return render(request, 'routeinfo_view.html', {'userdict': userdict})


def vehicleinfo(request):
    if request.method=="POST":
        vehicle_name = request.POST.get('t2', '')
        capacity = request.POST.get('t3', '')
        rate_per_km = request.POST.get('t4', '')
        hault_charge = request.POST.get('t5', '')
        fuel_type = request.POST.get('t6', '')
        condition = request.POST.get('t7', '')
        VehicleInfo.objects.create(vehicle_name=vehicle_name,capacity=capacity,rate_per_km=rate_per_km,hault_charge=hault_charge,fuel_type=fuel_type,condition=condition)
    return render(request,'vehicleinfo.html')

def vehicleinfo_view(request):
    userdict=VehicleInfo.objects.all()
    return render(request,'vehicleinfo_view.html',{'userdict':userdict})

def vehicleinfo_view_c(request):
    userdict=VehicleInfo.objects.all()
    return render(request,'vehicleinfo_view_c.html',{'userdict':userdict})

def vehicleinfo_del(request,pk):
    rid=VehicleInfo.objects.get(id=pk)
    rid.delete()
    userdict=VehicleInfo.objects.all()
    return render(request,'vehicleinfo_view.html',{'userdict':userdict})

def vehicleinfo_update(request,pk):
    userdict=VehicleInfo.objects.filter(id=pk).values()
    return render(request,'vehicleinfo_edit.html',{'userdict':userdict})

def vehicleinfo_db(request):
    if request.method=="POST":
        id = request.POST.get('id')
        vehicle_name = request.POST.get('t2', '')
        capacity = request.POST.get('t3', '')
        rate_per_km = request.POST.get('t4', '')
        hault_charge = request.POST.get('t5', '')
        fuel_type = request.POST.get('t6', '')
        condition = request.POST.get('t7', '')
        VehicleInfo.objects.filter(id=id).update(vehicle_name=vehicle_name,capacity=capacity,rate_per_km=rate_per_km,hault_charge=hault_charge,fuel_type=fuel_type,condition=condition)
        userdict = VehicleInfo.objects.all()
    return render(request, 'vehicleinfo_view.html', {'userdict': userdict})


def reg_del(request,pk):
    rid=UserRegistration.objects.get(id=pk)
    rid.delete()
    userdict=UserRegistration.objects.all()
    return render(request,'reg_view.html',{'userdict':userdict})

def simple_upload(request):
    if request.method=='POST' and request.FILES['myfile']:
        myfile=request.FILES['myfile']
        name=request.POST.get('t1')
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        uploaded_file_url=fs.url(filename)
        pat=os.path.join(BASE_DIR, '/media/'+filename)
        UploadImage.objects.create(name=name,image=myfile)
        return render(request,'index.html')
    return render(request,'simple_upload.html')


def resortinfo(request):

    if request.method=="POST" and request.FILES['myfile']:
        resort_name=request.POST.get('t1')
        city = request.POST.get('t2')
        address = request.POST.get('t3')
        contact = request.POST.get('t4')
        activities= request.POST.get('t5')
        facilities = request.POST.get('t6')
        package_type = request.POST.get('t7')
        charges = request.POST.get('t8')
        myfile=request.FILES['myfile']

        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        pat = os.path.join(BASE_DIR, '/media/' + filename)
        ResortInfo.objects.create(resort_name=resort_name,city=city,address=address,contact=contact,activities=activities,facilities=facilities,package_type=package_type,charges=charges,photo=myfile)
        return render(request,'resort_info.html')
    return render(request,'resort_info.html')

def resortinfo_view(request):
    userdict=ResortInfo.objects.all()
    return render(request,'resortinfo_view.html',{'userdict':userdict})

def resortinfo_view_c(request):
    userdict=ResortInfo.objects.all()
    return render(request,'resortinfo_view_c.html',{'userdict':userdict})

def resortinfo_update(request,pk):
    userdict=ResortInfo.objects.filter(id=pk).values()
    if request.method=="POST":
        resort_name = request.POST.get('t1')
        city = request.POST.get('t2')
        address = request.POST.get('t3')
        contact = request.POST.get('t4')
        activities = request.POST.get('t5')
        facilities = request.POST.get('t6')
        package_type = request.POST.get('t7')
        charges = request.POST.get('t8')
        myfile = request.FILES['myfile']

        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        pat = os.path.join(BASE_DIR, '/media/' + filename)
        ResortInfo.objects.filter(id=pk).update(resort_name=resort_name, city=city, address=address, contact=contact,activities=activities, facilities=facilities, package_type=package_type,charges=charges, photo=myfile)
        userdict=ResortInfo.objects.all()
        base_url=reverse('resortinfo_view')
        return redirect(base_url,userdict='userdict')
    return render(request,'resort_update.html',{'userdict':userdict})


def placeinfo_view_c(request):
    userdict=PlaceInfo.objects.all()
    return render(request,'placeinfo_view_c.html',{'userdict':userdict})


def placeinfo_view2_c(request):
    if request.method=="POST":
        place=request.POST.get('t2')
        userdict=PlaceInfo.objects.filter(tourist_spot=place).values()
        return render(request,'placeinfo_view2_c.html',{'userdict':userdict})



def simple_upload_view(request):
    user_dict=UploadImage.objects.all()
    return render(request,'simple_upload_view.html',{'user_dict':user_dict})


def change_password(request):
    if request.method=="POST":
        username=request.POST.get('t1','')
        current_password=request.POST.get('t2','')
        new_password=request.POST.get('t3','')
        confirm_password=request.POST.get('t4','')
        udata=UserLogin.objects.filter(username=username).filter(password=current_password).count()
        if udata >= 1:
            if new_password == confirm_password:
                UserLogin.objects.filter(username=username).update(password=new_password)
                base_url=reverse('login')
                return redirect(base_url)
            else:
                return render(request,'change_password.html')
        else:
            return render(request,'change_password.html')

    return render(request,'change_password.html')

def send_email(request):
    content="Testing email"
    mail=smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    mail.login('hemalatakwr@gmail.com','Hemu1995')
    mail.sendmail('hemalatakwr@gmail.com','komalpujar185@gmail.com',content)
    mail.close()
    return render(request,'send_email.html')



def forgotpass(request):
    if request.method=="POST":
        username=request.POST.get('t1')
        request.session['username']=username
        chcek=UserLogin.objects.filter(username=username).count()
        if chcek>=1:
            udata=UserLogin.objects.get(username=username)
            password=udata.password
            otp=random.randint(1,5000)
            OtpCode.objects.create(otp_code=otp,status='active')
            content=str(otp)
            mail=smtplib.SMTP('smtp.gmail.com',587)
            mail.ehlo()
            mail.starttls()
            mail.login('hemalatakwr@gmail.com','@hemu1995')
            mail.sendmail('hemalatakwr@gmail.com',username,content)
            mail.close()
            base_url=reverse('otp')
            return redirect(base_url)
            #return render(request,'otp.html',{'password':password})
        else:
            return render(request,'forgetpass.html',{'msg':'invalid username'})
    return render(request,'forgetpass.html')



def otp(request):
    username=request.session['username']
    if request.method=="POST":
        otp=request.POST.get('t1')
        ucheck=OtpCode.objects.filter(otp_code=otp).count()
        if ucheck >=1:
            base_url=reverse('pass_db')
            return redirect(base_url)
        else:
            url=reverse('otp')
            msg='invalid otp'
            return redirect(url,msg='msg')

        #newpass=request.POST.get('t1')
        #cpass=request.POST.get('t2')
        #UserLogin.objects.filter(username=username).update(password=newpass)
        #return render(request,'print.html')
    return render(request,'otp.html')

def pass_db(request):
    username = request.session['username']
    if request.method == "POST":
        newpass = request.POST.get('t1')
        cpass = request.POST.get('t2')
        if newpass==cpass:

            UserLogin.objects.filter(username=username).update(password=newpass)
            log_url=reverse('index')
            return redirect(log_url)
        else:
            return render(request, 'print.html',{'msg':'newpass and confirm pass must be same'})

    return render(request, 'print.html')


def google_map(request,stype):
    query = str(stype+","+"Karnataka")
    geolocator = Nominatim(user_agent="AIzaSyDqzzXXuRwP0cYHLBis4RPSaL2h3XBGp0I")
    location = geolocator.geocode(query,timeout=3000)
    # print(location.address)
    latitude = location.latitude
    longitude = location.longitude

    return render(request,'google_map.html',{'la':latitude,'lg':longitude})



def place_wise_year(request):
    userdict=PlaceInfo.objects.values('year').distinct()
    if request.method=="POST":
        year=request.POST.get('t1')
        count=PlaceInfo.objects.filter(year=year).count()
        userdict=PlaceInfo.objects.filter(year=year).values()
        return render(request,'place_wise_year_view.html',{'count':count,'userdict':userdict})
    return render(request,'place_wise_year.html',{'userdict':userdict})


# Advanced Search Function
def search_places(request):
    from touristapp.models import Rating
    places = PlaceInfo.objects.all()
    
    if request.method == "POST":
        search_query = request.POST.get('search', '')
        min_price = request.POST.get('min_price', '')
        max_price = request.POST.get('max_price', '')
        min_rating = request.POST.get('min_rating', '')
        
        if search_query:
            places = places.filter(tourist_spot__icontains=search_query)
        
        if min_price:
            places = places.filter(offer_cost__gte=min_price)
        
        if max_price:
            places = places.filter(offer_cost__lte=max_price)
        
        if min_rating:
            places = places.filter(rating__gte=min_rating)
    
    return render(request, 'search_places.html', {'places': places})


# Rating Submission for Places
def rate_place(request, pk):
    from touristapp.models import Rating
    username = request.session.get('username', 'guest')
    
    if request.method == "POST":
        rating_value = int(request.POST.get('rating', 0))
        review = request.POST.get('review', '')
        
        # Save rating
        Rating.objects.create(
            customer_id=username,
            item_type='place',
            item_id=pk,
            rating=rating_value,
            review=review
        )
        
        # Update place average rating
        place = PlaceInfo.objects.get(id=pk)
        all_ratings = Rating.objects.filter(item_type='place', item_id=pk)
        avg_rating = sum([r.rating for r in all_ratings]) / len(all_ratings)
        place.rating = round(avg_rating, 2)
        place.total_ratings = len(all_ratings)
        place.save()
        
        return redirect('/placeinfo_view_c/')
    
    place = PlaceInfo.objects.get(id=pk)
    return render(request, 'rate_place.html', {'place': place})


# Rating Submission for Resorts
def rate_resort(request, pk):
    from touristapp.models import Rating
    username = request.session.get('username', 'guest')
    
    if request.method == "POST":
        rating_value = int(request.POST.get('rating', 0))
        review = request.POST.get('review', '')
        
        # Save rating
        Rating.objects.create(
            customer_id=username,
            item_type='resort',
            item_id=pk,
            rating=rating_value,
            review=review
        )
        
        # Update resort average rating
        resort = ResortInfo.objects.get(id=pk)
        all_ratings = Rating.objects.filter(item_type='resort', item_id=pk)
        avg_rating = sum([r.rating for r in all_ratings]) / len(all_ratings)
        resort.rating = round(avg_rating, 2)
        resort.total_ratings = len(all_ratings)
        resort.save()
        
        return redirect('/resortinfo_view_c/')
    
    resort = ResortInfo.objects.get(id=pk)
    return render(request, 'rate_resort.html', {'resort': resort})


# Analytics Dashboard
def analytics_dashboard(request):
    from django.db.models import Sum, Count
    from touristapp.models import Rating
    
    # Booking statistics
    total_bookings = BookInfo.objects.count()
    accepted_bookings = BookInfo.objects.filter(status='Accepted').count()
    pending_bookings = BookInfo.objects.filter(status='pending').count()
    
    # Revenue statistics
    total_revenue = 0
    for booking in BookInfo.objects.all():
        try:
            total_revenue += float(booking.total)
        except:
            pass
    
    paid_revenue = 0
    for payment in PaymentInfo.objects.all():
        try:
            paid_revenue += float(payment.advance_payment)
        except:
            pass
    
    # Popular destinations
    popular_places = PlaceInfo.objects.order_by('-rating', '-total_ratings')[:5]
    popular_resorts = ResortInfo.objects.order_by('-rating', '-total_ratings')[:5]
    
    # Customer statistics
    total_customers = CustomerInfo.objects.count()
    total_feedback = FeedBackInfo.objects.count()
    
    # Recent ratings
    recent_ratings = Rating.objects.order_by('-created_at')[:10]
    
    context = {
        'total_bookings': total_bookings,
        'accepted_bookings': accepted_bookings,
        'pending_bookings': pending_bookings,
        'total_revenue': total_revenue,
        'paid_revenue': paid_revenue,
        'popular_places': popular_places,
        'popular_resorts': popular_resorts,
        'total_customers': total_customers,
        'total_feedback': total_feedback,
        'recent_ratings': recent_ratings,
    }
    
    return render(request, 'analytics_dashboard.html', context)
