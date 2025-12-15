from django.db import models

class UserRegistration(models.Model):
    name=models.CharField(max_length=40)
    city=models.CharField(max_length=30)
    address=models.CharField(max_length=100)
    email=models.CharField(max_length=40)
    contact=models.CharField(max_length=10)

class UserLogin(models.Model):
    username=models.CharField(max_length=40)
    password=models.CharField(max_length=20)
    utype=models.CharField(max_length=20)

class BookInfo(models.Model):
    customer_id=models.CharField(max_length=40)
    package_type=models.CharField(max_length=40)
    package_amount=models.CharField(max_length=100)
    book_date=models.DateField()
    book_time=models.CharField(max_length=100)
    no_of_members=models.CharField(max_length=10)
    total=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    pay_status=models.CharField(max_length=30,null=True)

class ResortInfo(models.Model):
    resort_name=models.CharField(max_length=200)
    city=models.CharField(max_length=400)
    address=models.CharField(max_length=400)
    contact=models.CharField(max_length=10)
    activities=models.CharField(max_length=100,null=True,blank=True)
    facilities=models.CharField(max_length=100)
    package_type=models.CharField(max_length=100)
    charges=models.CharField(max_length=100)
    photo=models.FileField(upload_to='documents/')
    rating=models.DecimalField(max_digits=3, decimal_places=2, default=0.0, null=True, blank=True)
    total_ratings=models.IntegerField(default=0, null=True, blank=True)


class CustomerInfo(models.Model):
    customer_id=models.CharField(max_length=40)
    customer_name=models.CharField(max_length=40)
    aadhar_no=models.CharField(max_length=100)
    upload_aadhar_copy=models.FileField(upload_to='documents/')
    address=models.CharField(max_length=100)
    contact_no=models.CharField(max_length=100)
    email=models.CharField(max_length=100)

class FeedBackInfo(models.Model):
    customer_id=models.CharField(max_length=40)
    about_service=models.CharField(max_length=40)
    about_facilities=models.CharField(max_length=40)
    comments=models.CharField(max_length=100)

class PaymentInfo(models.Model):
    customer_id=models.CharField(max_length=40)
    amount= models.CharField(max_length=100)
    advance_payment=models.CharField(max_length=100)
    balance=models.CharField(max_length=100)
    payment_mode=models.CharField(max_length=100)
    payment_status=models.CharField(max_length=100)

class PlaceInfo(models.Model):
    place_id=models.CharField(max_length=40)
    tourist_spot=models.CharField(max_length=100)
    climate=models.CharField(max_length=100)
    max_temp=models.CharField(max_length=100)
    min_temp=models.CharField(max_length=100)
    avg_rain_fall=models.CharField(max_length=100)
    population=models.CharField(max_length=40)
    languages=models.CharField(max_length=40)
    best_time_to_visit=models.CharField(max_length=50)
    clothing=models.CharField(max_length=50)
    visiting_places=models.CharField(max_length=50)
    total_cost=models.CharField(max_length=100)
    offer_cost=models.CharField(max_length=100)
    facilities=models.CharField(max_length=100)
    place_photo=models.FileField(upload_to='documents/')
    year = models.CharField(max_length=100,null=True,blank=True)
    rating=models.DecimalField(max_digits=3, decimal_places=2, default=0.0, null=True, blank=True)
    total_ratings=models.IntegerField(default=0, null=True, blank=True)


class RouteInfo(models.Model):
    place_id=models.CharField(max_length=40)
    transport_type=models.CharField(max_length=100)
    from_place=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)
    via=models.CharField(max_length=100)
    no_of_km=models.CharField(max_length=100)
    remarks=models.CharField(max_length=40)



class VehicleInfo(models.Model):
    vehicle_id=models.CharField(max_length=40)
    vehicle_name=models.CharField(max_length=100)
    capacity=models.CharField(max_length=100)
    rate_per_km=models.CharField(max_length=100)
    hault_charge=models.CharField(max_length=100)
    fuel_type=models.CharField(max_length=40)
    condition=models.CharField(max_length=100)

class UploadImage(models.Model):
    name=models.CharField(max_length=40)
    image=models.FileField(upload_to='documents/')

class ChangePassword(models.Model):
    username=models.CharField(max_length=40)
    current_password=models.CharField(max_length=40)
    new_password=models.CharField(max_length=40)
    confirm_password=models.CharField(max_length=40)

class OtpCode(models.Model):
    otp_code=models.CharField(max_length=40,null=True)
    status = models.CharField(max_length=40,null=True)

class Rating(models.Model):
    customer_id=models.CharField(max_length=40)
    item_type=models.CharField(max_length=20)  # 'place' or 'resort'
    item_id=models.IntegerField()
    rating=models.IntegerField()  # 1-5 stars
    review=models.TextField(null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)