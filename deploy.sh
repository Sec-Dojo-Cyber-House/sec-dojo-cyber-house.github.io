#!/bin/bash
set -e

WORKTREE_DIR="public"
cd "$WORKTREE_DIR" || exit 1

if [ -z "$(git status --porcelain)" ]; then
  echo "Nenhuma mudança detectada. Nenhum commit/push necessário."
  cd -
  exit 0
fi

BUILD_NUM=$(git rev-list --count HEAD)

git add -A 
git commit -m "blog build #$((BUILD_NUM + 1))"

git push origin gh-pages

cd -