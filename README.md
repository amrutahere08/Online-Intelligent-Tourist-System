# 🌍 Online Intelligent Tourist System

A comprehensive Django-based web application for managing tourist destinations, resort bookings, vehicle rentals, and travel packages across India. The system provides an intelligent platform for tourists, travel agencies, and administrators to streamline the entire travel planning and booking process.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Django](https://img.shields.io/badge/Django-4.2.27-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

### 🎯 Core Functionality
- **Multi-User System**: Role-based access for Admin, Agency, and Users
- **Tourist Destination Management**: Comprehensive information about Indian tourist spots
- **Resort Booking System**: Browse and book luxury accommodations
- **Vehicle Management**: Fleet management with various vehicle types
- **Route Planning**: Detailed route information with distance and transport options
- **Secure Payment Processing**: Track bookings, payments, and balances
- **Customer Feedback**: Rating and review system for places and resorts
- **Google Maps Integration**: Visual location display and geocoding

### 🆕 Enhanced Features
- ⭐ **Rating System**: 5-star ratings for destinations and resorts
- 🔍 **Advanced Search**: Filter by price, location, and rating
- 📊 **Analytics Dashboard**: Booking statistics and revenue tracking
- 📱 **Responsive Design**: Mobile-friendly interface
- 🖼️ **Image Management**: Automatic image sizing and optimization

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/TouristSystem.git
cd TouristSystem/tourist_db
```

2. **Create and activate virtual environment** (Optional but recommended)
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac
```

3. **Install dependencies**
```bash
pip install django==4.2.27
pip install geopy
pip install pillow
```

4. **Run database migrations**
```bash
python manage.py migrate
```

5. **Populate sample data** (Optional)
```bash
python manage.py populate_db
python manage.py add_ratings
python manage.py add_images
```

6. **Start the development server**
```bash
python manage.py runserver
```

7. **Access the application**
- Main Site: http://127.0.0.1:8000/
- Admin Panel: http://127.0.0.1:8000/admin/

## 👥 User Accounts

### Default Login Credentials

**Admin Account:**
- Email: `admin@tourist.com`
- Password: `admin123`

**Agency Account:**
- Email: `agency@travel.com`
- Password: `agency123`

**User Accounts:**
- `rajesh.kumar@gmail.com` / `rajesh123`
- `priya.sharma@gmail.com` / `priya123`
- `amit.patel@gmail.com` / `amit123`
- `sneha.reddy@gmail.com` / `sneha123`
- `vikram.singh@gmail.com` / `vikram123`

## 📂 Project Structure

```
TouristSystem/
├── tourist_db/                 # Main Django project
│   ├── tourist_db/            # Project settings
│   │   ├── settings.py        # Configuration
│   │   ├── urls.py            # URL routing
│   │   └── wsgi.py            # WSGI config
│   ├── touristapp/            # Main application
│   │   ├── models.py          # Database models
│   │   ├── views.py           # View controllers
│   │   ├── admin.py           # Admin configuration
│   │   └── management/        # Custom commands
│   ├── templates/             # HTML templates (50+ files)
│   ├── static/                # CSS, JS, images
│   │   └── css/               # Stylesheets
│   ├── media/                 # User uploads
│   ├── db.sqlite3             # Database file
│   └── manage.py              # Django CLI
└── README.md                  # This file
```

## 🗄️ Database Models

- **UserLogin**: Authentication and user types
- **UserRegistration**: User profile information
- **CustomerInfo**: Customer details with Aadhar verification
- **PlaceInfo**: Tourist destination details with ratings
- **ResortInfo**: Resort information with ratings
- **VehicleInfo**: Vehicle fleet management
- **RouteInfo**: Route planning and information
- **BookInfo**: Booking management
- **PaymentInfo**: Payment tracking
- **FeedBackInfo**: Customer feedback
- **Rating**: User ratings and reviews

## 🎨 Key Features Breakdown

### For Users
- Browse tourist destinations and resorts
- Search and filter by price, location, rating
- Make bookings and process payments
- Submit ratings and reviews
- View booking history
- Manage profile

### For Agencies
- Add and manage resorts
- View bookings and customer information
- Manage packages
- View payments and feedback

### For Admins
- Full system control
- Manage all destinations, resorts, and vehicles
- Approve/reject bookings
- View analytics dashboard
- Generate reports
- Manage customer information

## 📊 Sample Data

The system includes comprehensive sample data:
- **8 Tourist Destinations**: Goa, Kerala, Jaipur, Manali, Agra, Shimla, Udaipur, Varanasi
- **6 Premium Resorts**: Taj Exotica, Kumarakom Lake Resort, Rambagh Palace, etc.
- **6 Vehicle Types**: Tempo Traveller, Innova, Ertiga, Luxury Bus, etc.
- **8 Routes**: Major routes connecting Indian cities
- **80+ Ratings**: Sample ratings and reviews

## 🛠️ Technology Stack

**Backend:**
- Django 4.2.27
- Python 3.8+
- SQLite3

**Frontend:**
- HTML5
- CSS3 (Bootstrap)
- JavaScript
- Font Awesome Icons

**Additional Libraries:**
- geopy (Geographic services)
- Pillow (Image processing)
- smtplib (Email notifications)

## 🔒 Security Features

- Password hashing
- Session management
- CSRF protection
- SQL injection prevention (Django ORM)
- File upload validation

## 📱 Responsive Design

The application is fully responsive and works seamlessly on:
- Desktop computers
- Tablets
- Mobile devices

## 🚧 Future Enhancements

### Planned Features
- Payment gateway integration (Razorpay/PayU)
- Email notifications for bookings
- SMS integration for OTP
- Multi-language support (Hindi, regional languages)
- Weather API integration
- Social media sharing
- AI-powered recommendations
- Virtual tours (360°)

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/yourusername/TouristSystem/issues).

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Support

For support, email your.email@example.com or create an issue in the repository.

## 🙏 Acknowledgments

- Django Documentation
- Bootstrap Framework
- Font Awesome Icons
- Unsplash for sample images
- All contributors and testers

---

**⭐ If you find this project useful, please consider giving it a star!**

Made with ❤️ using Django
