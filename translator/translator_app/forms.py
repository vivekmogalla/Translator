from django import forms
from .models import Translation


class TranslationForm(forms.ModelForm):
    class Meta:
        model=Translation
        fields= ['source_language', 'destination_language', 'content_type', 'content']


class TextInputForm(forms.Form):
    input_text=forms.CharField(widget=forms.Textarea)


class YouTubeURLForm(forms.Form):
    youtube_url=forms.URLField()


class FileUploadForm(forms.Form):
    file = forms.FileField()