from catalog.models import Category


def categories(requets):
    return {
        'categories': Category.objects.all()
    }
