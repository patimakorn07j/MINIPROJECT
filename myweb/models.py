from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()  # ฟิลด์สำหรับเก็บเนื้อหาคอมเมนต์
    created_at = models.DateTimeField(auto_now_add=True)  # เวลาที่สร้างคอมเมนต์
    food = models.TextField(default="")

    def __str__(self):
        return f'Comment by {self.user.username} on {self.created_at}'