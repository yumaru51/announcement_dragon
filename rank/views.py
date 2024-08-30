from django.shortcuts import render, redirect
from django.db.models import Model  # Model情報を取得
from rank.models import Category1, Category2, RankData
from rank.forms import RankDataForm
import os


def top(request):
    if request.method == 'POST':
        form = RankDataForm(request.POST, request.FILES)
        if form.is_valid():
            obj = RankData.objects.create(id=None)
            request_form = RankDataForm(data=request.POST, instance=obj)
            request_form.save()
            user_name = form.cleaned_data['user_name']
            category1 = form.cleaned_data['category1']
            category2 = form.cleaned_data['category2']

            # ファイルが1件もない、または新規画面の時　アップロード不可
            if request.FILES.__len__() == 0:
                print("ファイル無し")
            else:
                product_pict = request.FILES['product_pict']

                file_name = form.cleaned_data['product_name'] + ".jpg"
                upload_file_path = 'C:\\Users\\y-kawauchi\\PycharmProjects\\announcement_dragon\\static\\img\\'
                with open(upload_file_path + file_name, 'wb+') as destination:
                    for chunk in product_pict.chunks():
                        destination.write(chunk)
        else:
            print(form.errors)
        return redirect('top')
    else:
        category_dict = {}
        for category_data in Category2.objects.all():
            category_dict[str(category_data.id)] = {
                'category1': category_data.category1,
                'category2': category_data.category2,
            }

        category1_list = Category1.objects.all().values_list('category1', 'category1')
        category2_list = Category2.objects.all().values_list('category2', 'category2')
        rankdatas = RankDataForm(
            initial=dict(user_name='yumaru51'),
            category1_choices=category1_list,
            category2_choices=category2_list,
        )
        # rankdatas.fields['category1'].choices = category1_list
        # rankdatas.fields['category2'].choices = category2_list

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


