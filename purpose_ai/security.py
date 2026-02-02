"""
Security Module for Purpose-AI-TTA
Implements encryption and secure practices for private development
"""

import os
from typing import Optional
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2
import base64


class SecurityManager:
    """Manages encryption and security for the war room"""
    
    def __init__(self, encryption_key: Optional[str] = None):
        """
        Initialize security manager
        
        Args:
            encryption_key: Base64-encoded encryption key. If None, reads from environment.
        """
        if encryption_key:
            self.key = encryption_key.encode()
        else:
            key_from_env = os.getenv('ENCRYPTION_KEY')
            if key_from_env:
                self.key = key_from_env.encode()
            else:
                # Generate a new key if none provided
                self.key = Fernet.generate_key()
                
        self.cipher = Fernet(self.key)
        
    @staticmethod
    def generate_key() -> str:
        """Generate a new encryption key"""
        return Fernet.generate_key().decode()
    
    def encrypt_data(self, data: str) -> str:
        """Encrypt sensitive data"""
        encrypted = self.cipher.encrypt(data.encode())
        return encrypted.decode()
    
    def decrypt_data(self, encrypted_data: str) -> str:
        """Decrypt sensitive data"""
        decrypted = self.cipher.decrypt(encrypted_data.encode())
        return decrypted.decode()
    
    @staticmethod
    def hash_password(password: str, salt: Optional[bytes] = None) -> tuple:
        """
        Hash a password using PBKDF2
        
        Returns:
            tuple: (hashed_password, salt)
        """
        if salt is None:
            salt = os.urandom(16)
            
        kdf = PBKDF2(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key.decode(), base64.urlsafe_b64encode(salt).decode()
    
    @staticmethod
    def verify_password(password: str, hashed: str, salt: str) -> bool:
        """Verify a password against its hash"""
        try:
            new_hash, _ = SecurityManager.hash_password(
                password, 
                base64.urlsafe_b64decode(salt.encode())
            )
            return new_hash == hashed
        except Exception:
            return False
    
    def secure_api_key(self, api_key: str) -> str:
        """Mask API key for display"""
        if len(api_key) <= 8:
            return "***"
        return api_key[:4] + "*" * (len(api_key) - 8) + api_key[-4:]
    
    @staticmethod
    def validate_secure_mode() -> bool:
        """Validate that secure mode is enabled"""
        return os.getenv('SECURE_MODE', 'false').lower() == 'true'
