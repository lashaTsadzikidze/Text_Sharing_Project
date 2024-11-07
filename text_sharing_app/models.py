from django.db import models
import hashlib

# Create your models here.
class SharedText(models.Model):
    content = models.TextField()
    slug = models.SlugField(max_length=64, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = hashlib.md5(self.content.encode()).hexdigest()[:10]
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Text shared on {self.created_at.strftime('%Y-%m-%d')}"