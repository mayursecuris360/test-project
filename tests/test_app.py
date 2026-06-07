from app import calculate_total

def test_calculate_total():
    assert calculate_total([10, 20, 30]) == 20.0

def test_calculate_total_empty():
    # This will fail — ZeroDivisionError
    result = calculate_total([])
    assert result == 0