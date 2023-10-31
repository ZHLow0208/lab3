import price_info as info

def test_costs_of_fruits():
    fruit = 'apple'
    quantity = 10
    result = info.cost_of_fruits(fruit,quantity)
    assert (result == 12.0)

def test_total_cost_shopping():

    result = info.total_cost_shopping()
    assert (result == 46.75)