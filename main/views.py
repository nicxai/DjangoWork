from django.shortcuts import render

# Create your views here.
def main(requests):
    context = {
        'name': 'Nicxai',
        'direction': 'BackEnd'
    }
    return render(requests, 'index.html', context=context)