from django.db import models
from users.models import User
from django_filters import FilterSet, CharFilter
from django.db.models import Q
from django.conf import settings

#↓機種多重選択
class Sample2Choice(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
#↑機種多重選択


class Item(models.Model):
    """
    データ定義クラス
      各フィールドを定義する
    参考：
    ・公式 モデルフィールドリファレンス
    https://docs.djangoproject.com/ja/2.1/ref/models/fields/
    """

    # 項目1 メーカー
    sample_1_choice = (
    ('GCC', 'GCC'),
    ('SEI', 'SEI'),
    ('ROC', 'ROC'),
    ('WAZER', 'WAZER'),
    ('BOFA', 'BOFA'),
    ('ORION', 'ORION'),
    ('アマノ', 'アマノ'),
    )

    sample_1 = models.CharField(
        verbose_name='メーカー',
        choices=sample_1_choice,
        max_length=20,  # 選択肢の最大長を指定します
        blank=True,#空欄でも登録できるように
        null=True,#空の状態を登録できるように
    )

    # 項目2 機種
    sample_2 = models.ManyToManyField(
        Sample2Choice,
        verbose_name='機種',
        blank=True,
    )
    #sample_2 = models.ManyToManyField(
    #    Sample2Choice,
    #    verbose_name='機種',
    #    choices=sample_2_choice,
    #    max_length=20,  # 選択肢の最大長を指定します
    #    blank=True,
    #    null=True,
    #)

    # サンプル項目3 症状ジャンル
    sample_3 = models.CharField(
        verbose_name='症状ジャンル',
        max_length=200,  # 選択肢の最大長を指定します
        blank=True,
        null=True,
    )

    # サンプル項目4 症状詳細
    sample_4 = models.CharField(
        verbose_name='症状詳細',
        max_length=200,  # 選択肢の最大長を指定します
        blank=True,
        null=True,
    )
   # サンプル項目4_1 添付ファイル(テスト)
    sample_4_1 = models.FileField(
        upload_to='uploads/%Y/%m/%d/',
        verbose_name='添付ファイル',
        blank=True,
        null=True,
    )

   # サンプル項目4_2 症状画像
    sample_4_2 = models.ImageField(
        verbose_name='症状画像',
        blank=True,
        null=True,
    )

    # サンプル項目5 エラーコード
    sample_5 = models.CharField(
        verbose_name='エラーコード',
        max_length=100,  # 選択肢の最大長を指定します
        blank=True,
        null=True,
    )

    # サンプル項目6 階層を上る
    sample_6 = models.CharField(
        verbose_name='階層を上る',
        max_length=100,  # 選択肢の最大長を指定します
        blank=True,
        null=True,
    )

    # サンプル項目7 選択肢1
    sample_7 = models.CharField(
        verbose_name='選択肢１',
        max_length=100,  # 選択肢の最大長を指定します
        blank=True,
        null=True,
    )
    # サンプル項目7_1 選択肢1URL
    sample_7_1 = models.URLField(
        verbose_name='選択肢１URL',
        max_length=100,  # 選択肢の最大長を指定します
        blank=True,
        null=True,
    )

    # サンプル項目8 選択肢2
    sample_8 = models.CharField(
        verbose_name='選択肢２',
        max_length=100,  # 選択肢の最大長を指定します
        blank=True,
        null=True,
    )
    # サンプル項目8_1 選択肢2URL
    sample_8_1 = models.URLField(
        verbose_name='選択肢2URL',
        max_length=100,  # 選択肢の最大長を指定します
        blank=True,
        null=True,
    )

    # サンプル項目9 選択肢3
    sample_9 = models.CharField(
        verbose_name='選択肢３',
        max_length=100,  # 選択肢の最大長を指定します
        blank=True,
        null=True,
    )
        # サンプル項目9_1 選択肢3URL
    sample_9_1 = models.URLField(
        verbose_name='選択肢3URL',
        max_length=100,  # 選択肢の最大長を指定します
        blank=True,
        null=True,
    )

        # サンプル項目11 タグ欄
    sample_11 = models.CharField(
        verbose_name='タグ欄',
        max_length=100,  # 選択肢の最大長を指定します
        blank=True,
        null=True,
    )

    # サンプル項目10 選択肢（マスタ連動）
    sample_10 = models.ForeignKey(
        User,
        verbose_name='サンプル項目10_選択肢（マスタ連動）',
        blank=True,
        null=True,
        related_name='sample_10',
        on_delete=models.SET_NULL,
    )

    # 以下、管理項目

    # 作成者(ユーザー)
    created_by = models.ForeignKey(
        User,
        verbose_name='作成者',
        blank=True,
        null=True,
        related_name='CreatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 作成時間
    created_at = models.DateTimeField(
        verbose_name='作成時間',
        blank=True,
        null=True,
        editable=False,
    )

    # 更新者(ユーザー)
    updated_by = models.ForeignKey(
        User,
        verbose_name='更新者',
        blank=True,
        null=True,
        related_name='UpdatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 更新時間
    updated_at = models.DateTimeField(
        verbose_name='更新時間',
        blank=True,
        null=True,
        editable=False,
    )

    def __str__(self):
        sample_2_names = [choice.name for choice in self.sample_2.all()]
        return f'{self.sample_1} - {", ".join(sample_2_names)}'
        """
        管理画面でのタイトル表示
        """
    class Meta:
        verbose_name = 'サンプル'
        verbose_name_plural = 'サンプル'


