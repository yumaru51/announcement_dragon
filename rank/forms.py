from django import forms
from .models import Category1, Category2, RankData


# list用意　外部参照でlist作成('value', 'text')形式
category1_list = []
for category1 in Category1.objects.all().values_list('category1', 'category1'):
    category1_list.append(category1)
category2_list = []
for category2 in Category2.objects.all().values_list('category2', 'category2'):
    category2_list.append(category2)


level_list = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
]


class RankDataForm(forms.ModelForm):
    user_name = forms.CharField(label='ユーザー名', widget=forms.TextInput(attrs={'class': 'form-control'}), initial='')
    category1 = forms.ChoiceField(label='カテゴリー1', choices=category1_list, widget=forms.Select(attrs={'size': 1, 'class': 'form-select'}), initial='')
    category2 = forms.ChoiceField(label='カテゴリー2', choices=category2_list, widget=forms.Select(attrs={'size': 1, 'class': 'form-select'}), initial='')
    product_name = forms.CharField(label='製品名', widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    maker = forms.CharField(label='メーカー', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    price = forms.ChoiceField(label='価格', choices=level_list, widget=forms.Select(attrs={'size': 1, 'class': 'form-select'}), required=True)
    durability = forms.ChoiceField(label='耐久性', choices=level_list, widget=forms.Select(attrs={'size': 1, 'class': 'form-select'}), required=True)
    portability = forms.ChoiceField(label='携帯性', choices=level_list, widget=forms.Select(attrs={'size': 1, 'class': 'form-select'}), required=True)
    functionality = forms.ChoiceField(label='機能性', choices=level_list, widget=forms.Select(attrs={'size': 1, 'class': 'form-select'}), required=True)
    repeat = forms.ChoiceField(label='リピート', choices=level_list, widget=forms.Select(attrs={'size': 1, 'class': 'form-select'}), required=True)
    category = forms.CharField(label='商品紹介', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 8, 'cols': 60}), initial='')
    # registration_time = forms.DateField(label='変更希望日', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), required=True)
    # update_time = forms.DateField(label='変更希望日', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), required=True)
    # lost_flag = forms.DateField(label='変更希望日', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), required=True)

    class Meta:
        model = RankData
        fields = ['user_name', 'category1', 'category2', 'product_name', 'maker', 'price', 'durability', 'portability',
                  'functionality', 'repeat', 'category']
        widgets = {}

    def __init__(self, *args, **kwargs):
        category1_choices = kwargs.pop('category1_choices', None)
        category2_choices = kwargs.pop('category2_choices', None)
        super(RankDataForm, self).__init__(*args, **kwargs)

        if category1_choices:
            self.fields['category1'].choices = category1_choices
        if category2_choices:
            self.fields['category2'].choices = category2_choices
