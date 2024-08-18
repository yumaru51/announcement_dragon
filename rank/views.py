from django.shortcuts import render

# Create your views here.
def top(request):

    data = {
        'message': 'データを出力しました'
    }
    return render(request, 'rank/top.html', data)

