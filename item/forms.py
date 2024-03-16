from django import forms
from .models import Item

INPUT_CLASS = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image',)
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASS 
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Name of the item'
            }),

            'description': forms.Textarea(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Description of the item'
            }),
            
            'price': forms.NumberInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Price of the item'
            }),

            'image': forms.FileInput(attrs={
                'class': INPUT_CLASS,
            })
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image','is_sold')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Name of the item'
            }),

            'description': forms.Textarea(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Description of the item'
            }),
            
            'price': forms.NumberInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Price of the item'
            }),

            'image': forms.FileInput(attrs={
                'class': INPUT_CLASS,
            })
        }