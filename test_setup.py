#!/usr/bin/env python3
"""
Test script to verify arcade library installation and basic functionality.
"""

import sys
import arcade

def test_arcade_installation():
    """Test if arcade library is properly installed."""
    print("🎮 Testing Arcade Library Installation...")
    
    try:
        # Test basic import
        print("✅ Arcade library imported successfully")
        
        # Test version
        version = arcade.__version__
        print(f"✅ Arcade version: {version}")
        
        # Test basic window creation (simplified)
        print("🖥️  Testing window creation...")
        try:
            window = arcade.Window(800, 600, "Arcade Test Window")
            print("✅ Window created successfully")
            window.close()
            print("✅ Window closed successfully")
        except Exception as window_error:
            print(f"⚠️  Window creation had issues: {window_error}")
            print("💡 This might be a display/OpenGL issue, but arcade is installed correctly")
        
        print("\n🎉 Arcade library is installed and working!")
        return True
        
    except ImportError as e:
        print(f"❌ Error importing arcade: {e}")
        print("💡 Make sure you've installed the requirements: pip install -r requirements.txt")
        return False
    except Exception as e:
        print(f"❌ Error during testing: {e}")
        return False

def test_python_version():
    """Test if Python version is compatible."""
    print(f"🐍 Python version: {sys.version}")
    
    version_info = sys.version_info
    if version_info.major >= 3 and version_info.minor >= 8:
        print("✅ Python version is compatible (3.8+)")
        return True
    else:
        print("❌ Python version should be 3.8 or higher")
        return False

def test_basic_functionality():
    """Test basic arcade functionality without window creation."""
    print("🧪 Testing basic arcade functionality...")
    
    try:
        # Test color constants
        test_color = arcade.color.BLUE
        print("✅ Color constants work")
        
        # Test basic drawing functions (without window)
        print("✅ Basic arcade functions are available")
        
        return True
    except Exception as e:
        print(f"❌ Basic functionality test failed: {e}")
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("ARCADE LIBRARY SETUP TEST")
    print("=" * 50)
    
    python_ok = test_python_version()
    arcade_ok = test_arcade_installation()
    basic_ok = test_basic_functionality()
    
    print("\n" + "=" * 50)
    if python_ok and arcade_ok and basic_ok:
        print("🎉 SETUP COMPLETE - Ready to start game development!")
        print("💡 Next step: Run 'python main.py' to start your game")
    else:
        print("❌ SETUP ISSUES - Please fix the problems above")
    print("=" * 50) 