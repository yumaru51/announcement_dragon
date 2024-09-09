from django.shortcuts import render, redirect
from django.db.models import Model  # Model情報を取得
from rank.models import Category1, Category2, RankData
from rank.forms import RankDataForm
from django.contrib import messages


def top(request):
    category_dict = {}
    for category_data in Category1.objects.all():
        category_dict[str(category_data.id)] = {
            'category1': category_data.category1,
        }

    if request.method == 'POST':
        rank_data_form = RankDataForm(request.POST, request.FILES)
        context = {
            'category_dict': category_dict,
            'rank_data_form': rank_data_form,
        }
        # ファイルがアップロードされているかをチェック
        if 'product_pict' not in request.FILES or not request.FILES['product_pict']:
            # アラートメッセージを表示
            messages.error(request, 'ファイルが選択されていません。')
            return render(request, 'rank/top.html', context)

        if rank_data_form.is_valid():
            obj = RankData.objects.create(id=None)
            request_form = RankDataForm(data=request.POST, instance=obj)
            request_form.save()

            product_pict = request.FILES['product_pict']
            file_name = rank_data_form.cleaned_data['product_name'] + ".jpg"
            upload_file_path = 'C:\\Users\\y-kawauchi\\PycharmProjects\\announcement_dragon\\static\\img\\'
            with open(upload_file_path + file_name, 'wb+') as destination:
                for chunk in product_pict.chunks():
                    destination.write(chunk)
            context['rank_data_form'] = rank_data_form
            return render(request, 'rank/top.html', context)
        else:  # 入力チェックエラー
            # context['rank_data_form'] = rank_data_form
            print(rank_data_form.errors)
            return render(request, 'rank/top.html', context)
    else:  # GET時
        rank_data_form = RankDataForm(
            initial=dict(user_name='yumaru51'),
        )
        context = {
            'category_dict': category_dict,
            'rank_data_form': rank_data_form,
        }
    return render(request, 'rank/top.html', context)


def detail(request, category1):
    if request.method == 'POST':
        # 商品説明更新
        category2 = request.POST['category2']
        category = request.POST['category']
        obj = RankData.objects.get(user_name='yumaru51', category1=category1, category2=category2)
        obj.category = category
        obj.save()

    rank_records = RankData.objects.filter(user_name='yumaru51', category1=category1)
    if not rank_records.exists():
        messages.error(request, 'データがありません。')

    # chart_data = [65, 59, 90, 81, 56]
    # labels = ['項目1', '項目2', '項目3', '項目4', '項目5']
    chart_data = {}
    labels = [
        RankData._meta.get_field('price').verbose_name,
        RankData._meta.get_field('durability').verbose_name,
        RankData._meta.get_field('portability').verbose_name,
        RankData._meta.get_field('functionality').verbose_name,
        RankData._meta.get_field('repeat').verbose_name,
    ]

    for records in rank_records:
        chart_data[records.category2] = [
            records.price,
            records.durability,
            records.portability,
            records.functionality,
            records.repeat
        ]

        print(RankData._meta.get_field('price').verbose_name, records.price)
        print(RankData._meta.get_field('durability').verbose_name, records.durability)
        print(RankData._meta.get_field('portability').verbose_name, records.portability)
        print(RankData._meta.get_field('functionality').verbose_name, records.functionality)
        print(RankData._meta.get_field('repeat').verbose_name, records.repeat)

    data = {
        'user_name': 'yumaru51',
        'rank_records': rank_records,
        'chart_data': chart_data,
        'labels': labels,
    }
    return render(request, 'rank/detail.html', data)


def detail2(request):

    return render(request, 'rank/datail.html', data)

