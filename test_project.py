import pytest
from project import ExpenseTracker

def test_add_expense():
    tracker = ExpenseTracker()
    tracker.add_expense("Test Expense", 100.0, "2024-07-13")
    assert len(tracker.expenses) == 1
    assert tracker.expenses[0].description == "Test Expense"
    assert tracker.expenses[0].amount == 100.0
    assert tracker.expenses[0].date == "2024-07-13"

def test_view_expense(capfd):
    tracker = ExpenseTracker()
    tracker.add_expense("Test Expense 1", 50.0, "2024-07-01")
    tracker.add_expense("Test Expense 2", 75.0, "2024-07-15")
    tracker.view_expense()
    captured = capfd.readouterr()
    assert "Expense Id : 1" in captured.out
    assert "Description : Test Expense 1" in captured.out
    assert "Amount : 50.0" in captured.out
    assert "Date : 2024-07-01" in captured.out

def test_delete_expense():
    tracker = ExpenseTracker()
    tracker.add_expense("Test Expense", 100.0, "2024-07-13")
    tracker.delete_expense(1)
    assert len(tracker.expenses) == 0

def test_generate_monthly_report(capfd):
    tracker = ExpenseTracker()
    tracker.add_expense("Expense 1", 50.0, "2024-07-01")
    tracker.add_expense("Expense 2", 75.0, "2024-07-15")
    tracker.add_expense("Expense 3", 100.0, "2024-06-20")
    tracker.generate_monthly_report()
    captured = capfd.readouterr()
    assert "2024-07" in captured.out
    assert "125.0" in captured.out
    assert "2024-06" in captured.out
    assert "100.0" in captured.out