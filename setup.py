#!/usr/bin/env python3
"""
NBA Game Predictor Setup Script

This script sets up the NBA Game Predictor environment and verifies
that all dependencies are correctly installed.

Usage:
    python setup.py
"""

import subprocess
import sys
import os
from pathlib import Path

def install_requirements():
    """Install required packages from requirements.txt"""
    try:
        print("Installing required packages...")
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
        ])
        print("✅ All packages installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing packages: {e}")
        return False

def verify_installation():
    """Verify that all required packages can be imported"""
    required_packages = [
        'pandas', 'numpy', 'sklearn', 'xgboost', 'matplotlib', 
        'seaborn', 'requests', 'bs4', 'joblib'
    ]
    
    print("\nVerifying package installations...")
    failed_imports = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package}")
            failed_imports.append(package)
    
    if failed_imports:
        print(f"\n❌ Failed to import: {', '.join(failed_imports)}")
        return False
    else:
        print("\n✅ All packages verified successfully!")
        return True

def check_data_files():
    """Check if required data files exist"""
    data_files = [
        "nba-data/nba.csv",
        "model-files/improved_nba_model_package.pkl"
    ]
    
    print("\nChecking data files...")
    missing_files = []
    
    for file_path in data_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} (will be generated when needed)")
            missing_files.append(file_path)
    
    if missing_files:
        print(f"\nℹ️  Missing files will be generated when you run the notebooks.")
    
    return True

def main():
    """Main setup function"""
    print("=" * 60)
    print("NBA Game Predictor - Setup Script")
    print("=" * 60)
    
    # Check if we're in the right directory
    if not os.path.exists("README.md") or not os.path.exists("requirements.txt"):
        print("❌ Please run this script from the project root directory")
        sys.exit(1)
    
    # Install requirements
    if not install_requirements():
        sys.exit(1)
    
    # Verify installation
    if not verify_installation():
        sys.exit(1)
    
    # Check data files
    check_data_files()
    
    print("\n" + "=" * 60)
    print("🎉 Setup completed successfully!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Start Jupyter: jupyter notebook")
    print("2. Open notebooks/nba_ml.ipynb to train models")
    print("3. Open real-time-predictions/testing.ipynb for predictions")
    print("\nFor more information, see the README.md file.")

if __name__ == "__main__":
    main()
