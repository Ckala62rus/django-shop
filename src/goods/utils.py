from goods.models import Products


def q_search(query: str):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))