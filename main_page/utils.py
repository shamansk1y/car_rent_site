import os
import uuid


def get_file_name(instance, filename):
    ext = filename.strip().split('.')[-1]
    new_file_name = f'{uuid.uuid4()}.{ext}'
    return os.path.join(instance.__class__.__name__.lower(), new_file_name)