"""
Unit tests for the Transaction class.
Tests all methods and properties of the Transaction class including
initialization, string representations, comparison methods, and sign calculation.
"""

import pytest
from transaction_class import Transaction


class TestTransaction:
    """Test suite for the Transaction class."""

    def test_init_with_all_parameters(self):
        """Test Transaction initialization with all parameters provided."""
        transaction = Transaction("i", 1000, "salary", "Monthly salary", "2023-10-15")
        
        assert transaction.type == "i"
        assert transaction.amount == 1000
        assert transaction.category == "salary"
        assert transaction.descr == "Monthly salary"
        assert transaction.date == "2023-10-15"
        assert transaction.sign == ""  # Income should have empty sign

    def test_init_with_defaults(self):
        """Test Transaction initialization with default values."""
        transaction = Transaction("e", 500, "food")
        
        assert transaction.type == "e"
        assert transaction.amount == 500
        assert transaction.category == "food"
        assert transaction.descr is None
        assert transaction.date == "00-00-00"
        assert transaction.sign == "-"  # Expense should have minus sign

    def test_str_representation_income(self):
        """Test string representation for income transactions."""
        transaction = Transaction("i", 1500, "salary", "Bonus", "2023-10-15")
        expected = "2023-10-15 salary: 1500kr"
        assert str(transaction) == expected

    def test_str_representation_expense(self):
        """Test string representation for expense transactions."""
        transaction = Transaction("e", 200, "food", "Lunch", "2023-10-15")
        expected = "2023-10-15 food: -200kr"
        assert str(transaction) == expected

    def test_repr_representation(self):
        """Test repr representation (should be same as str)."""
        transaction = Transaction("i", 1000, "salary", "Work", "2023-10-15")
        assert repr(transaction) == str(transaction)

    def test_get_sign_income(self):
        """Test get_sign method for income transactions."""
        transaction = Transaction("i", 1000, "salary")
        assert transaction.get_sign() == ""

    def test_get_sign_expense(self):
        """Test get_sign method for expense transactions."""
        transaction = Transaction("e", 500, "food")
        assert transaction.get_sign() == "-"

    def test_get_sign_unknown_type(self):
        """Test get_sign method for unknown transaction types."""
        transaction = Transaction("x", 500, "unknown")
        assert transaction.get_sign() == ""  # Defaults to empty for unknown types

    def test_less_than_comparison_by_date(self):
        """Test __lt__ method compares transactions by date."""
        earlier = Transaction("i", 1000, "salary", date="2023-10-10")
        later = Transaction("e", 500, "food", date="2023-10-15")
        
        assert earlier < later
        assert not later < earlier

    def test_less_than_same_date(self):
        """Test __lt__ method with same dates."""
        trans1 = Transaction("i", 1000, "salary", date="2023-10-15")
        trans2 = Transaction("e", 500, "food", date="2023-10-15")
        
        assert not trans1 < trans2
        assert not trans2 < trans1

    def test_equality_same_date_same_amount(self):
        """Test __eq__ method with same date and amount."""
        trans1 = Transaction("i", 1000, "salary", date="2023-10-15")
        trans2 = Transaction("e", 1000, "bonus", date="2023-10-15")
        
        assert trans1 == trans2

    def test_equality_same_date_different_amount(self):
        """Test __eq__ method with same date but different amounts."""
        trans1 = Transaction("i", 1000, "salary", date="2023-10-15")
        trans2 = Transaction("e", 500, "food", date="2023-10-15")
        
        assert not trans1 == trans2

    def test_equality_different_date_same_amount(self):
        """Test __eq__ method with different dates but same amounts."""
        trans1 = Transaction("i", 1000, "salary", date="2023-10-10")
        trans2 = Transaction("e", 1000, "food", date="2023-10-15")
        
        assert not trans1 == trans2

    def test_sorting_transactions(self):
        """Test that transactions can be sorted by date using built-in sort."""
        transactions = [
            Transaction("i", 1000, "salary", date="2023-10-15"),
            Transaction("e", 200, "food", date="2023-10-10"),
            Transaction("e", 500, "rent", date="2023-10-12")
        ]
        
        sorted_transactions = sorted(transactions)
        
        assert sorted_transactions[0].date == "2023-10-10"
        assert sorted_transactions[1].date == "2023-10-12"
        assert sorted_transactions[2].date == "2023-10-15"

    def test_transaction_with_numeric_strings(self):
        """Test transaction with amount as string (common from file input)."""
        transaction = Transaction("i", "1500", "salary")
        assert transaction.amount == "1500"  # Should preserve original type

    def test_transaction_with_empty_description(self):
        """Test transaction with empty string description."""
        transaction = Transaction("e", 300, "food", "")
        assert transaction.descr == ""

    def test_transaction_immutability_concept(self):
        """Test that transaction properties can be accessed and modified."""
        transaction = Transaction("i", 1000, "salary")
        original_amount = transaction.amount
        
        # Properties should be accessible
        assert transaction.amount == original_amount
        
        # Can be modified (not enforcing immutability in current design)
        transaction.amount = 1500
        assert transaction.amount == 1500


if __name__ == "__main__":
    # Run tests if file is executed directly
    pytest.main([__file__, "-v"])