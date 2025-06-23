### Como subir um novo post para o blog:

#### Pré-requisitos:

- Ter o Git e o Hugo instalados na máquina.

#### 1. Clonar o repositório na máquina local

|Não tem a pasta na máquina local|Tem a pasta na máquina|
|--------------------------------|---------------------------------------------------|
|`git clone <link repositorio>`|Antes de fazer alterações, sincronize o repositório local com o remoto usando `git pull`.|

#### 2. Abra a pasta clonada no VS Code.
#### 3. Montar a worktree da pasta `public` para o branch `gh-pages`:

`git worktree add -B gh-pages public origin/gh-pages`

> ⚠️ Se der erro, pode apagar a pasta public e recriar o worktree com:

`rm -rf public`

`git worktree prune`

`git worktree add -B gh-pages public origin/gh-pages`

> 💡 Isso não é um problema, pois a pasta public será sobrescrita sempre que o site for buildado novamente.

#### 4. Criar o post na pasta content/post

- Navegue até `content/post`
- Crie uma nova pasta com o título do post, exemplo: CVE-2025-12345

> 💡 Dica: para facilitar, copie e cole a pasta de um post anterior com a mesma severidade e exclua as imagens.

- Edite o conteúdo do `index.md`:

Altere:

- `title` (título do post, exemplo: CVE-2025-12345)
- `date` (CVE: dia da publicação da CVE / Artigo: dia da alteração do arquivo)
- Conteúdo principal do post

##### 🌐 Caso queira adicionar o conteúdo também em português:

- Altere o nome de `index.md` para `index.en.md`
- Adicione o parametro `translationKey` onde alterou o titulo, data etc
- O parametro `translationKey` deve ser exatamente o mesmo no conteudo em ingles e em portugues

> ***Exemplo na pasta: "CVE-2025-52474"***

- Espaços (" ") não são aceitos nos parametros `title`, `date`, `translationKey` etc, substitua por "-", quando houver necessidade.
- O arquivo do conteudo em portugues deve estar na **mesma** pasta do post em ingles com o nome `index.pt.md`

#### 5. Adicionar as mudanças:

- Na raiz do projeto (branch `main`), rode:

`git add .`

#### 6. Fazer o commit das alterações:

`git commit -m "Add: post <nome-do-post>"`

#### 7. Enviar para o repositório remoto:

`git push origin main`

#### 8. Buildar o site com Hugo:

`hugo --minify`

Isso irá gerar os arquivos estáticos atualizados na pasta `public`.

> ***⚠️ Não commit a pasta `public` na branch `main`***

> ***A pasta public está ligada à branch `gh-pages` via worktree, então não comite ela na `main`.***

#### 9. Publicar no GitHub Pages:

| Script Automatizado                         | Manual                                         |
|--------------------------------|---------------------------------------------------|
|Rode o script de deploy: `./deploy.sh`|Navegue até a pasta `public` vinculada à branch `gh-pages`: `cd public`                    |
| 💡 Esse script muda para a pasta `public` (vinculada à branch `gh-pages`), faz o `git add`, `commit`, `push` e retorna para a raiz do projeto vinculada à branch `main`.         | Adicione as mudanças: `git add .`    |
|         | Faça o commit: `git commit -m "blog build <# ultima versao + 1>"` ou `git commit -m "blog build <mes, dia>"`  |
|         | Envie as mudanças para o repositório remoto: `git push origin gh-pages`  |
|         | Retorne para a raiz do projeto vinculada à branch `main`: `cd ..`|

##### Caso ocorra erro no push:

Se houver erro no push (ex: conflito ou rejeição):

`cd public`

`git push -f origin gh-pages  # forçar o push`

#### 10. Confirmar se o post foi publicado

- Vá até o repositório no GitHub.
- Verifique se:
    - A branch `main` está com seu commit.
    - A branch `gh-pages` recebeu o push corretamente (ícone ✅).
- Acesse a URL do blog para ver o novo post no ar.

> ***Se algum erro inesperado acontecer, você pode descrever o problema e usar uma IA para te ajudar (soluciona na maior parte das vezes) ou entrar em contato com a Karina ou Natan.***