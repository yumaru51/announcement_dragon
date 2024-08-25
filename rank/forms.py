from django import forms
from .models import RankData


category1_list = [
    ('1', '家電'),
    ('2', 'ゲーム'),
    ('3', 'ファッション'),
]
category2_list = [
    ('1', 'ドライヤー'),
    ('2', 'スピーカー'),
    ('3', 'プロジェクター'),
]


class RankDataForm(forms.ModelForm):
    user_name = forms.ChoiceField(label='ユーザー名', widget=forms.Select(attrs={'size': 1, 'class': 'form-select'}), initial='')
    category1 = forms.ChoiceField(label='カテゴリー1', choices=category1_list, widget=forms.Select(attrs={'size': 1, 'class': 'form-select'}), initial='')
    category2 = forms.ChoiceField(label='カテゴリー2', choices=category2_list, widget=forms.Select(attrs={'size': 1, 'class': 'form-select'}), initial='')
    product_name = forms.MultipleChoiceField(label='変更対象', widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-inline_change_target', 'required': 'True'}), required=True)
    # maker = forms.CharField(label='その他', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    # price = forms.CharField(label='変更管理名称', widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    # durability = forms.CharField(label='変更内容概略', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 8, 'cols': 60}), required=True)
    # portability = forms.ChoiceField(label='継続/一過性', choices=level_list, widget=forms.Select(attrs={'size': 1, 'class': 'form-select'}), initial='')
    # functionality = forms.CharField(label='リスク低減処置', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    # repeat = forms.ChoiceField(label='安全面', choices=safety_list, widget=forms.Select(attrs={'size': 1, 'class': 'form-select'}), initial='')
    # category = forms.ChoiceField(label='品質面', choices=quality_list, widget=forms.Select(attrs={'size': 1, 'class': 'form-select'}), initial='')
    # registration_time = forms.DateField(label='変更希望日', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), required=True)
    # update_time = forms.DateField(label='変更希望日', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), required=True)
    # lost_flag = forms.DateField(label='変更希望日', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), required=True)

    class Meta:
        model = RankData
        fields = ['user_name', 'category1', 'category2', 'product_name']
        widgets = {}

