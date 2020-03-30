from django import forms
from . import models

# not used
class CustomArticleForm(forms.ModelForm):
    body = forms.CharField(strip=False, widget=forms.Textarea)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['body'].strip = False

    class Meta:
        model = models.Article
        fields = ('title', 'body',)

class CustomCommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = models.Comment
        fields = ('text',)