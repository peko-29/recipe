from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Q
from .models import Menu, Genre, Small_Genre, Material, Menu_Material

# Create your views here.
def index(request):
    # 仕様変更をしたい
    # 大ジャンルで選ぶと大ジャンルしか選択できない
    # 小ジャンルを選ぶと小ジャンルのみ
    # マテリアルを選ぶとマテリアルだけっていう風にしたい
    if request.method == "POST":    # 検索が押された場合
        # # 選択されたマテリアルでQオブジェクトを作る
        # materials = request.POST.getlist('materials')
        # materials_query = Q()
        # for material in materials:
        #     materials_query &= Q(material)
        # # マテリアル→レシピにAND検索する
        # recipe_query_set = Menu.object.filter(materials_query)

        # 検索を元にレシピを抽出(test)
        recipes_query_set = Menu.objects.all()
        # レシピをjson型にして返す
        recipes = {'recipes':list(recipes_query_set.values())}
        return render(request, 'recipe/result.html', recipes)

    else:   # GET方式でアクセスされた場合
        # 検索用データを抽出して辞書型のリストに変換
        genres_query_set = Genre.objects.exclude(name='調味料')
        genres_list = list(genres_query_set.values())
        small_genres_query_set = Small_Genre.objects.exclude(genre_id=4)
        small_genres_list = list(small_genres_query_set.values())
        materials_list = []
        for small_genre in small_genres_query_set:
            materials_query_set = small_genre.material_set.all()
            materials_list.append(list(materials_query_set.values()))
        # 抽出した辞書型のリストをモデルkeyの辞書型に格納
        materials_to_search = {'genres_list':genres_list, 'small_genres_list':small_genres_list, 'materials_list':materials_list}
        return render(request, 'recipe/index.html', materials_to_search)

def search(request):
    material = request.POST.get("materials")
    materials = Material.objects.get(id = material)
    menus = materials.menu.all()
    return render(request, 'recipe/search.html',{'menus':menus})

def detail(request, menu_id):
    menus = Menu.objects.get(id = menu_id)
    materials = menus.material_set.all()
    return render(request, 'recipe/detail.html',{'menus':menus, 'materials': materials})