import os

# Directory containing templates
template_dir = r'd:\resumeprojects\TouristSystem\tourist_db\templates'

# CSS to add to remove empty space
css_fix = """
<style>
/* Remove empty space at top */
body { margin: 0 !important; padding: 0 !important; }
.header { margin: 0 !important; padding: 10px 0 !important; }
.banner, .banner1 { margin: 0 !important; padding: 0 !important; min-height: 0 !important; }
.hero-section { margin-top: 0 !important; padding-top: 60px !important; }
.navbar { margin: 0 !important; }
.coaching_section, .container { padding-top: 20px !important; }
.w3_agile_team_grid { margin-top: 0 !important; padding-top: 0 !important; }
</style>
"""

# List of main template files
files_to_process = [
    'index1.html', 'user_home.html', 'admin_home.html', 'agency_home.html',
    'placeinfo_view_c.html', 'placeinfo_view2_c.html', 'placeinfo_view.html',
    'resortinfo_view_c.html', 'resortinfo_view.html',
    'vehicleinfo_view_c.html', 'vehicleinfo_view.html',
    'bookinfo_view.html', 'bookinfo_view_u.html',
    'customerinfo_view.html', 'feedbackinfo_view.html',
    'paymentinfo_view.html', 'routeinfo_view.html'
]

count = 0
for filename in files_to_process:
    filepath = os.path.join(template_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if CSS fix already exists
        if '/* Remove empty space at top */' not in content:
            # Add CSS before </head>
            new_content = content.replace('</head>', css_fix + '\n</head>')
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1
            print(f"✓ Updated {filename}")
        else:
            print(f"- Skipped {filename} (already has fix)")
    else:
        print(f"✗ File not found: {filename}")

print(f"\nTotal files updated: {count}")
