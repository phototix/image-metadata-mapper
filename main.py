from PIL import Image

# JSON metadata with position values (example)
json_data = {
    "image_metadata": {
        "elements": [
            {
                "item": "Woman",
                "description": "Dressed in a light pink dress with a lace neckline, sitting on a brown cushioned bench.",
                "position": {
                    "x": 0.4,
                    "y": 0.5
                }
            },
            {
                "item": "Pink Dress",
                "description": "Sleeveless with thin straps and a light texture, decorated with small details.",
                "position": {
                    "x": 0.4,
                    "y": 0.6
                }
            },
            {
                "item": "Necklace",
                "description": "A small pendant necklace worn by the woman.",
                "position": {
                    "x": 0.4,
                    "y": 0.4
                }
            },
            {
                "item": "Cushioned Bench",
                "description": "Brown, leather or leather-like seating with vertical stitching, typical of a café or restaurant booth.",
                "position": {
                    "x": 0.3,
                    "y": 0.5
                }
            },
            {
                "item": "Wooden Tables",
                "description": "Simple, small café tables visible in the background.",
                "position": {
                    "x": 0.7,
                    "y": 0.4
                }
            },
            {
                "item": "Pendant Lights",
                "description": "Multiple warm-colored hanging lights with exposed bulbs, creating an ambient feel.",
                "position": {
                    "x": 0.7,
                    "y": 0.2
                }
            },
            {
                "item": "Pillows",
                "description": "A beige cushion placed on the bench beside the woman.",
                "position": {
                    "x": 0.3,
                    "y": 0.6
                }
            },
            {
                "item": "Green Plant",
                "description": "A leafy potted plant is placed to the side of the seating.",
                "position": {
                    "x": 0.9,
                    "y": 0.7
                }
            },
            {
                "item": "Windows",
                "description": "Large windows in the background with a view of the outdoors, showing greenery and parked cars.",
                "position": {
                    "x": 0.8,
                    "y": 0.3
                }
            },
            {
                "item": "Wooden Interior",
                "description": "The café or restaurant features wooden walls and counters, enhancing the cozy atmosphere.",
                "position": {
                    "x": 0.1,
                    "y": 0.1
                }
            }
        ]
    }
}

# Load image to get dimensions
image_path = "image.jpeg"
img = Image.open(image_path)
width, height = img.size

# Start generating the HTML content
html_content = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Overlay</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
        }}
        .image-container {{
            position: relative;
            width: {width}px;
            height: {height}px;
            background-image: url("{image_path}");
            background-size: cover;
        }}
        .overlay-item {{
            position: absolute;
            color: white;
            background-color: rgba(0, 0, 0, 0.5);
            padding: 5px;
            border-radius: 5px;
            font-size: 12px;
        }}
    </style>
</head>
<body>
    <div class="image-container">
'''

# Loop through JSON elements and add to HTML
for element in json_data['image_metadata']['elements']:
    item_name = element['item']
    description = element['description']
    pos_x = element['position']['x']
    pos_y = element['position']['y']

    # Calculate pixel positions
    pixel_x = int(pos_x * width)
    pixel_y = int(pos_y * height)

    # Add overlay div for each item
    html_content += f'''
        <div class="overlay-item" style="left: {pixel_x}px; top: {pixel_y}px;">
            <strong>{item_name}</strong><br>{description}
        </div>
    '''

# Close the container div
html_content += '''
    </div>
</body>
</html>
'''

# Save the HTML file
html_file_path = "image.html"
with open(html_file_path, "w", encoding="utf-8") as html_file:
    html_file.write(html_content)

html_file_path
