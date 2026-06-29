# 1. Create the virtual environment (Using a stable Python version)
conda create -n wineq python=3.10 -y

# 2. Activate the virtual environment
conda activate wineq

# 3. Install your project requirements
pip install -r requirements.txt

# 4. Create the input data folder
mkdir data_given

# ------------------------------------------------------------------------
# NOTE: Download your data file from the link below and save it as:
# data_given/winequality.csv
https://drive.google.com/file/d/1y057-aS_1K5WYMZRQhayhbotFfIpipFn/view?usp=sharing

# ------------------------------------------------------------------------

# 5. Initialize Git and DVC version control
git init
dvc init

# 6. Start tracking the dataset using DVC
dvc add data_given/winequality.csv

# 7. Package and save your files and DVC pointers locally
git add .
git commit -m "first commit"

# 8. Link your local project directory to GitHub
git remote add origin https://github.com
git branch -M main

# 9. Push everything online to GitHub
git push -u origin main