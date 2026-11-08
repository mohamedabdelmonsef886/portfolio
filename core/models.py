from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"

# --- الموديل الجديد للمشاريع ---
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True) # لحفظ الصور
    live_url = models.URLField(max_length=500, blank=True, null=True) # رابط المعاينة
    github_url = models.URLField(max_length=500, blank=True, null=True) # رابط الكود

    def __str__(self):
        return self.title