from django.shortcuts import render, redirect
from django.db.models import Model  # Model情報を取得
from rank.models import Category1, Category2, RankData
from rank.forms import RankDataForm


def top(request):
    if request.method == 'POST':
        form = RankDataForm(request.POST)
        if form.is_valid():
            obj = RankData.objects.create(id=None)
            request_form = RankDataForm(data=request.POST, instance=obj)
            request_form.save()
            user_name = form.cleaned_data['user_name']
            category1 = form.cleaned_data['category1']
            category2 = form.cleaned_data['category2']
            return redirect('top')
    else:
        category_dict = {}
        for category_data in Category2.objects.all():
            category_dict[str(category_data.id)] = {
                'category1': category_data.category1,
                'category2': category_data.category2,
            }
        rankdatas = RankDataForm(initial=dict(
            user_name='yumaru51',
        ))

        data = {
            'category_dict': category_dict,
            'rankdatas': rankdatas,
        }
    return render(request, 'rank/top.html', data)


def detail(request, category1, category2):

    rank_records = RankData.objects.get(user_name='yumaru51', category1=category1, category2=category2)
    data = {
        'user_name': 'yumaru51',
        '製品名': ['東京都', '大阪府'],
        'メーカー': ['東京都', '大阪府'],
        'rank_records': rank_records,
    }
    return render(request, 'rank/detail.html', data)


