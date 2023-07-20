from src.models.ingredient import Ingredient, Restriction


# Req 1
def test_ingredient():
    # Teste 'queijo mussarela'
    mozzarella = Ingredient("queijo mussarela")
    assert mozzarella.name == "queijo mussarela"
    assert mozzarella.restrictions == {
        Restriction.LACTOSE, Restriction.ANIMAL_DERIVED
    }
    assert mozzarella == Ingredient("queijo mussarela")
    assert mozzarella != Ingredient("ovo")
    assert hash(mozzarella) == hash("queijo mussarela")
    assert hash(mozzarella) != hash(Ingredient("ovo"))
    assert repr(mozzarella) == "Ingredient('queijo mussarela')"

    # Teste 'farinha'
    farinha = Ingredient("farinha")
    assert farinha.name == "farinha"
    assert farinha.restrictions == {Restriction.GLUTEN}
    assert farinha == Ingredient("farinha")
    assert farinha != Ingredient("ovo")
    assert hash(farinha) == hash("farinha")
    assert hash(farinha) != hash(Ingredient("ovo"))
    assert repr(farinha) == "Ingredient('farinha')"

    # Teste  'sal'
    sal = Ingredient("sal")
    assert sal.name == "sal"
    assert sal.restrictions == set()
    assert sal == Ingredient("sal")
    assert sal != Ingredient("ovo")
    assert hash(sal) == hash("sal")
    assert repr(sal) == "Ingredient('sal')"
