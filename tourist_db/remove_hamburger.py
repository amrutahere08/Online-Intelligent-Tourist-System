import os
import re

# Directory containing templates
template_dir = r'd:\resumeprojects\TouristSystem\tourist_db\templates'

# Pattern to match the hamburger menu button
pattern = r'<button type="button" class="navbar-toggle collapsed"[^>]*>.*?</button>\s*'

# List of files to process
files_to_process = [
    'agency_home.html', 'bookinfo.html', 'bookinfo_view.html', 'bookinfo_view_u.html',
    'customerinfo.html', 'feedbackinfo.html', 'customerinfo_view.html', 'feedbackinfo_view.html',
    'login.html', 'otp.html', 'payment2.html', 'paymentinfo.html', 'paymentinfo_view.html',
    'placeinfo.html', 'placeinfo_edit.html', 'placeinfo_view_c.html', 'place_wise_year_view.html',
    'place_wise_year.html', 'placeinfo_view2_c.html', 'placeinfo_view.html', 'print.html',
    'resortinfo_view_c.html', 'resortinfo_view.html', 'resort_info.html', 'routeinfo.html',
    'resort_update.html', 'routeinfo_view2.html', 'routeinfo_view.html',
    'vehicleinfo.html', 'vehicleinfo_view_c.html', 'vehicleinfo_view.html', 'vehicleinfo_edit.html'
]

count = 0
for filename in files_to_process:
    filepath = os.path.join(template_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove hamburger menu button
        new_content = re.sub(pattern, '', content, flags=re.DOTALL)
        
        # Also replace "collapse navbar-collapse" with just "navbar-collapse"
        new_content = new_content.replace('class="collapse navbar-collapse"', 'class="navbar-collapse"')
        
        if content != new_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1
            print(f"✓ Updated {filename}")
        else:
            print(f"- Skipped {filename} (no changes needed)")
    else:
        print(f"✗ File not found: {filename}")

print(f"\nTotal files updated: {count}")
