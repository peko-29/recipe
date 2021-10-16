from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Q
from .models import Menu, Genre, Small_Genre, Material, Menu_Materialxxxxw

# Create your views here.
def index(request):

    if request.method == "POST":    # 検索が押された場合
        # ユーザーが選択したmaterialのidを受け取る
        materials = request.POST.getlist('materials')

        dup_recipes_list = []
        for material in materials:
            material = int(material)
            # マテリアル→レシピの検索(材料1つずつ)
            material_relate_recipe = Material.objects.get(pk=material)
            recipe_query = material_relate_recipe.menu.all()
            # 検索結果をlist型に変換
            recipe_list = list(recipe_query.values())
            # 取得したリストを結合する
            dup_recipes_list.extend(recipe_list)

        recipes_list = []
        # リスト内の重複をチェック
        for recipe in dup_recipes_list:
            # 選択されたmaterialの数と重複数が同じだった場合(AND検索の代用)
            if dup_recipes_list.count(recipe) == len(materials):
                # 既にrecipes_listに含まれていればスルー
                if recipe in recipes_list:
                    continue
                # result画面に返すレシピに加える
                recipes_list.append(recipe)

        # レシピを返す
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
            materials_list.extend(list(materials_query_set.values()))
        # 抽出した辞書型のリストをモデルkeyの辞書型に格納
        materials_to_search = {'genres_list':genres_list, 'small_genres_list':small_genres_list, 'materials_list':materials_list}
        return render(request, 'recipe/index.html', materials_to_search)


def detail(request, menu_id):
    menus = Menu.objects.get(id = menu_id)
    materials = []
    search_keys = list(Menu_Material.objects.filter(menu=menu_id).values('material', 'amount'))
    for key in search_keys:
        material_name = str(Material.objects.get(id=key['material']))
        materials.append({'name':material_name, 'amount':key['amount']})
    return render(request, 'recipe/detail.html',{'menus':menus,'materials':materials})

