from django import forms

from .models import Item


class ItemForm(forms.ModelForm):
    """
    モデルフォーム構成クラス
    ・公式 モデルからフォームを作成する
    https://docs.djangoproject.com/ja/2.1/topics/forms/modelforms/
    """

    class Meta:
        model = Item
        fields = '__all__'
        #↓機種をチェックにする？
        widgets = {
            'sample_2': forms.CheckboxSelectMultiple,
        }
        #↑機種をチェックにする？

        # 以下のフィールド以外が入力フォームに表示される
        # AutoField
        # auto_now=True
        # auto_now_add=Ture
        # editable=False
        
class SampleForm(forms.Form):
    sample_1_choice = (
        ('GCC', 'GCC'),
        ('SEI', 'SEI'),
        ('ROC', 'ROC'),
        ('WAZER', 'WAZER'),
    )

    sample_1 = forms.ChoiceField(
        label='メーカー',
        choices=sample_1_choice,
        widget=forms.Select(attrs={'id': 'sample-1'}),
        required=False,
    )

    sample_2 = forms.ChoiceField(
        label='機種',
        choices=(),
        widget=forms.Select(attrs={'id': 'sample-2'}),
        required=False,
    )
