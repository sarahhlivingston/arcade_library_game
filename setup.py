#!/usr/bin/env python3
"""
Setup script for the 2D Arcade Game Development Project.
This script will help set up the development environment.
"""

import os
import sys
import subprocess
import venv

def run_command(command, description):
    """Run a command and handle errors."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible."""
    print("🐍 Checking Python version...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} is compatible")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} is not compatible")
        print("💡 Please use Python 3.8 or higher")
        return False

def create_virtual_environment():
    """Create a virtual environment."""
    if os.path.exists("venv"):
        print("✅ Virtual environment already exists")
        return True
    
    print("🔄 Creating virtual environment...")
    try:
        venv.create("venv", with_pip=True)
        print("✅ Virtual environment created successfully")
        return True
    except Exception as e:
        print(f"❌ Failed to create virtual environment: {e}")
        return False

def get_activation_command():
    """Get the appropriate activation command for the current OS."""
    if sys.platform == "win32":
        return "venv\\Scripts\\activate"
    else:
        return "source venv/bin/activate"

def main():
    """Main setup function."""
    print("=" * 60)
    print("🎮 2D ARCADE GAME DEVELOPMENT SETUP")
    print("=" * 60)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Create virtual environment
    if not create_virtual_environment():
        sys.exit(1)
    
    # Get activation command
    activation_cmd = get_activation_command()
    
    print("\n📋 SETUP INSTRUCTIONS:")
    print("=" * 60)
    print("1. Activate the virtual environment:")
    print(f"   {activation_cmd}")
    print("\n2. Install dependencies:")
    print("   pip install -r requirements.txt")
    print("\n3. Test the setup:")
    print("   python test_setup.py")
    print("\n4. Run the game:")
    print("   python main.py")
    print("\n" + "=" * 60)
    
    # Ask if user wants to run the commands automatically
    try:
        response = input("🤔 Would you like me to run the installation commands now? (y/n): ")
        if response.lower() in ['y', 'yes']:
            print("\n🚀 Running installation commands...")
            
            # Install dependencies
            if sys.platform == "win32":
                pip_cmd = "venv\\Scripts\\pip install -r requirements.txt"
            else:
                pip_cmd = "venv/bin/pip install -r requirements.txt"
            
            if run_command(pip_cmd, "Installing dependencies"):
                print("\n🎉 Setup completed successfully!")
                print("💡 You can now run: python test_setup.py")
            else:
                print("\n❌ Setup failed. Please check the error messages above.")
        else:
            print("\n💡 Please follow the manual setup instructions above.")
            
    except KeyboardInterrupt:
        print("\n\n👋 Setup cancelled by user.")
        print("💡 You can run the setup commands manually when ready.")

if __name__ == "__main__":
    main() 