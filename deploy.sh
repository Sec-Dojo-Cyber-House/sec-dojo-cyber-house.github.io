#!/bin/bash
set -e

BRANCH="gh-pages"
BUILD_DIR="public"

echo "🚀 Iniciando deploy..."

# 0. Limpa tudo antes
echo "🧹 Limpando build anterior..."
rm -rf public

# 1. Gera gráficos
echo "📊 Gerando gráficos..."
python chartsGen.py

# 2. Build
echo "🏗️ Buildando site..."
hugo --cleanDestinationDir

# 3. Entra no build limpo
cd public

# 4. Repo novo
git init
git checkout -b gh-pages

# 5. Adiciona tudo
git add -A

# 6. Commit (sempre garante mudança)
BUILD_TIME=$(date +%s 2>/dev/null || echo %RANDOM%)
git commit -m "deploy $BUILD_TIME - atualizando CVEs"

# 7. Conecta ao repo remoto
echo "🔗 Conectando ao repositório..."
git remote add origin "$(git -C .. config --get remote.origin.url)"

# 8. Push forçado para gh-pages
echo "📤 Enviando para GitHub Pages..."
git push origin $BRANCH --force

cd ..

echo "✨ Deploy finalizado com sucesso!"