from django.urls import path
from recipe_data.views import home, recipe_new, recipe_list, recipe_update, recipe_delete

urlpatterns = [
    path('', home, name='home'),
    path('recipe_new', recipe_new, name='recipe_new'),
    path('recipe_list', recipe_list, name='recipe_list'),
    path('recipe_update/<int:id>/', recipe_update, name='recipe_update'),
    path('recipe_delete/<int:id>/', recipe_delete, name='recipe_delete'),
]