from PIL import Image
from django.core.exceptions import ValidationError

def validate_image(image):
    # 1) Haqiqiy rasm ekanini tekshiramiz
    try:
        img = Image.open(image)
        img.verify()
    except Exception:
        raise ValidationError("Image file is invalid!")

    # 2) Rasm hajmini tekshiramiz
    max_size_mb = 50
    max_size = max_size_mb * 1024 * 1024 

    if image.size > max_size:
        raise ValidationError(f"Image size must not exceed {max_size_mb} MB!")
