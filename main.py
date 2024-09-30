import json

# JSON metadata with image resolution and elements
metadata = {
    "image_metadata": {
        "resolution": {
            "width": 640,
            "height": 942
        },
        "elements": [
            {
                "item": "PCF Sparkletots @ Bishan East-Sin Ming Blk 409",
                "description": "Childcare center labeled in the top-left part of the image.",
                "position": {
                    "x": 0.1,
                    "y": 0.15
                }
            },
            {
                "item": "Hall of Great Compassion 大悲殿",
                "description": "A hall located near the upper right side of the image.",
                "position": {
                    "x": 0.75,
                    "y": 0.2
                }
            },
            {
                "item": "Kong Meng San Phor Kark See Monastery",
                "description": "A large monastery labeled toward the center-left of the image.",
                "position": {
                    "x": 0.35,
                    "y": 0.5
                }
            },
            {
                "item": "Buddhist College of Singapore 新加坡佛学院",
                "description": "A college located in the middle-left section of the image.",
                "position": {
                    "x": 0.32,
                    "y": 0.6
                }
            },
            {
                "item": "The Sacred Bodhi Tree 菩提树",
                "description": "Located slightly to the right of the middle of the image.",
                "position": {
                    "x": 0.65,
                    "y": 0.55
                }
            },
            {
                "item": "Prajna Meditation Hall 禅堂",
                "description": "Meditation hall located at the bottom right.",
                "position": {
                    "x": 0.8,
                    "y": 0.75
                }
            },
            {
                "item": "Domus Integration Pte",
                "description": "A business located in the lower-left corner of the image.",
                "position": {
                    "x": 0.1,
                    "y": 0.85
                }
            },
            {
                "item": "Comfort Transportation Pte",
                "description": "Transportation company located at the bottom right part of the image.",
                "position": {
                    "x": 0.85,
                    "y": 0.9
                }
            }
        ]
    }
}

# Image size
image_width = metadata['image_metadata']['resolution']['width']
image_height = metadata['image_metadata']['resolution']['height']

# Create HTML content
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Overlay</title>
    <style>
        body {{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f0f0f0;
        }}
        .image-container {{
            position: relative;
            width: {image_width}px;
            height: {image_height}px;
        }}
        .image-container img {{
            width: 100%;
            height: auto;
        }}
        .overlay {{
            position: absolute;
            color: white;
            font-size: 14px;
            background-color: rgba(0, 0, 0, 0.5);
            padding: 5px;
            border-radius: 5px;
        }}
    </style>
</head>
<body>
    <div class="image-container">
        <img src="image.png" alt="Map Image">
"""

# Add overlays
for element in metadata['image_metadata']['elements']:
    x = element['position']['x'] * image_width
    y = element['position']['y'] * image_height
    html_content += f"""
        <div class="overlay" style="left: {x}px; top: {y}px;">
            <strong>{element['item']}</strong><br>{element['description']}
        </div>
    """

# Close HTML tags
html_content += """
    </div>
</body>
</html>
"""

# Save HTML to file
with open('image.html', 'w') as file:
    file.write(html_content)

print("HTML file generated successfully.")
