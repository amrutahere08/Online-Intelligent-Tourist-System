from django.core.management.base import BaseCommand
from touristapp.models import PlaceInfo, ResortInfo, Rating
import random

class Command(BaseCommand):
    help = 'Add sample ratings to places and resorts'

    def handle(self, *args, **kwargs):
        self.stdout.write('Adding sample ratings...')
        
        # Sample customer IDs
        customers = [
            'rajesh.kumar@gmail.com',
            'priya.sharma@gmail.com',
            'amit.patel@gmail.com',
            'sneha.reddy@gmail.com',
            'vikram.singh@gmail.com',
            'user1@gmail.com',
        ]
        
        # Sample reviews
        place_reviews = [
            'Amazing destination! Highly recommended.',
            'Beautiful place with great facilities.',
            'Had a wonderful time. Will visit again!',
            'Perfect for family vacation.',
            'Excellent experience overall.',
            'Great place for relaxation.',
            'Loved the scenic beauty!',
            'Good value for money.',
        ]
        
        resort_reviews = [
            'Excellent resort with amazing amenities!',
            'Staff was very friendly and helpful.',
            'Beautiful property with great food.',
            'Perfect location and comfortable rooms.',
            'Highly recommend this resort!',
            'Great experience, will come back.',
            'Wonderful stay with family.',
            'Value for money resort.',
        ]
        
        # Add ratings for places
        places = PlaceInfo.objects.all()
        for place in places:
            num_ratings = random.randint(5, 15)
            total_rating = 0
            
            for i in range(num_ratings):
                rating_value = random.randint(3, 5)  # 3-5 stars
                customer = random.choice(customers)
                review = random.choice(place_reviews)
                
                Rating.objects.create(
                    customer_id=customer,
                    item_type='place',
                    item_id=place.id,
                    rating=rating_value,
                    review=review
                )
                total_rating += rating_value
            
            # Update place average rating
            avg_rating = total_rating / num_ratings
            place.rating = round(avg_rating, 2)
            place.total_ratings = num_ratings
            place.save()
            
            self.stdout.write(f'Added {num_ratings} ratings for {place.tourist_spot} (avg: {avg_rating:.2f})')
        
        # Add ratings for resorts
        resorts = ResortInfo.objects.all()
        for resort in resorts:
            num_ratings = random.randint(5, 15)
            total_rating = 0
            
            for i in range(num_ratings):
                rating_value = random.randint(3, 5)  # 3-5 stars
                customer = random.choice(customers)
                review = random.choice(resort_reviews)
                
                Rating.objects.create(
                    customer_id=customer,
                    item_type='resort',
                    item_id=resort.id,
                    rating=rating_value,
                    review=review
                )
                total_rating += rating_value
            
            # Update resort average rating
            avg_rating = total_rating / num_ratings
            resort.rating = round(avg_rating, 2)
            resort.total_ratings = num_ratings
            resort.save()
            
            self.stdout.write(f'Added {num_ratings} ratings for {resort.resort_name} (avg: {avg_rating:.2f})')
        
        self.stdout.write(self.style.SUCCESS('Successfully added sample ratings!'))
