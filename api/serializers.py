from rest_framework import serializers
from .models import RecipeGenre, RecipeMaterial, RecipeMenu, RecipeMenuMaterial, RecipeSmallGenre # モデルをインポート
class APISerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeMenu # 使用するモデル
        fields = '__all__' # 処理対象にするフィールド（今回は全項目）