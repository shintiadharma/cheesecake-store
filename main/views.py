from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Strawberry Cheesecake',
        'size': '30x20',
        'price': 'Rp647.900',
        'description': 'A party special that is loved by all. Vanilla flavored baked cheesecake with freshly strawberries.',
        'notes': '*Customizable for your loved ones special occasion!*'
    }

    return render(request, 'main.html', context)