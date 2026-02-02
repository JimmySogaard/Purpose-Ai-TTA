"""
Capital Management System with 369 Splits
Implements the unique capital allocation strategy
"""

from typing import Dict, List
from dataclasses import dataclass
from datetime import datetime


@dataclass
class CapitalSplit:
    """Represents a capital split allocation"""
    category: str
    percentage: float
    amount: float
    description: str


class CapitalManager:
    """
    369 Capital Management System
    Inspired by the 369 pattern (Nikola Tesla's sacred numbers)
    
    Split philosophy:
    - 3: Innovation/Growth (30%)
    - 6: Stability/Operations (60%)
    - 9: Give-back/Purpose (10%)
    """
    
    def __init__(self, total_capital: float):
        self.total_capital = total_capital
        self.giveback_pool = 0.0
        self.transaction_history = []
        self.splits = self._calculate_369_splits()
        
    def _calculate_369_splits(self) -> Dict[str, CapitalSplit]:
        """Calculate the 369 capital splits"""
        splits = {
            'innovation': CapitalSplit(
                category='Innovation/Growth',
                percentage=30.0,
                amount=self.total_capital * 0.30,
                description='Investment in new ideas, moonshot projects, and expansion'
            ),
            'stability': CapitalSplit(
                category='Stability/Operations',
                percentage=60.0,
                amount=self.total_capital * 0.60,
                description='Core operations, infrastructure, and sustainable practices'
            ),
            'giveback': CapitalSplit(
                category='Give-back to Folket',
                percentage=10.0,
                amount=self.total_capital * 0.10,
                description='Power to the people - community support and empowerment'
            )
        }
        
        self.giveback_pool = splits['giveback'].amount
        return splits
    
    def allocate(self, category: str, amount: float, purpose: str) -> bool:
        """Allocate capital from a specific category"""
        if category not in self.splits:
            return False
            
        split = self.splits[category]
        if amount > split.amount:
            return False
            
        split.amount -= amount
        
        self.transaction_history.append({
            'timestamp': datetime.now(),
            'category': category,
            'amount': amount,
            'purpose': purpose,
            'remaining': split.amount
        })
        
        return True
    
    def giveback_to_folket(self, amount: float, beneficiary: str, purpose: str) -> bool:
        """Distribute from the give-back pool to the community"""
        if amount > self.giveback_pool:
            return False
            
        self.giveback_pool -= amount
        
        self.transaction_history.append({
            'timestamp': datetime.now(),
            'category': 'giveback',
            'amount': amount,
            'beneficiary': beneficiary,
            'purpose': purpose,
            'remaining_pool': self.giveback_pool,
            'ethos': 'power_to_folket'
        })
        
        return True
    
    def get_balance_report(self) -> Dict[str, any]:
        """Get current balance across all splits"""
        return {
            'total_capital': self.total_capital,
            'splits': {
                name: {
                    'category': split.category,
                    'allocated_percentage': split.percentage,
                    'remaining_amount': split.amount,
                    'description': split.description
                }
                for name, split in self.splits.items()
            },
            'giveback_pool': self.giveback_pool,
            'total_allocated': sum(split.amount for split in self.splits.values())
        }
    
    def reallocate_369(self, new_total: float):
        """Reallocate capital with new total amount"""
        self.total_capital = new_total
        self.splits = self._calculate_369_splits()
