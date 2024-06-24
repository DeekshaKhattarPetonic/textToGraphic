from PIL import Image
import io

def modify_image_properties(input_json, image_path):
    with Image.open(image_path) as img:
        # Get original image properties
        original_width, original_height = img.size
        original_dpi = img.info.get('dpi', (72, 72))[0]  # Default to 72 if DPI info is not available
        original_color_depth = img.mode

        # Print original specifications
        print("Original Image Specifications:")
        print(f"Aspect Ratio: {original_width}:{original_height}")
        print(f"DPI: {original_dpi}")
        print(f"Color Depth: {original_color_depth}")
        print(f"Resolution: {original_width}x{original_height}")

        # Modify image properties if needed
        aspect_ratio = original_width / original_height
        target_aspect_ratio = eval(input_json['image_aspect_ratio'].replace(':', '/'))
        target_width, target_height = map(int, input_json['image_resolution'].split('x'))
        
        if aspect_ratio != target_aspect_ratio or \
           original_dpi != int(input_json['image_dpi']) or \
           original_color_depth != input_json['image_color_depth'] or \
           (original_width, original_height) != (target_width, target_height):
            # Resize to specified resolution
            modified_img = img.resize((target_width, target_height))
            # Convert color depth
            modified_img = modified_img.convert(input_json['image_color_depth'])
            # Save modified image to bytes
            img_byte_arr = io.BytesIO()
            modified_img.save(img_byte_arr, format='JPEG', dpi=(int(input_json['image_dpi']), int(input_json['image_dpi'])))
            img_byte_arr.seek(0)
            
            # Print modified specifications
            print("\nModified Image Specifications:")
            print(f"Aspect Ratio: {input_json['image_aspect_ratio']}")
            print(f"DPI: {input_json['image_dpi']}")
            print(f"Color Depth: {input_json['image_color_depth']}")
            print(f"Resolution: {input_json['image_resolution']}")

            return img_byte_arr
        else:
            return None

if __name__ == "__main__":
    # Example usage
    input_json = {
        "image_aspect_ratio": "16:9",
        "image_dpi": "300",
        "image_color_depth": "RGB",
        "image_resolution": "1920x1080"
    }
    image_path = 'path/to/your/image.jpg'
    modified_image_path = modify_image_properties(input_json, image_path)

    if modified_image_path:
        print(f"\nModified image saved as {modified_image_path}")
