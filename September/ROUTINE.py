from PIL import Image, ImageDraw, ImageFont

# Define the routine table
table_content = [
    ["Time", "Activity", "Notes"],
    ["6:00 AM - 7:00 AM", "Wake up, freshen up, breakfast", ""],
    ["7:00 AM - 8:00 AM", "DSA practice", "Problem-solving, practice problems"],
    ["8:00 AM - 1:00 PM", "Attend classes", "Morning classes"],
    ["1:00 PM - 2:00 PM", "Lunch and break", "Relax and recharge"],
    ["2:00 PM - 3:00 PM", "Review morning classes", "Consolidate what you learned"],
    ["3:00 PM - 6:00 PM", "Attend afternoon classes", "Afternoon classes"],
    ["6:00 PM - 7:00 PM", "Dinner", "Healthy meal"],
    ["7:00 PM - 9:00 PM", "Machine learning studies", "Tutorials, reading, small projects"],
    ["9:00 PM - 10:00 PM", "Relaxation", "Unwind, hobbies"],
    ["Saturdays", "", ""],
    ["9:00 AM - 11:00 AM", "DSA deep dive", "Challenging problems, advanced topics"],
    ["11:00 AM - 1:00 PM", "Coding project or contests", "Apply DSA skills, participate in contests"],
    ["1:00 PM - 2:00 PM", "Lunch and break", "Recharge"],
    ["2:00 PM - 4:00 PM", "Machine learning studies", "Continue learning, project work"],
    ["4:00 PM - 6:00 PM", "Review and planning", "Reflect on the week, plan ahead"],
    ["Sundays", "", ""],
    ["9:00 AM - 11:00 AM", "Physical activity or exercise", "Stay active"],
    ["11:00 AM - 1:00 PM", "Personal development", "Learning new skills, reading"],
    ["1:00 PM - 2:00 PM", "Lunch and break", "Recharge"],
    ["2:00 PM - 6:00 PM", "Academic review and preparation", "Study, assignments, upcoming classes"],
    ["6:00 PM onwards", "Relaxation and leisure activities", "Enjoy your evening"]
    ]

# Create a new image
image_width = 1200
image_height = 1000
background_color = (255, 255, 255)
image = Image.new("RGB", (image_width, image_height), background_color)
draw = ImageDraw.Draw(image)

# Set font size and load a font
font_size = 24
font = ImageFont.truetype("arial.ttf", font_size)

# Position variables
x_pos = 50
y_pos = 80
line_height = font_size + 15

# Draw the heading
heading = "ROUTINE"
heading_width, heading_height = draw.textsize(heading, font=font)
heading_x = (image_width - heading_width) // 2
draw.text((heading_x, y_pos), heading, fill=(0, 0, 0), font=font)
y_pos += heading_height + 20

# Draw the table
for row in table_content:
    for cell in row:
        draw.text((x_pos, y_pos), cell, fill=(0, 0, 0), font=font)
        x_pos += 400  # Adjust this value to align columns
    y_pos += line_height
    x_pos = 50

# Save the image
image.save("routine_image_beautiful.png")

print("Beautiful routine image created successfully.")
