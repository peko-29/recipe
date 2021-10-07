from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Q
from .models import Menu, Genre, Small_Genre, Material, Menu_Material

def index(request):
    if request.method == "POST":    # 検索が押された場合
        # ユーザーが選択したmaterialのidを受け取る
        materials = request.POST.getlist('materials')

        # 検索食材1つずつに該当するレシピをすべて取得
        dup_recipes_list = []
        for material in materials:
            material = int(material)
            # マテリアル→レシピの検索(材料1つずつ)
            material_relate_recipe = Material.objects.get(pk=material)
            recipe_query = material_relate_recipe.menu.all()
            # 検索結果をlist型に変換
            recipe_list = list(recipe_query.values())
            # 取得したリストを全て重複ありのレシピリストに入れる
            dup_recipes_list.extend(recipe_list)

        # 疑似AND検索
        recipes_list = []
        # リスト内の重複をチェック
        for recipe in dup_recipes_list:
            # 選択されたmaterialの数と重複数が同じだった場合(AND検索の代用)
            if dup_recipes_list.count(recipe) == len(materials):
                # result画面に返すレシピに加える
                recipes_list.append(recipe)

        # レシピを辞書型にして返す
        return render(request, 'recipe/result.html', {'recipes':recipes_list})

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