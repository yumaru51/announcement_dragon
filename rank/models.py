from django.db import models


# カテゴリーマスター1
class Category1(models.Model):
    category1 = models.CharField('カテゴリー1', max_length=20, blank=True, null=True)
    registration_time = models.DateTimeField('登録日時', blank=True, null=True)
    update_time = models.DateTimeField('更新日時', blank=True, null=True)
    lost_flag = models.IntegerField('無効FL', blank=True, null=True)

    class Meta:
        db_table = 'rank_m_category1'


# カテゴリーマスター2
class Category2(models.Model):
    category1 = models.CharField('カテゴリー1', max_length=20, blank=True, null=True)
    category2 = models.CharField('カテゴリー2', max_length=20, blank=True, null=True)
    registration_time = models.DateTimeField('登録日時', blank=True, null=True)
    update_time = models.DateTimeField('更新日時', blank=True, null=True)
    lost_flag = models.IntegerField('無効FL', blank=True, null=True)

    class Meta:
        db_table = 'rank_m_category2'


# 実データ
class RankData(models.Model):
    user_name = models.CharField('user_name', max_length=20, blank=True, null=True)
    category1 = models.CharField('カテゴリー1', max_length=20, blank=True, null=True)
    category2 = models.CharField('カテゴリー2', max_length=20, blank=True, null=True)
    product_name = models.CharField('製品名', max_length=20, blank=True, null=True)
    maker = models.CharField('メーカー', max_length=20, blank=True, null=True)
    price = models.IntegerField('価格', blank=True, null=True)
    durability = models.IntegerField('耐久性', blank=True, null=True)
    portability = models.IntegerField('携帯性', blank=True, null=True)
    functionality = models.IntegerField('機能性', blank=True, null=True)
    repeat = models.IntegerField('リピート', blank=True, null=True)
    category = models.CharField('商品紹介', max_length=100, blank=True, null=True)
    registration_time = models.DateTimeField('登録日時', blank=True, null=True)
    update_time = models.DateTimeField('更新日時', blank=True, null=True)
    lost_flag = models.IntegerField('無効FL', blank=True, null=True)

    class Meta:
        db_table = 'rank_t_rankdata'
        unique_together = (('user_name', 'category1', 'category2'),)

