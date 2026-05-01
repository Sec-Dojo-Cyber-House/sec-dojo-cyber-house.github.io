#!/bin/bash
set -e

WORKTREE_DIR="public"
BRANCH="gh-pages"

echo "🚀 Iniciando deploy..."

# 1. Garante worktree saudável
if [ ! -d "$WORKTREE_DIR" ]; then
    echo "📁 Criando worktree..."
    git worktree add -B $BRANCH $WORKTREE_DIR origin/$BRANCH
else
    if [ ! -f "$WORKTREE_DIR/.git" ]; then
        echo "🔧 Restaurando worktree..."
        git worktree remove --force $WORKTREE_DIR || true
        git worktree add -B $BRANCH $WORKTREE_DIR origin/$BRANCH
    fi
fi

# 2. Gera gráficos
echo "📊 Gerando gráficos..."
python chartsGen.py

# 3. Build Hugo
echo "🏗️ Buildando site..."
hugo --cleanDestinationDir

# 4. Agora sim checa mudanças
if [ -z "$(git status --porcelain $WORKTREE_DIR)" ]; then
    echo "✅ Nenhuma mudança detectada."
    exit 0
fi

# 5. Commit
cd "$WORKTREE_DIR"

BUILD_NUM=$(git rev-list --count HEAD 2>/dev/null || echo 0)

git add -A
git commit -m "build #$((BUILD_NUM + 1)) - atualizando CVEs"

echo "📤 Enviando..."
git push origin $BRANCH --force

cd ..
echo "✨ Deploy finalizado!"