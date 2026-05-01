#!/bin/bash
set -e

WORKTREE_DIR="public"

# Entra na pasta public
cd "$WORKTREE_DIR" || exit 1

# Força o Git a olhar para os arquivos de novo
git update-index -q --refresh

# Checa se realmente não tem nada (com mais precisão)
if git diff-index --quiet HEAD --; then
  echo "Nenhuma mudança detectada. Nenhum commit/push necessário."
  cd ..
  exit 0
fi

# Pega o número do build baseado na branch gh-pages
BUILD_NUM=$(git rev-list --count HEAD)

git add -A
git commit -m "blog build #$((BUILD_NUM + 1))"

echo "Tentando realizar push para gh-pages..."
if ! git push origin gh-pages; then
  echo "Push falhou. Forçando push com --force..."
  git push origin gh-pages --force
fi

# Volta para a raiz
cd ..