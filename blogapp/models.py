from django.db import models
from django.core.exceptions import ValidationError
from django_ckeditor_5.fields import CKEditor5Field

def validate_word_count(value):
    words = value.split()
    if len(words) > 20:
        raise ValidationError('Maximum 20 words allowed.')

class BlogPost(models.Model):
    CATEGORY_CHOICES = [
        ('IT & Startups', 'IT & Startups'),
        ('Finance', 'Finance')
    ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=200)
    content = CKEditor5Field()
    short_description = models.TextField(validators=[validate_word_count])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
