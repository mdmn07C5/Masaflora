from .models import Category, Option


def categories(request):
    return {"categories": Category.objects.all()}


def options(request):
    return {"options": Option.objects.all()}
