from django.db import models
from django.contrib.auth.models import User

class JournalEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Add these new fields:
    mood = models.CharField(
        max_length=20,
        choices=[
            ('happy', '😊 Happy'),
            ('sad', '😢 Sad'),
            ('angry', '😡 Angry'),
            ('anxious', '😟 Anxious'),
            ('neutral', '😐 Neutral')
        ],
        default='neutral'
    )
    image = models.ImageField(upload_to='journal_images/', null=True, blank=True)
    tags = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title
    
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return f"{self.name} ({self.rating})"