from django.core.management.base import BaseCommand
from touristapp.models import (
    UserLogin, UserRegistration, CustomerInfo, PlaceInfo, 
    ResortInfo, VehicleInfo, RouteInfo, BookInfo, 
    PaymentInfo, FeedBackInfo
)
from django.core.files.base import ContentFile
import datetime
import os

class Command(BaseCommand):
    help = 'Populate database with India-related sample data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting database population...')
        
        # Clear existing data (optional)
        self.stdout.write('Clearing existing data...')
        UserLogin.objects.all().delete()
        UserRegistration.objects.all().delete()
        CustomerInfo.objects.all().delete()
        PlaceInfo.objects.all().delete()
        ResortInfo.objects.all().delete()
        VehicleInfo.objects.all().delete()
        RouteInfo.objects.all().delete()
        BookInfo.objects.all().delete()
        PaymentInfo.objects.all().delete()
        FeedBackInfo.objects.all().delete()
        
        # 1. Create User Logins
        self.stdout.write('Creating user logins...')
        logins = [
            {'username': 'admin@tourist.com', 'password': 'admin123', 'utype': 'admin'},
            {'username': 'agency@travel.com', 'password': 'agency123', 'utype': 'agency'},
            {'username': 'user1@gmail.com', 'password': 'user123', 'utype': 'user'},
            {'username': 'user2@gmail.com', 'password': 'user123', 'utype': 'user'},
            {'username': 'user3@gmail.com', 'password': 'user123', 'utype': 'user'},
            {'username': 'rajesh.kumar@gmail.com', 'password': 'rajesh123', 'utype': 'user'},
            {'username': 'priya.sharma@gmail.com', 'password': 'priya123', 'utype': 'user'},
            {'username': 'amit.patel@gmail.com', 'password': 'amit123', 'utype': 'user'},
            {'username': 'sneha.reddy@gmail.com', 'password': 'sneha123', 'utype': 'user'},
            {'username': 'vikram.singh@gmail.com', 'password': 'vikram123', 'utype': 'user'},
        ]
        
        for login in logins:
            UserLogin.objects.create(**login)
        self.stdout.write(self.style.SUCCESS(f'Created {len(logins)} user logins'))
        
        # 2. Create User Registrations
        self.stdout.write('Creating user registrations...')
        registrations = [
            {'name': 'Rajesh Kumar', 'city': 'Mumbai', 'address': '123 Marine Drive, Mumbai', 'email': 'rajesh.kumar@gmail.com', 'contact': '9876543210'},
            {'name': 'Priya Sharma', 'city': 'Delhi', 'address': '456 Connaught Place, Delhi', 'email': 'priya.sharma@gmail.com', 'contact': '9876543211'},
            {'name': 'Amit Patel', 'city': 'Ahmedabad', 'address': '789 SG Highway, Ahmedabad', 'email': 'amit.patel@gmail.com', 'contact': '9876543212'},
            {'name': 'Sneha Reddy', 'city': 'Hyderabad', 'address': '321 Banjara Hills, Hyderabad', 'email': 'sneha.reddy@gmail.com', 'contact': '9876543213'},
            {'name': 'Vikram Singh', 'city': 'Jaipur', 'address': '654 MI Road, Jaipur', 'email': 'vikram.singh@gmail.com', 'contact': '9876543214'},
        ]
        
        for reg in registrations:
            UserRegistration.objects.create(**reg)
        self.stdout.write(self.style.SUCCESS(f'Created {len(registrations)} user registrations'))
        
        # 3. Create Customer Info
        self.stdout.write('Creating customer information...')
        customers = [
            {'customer_id': 'user1@gmail.com', 'customer_name': 'Arjun Mehta', 'aadhar_no': '123456789012', 'address': '12 MG Road, Bangalore', 'contact_no': '9876543215', 'email': 'user1@gmail.com'},
            {'customer_id': 'rajesh.kumar@gmail.com', 'customer_name': 'Rajesh Kumar', 'aadhar_no': '234567890123', 'address': '123 Marine Drive, Mumbai', 'contact_no': '9876543210', 'email': 'rajesh.kumar@gmail.com'},
            {'customer_id': 'priya.sharma@gmail.com', 'customer_name': 'Priya Sharma', 'aadhar_no': '345678901234', 'address': '456 Connaught Place, Delhi', 'contact_no': '9876543211', 'email': 'priya.sharma@gmail.com'},
            {'customer_id': 'amit.patel@gmail.com', 'customer_name': 'Amit Patel', 'aadhar_no': '456789012345', 'address': '789 SG Highway, Ahmedabad', 'contact_no': '9876543212', 'email': 'amit.patel@gmail.com'},
            {'customer_id': 'sneha.reddy@gmail.com', 'customer_name': 'Sneha Reddy', 'aadhar_no': '567890123456', 'address': '321 Banjara Hills, Hyderabad', 'contact_no': '9876543213', 'email': 'sneha.reddy@gmail.com'},
        ]
        
        # Create dummy file for upload_aadhar_copy
        dummy_file = ContentFile(b'dummy aadhar content', name='aadhar_dummy.pdf')
        
        for customer in customers:
            CustomerInfo.objects.create(
                customer_id=customer['customer_id'],
                customer_name=customer['customer_name'],
                aadhar_no=customer['aadhar_no'],
                upload_aadhar_copy=dummy_file,
                address=customer['address'],
                contact_no=customer['contact_no'],
                email=customer['email']
            )
        self.stdout.write(self.style.SUCCESS(f'Created {len(customers)} customer records'))
        
        # 4. Create Tourist Places (India-focused)
        self.stdout.write('Creating tourist places...')
        places = [
            {
                'place_id': '1',
                'tourist_spot': 'Goa Beaches',
                'climate': 'Tropical',
                'max_temp': '33°C',
                'min_temp': '20°C',
                'avg_rain_fall': '3000mm',
                'population': '1.5 Million',
                'languages': 'Konkani, Marathi, Hindi, English',
                'best_time_to_visit': 'November to February',
                'clothing': 'Light cotton, beachwear',
                'visiting_places': 'Baga Beach, Calangute, Fort Aguada',
                'total_cost': '25000',
                'offer_cost': '20000',
                'facilities': 'Beach resorts, Water sports, Nightlife',
                'year': '2024'
            },
            {
                'place_id': '2',
                'tourist_spot': 'Kerala Backwaters',
                'climate': 'Tropical Monsoon',
                'max_temp': '32°C',
                'min_temp': '22°C',
                'avg_rain_fall': '3055mm',
                'population': '3.5 Million',
                'languages': 'Malayalam, Tamil, English',
                'best_time_to_visit': 'September to March',
                'clothing': 'Light cotton, traditional wear',
                'visiting_places': 'Alleppey, Kumarakom, Vembanad Lake',
                'total_cost': '30000',
                'offer_cost': '25000',
                'facilities': 'Houseboats, Ayurveda, Traditional cuisine',
                'year': '2024'
            },
            {
                'place_id': '3',
                'tourist_spot': 'Jaipur - Pink City',
                'climate': 'Semi-arid',
                'max_temp': '45°C',
                'min_temp': '8°C',
                'avg_rain_fall': '650mm',
                'population': '3.1 Million',
                'languages': 'Hindi, Rajasthani, English',
                'best_time_to_visit': 'October to March',
                'clothing': 'Light cotton in summer, woolens in winter',
                'visiting_places': 'Amber Fort, City Palace, Hawa Mahal',
                'total_cost': '22000',
                'offer_cost': '18000',
                'facilities': 'Heritage hotels, Camel rides, Cultural shows',
                'year': '2024'
            },
            {
                'place_id': '4',
                'tourist_spot': 'Manali - Hill Station',
                'climate': 'Alpine',
                'max_temp': '25°C',
                'min_temp': '-2°C',
                'avg_rain_fall': '1363mm',
                'population': '8000',
                'languages': 'Hindi, Punjabi, English',
                'best_time_to_visit': 'May to June, December to February',
                'clothing': 'Heavy woolens, jackets',
                'visiting_places': 'Rohtang Pass, Solang Valley, Hadimba Temple',
                'total_cost': '28000',
                'offer_cost': '23000',
                'facilities': 'Adventure sports, Skiing, Trekking',
                'year': '2024'
            },
            {
                'place_id': '5',
                'tourist_spot': 'Agra - Taj Mahal',
                'climate': 'Humid Subtropical',
                'max_temp': '45°C',
                'min_temp': '6°C',
                'avg_rain_fall': '650mm',
                'population': '1.7 Million',
                'languages': 'Hindi, Urdu, English',
                'best_time_to_visit': 'October to March',
                'clothing': 'Light cotton in summer, woolens in winter',
                'visiting_places': 'Taj Mahal, Agra Fort, Fatehpur Sikri',
                'total_cost': '15000',
                'offer_cost': '12000',
                'facilities': 'Heritage sites, Shopping, Mughlai cuisine',
                'year': '2024'
            },
            {
                'place_id': '6',
                'tourist_spot': 'Shimla - Queen of Hills',
                'climate': 'Subtropical Highland',
                'max_temp': '28°C',
                'min_temp': '0°C',
                'avg_rain_fall': '1575mm',
                'population': '170000',
                'languages': 'Hindi, Punjabi, English',
                'best_time_to_visit': 'March to June, December to January',
                'clothing': 'Woolens, jackets',
                'visiting_places': 'Mall Road, Jakhu Temple, Kufri',
                'total_cost': '24000',
                'offer_cost': '20000',
                'facilities': 'Toy train, Shopping, Ice skating',
                'year': '2024'
            },
            {
                'place_id': '7',
                'tourist_spot': 'Udaipur - City of Lakes',
                'climate': 'Semi-arid',
                'max_temp': '42°C',
                'min_temp': '11°C',
                'avg_rain_fall': '610mm',
                'population': '475000',
                'languages': 'Hindi, Rajasthani, English',
                'best_time_to_visit': 'September to March',
                'clothing': 'Light cotton, traditional Rajasthani wear',
                'visiting_places': 'Lake Pichola, City Palace, Jag Mandir',
                'total_cost': '26000',
                'offer_cost': '21000',
                'facilities': 'Lake cruises, Heritage hotels, Cultural shows',
                'year': '2024'
            },
            {
                'place_id': '8',
                'tourist_spot': 'Varanasi - Spiritual Capital',
                'climate': 'Humid Subtropical',
                'max_temp': '46°C',
                'min_temp': '5°C',
                'avg_rain_fall': '1110mm',
                'population': '1.2 Million',
                'languages': 'Hindi, Bhojpuri, English',
                'best_time_to_visit': 'October to March',
                'clothing': 'Light cotton, traditional wear',
                'visiting_places': 'Dashashwamedh Ghat, Kashi Vishwanath, Sarnath',
                'total_cost': '18000',
                'offer_cost': '15000',
                'facilities': 'Ganga Aarti, Boat rides, Spiritual tours',
                'year': '2024'
            },
        ]
        
        dummy_image = ContentFile(b'dummy image content', name='place_dummy.jpg')
        
        for place in places:
            PlaceInfo.objects.create(
                place_id=place['place_id'],
                tourist_spot=place['tourist_spot'],
                climate=place['climate'],
                max_temp=place['max_temp'],
                min_temp=place['min_temp'],
                avg_rain_fall=place['avg_rain_fall'],
                population=place['population'],
                languages=place['languages'],
                best_time_to_visit=place['best_time_to_visit'],
                clothing=place['clothing'],
                visiting_places=place['visiting_places'],
                total_cost=place['total_cost'],
                offer_cost=place['offer_cost'],
                facilities=place['facilities'],
                place_photo=dummy_image,
                year=place['year']
            )
        self.stdout.write(self.style.SUCCESS(f'Created {len(places)} tourist places'))
        
        # 5. Create Resorts
        self.stdout.write('Creating resorts...')
        resorts = [
            {
                'resort_name': 'Taj Exotica Goa',
                'city': 'Goa',
                'address': 'Calwaddo, Benaulim, South Goa',
                'contact': '9876501234',
                'activities': 'Water sports, Beach volleyball, Yoga',
                'facilities': 'Pool, Spa, Restaurant, Bar',
                'package_type': 'Beach Resort Package',
                'charges': '15000'
            },
            {
                'resort_name': 'Kumarakom Lake Resort',
                'city': 'Kerala',
                'address': 'Kumarakom, Kottayam District',
                'contact': '9876502234',
                'activities': 'Houseboat cruise, Ayurveda, Bird watching',
                'facilities': 'Pool, Ayurveda center, Restaurant',
                'package_type': 'Backwater Package',
                'charges': '18000'
            },
            {
                'resort_name': 'Rambagh Palace',
                'city': 'Jaipur',
                'address': 'Bhawani Singh Road, Jaipur',
                'contact': '9876503234',
                'activities': 'Heritage walk, Cultural shows, Camel rides',
                'facilities': 'Heritage rooms, Pool, Spa, Restaurant',
                'package_type': 'Heritage Package',
                'charges': '25000'
            },
            {
                'resort_name': 'The Oberoi Udaivilas',
                'city': 'Udaipur',
                'address': 'Haridasji Ki Magri, Udaipur',
                'contact': '9876504234',
                'activities': 'Lake cruise, Cultural shows, Shopping',
                'facilities': 'Lake view rooms, Pool, Spa, Fine dining',
                'package_type': 'Lake Palace Package',
                'charges': '30000'
            },
            {
                'resort_name': 'Manu Allaya Resort',
                'city': 'Manali',
                'address': 'Sunny Side, Chadiyari, Manali',
                'contact': '9876505234',
                'activities': 'Trekking, Skiing, Paragliding',
                'facilities': 'Mountain view, Restaurant, Bonfire',
                'package_type': 'Adventure Package',
                'charges': '12000'
            },
            {
                'resort_name': 'ITC Mughal',
                'city': 'Agra',
                'address': 'Taj Ganj, Agra',
                'contact': '9876506234',
                'activities': 'Heritage tours, Shopping, Cultural shows',
                'facilities': 'Pool, Spa, Multiple restaurants',
                'package_type': 'Heritage Tour Package',
                'charges': '10000'
            },
        ]
        
        for resort in resorts:
            ResortInfo.objects.create(
                resort_name=resort['resort_name'],
                city=resort['city'],
                address=resort['address'],
                contact=resort['contact'],
                activities=resort['activities'],
                facilities=resort['facilities'],
                package_type=resort['package_type'],
                charges=resort['charges'],
                photo=dummy_image
            )
        self.stdout.write(self.style.SUCCESS(f'Created {len(resorts)} resorts'))
        
        # 6. Create Vehicles
        self.stdout.write('Creating vehicles...')
        vehicles = [
            {'vehicle_id': '1', 'vehicle_name': 'Tempo Traveller 17 Seater', 'capacity': '17', 'rate_per_km': '25', 'hault_charge': '500', 'fuel_type': 'Diesel', 'condition': 'Excellent'},
            {'vehicle_id': '2', 'vehicle_name': 'Toyota Innova Crysta', 'capacity': '7', 'rate_per_km': '18', 'hault_charge': '400', 'fuel_type': 'Diesel', 'condition': 'Excellent'},
            {'vehicle_id': '3', 'vehicle_name': 'Maruti Ertiga', 'capacity': '7', 'rate_per_km': '14', 'hault_charge': '300', 'fuel_type': 'Petrol', 'condition': 'Good'},
            {'vehicle_id': '4', 'vehicle_name': 'Luxury Bus 45 Seater', 'capacity': '45', 'rate_per_km': '40', 'hault_charge': '1000', 'fuel_type': 'Diesel', 'condition': 'Excellent'},
            {'vehicle_id': '5', 'vehicle_name': 'Mahindra Scorpio', 'capacity': '8', 'rate_per_km': '16', 'hault_charge': '350', 'fuel_type': 'Diesel', 'condition': 'Good'},
            {'vehicle_id': '6', 'vehicle_name': 'Force Urbania', 'capacity': '13', 'rate_per_km': '22', 'hault_charge': '450', 'fuel_type': 'Diesel', 'condition': 'Excellent'},
        ]
        
        for vehicle in vehicles:
            VehicleInfo.objects.create(**vehicle)
        self.stdout.write(self.style.SUCCESS(f'Created {len(vehicles)} vehicles'))
        
        # 7. Create Routes
        self.stdout.write('Creating routes...')
        routes = [
            {'place_id': '1', 'transport_type': 'Flight + Taxi', 'from_place': 'Mumbai', 'destination': 'Goa', 'via': 'Direct', 'no_of_km': '450', 'remarks': 'Scenic coastal route'},
            {'place_id': '2', 'transport_type': 'Flight + Car', 'from_place': 'Bangalore', 'destination': 'Kerala', 'via': 'Kochi', 'no_of_km': '550', 'remarks': 'Beautiful backwater journey'},
            {'place_id': '3', 'transport_type': 'Train + Taxi', 'from_place': 'Delhi', 'destination': 'Jaipur', 'via': 'Direct', 'no_of_km': '280', 'remarks': 'Golden Triangle route'},
            {'place_id': '4', 'transport_type': 'Bus', 'from_place': 'Delhi', 'destination': 'Manali', 'via': 'Chandigarh', 'no_of_km': '540', 'remarks': 'Mountain highway'},
            {'place_id': '5', 'transport_type': 'Train', 'from_place': 'Delhi', 'destination': 'Agra', 'via': 'Direct', 'no_of_km': '230', 'remarks': 'Yamuna Expressway'},
            {'place_id': '6', 'transport_type': 'Toy Train + Taxi', 'from_place': 'Kalka', 'destination': 'Shimla', 'via': 'Direct', 'no_of_km': '96', 'remarks': 'UNESCO heritage toy train'},
            {'place_id': '7', 'transport_type': 'Flight + Car', 'from_place': 'Delhi', 'destination': 'Udaipur', 'via': 'Jaipur', 'no_of_km': '650', 'remarks': 'Rajasthan heritage route'},
            {'place_id': '8', 'transport_type': 'Train', 'from_place': 'Delhi', 'destination': 'Varanasi', 'via': 'Lucknow', 'no_of_km': '820', 'remarks': 'Spiritual journey'},
        ]
        
        for route in routes:
            RouteInfo.objects.create(**route)
        self.stdout.write(self.style.SUCCESS(f'Created {len(routes)} routes'))
        
        # 8. Create Bookings
        self.stdout.write('Creating bookings...')
        bookings = [
            {
                'customer_id': 'rajesh.kumar@gmail.com',
                'package_type': 'Beach Resort Package',
                'package_amount': '15000',
                'book_date': datetime.date(2024, 12, 20),
                'book_time': '10:30:00',
                'no_of_members': '4',
                'total': '60000',
                'status': 'Accepted',
                'pay_status': 'paid'
            },
            {
                'customer_id': 'priya.sharma@gmail.com',
                'package_type': 'Heritage Package',
                'package_amount': '25000',
                'book_date': datetime.date(2024, 12, 22),
                'book_time': '11:00:00',
                'no_of_members': '2',
                'total': '50000',
                'status': 'Accepted',
                'pay_status': 'paid'
            },
            {
                'customer_id': 'amit.patel@gmail.com',
                'package_type': 'Backwater Package',
                'package_amount': '18000',
                'book_date': datetime.date(2024, 12, 25),
                'book_time': '09:00:00',
                'no_of_members': '3',
                'total': '54000',
                'status': 'pending',
                'pay_status': None
            },
            {
                'customer_id': 'sneha.reddy@gmail.com',
                'package_type': 'Adventure Package',
                'package_amount': '12000',
                'book_date': datetime.date(2024, 12, 28),
                'book_time': '14:30:00',
                'no_of_members': '5',
                'total': '60000',
                'status': 'Accepted',
                'pay_status': 'paid'
            },
        ]
        
        for booking in bookings:
            BookInfo.objects.create(**booking)
        self.stdout.write(self.style.SUCCESS(f'Created {len(bookings)} bookings'))
        
        # 9. Create Payments
        self.stdout.write('Creating payments...')
        payments = [
            {
                'customer_id': 'rajesh.kumar@gmail.com',
                'amount': '60000',
                'advance_payment': '30000',
                'balance': '30000',
                'payment_mode': 'online',
                'payment_status': 'paid'
            },
            {
                'customer_id': 'priya.sharma@gmail.com',
                'amount': '50000',
                'advance_payment': '50000',
                'balance': '0',
                'payment_mode': 'online',
                'payment_status': 'paid'
            },
            {
                'customer_id': 'sneha.reddy@gmail.com',
                'amount': '60000',
                'advance_payment': '20000',
                'balance': '40000',
                'payment_mode': 'online',
                'payment_status': 'partial'
            },
        ]
        
        for payment in payments:
            PaymentInfo.objects.create(**payment)
        self.stdout.write(self.style.SUCCESS(f'Created {len(payments)} payment records'))
        
        # 10. Create Feedback
        self.stdout.write('Creating feedback...')
        feedbacks = [
            {
                'customer_id': 'rajesh.kumar@gmail.com',
                'about_service': 'Excellent',
                'about_facilities': 'Very Good',
                'comments': 'Amazing beach resort experience! Highly recommended.'
            },
            {
                'customer_id': 'priya.sharma@gmail.com',
                'about_service': 'Outstanding',
                'about_facilities': 'Excellent',
                'comments': 'The heritage hotel was magnificent. Great cultural experience.'
            },
            {
                'customer_id': 'sneha.reddy@gmail.com',
                'about_service': 'Good',
                'about_facilities': 'Good',
                'comments': 'Adventure activities were thrilling. Would visit again!'
            },
        ]
        
        for feedback in feedbacks:
            FeedBackInfo.objects.create(**feedback)
        self.stdout.write(self.style.SUCCESS(f'Created {len(feedbacks)} feedback entries'))
        
        self.stdout.write(self.style.SUCCESS('Database population completed successfully!'))
        self.stdout.write(self.style.SUCCESS('Login credentials:'))
        self.stdout.write('  Admin: admin@tourist.com / admin123')
        self.stdout.write('  Agency: agency@travel.com / agency123')
        self.stdout.write('  Users: user1@gmail.com / user123')
        self.stdout.write('         rajesh.kumar@gmail.com / rajesh123')
        self.stdout.write('         priya.sharma@gmail.com / priya123')
        self.stdout.write('         amit.patel@gmail.com / amit123')
        self.stdout.write('         sneha.reddy@gmail.com / sneha123')
        self.stdout.write('         vikram.singh@gmail.com / vikram123')
