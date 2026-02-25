from django.shortcuts import render

def live_calculator_view(request):
    return render(request, 'livecalculator/index.html')
