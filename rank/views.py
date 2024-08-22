from django.shortcuts import render
from django.db.models import Model  # Model情報を取得
from rank.models import Category1, Category2, RankData


def top(request):
    category_dict = {}
    for category_data in Category2.objects.all():
        category_dict[str(category_data.id)] = {
            'category1': category_data.category1,
            'category2': category_data.category2,
        }
    data = {
        'category_dict': category_dict,
        'message': 'データを出力しました'
    }
    return render(request, 'rank/top.html', data)


def detail(request, category1, category2):
    # data = {
    #     'user_name': ['川内', ],
    #     'カテゴリー1': [30, 25],
    #     'カテゴリー2': ['東京都', '大阪府'],
    #     '製品名': ['東京都', '大阪府'],
    #     'メーカー': ['東京都', '大阪府'],
    #     '': ['東京都', '大阪府'],
    #     '': ['東京都', '大阪府'],
    # }
    data = {
        'user_name': ['yumaru51'],
        'カテゴリー1': [category1],
        'カテゴリー2': [category2],
        '製品名': ['東京都', '大阪府'],
        'メーカー': ['東京都', '大阪府'],
        '': ['東京都', '大阪府'],
        '': ['東京都', '大阪府'],
    }
    return render(request, 'rank/detail.html', {'data': data})

    # category_dict = {}
    # for category_data in Category2.objects.all():
    #     category_dict[str(category_data.id)] = {
    #         'category1': category_data.category1,
    #         'category2': category_data.category2,
    #     }
    # data = {
    #     'category_dict': category_dict,
    #     'message': 'データを出力しました'
    # }
    # return render(request, 'rank/detail.html', data)

