# todo_app

# repository 만들 때 처음부터 파일이 존재하게 만들면 (ex. README< License 등)
# 1. Sourcetree 사용 시 고려 사항
## 1. clone으로 시작 (원격지에 있는 파일부터 시작해서 local repository에 프로젝트 시작하면 OK)
## 2. 이미 local repository에 파일이 존재하면 Sourcetree로 pull부터 시작해도 Branch가 나뉘어 있다. (git bash로 git cli 환경에서 명령어로 처리)


```bash
# local repository

git init

git remote add origin <원격지 주소>

git pull origin main

# git status : add, commit 여부 확인

git add -A

git commit -m '<커밋 메시지>'

git push origin main 
```
