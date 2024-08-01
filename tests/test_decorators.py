from src.decorators import log


def test_log(capsys):
    """Test log"""

    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y

    # Test function
    my_function(1, 2)
    captured = capsys.readouterr()
    assert "my_function called with args: (1, 2), kwargs:{}. Result: 3\n" in captured.out
    # Test mistake
    try:
        my_function(0, 2)
    except TypeError:
        captured = capsys.readouterr()
        assert "my function error: " in captured.out
