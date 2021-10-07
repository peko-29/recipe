from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import APISerializer
from .models import RecipeGenre, RecipeMaterial, RecipeMenu, RecipeMenuMaterial, RecipeSmallGenre # モデルをインポート

@api_view(['GET']) # GET のみに対応
def dataList(request):
    # indexに実装した検索のフィルターをこちらに持ってくるには？
    api_data = RecipeMenu.objects.all() # モデルからデータを抽出する
    serializer = APISerializer(api_data, many=True) # シリアライザにデータを渡す
    return Response(serializer.data) # シリアル可されたデータを return で返す