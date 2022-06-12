from devopslib.randomfruit import fruit


def test_fruit():
    fruit_choices = fruit()
    assert fruit_choices in ["apple", "cherry", "strawberry"]
