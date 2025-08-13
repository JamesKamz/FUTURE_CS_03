from django.db import models
import uuid
# Create your models here.


class EncryptedFile(models.Model):
    uid=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    filename=models.CharField(max_length=255)
    file=models.FileField(upload_to='encrypted_files/')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.filename
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('download_file', args=[str(self.uid)])
    
    