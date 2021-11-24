import graphene
from graphene_django import DjangoObjectType

from ingredients.models import CategoryI, Ingredient

class CategoryType(DjangoObjectType):
    class Meta:
        model = CategoryI
        fields = ("id", "name", "ingredients")

class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = ("id", "name", "notes", "category")

class Query(graphene.ObjectType):
    all_ingredients = graphene.List(IngredientType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_all_ingredients(root, info):
        # We can easily optimize query count in the resolve method
        return Ingredient.objects.select_related("category").all()

    def resolve_category_by_name(root, info, name):
        try:
            return CategoryI.objects.get(name=name)
        except CategoryI.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)