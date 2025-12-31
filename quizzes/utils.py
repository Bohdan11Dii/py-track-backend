from django.utils.text import slugify

def test_upload_path(instance, filename):
    return f"tests/imports/{slugify(instance.title)}/{filename}"
