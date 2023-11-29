from .models import Category, Option


def categories(request):
    return {"categories": Category.objects.all()}
