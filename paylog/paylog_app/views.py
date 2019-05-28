from django.shortcuts import render

def main_view(request):
    return render(request, 'paylog/paylog_app/templates/main_view.html', {})