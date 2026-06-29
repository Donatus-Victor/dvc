# Env setup
conda create -n wineq python=3.10 -y
conda activate wineq

# Dependencies
pip install -r requirements.txt

# Data dir
mkdir data_given

# Data link: https://drive.google.com/file/d/1y057-aS_1K5WYMZRQhayhbotFfIpipFn/view?usp=sharing
# Save downloaded file as: data_given/winequality.csv

# Init repo
git init
dvc init

# Track data
dvc add data_given/winequality.csv

# Save local
git add .
git commit -m "first commit"

# Push remote
git push -u origin main
