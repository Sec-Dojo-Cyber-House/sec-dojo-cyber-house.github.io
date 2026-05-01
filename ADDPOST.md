### Como subir um novo post para o blog:

#### Pré-requisitos:

- Ter o Git instalado
- Ter o Hugo instalado

#### 1. Clonar o repositório

|Não tem a pasta na máquina local|Tem a pasta na máquina|
|--------------------------------|---------------------------------------------------|
|`git clone <link-do-repositorio>`|Antes de fazer alterações, sincronize o repositório local com o remoto usando: </br> `git pull origin main`.|

## 🧱 2. Criar posts

### 📂 Estrutura:

- CVEs → `content/post`
- Artigos → `content/articles`

### 📌 Passos:

1. Navegue até a pasta correspondente
2. Crie uma nova pasta com o nome do post  
   Exemplo: CVE-2026-12345
> 💡 Dica: copie a estrutura de um post anterior para manter o padrão.

---

## ✍️ 4. Editar o conteúdo (`index.md`)

Ajuste os metadados no topo:

- `title` → título do post  
- `date` → data da publicação  
- `description` → descrição  
- `image` → imagem de capa  

![](image-4.png)

---

## 🖼️ Capa do post</h2>
     
- Tamanho recomendado: **1200x600 px**

| Base no template | Preview |
|--------------------------------|---------------------------------------------------|
|![](image-3.png)|![](image-2.png)|

- Ferramentas: Photopea (online) ou Photoshop
     
> ⚠️ Use o template como base, mas não altere dentro do repositório `template-capa-post.psd`

![](image-2.png)

> Se a imagem tiver texto, precisa ser ajustada conforme os idiomas, use o modelo base (`template-capa-post.psd`)

---

## 📌 Fixar posts

Use o parâmetro:

```
weight: 100
```

- Menor que 99 → acima dos fixados
- Maior que 100 → abaixo

> Se não quiser um post fixado, apenas apague a linha do parâmetro `weight`

---

## 🌐 Tradução (EN/PT)

### Para adicionar versão em português:

1. Renomeie: `index.md → index.en.md`
2. Crie: `index.pt.md`
3. Adicione: `translationKey: nome-do-post`

> ⚠️ Deve ser igual nos dois arquivos

---

- Espaços (" ") não são aceitos nos parametros `title`, `date`, `translationKey` etc, substitua por "-", quando houver necessidade.
- O arquivo do conteudo em portugues deve estar na **mesma** pasta do post em ingles com o nome `index.pt.md`
- O texto alternativo [alt text] das imagens coladas são interpretadas como legendas e só devem ser preenchidos quando for necessário explicação, caso contrário é só apagar. 

| Evitar: | Top das Galaxias: |
|--------------------------------|---------------------------------------------------|
|![](image-1.png)|![](image.png)|

- Arquivos de imagens não devem conter espaços (image 1.png), se nao quebra. 

> Use por exemplo: `image-1.png`, não image 1.png.

---

## 🧠 Boas práticas ao escrever os posts

A maior parte da formatação dos artigos deve ser feita em HTML, para evitar problemas de parsing do Hugo (erro comum).

|Propósito|HTML recomendado|Tradução do Markdown|
|--------------------------------|---------------------------------------------------|---------------------------------------------------|
|Parágrafo justificado|`<p align="justify">Texto</p>`|nao é possivel justificar texto com markdown|
|Negrito|`<b>texto</b> ou <strong>texto</strong>`|`**texto**` / **texto**|
|Itálico|`<i>texto</i> ou <em>texto</em>`|`*texto*` / *texto*|
|Código em linha|`<code>código</code>`|`código`|

- Caso seja necessario adicionar um link no meio do parágrafo em HTML, use a tag `<a></a>`:
    - `<a href="link-aqui" target="_blank">Palavra que quiser que refira ao site aqui</a>`
    > `target="_blank"` é um parâmetro para que a aba do link abra automaticamente em uma nova aba, ao invés de apenas redirecionar o link da página atual

- Após o bloco de metadados (no topo do arquivo, onde fica o titulo, data etc), nunca use --- (hifens) novamente. Use apenas markdown ou HTML, pois o Hugo pode interpretar isso como um novo bloco de metadados e quebrar o post:

![](image-8.png)

- Nao precisa colocar numero nos indices, eles sao acicionados automaticamente:

![](image-7.png)

| Evitar: | Top das galaxias: |
|--------------------------------|---------------------------------------------------|
|![](image-6.png)|![](image-5.png)|

#### Vale lembrar que todas as alterações podem ser vistas em tempo real utilizando o servidor local do Hugo com comando: `hugo server -D` e no endereço `http://localhost:1313` do navegador.

> ***sempre verifique se a versão do Hugo está atualizada, caso contrário, pode dar erros.***

### Para parar de rodar o servidor local e fazer outras operações no terminal, use `ctrl+c`.

---

## Terminei de escrever o post e agora?

- Sempre revise: titulo, data, descrição etc, tanto no inglês quanto no português. Muitos erros comuns de quebra do site vêm de copiar/colar o topo do arquivo e esquecer de ajustar os valores conforme o idioma.

### Adicionar as mudanças:

- Na raiz do projeto, rode: `git add .`
- `git commit -m "Add: post <nome-do-post>"`
- `git push origin main`

### Publicar o site:

- `./deploy.sh`(linux)
- `sh .\deploy.sh` ou `bash deploy.sh` (Windows)

---

#### ⚙️ Como funciona o deploy?

O script `deploy.sh`:

- Gera gráficos automaticamente (chartsGen.py)
- Builda o site com o Hugo
- Publica na branch `gh-pages`

#### ⚠️ Importante
- ❌ Não edite a pasta `public`.
- ❌ Não use `git` dentro da `public`.
- ❌ Não faça deploy manual.

---

### Confirmar se o post foi publicado

- Vá até o repositório no GitHub.
- Verifique se:
    - A branch `main` está com seu commit.
    - A branch `gh-pages` recebeu o push corretamente (ícone ✅).
- Acesse a URL do blog para ver o novo post no ar.

> ***Se algum erro inesperado acontecer, você pode descrever o problema e usar uma IA para te ajudar (soluciona na maior parte das vezes) ou entrar em contato com a Karina ou Natan.***