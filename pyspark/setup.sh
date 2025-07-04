#!/bin/bash

# PySpark Setup Script for macOS
# This script installs Java, Python dependencies, and sets up the environment

echo "🚀 PySpark Setup Script for macOS"
echo "=================================="

# Check if Homebrew is installed
if ! command -v brew &> /dev/null; then
    echo "❌ Homebrew not found. Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
else
    echo "✅ Homebrew is already installed"
fi

# Update Homebrew
echo "🔄 Updating Homebrew..."
brew update

# Install Java 11 (required for PySpark)
echo "☕ Installing Java 11..."
if brew list --cask | grep -q "^temurin@11$"; then
    echo "✅ Java 11 is already installed"
else
    brew install --cask temurin@11
    echo "✅ Java 11 installed successfully"
fi

# Install Python 3 if not already installed
echo "🐍 Checking Python installation..."
if command -v python3 &> /dev/null; then
    echo "✅ Python 3 is already installed"
    python3 --version
else
    echo "Installing Python 3..."
    brew install python3
fi

# Install pip if not available
echo "📦 Checking pip installation..."
if command -v pip3 &> /dev/null; then
    echo "✅ pip3 is already installed"
else
    echo "Installing pip3..."
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python3 get-pip.py
    rm get-pip.py
fi

# Create virtual environment
echo "🌎 Creating virtual environment..."
if [ -d "venv" ]; then
    echo "✅ Virtual environment already exists"
else
    python3 -m venv venv
    echo "✅ Virtual environment created"
fi

# Activate virtual environment and install dependencies
echo "📚 Installing Python dependencies..."
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# Set environment variables
echo "🌍 Setting environment variables..."
export JAVA_HOME=$(/usr/libexec/java_home -v 11)
export PYSPARK_PYTHON=python3
export PYSPARK_DRIVER_PYTHON=python3

# Add to shell profile
SHELL_PROFILE=""
if [ -f ~/.zshrc ]; then
    SHELL_PROFILE=~/.zshrc
elif [ -f ~/.bashrc ]; then
    SHELL_PROFILE=~/.bashrc
elif [ -f ~/.bash_profile ]; then
    SHELL_PROFILE=~/.bash_profile
fi

if [ -n "$SHELL_PROFILE" ]; then
    echo "📝 Adding environment variables to $SHELL_PROFILE"
    echo "" >> $SHELL_PROFILE
    echo "# PySpark Environment Variables" >> $SHELL_PROFILE
    echo "export JAVA_HOME=\$(/usr/libexec/java_home -v 11)" >> $SHELL_PROFILE
    echo "export PYSPARK_PYTHON=python3" >> $SHELL_PROFILE
    echo "export PYSPARK_DRIVER_PYTHON=python3" >> $SHELL_PROFILE
    echo "✅ Environment variables added to $SHELL_PROFILE"
fi

echo ""
echo "🎉 Setup completed successfully!"
echo "=================================="
echo "Next steps:"
echo "1. Run: source venv/bin/activate"
echo "2. Run: python pyspark_setup.py"
echo ""
echo "Note: You may need to restart your terminal or run:"
echo "source $SHELL_PROFILE" 