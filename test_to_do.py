from to_do import add, clear, todos


def test_add_task():
    """Test adding a task to the to-do list"""
    add("Buy milk")
    assert "Buy milk" in todos


def test_clear():
    """Test celaring the to-do list"""
    add("buy milk")
    clear()
    assert len(todos) == 0
