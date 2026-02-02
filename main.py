"""
Purpose-AI-TTA Main Entry Point
Adaptive AI War Room for Chaos-to-Purpose Elevation
"""

import asyncio
import sys
import os
from pathlib import Path

# Add the project root to the path
sys.path.insert(0, str(Path(__file__).parent))

from purpose_ai.war_room import WarRoom


def check_environment():
    """Check if environment is properly configured"""
    env_file = Path(__file__).parent / '.env'
    
    if not env_file.exists():
        print("⚠️  No .env file found. Creating from template...")
        env_example = Path(__file__).parent / '.env.example'
        if env_example.exists():
            print("📝 Please copy .env.example to .env and configure your API keys")
            print("   You can run: cp .env.example .env")
        return False
    return True


def main():
    """Main entry point"""
    print("🚀 Starting Purpose-AI-TTA War Room...")
    
    # Load environment variables
    try:
        from dotenv import load_dotenv
        load_dotenv()
        print("✓ Environment loaded")
    except ImportError:
        print("⚠️  python-dotenv not installed. Install requirements first:")
        print("   pip install -r requirements.txt")
        return
    
    # Check environment configuration
    if not check_environment():
        print("\n💡 Note: The system will work with default settings, but AI features")
        print("   require API keys to be configured in .env file")
        print()
    
    # Start the war room
    try:
        war_room = WarRoom()
        asyncio.run(war_room.run())
    except KeyboardInterrupt:
        print("\n\n👋 War room session ended. Power to folket!")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
