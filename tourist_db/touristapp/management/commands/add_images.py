from django.core.management.base import BaseCommand
from touristapp.models import PlaceInfo, ResortInfo
from django.core.files.base import ContentFile
import urllib.request
import os

class Command(BaseCommand):
    help = 'Download and add images to places and resorts'

    def handle(self, *args, **kwargs):
        self.stdout.write('Downloading images for places and resorts...')
        
        # Image URLs for tourist places
        place_images = {
            'Goa Beaches': 'https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?w=800',  # Goa beach
            'Kerala Backwaters': 'https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?w=800',  # Kerala houseboat
            'Jaipur - Pink City': 'https://images.unsplash.com/photo-1599661046289-e31897846e41?w=800',  # Hawa Mahal
            'Manali - Hill Station': 'https://images.unsplash.com/photo-1626621341517-bbf3d9990a23?w=800',  # Manali mountains
            'Agra - Taj Mahal': 'https://images.unsplash.com/photo-1564507592333-c60657eea523?w=800',  # Taj Mahal
            'Shimla - Queen of Hills': 'https://images.unsplash.com/photo-1605649487212-47bdab064df7?w=800',  # Shimla
            'Udaipur - City of Lakes': 'https://images.unsplash.com/photo-1609920658906-8223bd289001?w=800',  # Udaipur palace
            'Varanasi - Spiritual Capital': 'https://images.unsplash.com/photo-1561361513-2d000a50f0dc?w=800',  # Varanasi ghat
        }
        
        # Image URLs for resorts
        resort_images = {
            'Taj Exotica Goa': 'https://images.unsplash.com/photo-1571896349842-33c89424de2d?w=800',  # Beach resort
            'Kumarakom Lake Resort': 'https://images.unsplash.com/photo-1566073771259-6a8506099945?w=800',  # Lake resort
            'Rambagh Palace': 'https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?w=800',  # Heritage palace
            'The Oberoi Udaivilas': 'https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?w=800',  # Luxury hotel
            'Manu Allaya Resort': 'https://images.unsplash.com/photo-1551882547-ff40c63fe5fa?w=800',  # Mountain resort
            'ITC Mughal': 'https://images.unsplash.com/photo-1455587734955-081b22074882?w=800',  # Heritage hotel
        }
        
        # Download and update place images
        for place in PlaceInfo.objects.all():
            place_name = place.tourist_spot
            if place_name in place_images:
                try:
                    url = place_images[place_name]
                    self.stdout.write(f'Downloading image for {place_name}...')
                    
                    # Download image
                    response = urllib.request.urlopen(url)
                    image_data = response.read()
                    
                    # Save to model
                    filename = f'{place_name.lower().replace(" ", "_").replace("-", "")}.jpg'
                    place.place_photo.save(filename, ContentFile(image_data), save=True)
                    
                    self.stdout.write(self.style.SUCCESS(f'✓ Added image for {place_name}'))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'✗ Failed to download image for {place_name}: {str(e)}'))
        
        # Download and update resort images
        for resort in ResortInfo.objects.all():
            resort_name = resort.resort_name
            if resort_name in resort_images:
                try:
                    url = resort_images[resort_name]
                    self.stdout.write(f'Downloading image for {resort_name}...')
                    
                    # Download image
                    response = urllib.request.urlopen(url)
                    image_data = response.read()
                    
                    # Save to model
                    filename = f'{resort_name.lower().replace(" ", "_")}.jpg'
                    resort.photo.save(filename, ContentFile(image_data), save=True)
                    
                    self.stdout.write(self.style.SUCCESS(f'✓ Added image for {resort_name}'))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'✗ Failed to download image for {resort_name}: {str(e)}'))
        
        self.stdout.write(self.style.SUCCESS('Image download completed!'))
