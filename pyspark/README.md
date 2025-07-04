# PySpark Setup Guide

This repository contains everything you need to set up and run PySpark on macOS.

## 🚀 Complete Step-by-Step Setup Process

### Prerequisites
- macOS (tested on darwin 24.5.0+)
- Terminal access
- Internet connection for downloading dependencies

### Step 1: Automated Setup (Recommended)
```bash
# Make the setup script executable
chmod +x setup.sh

# Run the automated setup
./setup.sh
```

### Step 2: Manual Setup (Alternative)

If you prefer to set up manually, follow these steps:

#### 2.1 Install Homebrew (if not already installed)
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

#### 2.2 Install Java 11 (Required for PySpark)
```bash
brew install --cask temurin@11
```

#### 2.3 Install Python 3 (if not already installed)
```bash
brew install python3
```

#### 2.4 Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 2.5 Install PySpark Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

#### 2.6 Set Environment Variables
Add these to your shell profile (`~/.zshrc`, `~/.bashrc`, or `~/.bash_profile`):

```bash
export JAVA_HOME=$(/usr/libexec/java_home -v 11)
export PYSPARK_PYTHON=python3
export PYSPARK_DRIVER_PYTHON=python3
```

Then reload your shell:
```bash
source ~/.zshrc  # or your appropriate shell profile
```

### Step 3: Test Your Setup
```bash
# Activate virtual environment
source venv/bin/activate

# Run the test script
python pyspark_setup.py
```

### Step 4: Verify Installation
If everything is working correctly, you should see:
- ✅ Spark Session Created Successfully!
- Sample DataFrame operations
- Advanced PySpark operations
- Performance examples

## 📁 Files in This Repository

- `requirements.txt` - Python dependencies
- `pyspark_setup.py` - Main PySpark demo script with examples
- `my_pyspark_project.py` - Starter template for your projects
- `setup.sh` - Automated setup script for macOS
- `.vscode/settings.json` - VS Code configuration
- `README.md` - This comprehensive guide

## 🔄 Reusing This Setup

To reuse this setup for future projects:

1. **Copy these files** to your new project folder:
   ```bash
   cp requirements.txt your-new-project/
   cp setup.sh your-new-project/
   cp -r .vscode your-new-project/
   cp README.md your-new-project/
   ```

2. **Run the setup** in your new project:
   ```bash
   cd your-new-project
   chmod +x setup.sh
   ./setup.sh
   ```

3. **Activate environment** and start coding:
   ```bash
   source venv/bin/activate
   python your_pyspark_script.py
   ```

## 🌍 Cross-Platform Notes

### Windows Users:
- Install **WSL2** (Windows Subsystem for Linux) first
- Or use **Git Bash** and modify setup.sh for Windows commands
- Install Java 11 manually from [Adoptium](https://adoptium.net/)

### Linux Users:
- Replace `brew` commands with your package manager (`apt`, `yum`, etc.)
- Install Java 11: `sudo apt install openjdk-11-jdk` (Ubuntu/Debian)
- Modify `JAVA_HOME` path in setup.sh accordingly

## 🔧 Common Issues and Solutions

### Issue 1: Java not found
**Error**: `JAVA_HOME is not set`
**Solution**: 
```bash
export JAVA_HOME=$(/usr/libexec/java_home -v 11)
```

### Issue 2: Permission denied
**Error**: `Permission denied` when running setup.sh
**Solution**: 
```bash
chmod +x setup.sh
```

### Issue 3: PySpark not found
**Error**: `No module named 'pyspark'`
**Solution**: 
```bash
source venv/bin/activate
pip install pyspark
```

### Issue 4: Port already in use
**Error**: Spark UI port conflicts
**Solution**: The script automatically handles this, but you can also specify a different port:
```python
spark = SparkSession.builder \
    .appName("MyApp") \
    .config("spark.ui.port", "4041") \
    .getOrCreate()
```

## 📊 What the Demo Script Does

The `pyspark_setup.py` script demonstrates:

1. **Spark Session Creation** - Sets up PySpark environment
2. **DataFrame Operations** - Creating, filtering, and manipulating data
3. **Advanced Operations** - Grouping, aggregation, sorting
4. **SQL Operations** - Running SQL queries on DataFrames
5. **RDD Operations** - Low-level Spark operations
6. **Performance Examples** - Caching and optimization techniques

## 🎯 Next Steps

After successful setup, you can:

1. **Modify the demo script** to work with your own data
2. **Create new Python files** for your specific PySpark projects
3. **Use Jupyter notebooks** for interactive development:
   ```bash
   source venv/bin/activate
   jupyter notebook
   ```
4. **Process real data** by loading CSV, JSON, or Parquet files

## 💻 VS Code Integration

### Setting up VS Code with PySpark:

1. **Install Python extension** in VS Code
2. **Select Python interpreter** from your virtual environment:
   - Open VS Code in your project folder
   - Press `Cmd+Shift+P` (macOS) or `Ctrl+Shift+P` (Windows/Linux)
   - Type "Python: Select Interpreter"
   - Select the interpreter from `./venv/bin/python`

3. **Configure VS Code settings** (create `.vscode/settings.json`):
   ```json
   {
     "python.defaultInterpreterPath": "./venv/bin/python",
     "python.terminal.activateEnvironment": true,
     "python.envFile": "${workspaceFolder}/.env"
   }
   ```

4. **Create environment file** (`.env` in your project root):
   ```bash
   # PySpark Environment Variables
   JAVA_HOME=/usr/libexec/java_home -v 11
   PYSPARK_PYTHON=python3
   PYSPARK_DRIVER_PYTHON=python3
   
   # Optional: Spark configurations
   SPARK_LOCAL_IP=127.0.0.1
   PYSPARK_DRIVER_PYTHON_OPTS=notebook
   ```

### Useful VS Code Extensions:
- **Python** - Microsoft
- **Jupyter** - Microsoft
- **Python Docstring Generator** - Nils Werner
- **autoDocstring** - Nils Werner

## 📚 Learning Resources

- [PySpark Documentation](https://spark.apache.org/docs/latest/api/python/)
- [Spark SQL Guide](https://spark.apache.org/docs/latest/sql-programming-guide.html)
- [PySpark Examples](https://github.com/apache/spark/tree/master/examples/src/main/python)

## 🆘 Getting Help

If you encounter issues:
1. Check the error messages carefully
2. Ensure all environment variables are set correctly
3. Try restarting your terminal
4. Verify Java and Python installations

## ✅ Complete Setup Checklist

Use this checklist when setting up PySpark in a new project:

### Prerequisites Check:
- [ ] macOS/Linux/WSL2 environment
- [ ] Internet connection available
- [ ] Terminal access confirmed

### Setup Steps:
- [ ] Copy setup files to new project folder
- [ ] Run `chmod +x setup.sh`
- [ ] Execute `./setup.sh`
- [ ] Verify Java 11 installation: `java -version`
- [ ] Activate virtual environment: `source venv/bin/activate`
- [ ] Test PySpark: `python pyspark_setup.py`

### VS Code Setup:
- [ ] Install Python extension
- [ ] Select correct Python interpreter (./venv/bin/python)
- [ ] Copy `.vscode/settings.json`
- [ ] Create `.env` file with environment variables
- [ ] Test import in VS Code: `from pyspark.sql import SparkSession`

### Development Ready:
- [ ] Spark session creates successfully
- [ ] Can run basic DataFrame operations
- [ ] Jupyter notebook accessible (optional)
- [ ] Ready to process your data!

## 🛠️ Additional Development Tools

### Optional but Recommended:
```bash
# Install additional development tools
pip install black flake8 pylint pytest
```

### Git Configuration:
Create `.gitignore` file:
```gitignore
# Virtual environment
venv/
.env

# Python cache
__pycache__/
*.pyc
*.pyo

# Jupyter notebooks
.ipynb_checkpoints/

# Spark temporary files
spark-warehouse/
derby.log
metastore_db/
```

## 📊 Performance Tips

1. **Use appropriate cluster modes** for large datasets
2. **Cache DataFrames** when reusing: `df.cache()`
3. **Optimize partitioning** for better performance
4. **Use columnar formats** (Parquet) for better I/O
5. **Monitor Spark UI** at `http://localhost:4040`

Happy coding with PySpark! 🚀 