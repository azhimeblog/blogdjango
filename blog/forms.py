from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django import forms
from .models import Post

# Apply summernote to specific fields.
class SomeForm(forms.Form):
    foo = forms.CharField(widget=SummernoteWidget())  # instead of forms.Textarea

class Createcontent(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title','content','slug','content_images','status',)
        file = forms.FileField()
        widgets = {
            'content': SummernoteWidget(),
        }
