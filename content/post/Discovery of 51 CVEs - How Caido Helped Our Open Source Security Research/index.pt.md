---
title: Descoberta de 51 CVEs - Como o Caido Ajudou Nossa Pesquisa em Segurança de Código Aberto
description: Fortalecendo a Segurança de Software Open Source através da Detecção Eficaz de Vulnerabilidades
date: 2025-06-04
weight: 100
translationKey: "article-cvehuntersandcaido"
image: cve-hunters+caido.png
tags:
  - CVE-Hunters
  - Ferramenta Caido
  - Proxy Caido
  - Pesquisa de vulnerabilidades
  - Segurança de aplicações web
  - Divulgação responsável
  - Vulnerabilidades em código aberto
  - Ferramentas de segurança para pentesters
  - Ferramentas de bug bounty
  - Hacking ético
  - Alternativa ao Burp Suite
  - Publicação de CVE
  - Detecção de XSS
  - Vulnerabilidade IDOR
  - Proteção contra CSRF
  - Filtro HTTPQL

categories:
  - Pesquisa de Vulnerabilidades
  - Segurança de Código Aberto
  - Segurança de Aplicações Web
  - Ferramentas de Pentest
  - Projetos de Hacking Ético
  - Divulgação de CVE
  - Educação em Cibersegurança
  - Estudos de Caso
---

##  Contribuições do Grupo CVE-Hunters usando o Caido

<p style="text-align: justify;">A segurança da informação é uma ajuda preciosa para o design, instalação e atualização contínua de sistemas computacionais, especialmente para uso público, sem fins lucrativos ou educacional. Com o aumento dos ataques cibernéticos e vazamentos de dados, nunca foi tão crítico melhorar a segurança dos projetos open source.</p>

<p style="text-align: justify;">Nosso grupo, CVE-Hunters, se esforça para encontrar, pesquisar e divulgar de forma responsável vulnerabilidades (CVEs) em softwares de código aberto amplamente utilizados. Contribuímos com a comunidade global de cibersegurança relatando CVEs, melhorando a segurança do código e ajudando os mantenedores a corrigirem vulnerabilidades de segurança do mundo real antes que se tornem alvos de ataques.</p> 

<p style="text-align: justify;">Por meio de pesquisas de vulnerabilidade no trabalho e testes de penetração ao vivo, nosso programa não apenas protege aplicações web críticas, mas também oferece treinamento prático para a futura geração de hackers éticos e especialistas em cibersegurança. Buscamos fomentar uma cultura de cibersegurança ativa, aberta e inclusiva — permitindo que estudantes e pesquisadores utilizem ferramentas de ponta como o Caido para realizar ataques simulados, automatizar testes de segurança e facilitar práticas de desenvolvimento seguro.</p>

## Objetivos do Projeto

<p style="text-align: justify;">Nossa pesquisa em cibersegurança se apoia em três pilares centrais que sustentam a excelência técnica e a responsabilidade social:</p>

<p style="text-align: justify;">
 <ul>
  <li>Reforçar a segurança de softwares open source comumente utilizados por meio da descoberta, verificação e apoio à correção de vulnerabilidades do mundo real. Esses bugs centrais — como Cross-Site Scripting (XSS), Insecure Direct Object References (IDOR) ou autenticação falha — podem ser explorados em produção, expondo informações sensíveis.</li>
  <li>Oferecer treinamento experiencial em cibersegurança para futuros profissionais por meio de projetos reais de avaliação de vulnerabilidades. Os estudantes ganham experiência prática em descoberta de bugs, análise de código seguro e divulgação ética de vulnerabilidades usando ferramentas modernas como Caido, Burp Suite e scripts de automação personalizados.</li>
  <li>Incentivar a pesquisa colaborativa e a publicação responsável de CVEs (Common Vulnerabilities and Exposures) para facilitar a conscientização sobre ameaças emergentes, melhorar a transparência e ajudar no fortalecimento contínuo de sistemas críticos.</li>
 </ul>
</p>

## Case 1: Platforma WeGIA 

![](wegia.png)

<p style="text-align: justify;">Um dos principais alvos de nossa pesquisa em segurança foi a aplicação web WeGIA (Web Manager for Assistance Institutions) — uma aplicação open source para gerenciamento de instituições do terceiro setor no Brasil, incluindo ONGs, abrigos sociais e instituições sem fins lucrativos. Tais organizações dependem fortemente de doações, apoio voluntário e processamento seguro de dados para funcionar de forma eficaz.</p>

<p style="text-align: justify;">As falhas de segurança descobertas incluíram vulnerabilidades críticas como acesso não autorizado, processos de autenticação inadequados e exposição de dados com impacto considerável na confidencialidade, integridade e disponibilidade de informações sensíveis. Em um desafio colaborativo fascinante de pentest, a comunidade CVE-Hunters descobriu, divulgou de forma responsável e reavaliou 48 vulnerabilidades (CVEs) no sistema WeGIA.</p>

<p style="text-align: justify;">A correção eficaz e a descoberta dessas falhas contribuíram para o status geral de segurança da plataforma e facilitaram a sustentabilidade e confiabilidade do software a longo prazo. Este caso reforça a necessidade de escaneamento constante de vulnerabilidades e a presença do hacking ético na defesa de ferramentas open source utilizadas em contextos sociais críticos.</p>

## Case 2: Platforma i-Educar 

![](i-educar.png)

<p style="text-align: justify;">Dando continuidade ao nosso esforço para promover a segurança cibernética da infraestrutura digital crítica, nossa equipe de pesquisa direcionou seu foco para a plataforma i-Educar, um sistema de gestão escolar open source amplamente adotado por escolas públicas e instituições de ensino no Brasil.</p> 

<p style="text-align: justify;">O i-Educar é projetado para lidar com dados sensíveis de estudantes, incluindo informações pessoais dos alunos, professores e históricos escolares. Isso torna a plataforma um alvo privilegiado para possíveis atacantes, o que reforça a importância de protegê-la contra ameaças futuras.</p>

<p style="text-align: justify;">Durante uma auditoria profissional de segurança de aplicações, nossa equipe de pesquisadores encontrou outras vulnerabilidades no sistema i-Educar. Estas incluíam bypass de autenticação, exposição insegura de dados e controles de acesso inadequados — que podem comprometer a confidencialidade, integridade e disponibilidade das informações educacionais.</p>

<p style="text-align: justify;">Até o momento, 3 das vulnerabilidades receberam oficialmente IDs de CVE e foram divulgadas de forma responsável aos mantenedores do projeto seguindo as melhores práticas de divulgação coordenada. As demais descobertas estão aguardando validação técnica e documentação e serão submetidas para publicação como CVE nas próximas semanas.</p> 

<p style="text-align: justify;">Este estudo de caso ilustra a importância da pesquisa de vulnerabilidades para a comunidade educacional, especialmente ao lidar com plataformas open source que armazenam informações pessoais identificáveis (PII). Ao proteger o i-Educar, estamos comprometidos em construir uma comunidade online mais segura para escolas e estudantes.</p>

## Ferramenta de Suporte: Caido

![](caido.webp)

<p style="text-align: justify;">Em nossos testes aprofundados de segurança de aplicações web, o Caido tem sido uma de nossas ferramentas preferidas para descobrir, explorar e documentar vulnerabilidades. Criado para pentesters, pesquisadores de segurança e caçadores de bugs, o Caido é uma alternativa moderna e leve ao Burp Suite, com uma interface amigável sem perder funcionalidades.</p> 

<p style="text-align: justify;">Com funcionalidades voltadas para hacking ético e pentests em aplicações web, o Caido permite fluxos de trabalho eficientes tanto em ambientes manuais quanto semi-automatizados. A capacidade do Caido de interceptar tráfego, mapear a estrutura de sites e gerenciar grandes volumes de requisições HTTP o qualifica para identificar problemas como XSS, CSRF, IDOR, falhas de autenticação e gerenciamento inseguro de sessões.</p> 

<p style="text-align: justify;">Além de sua interface limpa e fluidez, o design do Caido é escalável — tornando-o uma das melhores ferramentas para profissionais de segurança que buscam um scanner e ferramenta de exploração de vulnerabilidades web em nível corporativo para uso em cenários reais. Seja para testar o OWASP Top 10 ou realizar auditorias técnicas profundas, o Caido é um componente essencial do kit de ferramentas de segurança ofensiva no mundo moderno.</p>

### *Interface simples e funcional*

![](interface.png)

<p style="text-align: justify;">O Caido possui uma interface minimalista, moderna e amigável, projetada para facilitar o processo de pentest em aplicações web. Recursos úteis como mapa dinâmico do site, histórico completo de navegação e interceptação em tempo real do tráfego HTTP permitem que pesquisadores de segurança tenham ampla visibilidade sobre a estrutura e operação da aplicação alvo.</p> 

<p style="text-align: justify;">Isso permite identificar vetores de ataque potenciais de forma mais rápida e precisa, fazendo do Caido a solução preferida entre profissionais que buscam uma plataforma fácil de usar e poderosa para exploração de requisições em tempo real, inspeção de parâmetros e detecção de vulnerabilidades. Desde o mapeamento de endpoints complexos até a análise de sessões ao vivo, o Caido otimiza o processo sem comprometer profundidade ou precisão.</p>

### *Automação com "Automate"*

![](automate.png)

<p style="text-align: justify;">O recurso "Automate" do Caido permite que profissionais de segurança configurem e executem varreduras de vulnerabilidade personalizadas com precisão e velocidade. É especialmente útil na automação da detecção de vulnerabilidades comuns em aplicações web, como XSS, CSRF, IDOR e falhas de autenticação ou gerenciamento de sessão.</p> 

<p style="text-align: justify;">Com suporte para automação de testes com scripts e injeção de payloads personalizados, a funcionalidade Automate do Caido reduz significativamente o trabalho manual, mas aumenta a precisão na identificação de falhas de segurança em ambientes web complexos. É uma adição ideal para pentesters e caçadores de bugs que desejam melhorar seus testes com varreduras automatizadas e eficientes adaptadas ao seu escopo.</p>

### *Gerenciamento de projetos*

![](scopes.png)

<p style="text-align: justify;">O Caido oferece suporte a procedimentos eficientes de pentest com a capacidade de trabalhar em vários projetos simultaneamente sem precisar reiniciar o aplicativo. Esse tipo de funcionalidade é essencial para especialistas que conduzem múltiplos testes de segurança ao mesmo tempo, permitindo alternância fácil entre alvos sem comprometer a integridade das informações.</p> 

<p style="text-align: justify;">Para tornar o gerenciamento de campanhas de pentest ainda mais simples, o Caido possui um recurso completo chamado Scopes. Com ele, os usuários podem definir, segmentar e gerenciar escopos de teste múltiplos dentro de um único projeto. Isso é útil para segmentar testes em diferentes domínios, aplicações ou ambientes — melhorando a organização, reduzindo ruídos e apoiando uma análise de vulnerabilidades mais direcionada.</p> <p style="text-align: justify;">Ao combinar a capacidade de múltiplos projetos com testes limitados por escopo, o Caido mantém pentesters, caçadores de bugs e pesquisadores de segurança produtivos, eficazes e concentrados nos bugs mais importantes.</p>

<p style="text-align: justify;">By combining multi-project capability with scope-limited testing via environments, Caido keeps penetration testers, bug bounty hunters, and security researchers productive, effective, and concentrated on the most important bugs.</p>

### *Filtros com HTTPQL*

![](filters.png)

<p style="text-align: justify;">O mecanismo de busca HTTPQL do Caido oferece filtragem precisa e exame minucioso de requisições HTTP, mesmo em tráfego web pesado. Como pesquisador de segurança e pentester, essa linguagem de consulta concisa e direta ajuda você a navegar rapidamente por grandes volumes de dados sem precisar ser um programador experiente.</p> 

<p style="text-align: justify;">Com o HTTPQL, a filtragem avançada de requisições se torna mais fácil de implementar, acelerando a identificação de falhas de segurança como pontos de injeção, erros de autenticação e irregularidades de sessão, tornando-o uma ferramenta essencial para auditorias automatizadas de tráfego web e testes de vulnerabilidades em larga escala.</p> 

<p style="text-align: justify;">O Caido também se destaca ao oferecer recursos de ponta que o tornam mais forte em cenários reais de pentest e auditoria de segurança:</p> 

<p style="text-align: justify;"> 
  <ul> 
    <li><b>Proxy invisível:</b> Captura e salva convenientemente o tráfego de rede de clientes e dispositivos que não suportam configuração manual de proxy. Isso é especialmente útil ao testar softwares embarcados, dispositivos IoT, aplicativos móveis e navegadores bloqueados para análises profundas de segurança em casos difíceis de testar.</li> 
    <li><b>Substituição de DNS:</b> Fornece controle refinado sobre a resolução de nomes de domínio durante testes de segurança, permitindo que pentesters falsifiquem DNS, redirecionem tráfego e criem casos de teste realistas. É essencial para verificar vulnerabilidades relacionadas a DNS, realizar ataques de phishing e analisar vetores complexos de ataque em rede.</li> 
    <li><b>Integração com navegador:</b> Facilita a inspeção instantânea e dinâmica do tráfego HTTP/HTTPS de navegadores modernos, incluindo aqueles fortemente baseados em JavaScript e carregamento dinâmico de conteúdo. A integração melhora a eficiência nos testes de aplicações web altamente interativas, aplicações de página única (SPA) e ambientes de cliente rico, permitindo a detecção de XSS, problemas de autenticação e outros ataques client-side.</li>
  </ul> 
</p>

## Sobre o Grupo CVE-Hunters: Formação, Evolução e Missão

![](repo.png)

<p style="text-align: justify;">O CVE-Hunters é um grupo de pesquisa dedicado à segurança da informação, especializado na descoberta, análise e divulgação responsável de vulnerabilidades em aplicativos de software críticos. Fundado em dezembro de 2024 pelo especialista em segurança cibernética, Professor <a href="https://www.linkedin.com/in/nmmorette">Natan Morette</a>, o grupo começou com apenas quatro alunos apaixonados, ansiosos por aprofundar seus conhecimentos em segurança ofensiva e hacking ético.</p>

<p style="text-align: justify;">Sob a orientação técnica e ética especializada do Professor <a href="https://www.linkedin.com/in/nmmorette">Natan</a>, o CVE-Hunters cresceu e amadureceu de forma constante. Hoje, contamos com orgulho com 10 pesquisadores ativos em segurança cibernética que aplicam as habilidades práticas aprendidas tanto em ambientes acadêmicos quanto em ambientes de laboratório. Nossas principais áreas de foco incluem testes de penetração, avaliação de vulnerabilidades, publicação de CVE e contribuição para o fortalecimento da segurança de projetos de código aberto impactantes com relevância social significativa.</p>

<p style="text-align: justify;">Nosso trabalho de pesquisa e desenvolvimento está em constante evolução. Estamos analisando ativamente novas falhas de segurança, documentando detalhes técnicos e preparando divulgações de vulnerabilidades responsáveis ​​adicionais para a comunidade.</p>

<p style="text-align: justify;">Para saber mais sobre os membros da nossa equipe, explorar nossos projetos em andamento e acompanhar as últimas publicações do CVE, visite nosso repositório oficial do GitHub em: <a href="https://github.com/Sec-Dojo-Cyber-House/cve-hunters">https://github.com/Sec-Dojo-Cyber-House/cve-hunters</a>.</p>

<p style="text-align: justify;">Todas as vulnerabilidades identificadas e CVEs oficialmente publicadas pelo CVE-Hunters são catalogadas de forma transparente e acessíveis em nosso site oficial: <a href="https://sec-dojo-cyber-house.github.io/">https://sec-dojo-cyber-house.github.io/</a>.</p>

## Escrito por

[![](elisangela50x50.png)](https://www.linkedin.com/in/elisangelasilvademendonca/) [Elisangela Mendonça](https://www.linkedin.com/in/elisangelasilvademendonca/)

## Contribuidores

[![](karina50x50.png)](https://www.linkedin.com/in/karina-gante/) [Karina Gante](https://www.linkedin.com/in/karina-gante/)

[![](natan50x50.png)](https://www.linkedin.com/in/nmmorette) [Natan Maia Morette](https://www.linkedin.com/in/nmmorette) 

> *Por: [CVE-Hunters](https://github.com/Sec-Dojo-Cyber-House/cve-hunters)*