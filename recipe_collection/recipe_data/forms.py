from django import forms
from recipe_data.models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        labels = {
            'title' : 'Title of Recipe',
            'ingredients' : 'Ingredients Used',
            'preparation_time' : 'Preparation Time',
            'instructions' : 'Description About Recipe',
        }
        
        widgets = {
            'title' : forms.TextInput(attrs={
                'type' : 'text',
                'placeholder' : 'Enter Recipe name',
            }),
            'ingredients' : forms.TextInput(attrs={
                'type' : 'text',
                'placeholder' : 'Enter ingredients',
            }),
        }
        
        
        