# Web bot Sherlockcups Project 

Titulo: Sherlockcups 

Descrição: Web bot com a função de trazer dados referentes ao preço de bebidas em sites na web.

## Introdução

A ideia do projeto surgiu com base em outros Web Bots que informam preços de alimentos para o usuário. Assim, pensamos: "Porque não um Web Bot 
faça uma raspagem de dados trazendo preços de cervejas?", após detectar essa brecha no mercado, analisamos com cuidado a problemática. 
Percebemos que cerveja era algo muito específico e que não teríamos fontes suficientes para extrair os dados necessários. 
Levando esse fator em consideração, decidimos abrangir o leque de opções para bebidas no geral. 
Posteriormente, tinhamos que pensar em um nome que transmitisse o que o Bot faz de forma objetiva, durante um brainstorm de ideias chegamos ao nome Sherlokcups.
Sherlocups faz referência ao famoso detetive Sherlock Holmes cuja origem é do Reino Unido, e "cups" vem de "copos" da lingua inglesa. 
Achamos o trocadilho apropriado, levando em consideração que o ojetivo do Bot é vasculhar a internet em busca de preços de bebidas.  
E assim o Sherlockcups nasceu! O Web Bot terá como publico alvo, consumidores que gostam de apreciar cerveja ou qualquer bebida especifica (ou seja, todo mundo!) 
Porém, com um preço acessivel (até porque não está fácil para ninguem, não é mesmo?). 
A função do Web Bot nada mais é do que coletar inputs dos usuários, usar esses inputs para fazer uma pesquisa na web, e posteriormente, coletar os resultados e exibi-los para o usuário.
Ele será programado ultilizando a linguagem de programação Python juntamente com o Selenium, que irá simular as ações de um usuário na internet.

![](Sherlock_rev1.png)

# De que modo os dados serão exibidos para o usuário?

interface:
*substantivo feminino*
1. elemento que proporciona uma ligação física ou lógica entre dois sistemas ou partes de um sistema que não poderiam ser conectados diretamente.

Uma Interface é necessária para estabelecer a comunicação entre usuário e sistema. 
Atualmente, estamos em busca de aperfeiçoar a Interface do Sherlockups, deixando-a atrativa e intuitiva para que nosso usuário consiga de forma prática, utilizar nossos serviços.

# Por quê Python?

Optamos por Python, pois além de ser a primeira Linguagem de Programação que iremos aprender na faculdade (o que acaba nos resultando uma via dupla de aprendizado), 
Python também é uma linguagem dinâmica, interpretada, multiplataforma, orientada à objetos, funcional, refletiva e imperativa.
Podendo ser usada na construção de sistemas Web com Django, Flask, Pyramid, etc. Lançada em 1991 por Guido van Rossum,  é uma linguagem livre e hoje pode-se programar para desktops, web e mobile.
O nome Python foi inspirado na cobra Python, grupo humorístico britânico criador do programa Monty Python’s Flying Circus.

# O que é Selenium?

Selenium Webdriver é uma ferramenta que oferece uma API (*Application Programming Interface*) que permite a escrita de forma mais produtiva e organizada de scripts de testes, permitindo assim, ao usuário 
reproduzi-los rapidamente no ambiente real da aplicação.
Optamos pelo Selenium pois ele suporta a maioria dos navegadores web existentes.

# Django. Quem??

Lançado em 2005, o Django foi desenvolvido inicialmente como um sistema de gerenciamento de um site jornalístico. Tem como seus co-criadores os desenvolvedores Adrian Holovaty e Simon Willison. 
A escolha do nome “Django” foi inspirado no músico de jazz Django Reinhardt, considerado um dos melhores e mais influentes guitarristas de todos os tempos. 

Django é um framework para aplicações web de código aberto. 
Temos como objetivo o utilizarmos para desenvolver nossa página na web, para que assim, nosso Bot possa ser acessado por qualquer máquina provida de internet. 

## Framework:

Um web framework é um conjunto de bibliotecas ou componentes que são usados para criar uma base onde sua aplicação será construída.
Sendo que, Frameworks ajudam no desenvolvimento rápido e seguro de aplicações.

### Como Django funciona?

Quando uma requisição chega a um servidor web, ela é passada para o Django. Primeiro, ele pega um endereço de página web e tenta descobrir o que fazer. 
Parte desse trabalho é feito pelo urlresolver do Django que formula uma lista de padrões e tenta achar em qual deles a URL se encaixa.
O Django checa a lista de cima pra baixo, e se algum padrão é encontrado, ele passa a requisição para a função associada que é chamada de "view".

Uma view é uma função manipuladora de solicitações, que recebe solicitações HTTP e retorna respostas HTTP.
As views acessam os dados necessários para satisfazer solicitações por meio dos "models" que são objetos em Python que definem a estrutura dos dados de um aplicativo
e fornecem mecanismos para gerenciar e consultar registros no banco de dados.
A partir daí a view gera uma resposta e o Django pode enviá-la para o navegador web do usuário através do "template".

# MongoDB 
## Nosso próprio Banco de Dados.

Este Banco de Dados tem como característica seu código-fonte aberto licenciado pela GNU AGPL (Affero General Public License), ele possui alta performance, 
é escrito em C++, é multiplataforma e formado por um conjunto de aplicativos JSON. Apesar do projeto MongoDB ter iniciado em 2007 o Banco de Dados somente foi concluído em 2009, lançando assim,
a primeira versão do MongoDB. Diversas linguagens e plataforma já possuem drivers para o MongoDB, entre elas destacam-se: C, C#, C++, Haskell, Java, JavaScript, Perl, PHP, Python, Ruby e Scala. 
Além disso, o MongoDB possui binários para diversas plataformas como Windows, Mac OS X, Linux e Solaris. Optamos por sua utilização, para termos melhor controle sobre os dados dos produtos armazenados, 
para que assim, o nosso cliente possa fazer um comparativo de preço com dias anteriores. Legal não?

# Qual o objetivo principal do Sherlockcups?
## Facilitar a vida do usuário!

Estudos recentes apontam que o consumidor esta cada vez menos disposto a sair de casa em busca dos seus produtos.
O fator responsável por essa brusca mudança? A Internet. De acordo com uma pesquisa realizada pela Connected Life, com mais de 60 mil consumidores em 50 países, 
cerca de 7 a cada 10 brasileiros (68%) realizam pesquisas online antes de efetuar a compra em lojas físicas, enquanto 74% preferem comprar pela internet. 
O consumidor tem optado cada vez mais pelo uso da internet como meio de fazer suas compras. 
Um estudo realizado pela CNDL (*Confederação Nacional de Dirigentes Lojistas*), e pelo SPC Brasil (*Serviço de Proteção ao Crédito*) 
avaliou o comportamento do usuário em relação aos e-commerces.

A pesquisa considerou o período de 12 meses e comparou os consumidores que realizaram compras pela internet com os que compraram seus produtos em lojas físicas.
O estudo concluiu que quase 50% dos consumidores procuram fontes de preço online antes de efetuar a compra do objeto em uma loja física. 
Essa parcela da população é levada por algumas motivações:
* 38% desejam realizar pesquisa de preço;
* 22% buscam mais informações com relação ao produto;
* 10% querem saber a opinião de outros consumidores.

Com nosso Bot, pretendemos facilitar a vida desses 38% de brasileiros.

Fontes: <https://exame.abril.com.br/negocios/dino/757-das-pessoas-pesquisam-precos-on-line-antes-de-fazer-uma-compra-segundo-levantamento/>
<https://www.ecommercebrasil.com.br/noticias/estudo-jovens-compra-online/>


# Agora, para quem quiser conhecer mais afundo nossos serviços, desenvolvemos um tutorial para simulação.

# Usuário Teste Para Ambiente Windows

# Bem Vindo!
Somos o SherlockCups, o melhor jeito de encontrar a sua bebida online!

# Objetivo:
Buscamos oferecer aos nossos usuários uma maneira simples e rápida de obter bebidas variadas, sem cobranças pelo serviço.

# Usuário Teste:
Como um usuário de teste, convidamos a esta experiência para poder entender os nossos métodos e gostaríamos de sua opinião sobre o nosso trabalho, todas críticas consrutivas são bem vindas para o nosso aprimoramento!!!!

## Pré Requisito Funcional:
Ter a vesão do windows 8 ou superior
Instalar o programa [Python](https://www.python.org/downloads/)  (Observação: ao instalar guardar o endereço de instalação do programa)
Instalar o programa [Pycharm](https://www.jetbrains.com/pycharm/download/#section=windows)

## Siga os Passos abaixo:

### Acessar o Repositório

01. Acessar o repositório do projeto; 
02. Executar o comando git clone https://gitlab.com/gof-webbot/projetowebbot;
03. Executar na raiz do projeto o comando: python manage.py runserver;
04. Abrir o navegador e acessar a página do localhost http://localhost:8000/;

### Acessar o Programa Python
06. Acessar o caminho raiz do python;
07. Acessar pasta python37-32>scripts;
08. Copiar o caminho da barra de endereço;
09. Acessar o Painel de Controle > sistema de segurança>sistema>configurações avançadas do sistema;
10. Clicar em “variáveis de ambiente”;
11. Encontrar a variável “path” e clicar em editar;
12. Clicar no ícone “novo”;
13. Adicionar o caminho copiado do python e clicar em ok;

### Atualização do Chrome
14. Acessar o Chrome;![](Chrome_1.jpg)
15. Atualizar o Chrome > configurações > sobre o chrome> atualizar;
16. Identificar a versão do Chrome;
17. Baixar chromeDriver conforme a versão marcada e sistema operacional (https://chromedriver.chromium.org/downloads);
18. Descompactar o chromeDriver;
19. Acessar a pasta e copiar o endereço;
20. Adicionar o endereço na variável de ambiente Path, como foi realizado no endereço do Python;

### Command Prompt
21. Acessar o CMD (Através do ícone iniciar do menu);
22. Executar  o comando “pip install selenium”;
23. Executar o comando “pip install django”;
24. Acessar  o caminho do programa em sua máquina, até encontrar o arquivo executável “manage.py”;
25. Copiar o endereço e colar no CMD;
26. Executar o comando “python manage.py runserver”.

======================================================================

# Usuário Teste Para Ambiente Linux - Ubuntu

## Pré Requisito Funcional:
* Ter a versão atualizada Ubuntu 18.04 ou superior.
* Ubuntu já inclui Python. Você pode confirmar sua versão rodando o seguinte comando no seu terminal: python3 -V.
* Caso sua versão for inferior a 3.8, atualize utilizando os seguintes passos:


<em>1- Baixar: [Python](https://www.python.org/downloads/)  
2- sudo tar xzf Python-3.8.0.tgz
3- cd Python-3.8.0
4- sudo ./configure --enable-optimizations
5- sudo make altinstall<em>
 

* Instalar a biblioteca Django rodando o comando: sudo apt install python3-pip no seu terminal.
* Posteriormente execute: sudo pip3 install virtualenvwrapper.


## Siga os Passos abaixo:

### Acessar o Repositório
1. Acessar o repositório do projeto; 
2. Abrir o Terminal; 
3. Executar o comando git clone https://gitlab.com/gof-webbot/projetowebbot;
4. Executar na raiz do projeto o comando: python manage.py runserver;
5. Abrir o navegador e acessar a página do localhost http://localhost:8000/;


### Atualização do Chrome e Instalação do ChromeDriver:
#### Instalando o Chrome.
No seu terminal execute a sequencia de comandos:
1. sudo curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add;
2. sudo echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list;
3. sudo apt-get -y update;
4. sudo apt-get -y install google-chrome-stable;

#### Instalando o ChromeDriver.
Agora para instalar o ChromeDriver:
1. wget -N http://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip -P ~/;
2. unzip ~/chromedriver_linux64.zip -d ~/;
3. rm ~/chromedriver_linux64.zip;

#### Para definir as variavéis de ambiente:

1. sudo mv -f ~/chromedriver /usr/local/bin/chromedriver;
2. sudo chown root:root /usr/local/bin/chromedriver;
3. sudo chmod 0755 /usr/local/bin/chromedriver;

### Comandos do Prompt
1. Acessar o Terminal;
2. Executar  o comando “pip install selenium”;
3. Executar o comando “pip install django”;
4. Acessar  o caminho do programa em sua máquina, até encontrar o arquivo executável “manage.py”;
5. Copiar o endereço e colar no Terminal;
6. Executar o comando “python manage.py runserver”.

Pronto!! Você já pode utilizar os serviços do primeiro Web Bot de bebidas do Brasil! :sunglasses: