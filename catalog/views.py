from django.shortcuts import render

from catalog.models import Product


def home(request):
    # Выборка последних 5 созданных продуктов
    latest_products = Product.objects.order_by("created_at")[:5]

    # Вывод данных в консоль сервера
    print("Последние 5 созданных продуктов:")
    for product in latest_products:
        print(f"- {product.name} (создан: {product.created_at})")

    return render(request, "home.html")


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"You have new message from {name}({phone}): {message}")
    return render(request, "contacts.html")
