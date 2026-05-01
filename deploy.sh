#!/bin/bash
set -e

# 1. Configurações
WORKTREE_DIR="public"
BRANCH="gh-pages"

echo "🚀 Iniciando deploy..."

# 2. Garante que o Worktree existe e está saudável
if [ ! -d "$WORKTREE_DIR" ]; then
    echo "📁 Criando pasta public..."
    git worktree add -B $BRANCH $WORKTREE_DIR origin/$BRANCH
else
    # Se a pasta existe mas perdeu a conexão (.git sumiu), restaura
    if [ ! -f "$WORKTREE_DIR/.git" ]; then
        echo "🔧 Restaurando conexão com a branch $BRANCH..."
        git worktree remove --force $WORKTREE_DIR || true
        git worktree add -B $BRANCH $WORKTREE_DIR origin/$BRANCH
    fi
fi

# 3. Entra na pasta e limpa o índice (prevenção de erro no Windows)
cd "$WORKTREE_DIR"
git update-index -q --refresh
cd ..

# 4. Checa se houve mudanças reais
if [ -z "$(git status --porcelain $WORKTREE_DIR)" ]; then
    echo "✅ Nenhuma mudança detectada. O site já está atualizado."
    exit 0
fi

# 5. Commit e Push
cd "$WORKTREE_DIR"
BUILD_NUM=$(git rev-list --count HEAD)
git add -A
git commit -m "blog build #$((BUILD_NUM + 1)) - atualizando CVEs"

echo "📤 Enviando para o GitHub..."
git push origin $BRANCH --force

cd ..
echo "✨ Deploy finalizado com sucesso!"
