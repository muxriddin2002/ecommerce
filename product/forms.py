from django.forms import ModelForm, TextInput,Textarea,Select
from .models import Comment

class Product_CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['review','rating','user','product']

        widgets = {
            'review': Textarea(attrs={
                'name': "comment",
                'cols': "45",
                'rows': "8",
                'aria - required': "true",
            }),

            'rating': Select(attrs={
                'class': 'star-rating',
            })
        }