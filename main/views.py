from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Shintia Dharma Shanty',
        'kelas': 'PBP F',
        'items': [
            {'name': 'Strawberry Cheesecake', 'size': '30x20', 'price': 'RP647.900', 'description': 'A party special that is loved by all. Vanilla flavored baked cheesecake with freshly picked strawberries.', 'notes': 'Customizable for your loved ones special occasion!'},
            {'name': 'Blueberry Cheesecake', 'size': '30x20', 'price': 'RP616.000', 'description': 'Our famous cheesecake pairs perfectly with natural blueberries.', 'notes': 'Customizable for your loved ones special occasion!'},
        ]
    }

    return render(request, 'main.html', context)