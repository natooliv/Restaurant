import pytest
from src.models.dish import Dish
from src.models.ingredient import Ingredient, Restriction


def test_dish():
    bacon_burguer_dish = Dish('Lombo Canadense', 30.0)
    assert bacon_burguer_dish.name == 'Lombo Canadense'
    assert bacon_burguer_dish.price == 30.0
    assert bacon_burguer_dish == Dish('Lombo Canadense', 30.0)
    assert repr(bacon_burguer_dish) == "Dish('Lombo Canadense', R$30.00)"
    assert hash(bacon_burguer_dish) == hash(Dish('Lombo Canadense', 30.0))
    assert hash(bacon_burguer_dish) != hash(Dish('Marguerita', 28.0))

    with pytest.raises(TypeError):
        Dish('Lombo Canadense', '-30')
    with pytest.raises(ValueError):
        Dish('Lombo Canadense', -30)

    bacon_ingredient = Ingredient('bacon')
    bacon_burguer_dish.add_ingredient_dependency(bacon_ingredient, 1)
    assert bacon_burguer_dish.recipe == {Ingredient('bacon'): 1}
    assert bacon_burguer_dish.get_ingredients() == {bacon_ingredient}
    assert bacon_burguer_dish.get_restrictions() == {
        Restriction.ANIMAL_MEAT, Restriction.ANIMAL_DERIVED
    }
