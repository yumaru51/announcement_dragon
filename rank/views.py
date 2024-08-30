from django.shortcuts import render, redirect
from django.db.models import Model  # Model情報を取得
from rank.models import Category1, Category2, RankData
from rank.forms import RankDataForm
from django.contrib import messages


def top(request):
    if request.method == 'POST':
        rank_data_form = RankDataForm(request.POST, request.FILES)

        # ファイルがアップロードされているかをチェック
        if 'product_pict' not in request.FILES or not request.FILES['product_pict']:
            # アラートメッセージを表示
            messages.error(request, 'ファイルが選択されていません。')
        elif rank_data_form.is_valid():
            obj = RankData.objects.create(id=None)
            request_form = RankDataForm(data=request.POST, instance=obj)
            request_form.save()
            user_name = rank_data_form.cleaned_data['user_name']
            category1 = rank_data_form.cleaned_data['category1']
            category2 = rank_data_form.cleaned_data['category2']

            # ファイルが1件もない、または新規画面の時　アップロード不可
            if request.FILES.__len__() == 0:
                print("ファイル無し")
            else:
                product_pict = request.FILES['product_pict']

                file_name = rank_data_form.cleaned_data['product_name'] + ".jpg"
                upload_file_path = 'C:\\Users\\y-kawauchi\\PycharmProjects\\announcement_dragon\\static\\img\\'
                with open(upload_file_path + file_name, 'wb+') as destination:
                    for chunk in product_pict.chunks():
                        destination.write(chunk)
            return redirect('top')
        else:
            print(rank_data_form.errors)
        return redirect('top')
    else:
        category_dict = {}
        for category_data in Category2.objects.all():
            category_dict[str(category_data.id)] = {
                'category1': category_data.category1,
                'category2': category_data.category2,
            }
        rank_data_form = RankDataForm(
            initial=dict(user_name='yumaru51'),
        )
        data = {
            'category_dict': category_dict,
            'rank_data_form': rank_data_form,
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


