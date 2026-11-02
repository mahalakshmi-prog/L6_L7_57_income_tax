import pytest
from income_tax import taxable_income, tax_due, refund_status


# ---------- taxable_income() ----------

def test_new_regime():
    assert taxable_income(1000000, "new", 0) == 925000


def test_old_regime():
    assert taxable_income(1000000, "old", 100000) == 850000


def test_old_regime_max_investment():
    assert taxable_income(1000000, "old", 200000) == 800000


def test_negative_income():
    with pytest.raises(ValueError):
        taxable_income(-1000, "new", 0)


def test_unknown_regime():
    with pytest.raises(ValueError):
        taxable_income(500000, "abc", 0)


def test_taxable_negative_returns_zero():
    assert taxable_income(50000, "old", 150000) == 0


# ---------- tax_due() ----------

def test_below_exemption():
    assert tax_due(200000, 30) == 0


def test_negative_taxable():
    with pytest.raises(ValueError):
        tax_due(-1000, 25)


def test_senior_citizen():
    assert tax_due(350000, 65) == 2500


def test_super_senior():
    assert tax_due(600000, 85) == 5000


def test_first_slab():
    assert tax_due(300000, 30) == 2500


def test_second_slab():
    assert tax_due(600000, 30) == 32500


# ---------- refund_status() ----------

def test_refund():
    assert refund_status(50000, 30000, True) == "refund"


def test_refund_delayed():
    assert refund_status(50000, 30000, False) == "refund delayed"


def test_pay_balance():
    assert refund_status(10000, 30000, True) == "pay balance"


def test_pay_balance_penalty():
    assert refund_status(10000, 30000, False) == "pay balance with penalty"


def test_settled():
    assert refund_status(30000, 30000, True) == "settled"