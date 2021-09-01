from django.shortcuts import render

# Create your views here.
#Контроллер-функция
def index(request):
    return render(request,'index.html')

def products(request):
    return render(request, 'products.html')


def test(request):
    context = {
        'title': 'geekshop',
        'user': 'Ivanov',
        'description': 'Добро пожаловать в Geekshop!',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals','price': '6 090,00' },
            {'name': 'Синяя куртка The North Face', 'price': '23 725,00'},
            {'name': 'Черный рюкзак Nike Heritage', 'price': '2 340,00'},
    ],
    'promotion': True,
    'products_of_promotion': [
        #{'name': 'Синяя куртка The North Face', 'price': '23 725,00'},
        #{'name': 'Худи черного цвета с монограммами adidas Originals', 'price': '6 090,00'},
        ]
    }

    return render(request, 'test.html', context)