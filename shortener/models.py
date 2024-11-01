from django.db import models

# Create your models here.
import random
import string
from django.db import models

class URL(models.Model):
    original_url = models.URLField(max_length=200)
    short_code = models.CharField(max_length=6, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code = self.generate_short_code()
        super().save(*args, **kwargs)

    def generate_short_code(self):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

    def __str__(self):
        return f'{self.original_url} -> {self.short_code}'
