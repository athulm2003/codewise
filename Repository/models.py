from django.db import models

# Create your models here.
"""
Schema : QuestionDb
Fields : title,language,difficulty_level,sample_input,sample_output,topic,published_date,is_active

"""
class QuestionDb(models.Model):
    title=models.CharField(max_length=100)

    LANGUAGE_CHOICES=(
        ("python","Python"),
        ("java","Java"),
        ("javascript","JavaScript")
    )

    language=models.CharField(max_length=100,choices=LANGUAGE_CHOICES,default="python")

    DIFFICULTY_CHOICES=(
        ("easy","Easy"),
        ("medium","Medium"),
        ("hard","Hard")
    )

    difficulty_level=models.CharField(max_length=100,choices=DIFFICULTY_CHOICES,default="easy",null=True)
    sample_input=models.TextField(null=True)
    sample_output=models.TextField(null=True)
    notes=models.TextField(null=True)
    topic=models.CharField(max_length=200,null=True)
    published_date=models.DateTimeField(auto_now_add=True,null=True)
    is_active=models.BooleanField(default=True,null=True)