<table>
<tr>
<td>
<a href= "https://www.ipt.br/"><img src="https://www.ipt.br/imagens/logo_ipt.gif" alt="IPT" border="0" width="70%"></a>
</td>
<td><a href= "https://www.inteli.edu.br/"><img src="https://www.inteli.edu.br/wp-content/uploads/2021/08/20172028/marca_1-2.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0" width="30%"></a>
</td>
</tr>
</table>

<font size="+12"><center>
Concepção de sistema de automação industrial
</center></font>

>*Observação 1: A estrutura inicial deste documento é só um exemplo. O seu grupo deverá alterar esta estrutura de acordo com o que está sendo solicitado nos artefatos.*

>*Observação 2: O índice abaixo não precisa ser editado se você utilizar o Visual Studio Code com a extensão **Markdown All in One**. Essa extensão atualiza o índice automaticamente quando o arquivo é salvo.*

**Conteúdo**

- [Autores](#autores)
- [Visão Geral do Projeto](#visão-geral-do-projeto)
  - [Empresa](#empresa)
  - [O Problema](#o-problema)
  - [Objetivos](#objetivos)
    - [Objetivos gerais](#objetivos-gerais)
    - [Objetivos específicos](#objetivos-específicos)
  - [Partes interessadas](#partes-interessadas)
- [Análise do Problema](#análise-do-problema)
  - [Análise da área de atuação](#análise-da-área-de-atuação)
  - [Análise do cenário: Matriz de Oceano Azul](#análise-do-cenário-matriz-de-oceano-azul)
  - [Proposta de Valor: Value Proposition Canvas](#proposta-de-valor-value-proposition-canvas)
  - [Matriz de Risco](#matriz-de-risco)
- [Requisitos do Sistema](#requisitos-do-sistema)
  - [Personas](#personas)
  - [Histórias dos usuários (user stories)](#histórias-dos-usuários-user-stories)
- [Arquitetura do Sistema](#arquitetura-do-sistema)
  - [Módulos do Sistema e Visão Geral (Big Picture)](#módulos-do-sistema-e-visão-geral-big-picture)
  - [Descrição dos Subsistemas](#descrição-dos-subsistemas)
    - [Requisitos de software](#requisitos-de-software)
  - [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [UX e UI Design](#ux-e-ui-design)
  - [Wireframe + Storyboard](#wireframe--storyboard)
  - [Design de Interface - Guia de Estilos](#design-de-interface---guia-de-estilos)
- [Projeto de Banco de Dados](#projeto-de-banco-de-dados)
  - [Modelo Conceitual](#modelo-conceitual)
  - [Modelo Lógico](#modelo-lógico)
- [Teste de Software](#teste-de-software)
  - [Testes Unitários](#testes-unitários)
  - [Teste de Usabilidade](#teste-de-usabilidade)
- [Análise de Dados](#análise-de-dados)
- [Manuais](#manuais)
  - [Manual de Implantação](#manual-de-implantação)
  - [Manual do Usuário](#manual-do-usuário)
  - [Manual do Administrador](#manual-do-administrador)
- [Referências](#referências)


# Autores

* [Alberto da Rocha](https://www.linkedin.com/in/alberto-da-rocha-miranda-angrysine/)
* [Bianca Cassemiro](https://www.linkedin.com/in/bianca-cassemiro/)
* [Caio Martins](https://www.linkedin.com/in/caio-m1849/)
* [Igor Garcia](https://www.linkedin.com/in/igor-garcia-126a1823b/)
* [Israel Carvalho](https://www.linkedin.com/in/israel-carvalho-706133241/)
* [Paulo Presa Evangelista](https://www.linkedin.com/in/paulo-evangelista/)
* [Tainara Rodrigues](https://www.linkedin.com/in/tainara-rodrigues-763a42233/)


# Visão Geral do Projeto

## Empresa

O Instituto de Pesquisas Tecnológicas, IPT, é um centro de pesquisa que atua diretamente com diversas indústrias e realiza desenvolvimento de novas ferramentas ou métodos para lidar com os problemas que seus clientes propõem.

## O Problema
O processo de separação magnética realizada pelo IPT é manual e toma o tempo dos funcionários, estes que poderiam estar realizando outras atividades que não a separação de minerais metálicos em uma mistura.

## Objetivos

### Objetivos gerais

Com o objetivo de salientar as dores apresentadas pelo cliente, o tempo despendido com um processo totalmente manual e a necessidade de um profissional treinado para realizar a tarefa, pretende-se conceber uma ferramenta que automatize este processo. 

### Objetivos específicos

Tendo em vista a otimização do tempo dos pesquisadores que trabalham no IPT, o grupo IPTech propõe o desenvolvimento de uma ferramenta que possa automatizar o processo de separação magnética, neste caso será utilizado um braço mecânico acoplado com um microcontrolador, Raspberry Pi Pico W, e atuadores, conjunto de eletroimãs, que irão realizar a tarefa de coletar, lavar e separar os itens de uma mistura. 

## Partes interessadas

* Setor de materiais avançados do IPT
* Inteli

# Análise do Problema

Para fazer a análise do problema, foram utilizados três métodos, a matriz de oceano azul, o Canvas Value Proposition e foi realizado um Workshop com o cliente para conhecer como o processo é feito atualmente. 

Dentre os três métodos supramensionados, aquele que mais se destaca para a compreensão do problema foi o workshop, no qual pudemos conhecer as instalações do cliente e discutir possíveis features e necessidades que este tem em relação a ferramenta que será desenvolvida. 

## Análise da área de atuação

*Descrição_da_análise_da_área_de_atuação*

## Análise do cenário: Matriz de Oceano Azul

![img](https://github.com/2023M5T2-Inteli/grupo2/blob/main/docs/img/project/Matriz-Oceano-Azul.png)

## Proposta de Valor: Value Proposition Canvas

![img](https://github.com/2023M5T2-Inteli/grupo2/blob/main/docs/img/project/Canvas-Value-Propostion-1.png)


## Matriz de Risco

![img](https://github.com/2023M5T2-Inteli/grupo2/blob/main/docs/img/project/Matriz-Risco.png)


# Requisitos do Sistema

1. Um braço mecânico capaz de operar um atuador, eletroimã;

2. Atuador acoplado no braço mecânico, sendo este capaz de alternar a itensidade do campo eletromagnético em uma faixa de 800 a 12000 gauss;

3. Pre-definição do espaço onde o braço mecânico deve atuar respeitando os limites de movimentação do equipamento;

4. Automação do processo de lavagem da mistura no processo de separação;

5. Automatização do processo de pesagem da mistura disponibilizada (opcional);

6. Análise dos processo de automação: taxa de separação, graua de lavabildiade da misutra, etc (opcional).

## Personas

Foram desenvolvidas duas personas referente ao público que se pretende atender com a solução proposta. A primeira persona seria o operário que lida com as tarefas cotidianas, e manuais, do IPT, já a segunda persona é aquela que lida com os materiais que são separados pelo operário. Seguem referenciadas, respectivamente.

![img](https://github.com/2023M5T2-Inteli/grupo2/blob/main/docs/img/project/Persona-Diogo.png)

![img](https://github.com/2023M5T2-Inteli/grupo2/blob/main/docs/img/project/Persona-Fernando.png) 


## Histórias dos usuários (user stories)

![img](https://github.com/2023M5T2-Inteli/grupo2/blob/main/docs/img/project/User-Story.jpg)

# Arquitetura do Sistema

1. Primeira versão da Arquitetura em blocos

![img](https://github.com/2023M5T2-Inteli/grupo2/blob/main/docs/img/project/Aquitetura-por-blocos1.png)

 Alterações feita na arquitetura em blocos
![img](https://github.com/2023M5T2-Inteli/grupo2/blob/main/docs/img/project/Altera%C3%A7%C3%B5es-arquitetura1.png)

2. Segunda versão da Arquitetura em blocos
![img](https://github.com/2023M5T2-Inteli/grupo2/blob/main/docs/img/project/Arquitetura-por-blocos-2.png)

## Módulos do Sistema e Visão Geral (Big Picture)
![img](https://github.com/2023M5T2-Inteli/grupo2/blob/main/docs/img/project/Arquitetura-do-sistema.jpg)

## Descrição dos Subsistemas
| Componente  | Descrição da Função 	|
|---	|---	|
| Magician Lite 	| Braço robótico responsável por segurar os eletroimãs e fazer o transporteda mistura entre os recipien-<br>tes 	|
| Raspberry Pi Pico W 	| Microcontrolador responsável por coordenar as funções do braço robótico. 	|
| Eletroimã 	| Atuador responsável por criar um campo eletromagnético que fará a coleta do material metálico. 	|
| Célula de Carga HX711	| Responsável por fazer o controle de tensão para o eletroimã, de modo a variar o campo eletromagnético. 	|
| Bandeja 	| Serão utilizadas três bandejas, sendo a primeira para despejar a mistura e iniciar a separação via<br>eletroimã, a segunda para fazer a lavagem do material coletado retirando assim as impurezas não metá-<br>licas da mistura e a terceira será utilizada para depositar o material já separado. 	|

## Requisitos de software


## Tecnologias Utilizadas
* Backend-Microcontrolador: Python
* Backend-Aplicação: Flask, Python 
* Frontend: TypeScript, Next.js, CSS

# UX e UI Design

## Wireframe + Storyboard

## Design de Interface - Guia de Estilos


# Projeto de Banco de Dados

## Modelo Conceitual

## Modelo Lógico


# Teste de Software

## Testes Unitários

## Teste de Usabilidade


# Análise de Dados


# Manuais

## Manual de Implantação

## Manual do Usuário

## Manual do Administrador


# Referências
