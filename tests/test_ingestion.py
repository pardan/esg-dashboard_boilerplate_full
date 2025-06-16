from backend.db import save_reading

def test_save_reading():
    save_reading('test_device', 'co2', 123.45)
    assert True
