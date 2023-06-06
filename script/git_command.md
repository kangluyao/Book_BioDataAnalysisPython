# 对git进行简单配置
git config --global user.name "kangluyao"
git config --global user.email "luyaokang@outlook.com"
git config --global --list

# create a new repository on the command line
git init
echo "# Microbes in Tibetan permafrost" > README.md # > 覆盖原先文件；>>追加内容，原内容将保留
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/kangluyao/Book_BioDataAnalysisPython.git
git push -u origin main

# git rm --cached script -rf
git add script/.
git commit -m "upload"
git push -u origin master

git remote set-url origin https://github.com/kangluyao/Book_BioDataAnalysisPython.git

# Rename master to main
## First thing to do is to checkout the master branch if you didn’t already:
git checkout master
# Also be sure you have the latest changes
git pull origin master
## Now you can rename the local branch with the following command:
git branch -m main
## But now this change is only in your local git folder, what you need to do next is to push this the remote, which is as simple as to run this command:
git push origin -u main

# Change the default branch

## Now, at this point you have both master and main on your remote, and before you can delete the master branch, you need to go in the repository settings, go into the Branches section, and check what’s the default branch there. 
git push origin --delete master