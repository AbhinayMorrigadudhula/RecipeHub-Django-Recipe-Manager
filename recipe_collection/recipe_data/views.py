from django.shortcuts import render, redirect
from django.http import HttpResponse
from recipe_data.models import Recipe
from recipe_data.forms import RecipeForm

# Create your views here.
def home(request):
    context = {
        'title' : 'HomePage',
    }
    return render(request, 'home.html', context)

def recipe_new(request):
    if request.method == 'POST':
        form= RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RecipeForm
        
    context = {
        'title' : 'AddRecipe',
        'form' : form,
    }
    return render(request, 'recipe_new.html', context)


def recipe_list(request):
    search = request.GET.get('search')
    recipes_data = Recipe.objects.all().order_by('-id')
    if search:
        recipes_data = Recipe.objects.filter(title__icontains=search)
    context = {
        'title' : 'RecipesList',
        'recipes_data' : recipes_data,
    }
    return render(request, 'recipe_list.html', context)


def recipe_update(request, id):
    try:
        recipe_data=Recipe.objects.get(id=id)
    except Recipe.DoesNotExist:
        return HttpResponse("Recipe Not Found")
    
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe_data)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm(instance=recipe_data)
    context = {
        'title' : 'RecipeUpdatePage',
        'form' : form,
        'recipe_data' : recipe_data,
    }
    return render(request, 'recipe_update.html', context)

def recipe_delete(request, id):
    recipe_data = Recipe.objects.get(id=id)
    recipe_data.delete()
    return redirect('recipe_list')



