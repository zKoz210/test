import pytest
from pip._vendor import requests

def test_file1_method1():
    response = requests.get("http://localhost:3000")
    assert response.ok


def test_file1_method2():
    response = requests.get("http://localhost:3000/amount")
    assert not response.ok


def test_file1_method3():
    response = requests.get("http://localhost:3000/amount/TEST")
    assert not response.ok


def test_file1_method4():
    response = requests.get("http://localhost:3000/amount/6000")
    assert response.ok
    data = response.json()
    assert data == {
        'RUB': data['RUB'],
        'AMOUNT_USD': 6000,
        'RESULT': data['RUB'] * 6000
    }
