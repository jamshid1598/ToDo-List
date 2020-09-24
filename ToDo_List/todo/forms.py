from django import forms

from .models import ToDo_List

class ToDo_List_Form(forms.ModelForm):
    item=forms.CharField(
        max_length=250, 
        required=False,
        label='',
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control mr-sm-2',
                'placeholder' : 'Add Item',
            }
        )    
    )
    class Meta:
        model=ToDo_List
        fields=[
            'item',
            'complated',
        ]