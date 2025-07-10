# File: push.ps1
python main.py

Write-Host "`nPushing Refs to GitHub..."

git add . > $null 2>&1

$a = Read-Host "Enter Commit Message"
git commit -m "$a" > $null 2>&1

Write-Host "Commit Created"

git push -u origin main > $null 2>&1

Write-Host "PUSHED to origin/main!"