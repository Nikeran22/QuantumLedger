# test_quantumledger.py
"""
Tests for QuantumLedger module.
"""

import unittest
from quantumledger import QuantumLedger

class TestQuantumLedger(unittest.TestCase):
    """Test cases for QuantumLedger class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = QuantumLedger()
        self.assertIsInstance(instance, QuantumLedger)
        
    def test_run_method(self):
        """Test the run method."""
        instance = QuantumLedger()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
