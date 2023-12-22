from django.contrib import admin
from .models import Item, Sample2Choice

# Sample2Choiceモデルを管理画面に登録
admin.site.register(Sample2Choice)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """
    管理画面上の動作の設定
      項目の表示非表示や検索項目の指定が可能
    """
    list_display = ('sample_1', 'get_sample_2_display')

    def get_sample_2_display(self, obj):
        return ", ".join([str(choice) for choice in obj.sample_2.all()])
    get_sample_2_display.short_description = '機種'

    class Meta:
        pass
