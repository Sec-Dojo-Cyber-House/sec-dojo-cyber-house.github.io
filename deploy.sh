#!/bin/bash
set -e

BRANCH="gh-pages"
BUILD_DIR="public"

echo "🚀 Iniciando deploy..."

# 1. Gera os gráficos
echo "📊 Gerando gráficos..."
python chartsGen.py

# 2. Build do Hugo (gera /public)
echo "🏗️ Buildando site..."
hugo --cleanDestinationDir

# 3. Entra na pasta de build
cd "$BUILD_DIR"

# 4. Inicializa repo temporário (sempre limpo)
echo "🔧 Inicializando repositório temporário..."
rm -rf .git

git init
git checkout -b $BRANCH

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