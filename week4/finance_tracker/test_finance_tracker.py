"""
Unit tests for the finance_tracker module.
Tests core functionality including transaction management, balance calculation,
file operations, and menu functions.
"""

import pytest
import os
import tempfile
from unittest.mock import patch, mock_open, MagicMock
from transaction_class import Transaction
from finance_tracker import (
    add_transaction, 
    calculate_balance, 
    show_balance,
    show_transactions_history,
    read_financial_data_from_file,
    write_financial_data_to_file,
    show_main_menu
)


class TestFinanceTracker:
    """Test suite for finance tracker functions."""

    def test_add_transaction_empty_list(self):
        """Test adding a transaction to an empty list."""
        transaction = Transaction("i", 1000, "salary")
        transactions = []
        
        result = add_transaction(transaction, transactions)
        
        assert len(result) == 1
        assert result[0] == transaction
        assert result is transactions  # Should modify the original list

    def test_add_transaction_existing_list(self):
        """Test adding a transaction to an existing list."""
        existing_transaction = Transaction("e", 500, "food")
        new_transaction = Transaction("i", 1000, "salary")
        transactions = [existing_transaction]
        
        result = add_transaction(new_transaction, transactions)
        
        assert len(result) == 2
        assert result[0] == existing_transaction
        assert result[1] == new_transaction

    def test_calculate_balance_empty_list(self):
        """Test balance calculation with empty transaction list."""
        transactions = []
        balance = calculate_balance(transactions)
        assert balance == 0

    def test_calculate_balance_income_only(self):
        """Test balance calculation with only income transactions."""
        transactions = [
            Transaction("i", "1000", "salary"),
            Transaction("i", "500", "bonus")
        ]
        balance = calculate_balance(transactions)
        assert balance == 1500

    def test_calculate_balance_expense_only(self):
        """Test balance calculation with only expense transactions."""
        transactions = [
            Transaction("e", "200", "food"),
            Transaction("e", "300", "transport")
        ]
        balance = calculate_balance(transactions)
        assert balance == -500

    def test_calculate_balance_mixed_transactions(self):
        """Test balance calculation with mixed income and expense transactions."""
        transactions = [
            Transaction("i", "1000", "salary"),
            Transaction("e", "200", "food"),
            Transaction("i", "500", "bonus"),
            Transaction("e", "150", "transport")
        ]
        balance = calculate_balance(transactions)
        assert balance == 1150  # 1000 - 200 + 500 - 150

    def test_calculate_balance_invalid_amount(self):
        """Test balance calculation with invalid amount data."""
        # Create a mock transaction with invalid amount
        mock_transaction = MagicMock()
        mock_transaction.type = "i"
        mock_transaction.amount = "invalid"
        
        transactions = [mock_transaction]
        
        with patch('builtins.print') as mock_print:
            balance = calculate_balance(transactions)
            assert balance == 0
            mock_print.assert_called_with("Invalid transaction data.")

    def test_show_balance_positive(self, capsys):
        """Test show_balance function with positive balance."""
        show_balance(1500)
        captured = capsys.readouterr()
        assert "Your balance is 1500" in captured.out

    def test_show_balance_negative(self, capsys):
        """Test show_balance function with negative balance."""
        show_balance(-500)
        captured = capsys.readouterr()
        assert "Your balance is -500" in captured.out

    def test_show_balance_zero(self, capsys):
        """Test show_balance function with zero balance."""
        show_balance(0)
        captured = capsys.readouterr()
        assert "Your balance is 0" in captured.out

    def test_show_transactions_history(self, capsys):
        """Test show_transactions_history function."""
        transactions = [
            Transaction("i", "1000", "salary", date="2023-10-10"),
            Transaction("e", "200", "food", date="2023-10-15")
        ]
        
        show_transactions_history(transactions)
        captured = capsys.readouterr()
        
        # Should print sorted transactions (reverse order)
        assert captured.out.count('\n') >= 2  # At least some newlines
        # The function prints the sorted list, so we just check it doesn't crash

    def test_show_main_menu(self, capsys):
        """Test show_main_menu function displays all menu options."""
        show_main_menu()
        captured = capsys.readouterr()
        
        assert "Welcome to your Finance Tracker" in captured.out
        assert "1. Add transaction" in captured.out
        assert "2. Show financial status" in captured.out
        assert "3. Create budget" in captured.out
        assert "4. Show budget" in captured.out
        assert "5. Budget monitoring" in captured.out
        assert "6. Quit" in captured.out


class TestFileOperations:
    """Test suite for file operations."""

    def test_read_financial_data_from_file_success(self):
        """Test successful reading of financial data from file."""
        mock_file_content = """i,5000,Salary,test description,2023-10-15
e,1500,Rent,test description,2023-10-12
e,600,Food,test description,2023-10-20"""
        
        with patch('builtins.open', mock_open(read_data=mock_file_content)):
            transactions = read_financial_data_from_file()
            
            assert len(transactions) == 3
            
            # Check first transaction
            assert transactions[0].type == "i"
            assert transactions[0].amount == "5000"
            assert transactions[0].category == "Salary"
            assert transactions[0].descr == "test description"
            assert transactions[0].date == "2023-10-15"
            
            # Check second transaction
            assert transactions[1].type == "e"
            assert transactions[1].amount == "1500"
            assert transactions[1].category == "Rent"

    def test_read_financial_data_file_not_found(self, capsys):
        """Test reading financial data when file doesn't exist."""
        with patch('builtins.open', side_effect=FileNotFoundError):
            transactions = read_financial_data_from_file()
            
            assert transactions == []
            captured = capsys.readouterr()
            assert "File could not be read." in captured.out

    def test_read_financial_data_io_error(self, capsys):
        """Test reading financial data with IO error."""
        with patch('builtins.open', side_effect=IOError("Permission denied")):
            transactions = read_financial_data_from_file()
            
            assert transactions == []
            captured = capsys.readouterr()
            assert "File could not be read." in captured.out

    def test_write_financial_data_to_file_success(self):
        """Test successful writing of financial data to file."""
        transactions = [
            Transaction("i", "1000", "salary", "Monthly pay", "2023-10-15"),
            Transaction("e", "200", "food", "Groceries", "2023-10-16")
        ]
        
        mock_file = mock_open()
        with patch('builtins.open', mock_file):
            write_financial_data_to_file(transactions)
            
            # Check that file was opened for writing
            mock_file.assert_called_once_with("transaction_data.txt", 'w')
            
            # Check that correct data was written
            written_calls = mock_file().write.call_args_list
            assert len(written_calls) == 2
            
            # Check first transaction line
            first_line = written_calls[0][0][0]
            assert "i,1000,salary,Monthly pay,2023-10-15" in first_line
            
            # Check second transaction line
            second_line = written_calls[1][0][0]
            assert "e,200,food,Groceries,2023-10-16" in second_line

    def test_write_financial_data_io_error(self, capsys):
        """Test writing financial data with IO error."""
        transactions = [Transaction("i", "1000", "salary")]
        
        with patch('builtins.open', side_effect=IOError("Disk full")):
            write_financial_data_to_file(transactions)
            
            captured = capsys.readouterr()
            assert "File could not be written." in captured.out

    def test_write_financial_data_empty_list(self):
        """Test writing empty transaction list."""
        transactions = []
        
        mock_file = mock_open()
        with patch('builtins.open', mock_file):
            write_financial_data_to_file(transactions)
            
            # Should still open file but write nothing
            mock_file.assert_called_once_with("transaction_data.txt", 'w')
            mock_file().write.assert_not_called()


class TestIntegration:
    """Integration tests combining multiple functions."""

    def test_add_and_calculate_balance_integration(self):
        """Test integration between add_transaction and calculate_balance."""
        transactions = []
        
        # Add some transactions
        transaction1 = Transaction("i", "1000", "salary")
        transaction2 = Transaction("e", "300", "food")
        transaction3 = Transaction("i", "200", "bonus")
        
        transactions = add_transaction(transaction1, transactions)
        transactions = add_transaction(transaction2, transactions)
        transactions = add_transaction(transaction3, transactions)
        
        # Calculate balance
        balance = calculate_balance(transactions)
        
        assert balance == 900  # 1000 - 300 + 200
        assert len(transactions) == 3

    def test_file_roundtrip_integration(self):
        """Test writing transactions to file and reading them back."""
        original_transactions = [
            Transaction("i", "1500", "salary", "Work", "2023-10-15"),
            Transaction("e", "250", "food", "Lunch", "2023-10-16")
        ]
        
        # Create temporary file
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as temp_file:
            temp_filename = temp_file.name
        
        try:
            # Patch the filename in both functions
            with patch('finance_tracker.open', mock_open()) as mock_file:
                # Write transactions
                write_financial_data_to_file(original_transactions)
                
                # Simulate the file content that would be written
                written_content = ""
                for call in mock_file().write.call_args_list:
                    written_content += call[0][0]
                
                # Now mock reading that content back
                with patch('finance_tracker.open', mock_open(read_data=written_content)):
                    read_transactions = read_financial_data_from_file()
                    
                    # Should have same number of transactions
                    assert len(read_transactions) == len(original_transactions)
                    
                    # Check first transaction data matches
                    assert read_transactions[0].type == original_transactions[0].type
                    assert read_transactions[0].amount == original_transactions[0].amount
                    assert read_transactions[0].category == original_transactions[0].category
                    
        finally:
            # Clean up temp file
            if os.path.exists(temp_filename):
                os.unlink(temp_filename)


if __name__ == "__main__":
    # Run tests if file is executed directly
    pytest.main([__file__, "-v"])