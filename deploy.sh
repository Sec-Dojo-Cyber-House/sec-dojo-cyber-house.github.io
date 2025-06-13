WORKTREE_DIR="public"

cd "$WORKTREE_DIR" || exit 1

if git diff --quiet && git diff --cached --quiet; then
  echo "Nenhuma mudança detectada. Nenhum commit/push necessário."
  exit 0
fi

BUILD_NUM=$(git rev-list --count HEAD)

git add .
git commit -m "blog build #$((BUILD_NUM + 1))"

git push origin gh-pages

cd -