# Avaliando o Buzz de Issues do GitHub no StackOverflow

## 1. Introdução

GitHub e StackOverflow são plataformas amplamente utilizadas no desenvolvimento de software moderno. Apesar de possuírem objetivos distintos (a primeira preocupa-se com hospedagem e compartilhamento de código aberto, enquanto a segunda destina-se à discussão de dúvidas de programação), ambas são frequentemente adotadas de maneira complementar pelos desenvolvedores. Entre os serviços mais populares disponibilizados pelo GitHub, o gerenciamento de issues através do seu issue tracker apresenta-se como ferramenta eficaz na solução e discussão de problemas mais comuns. Neste laboratório, vamos avaliar se a discussão de issues nos repositórios mais populares do GitHub se refletem em perguntas e repostas relacionadas no StackOverflow.

## 2. Metodologia

### 2.1. Seleção de GitHub Issues

Para formação do dataset de issues a serem avaliadas neste estudo, você deverá, inicialmente, definir o conjunto de repositórios que pretende estudar, segundo algum critério que achar mais interessante. Por exemplo: os mil repositórios mais populares do GitHub, ou os top-10 mais populares de algumas linguagens de programação específicas.

Lembre-se que a definição de um dataset deve amenizar ameaças à validade relacionadas à generalização dos seus resultados. Neste caso, escolha um subconjunto de repositórios que seja interessante para o estudo e minere as suas issues a partir da API GraphQL do GitHub.

### 2.2. Identificação de SO Posts

A partir do conjunto de issues selecionadas, é necessário que identifiquemos a ocorrência da discussão dessas issues em posts do StackOverflow. Para tanto, você pode escolher entre duas técnicas sugeridas (ou propor uma nova):

* Identificar no título das issues palavras chave específicas, que indiquem qual parte do código está sendo discutido (por exemplo, a partir de exepressões regulares que incluam o padrão camelcase). Para cada módulo identificado nas issues, buscar no dump do StackOverflow perguntas que possuam referência a eles, numa janela de tempo próxima à criação da issue.

* Buscar pelo código das issues (string: "Issue #CODIGO") no dump do StackOverflow. Neste caso, adicione também o nome e o onwer do repositório na sua consulta, para garantir que a issue pesquisada é referente ao repositório analisado.

**Atenção:** No relatrio final, você deve indicar e justificar a abordagem escolhida. Apresente os resultados obtidos com esta mineração.

### 2.3. Definição de Questões de Pesquisa

Inicialmente, este laboratório tem o objetivo de responder:

**RQ 01:** Com que frequência issues do GitHub são discutidas no StackOverflow?

**RQ 02:** Qual o impacto das discussões de issues do GitHub no StackOverflow?

**RQ 03:** Existe alguma relação entre a popularidade dos repositórios e o buzz gerado?

**Atenção:** três questões de pesquisa adicionais devem ser adicionadas pelo grupo (Sprint 01).

### 2.4. Definição de Métricas

Para cada questão de pesquisa, as seguintes métricas serão calculadas:  

* **RQ 01:** total de perguntas relacionadas _(PostType: Question)_

* **RQ 02:** total de repostas / total de perguntas relacionadas _(PostTypes: Answer / Question)_

* **RQ 03:** número de estrelas vs total de perguntas relacionadas

**Atenção:** defina as métricas necessárias para responder às questões de pesquisa definidas pelo grupo e discuta no relatório final.

## 3. Ameaças à Validade

De acordo com a metodologia escolhida e a estratégia adotada para selecionar os Posts no SO, discuta as ameaças a validade do seu trabalho, dividindo-as em validade de construção, interna e externa. Discuta cada uma delas e aponte abordagens que você adotou (ou poderia ter adotado) para mitigar essas ameaças.

## 4. Relatório Final

Elabore um documento que apresente (i) uma introdução simples com hipóteses informais; (ii) as questões de pesquisa investigadas; (iii) a metodologia que você utilizou para respondê-las; (iv) os resultados obtidos; (v) a discussão sobre o que você esperava como resultado (suas hipóteses) e os valores obtidos; (vi) as ameaças à validade do seu estudo.  

## 5. Processo de Desenvolvimento

Utilize as tags em negrito (**LabXXSYY**) para identificar as entregas deste laboratório. 

### 5.1. Sprints

**Lab02S01**: Criação das questões de pesquisa e definição do dataset (documento de texto descrevendo as RQs escolhidas, as métricas associadas e o dataset a ser analisado) | **Prazo:** 30/04 | **Valor:** 3 pontos

**Lab02S02**: Coleta de issues (arquivo .csv contendo as issues do dataset definido) | **Prazo:** 07/05 | **Valor:** 7 pontos

**Lab02S03**: Mineração do StackOverflow (consulta dos posts no StackOverflow + valores das métricas do estudo) | **Prazo:** 14/05 | **Valor:** 7 pontos

**Lab02S04**: Relatório final (incluindo a seção de ameaças à validade). | **Prazo:** 21/05 | **Valor:** 13 pontos

### 5.2. Prazos e Avaliação

Este laboratório deve ser desenvolvido em dupla. Para tanto, responda [esta issue](https://github.com/xavierlaerte/labex-20.1/issues/10), apontando a dupla com quem irá trabalhar e o repositório que será utilizado nas Sprints.

**Prazo final:** 21/05 | **Valor total:** 30 pontos | **Desconto de 0.5 pontos por dia de atraso**

### 5.3. Material de Apoio

1. [Slides de Apresentação do Lab](https://github.com/xavierlaerte/labex-20.1/blob/master/geral/Lab03%20-%20Avaliando%20o%20Buzz%20de%20issues%20do%20Github%20no%20StackOverflow.pdf)
2. [Mineração de StackOverflow](https://github.com/xavierlaerte/labex-20.1/blob/master/geral/Lab03%20-%20stackoverflow%20api.pdf)
3. [Visualização de Dados]()
