import pytest
from everycheese.cheeses.models import Cheese

pytestmark = pytest.mark.django_db


def test__str__():
    cheese = Cheese.objects.create(
        name = 'Mozzarella',
        description = 'Italian Cheese',
        firmness = Cheese.Firmness.SOFT
    )
    assert cheese.__str__() == 'Mozzarella'
    assert str(cheese) == 'Mozzarella'
