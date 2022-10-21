from django import forms
from .models import Comments, Post, Profile

class PostForm(forms.ModelForm):
    
    description = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "row":"2",
                "placeholder": "How was your day?",
                "class": "form-control",
                "style": "resize:none",
                "size":4
                
            })
    )
    
    photo = forms.ImageField(
        label="",
        required=False, 
                   
    )
    
    class Meta:
        model = Post     
        fields = ["description", "photo"]

class CommForm(forms.ModelForm):
    
    comm_text = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Post a comment",
                "class": "form-control",
                "style": "resize:none",
                "size":4
                
            })
    )
    class Meta:
        model = Comments     
        fields = ["comm_text"]
        

class BioUpdateForm(forms.ModelForm):
    
    bio = forms.CharField(
        max_length=100,
        label="",
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Update your bio",
                "class": "form-control",
                "style": "resize:none",
                "size":10
                
            })
    )
    
    
    class Meta:
        model = Profile     
        fields = ["bio"]
        
        
class PhotoUpdateForm(forms.ModelForm):       
       
    profileimg = forms.ImageField(
        label="",
        required=False, 
        )
    
    class Meta:
        model = Profile     
        fields = ["profileimg"]
        
