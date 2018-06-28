from django.db import models

# Create your models here.

class blogFiles(models.Model):
    id = models.AutoField(primary_key=True)
    images=models.FileField(upload_to="images")
    image_desc=models.CharField(max_length=100)
    uploaded_date=models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "blog_files"