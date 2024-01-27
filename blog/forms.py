from django import forms
from . models import Comments
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields=['name','email','message']
        
    
    
    
    
    
#----------------------------------------------------
    # name=forms.CharField(max_length=200)
    # email:forms.EmailField(max_length=200, required=False)
    # message=forms.CharField(widget=forms.Textarea)
    # date=forms.DateTimeField()
    
    
    
        
        
    