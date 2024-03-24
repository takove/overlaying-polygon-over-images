import cv2
import numpy as np

def draw_polygon(image, polygon, color=(255, 0, 0), thickness=2):
    cv2.polylines(image, [polygon], True, color, thickness)

def draw_filled_polygon_with_holes(image, outer_polygon, inner_polygons, color=(255, 0, 0), hole_color=(0, 0, 0)):
    # Draw the outer polygon
    cv2.fillPoly(image, [outer_polygon], color)

    # Draw the inner polygons (holes)
    for inner_polygon in inner_polygons:
        cv2.fillPoly(image, [inner_polygon], hole_color)

def overlay_image(image, overlay, alpha=0.5):
    return cv2.addWeighted(image, 1 - alpha, overlay, alpha, 0)

# Load the map image
map_image = cv2.imread('map.png')

# Create a mask image of the same size
mask = np.zeros_like(map_image)

# Define the outer polygon and inner polygons (holes)
outer_polygon = np.array([(100, 100), (200, 100), (200, 200), (100, 200)], dtype=np.int32)
inner_polygons = [
    np.array([(120, 120), (180, 120), (180, 180), (120, 180)], dtype=np.int32),
    # Add more inner polygons here if needed
]

# Draw the polygon with holes onto the mask
draw_filled_polygon_with_holes(mask, outer_polygon, inner_polygons)

# Overlay the mask onto the map image
result = overlay_image(map_image, mask)

# Save the result
cv2.imwrite('result.png', result)