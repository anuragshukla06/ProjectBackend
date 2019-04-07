import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage

class PointFileStorage(FileSystemStorage):

    # This method is actually defined in Storage
    def get_available_name(self, name):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name # simply returns the name passed