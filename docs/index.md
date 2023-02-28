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

> _Observação 1: A estrutura inicial deste documento é só um exemplo. O seu grupo deverá alterar esta estrutura de acordo com o que está sendo solicitado nos artefatos._

> _Observação 2: O índice abaixo não precisa ser editado se você utilizar o Visual Studio Code com a extensão **Markdown All in One**. Essa extensão atualiza o índice automaticamente quando o arquivo é salvo._

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
- [Arquitetura do Sistema Lembrar aqui](#arquitetura-do-sistema-lembrar-aqui)
  - [Módulos do Sistema e Visão Geral (Big Picture)](#módulos-do-sistema-e-visão-geral-big-picture)
  - [V1](#v1)
  - [Descrição dos Subsistemas](#descrição-dos-subsistemas)
  - [Requisitos de software](#requisitos-de-software)
  - [Tecnologias Utilizadas](#tecnologias-utilizadas)
  - [Testes de atuadores, sensores e do microcontrolador](#testes-de-atuadores-sensores-e-do-microcontrolador)
    - [Braço Robótico](#braço-robótico)
    - [Eletroimã](#eletroimã)
    - [Bomba de água](#bomba-de-água)
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

- [Alberto da Rocha](https://www.linkedin.com/in/alberto-da-rocha-miranda-angrysine/)
- [Bianca Cassemiro](https://www.linkedin.com/in/bianca-cassemiro/)
- [Caio Martins](https://www.linkedin.com/in/caio-m1849/)
- [Igor Garcia](https://www.linkedin.com/in/igor-garcia-126a1823b/)
- [Israel Carvalho](https://www.linkedin.com/in/israel-carvalho-706133241/)
- [Paulo Presa Evangelista](https://www.linkedin.com/in/paulo-evangelista/)
- [Tainara Rodrigues](https://www.linkedin.com/in/tainara-rodrigues-763a42233/)

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

- Setor de materiais avançados do IPT
- Inteli

# Análise do Problema

Para fazer a análise do problema, foram utilizados três métodos, a matriz de oceano azul, o Canvas Value Proposition e foi realizado um Workshop com o cliente para conhecer como o processo é feito atualmente.

Dentre os três métodos supramensionados, aquele que mais se destaca para a compreensão do problema foi o workshop, no qual pudemos conhecer as instalações do cliente e discutir possíveis features e necessidades que este tem em relação a ferramenta que será desenvolvida.

## Análise da área de atuação

_Descrição*da_análise_da*área_de_atuação_

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

# Arquitetura do Sistema Lembrar aqui

1. Primeira versão da Arquitetura em blocos

![img](https://github.com/2023M5T2-Inteli/grupo2/blob/main/docs/img/project/Aquitetura-por-blocos1.png)

Alterações feita na arquitetura em blocos

Ao concluir a testagem com as células de carga, não conseguimos chegar a uma conclusão especificamente, visto que, o equipamento de pesagem não funcionou como esperávamos. Em vista disso, recorremos a uma nova arquitetura do sistema, retirando a célula de carga e possibilitando uma construção mais compacta para a solução, tendo apenas uma função principal de separação dos materiais com o uso dos eletroímãs.

![img](https://github.com/2023M5T2-Inteli/grupo2/blob/main/docs/img/project/Altera%C3%A7%C3%B5es-arquitetura1.png)

2. Segunda versão da Arquitetura em blocos

![img](https://github.com/2023M5T2-Inteli/grupo2/blob/main/docs/img/project/Arquitetura-por-blocos-2.png)

## Módulos do Sistema e Visão Geral (Big Picture)

## Descrição dos Subsistemas

| Componente            | Descrição da Função                                                                                                                                                                                                                                                                                |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Magician Lite         | Braço robótico responsável por segurar os eletroimãs e fazer o transporteda mistura entre os recipien-<br>tes                                                                                                                                                                                      |
| Raspberry Pi Pico W   | Microcontrolador responsável por coordenar as funções do braço robótico.                                                                                                                                                                                                                           |
| Eletroimã             | Atuador responsável por criar um campo eletromagnético que fará a coleta do material metálico.                                                                                                                                                                                                     |
| Célula de Carga HX711 | Responsável por fazer o controle de tensão para o eletroimã, de modo a variar o campo eletromagnético.                                                                                                                                                                                             |
| Bandeja               | Serão utilizadas três bandejas, sendo a primeira para despejar a mistura e iniciar a separação via<br>eletroimã, a segunda para fazer a lavagem do material coletado retirando assim as impurezas não metá-<br>licas da mistura e a terceira será utilizada para depositar o material já separado. |

## Requisitos de software

## Tecnologias Utilizadas

- Backend-Microcontrolador: Python
- Backend-Aplicação: Flask, Python
- Frontend: TypeScript, Next.js, CSS

## Testes de atuadores, sensores e do microcontrolador

### Braço Robótico

Um dos primeiros testes realizados foi sobre o alcance do braço, que apresentou um ângulo de rotação de um pouco menos que 180 graus. Além disso, o robô apresentou uma boa capacidade de alcance na horizontal, podendo alcançar áreas maiores do que o tamanho da bandeja utilizada nos testes. Já na vertical, o robô conseguiu alcançar a bandeja sem problemas.

Durante os testes, no entanto, houve momentos em que o robô travou ao tentar movimentá-lo além do seu alcance, tornando-se incapaz de se mover após isso. Esse tipo de limitação é importante para ser levado em consideração em aplicações futuras do robô. Não fomos capazes de identificar como corrigir o erro sem desligar e ligar denovo o robo.

Outro aspecto observado nos testes foi o delay de alguns segundos após a execução do código para o braço robótico se movimentar. Esse delay pode ser relevante em situações que exigem uma resposta rápida do robô, porém, acreditamos que isso não impactará nosso projeto.

Além disso testes com a garra mostraram que apesar da garra facilmente pegar o imâ existem momentos em que o imã escorrega caindo da garra quando ela se move muito rápido.
[vídeo do braço carregando imã](https://github.com/2023M5T2-Inteli/grupo2/blob/main/docs/v%C3%ADdeos/bra%C3%A7o%20levantando%20im%C3%A3.mp4)

### Eletroimã

Além do teste que realizamos da garra levantando imã (citado na seção acima) realizamos um teste para medir a capacidade magnética do ima. Ligamos o imã a uma fonte de voltagem variável e fomos gradativamente aumentando a voltagem. Percebemos que quanto maior a voltagem maior a capacidade de captação do ima. Magnetizamos moedas pois sabendo o peso das moedas poderemos estimar a massa de metal que o imã é capaz de reter (ainda não realizamos esse cálculo). Concluimos também que a forma como os metais se acumulam no imã impacta a massa que ele consegue segurar, já que se o material for depositado no sentido horizontal ele afeta o impacto di imã negativamente já que o campo magnético é inversamente proporcional a distância por isso deve-se botar o material na vertical.
[vídeo do imã sendo testado](https://github.com/2023M5T2-Inteli/grupo2/blob/main/docs/v%C3%ADdeos/testes%20im%C3%A3.mp4)

### Bomba de água

Foram realizados teste com a bomba e percebemos que ele foi capaz de agitar a água, porém chegamos a conclusão de que quando o material for disperso na água a chance da bomba não atuar de forma similar ao nossos teste é grande. Logo, mais testes devem ser realuzados

# UX e UI Design

## Wireframe + Storyboard
O front end a ser desenvolvido é um website utilizando o framework Next JS, que permitirá ao usuário acessar as principais funcionalidades do projeto. O website terá um design claro e minimalista, com uma interface de usuário intuitiva para facilitar a interação do usuário com as funcionalidades.
O website apresentará um controle para o braço robótico, permitindo ao usuário selecionar as diferentes posições e movimentos que o braço deve realizar. Essas opções estarão disponíveis em botões, dropdowns ou outras formas de interação, dependendo do design escolhido para o projeto.
Além disso, o usuário terá a opção de executar e salvar a rota selecionada, permitindo assim que possa ser usada posteriormente, sem precisar ser reconfigurada novamente.
Outra funcionalidade importante presente no front end será o controle de intensidade de imã. Este controle permitirá ao usuário ajustar a intensidade do ímã utilizado no braço robótico. Isso pode ser útil em diferentes situações, dependendo das necessidades específicas do usuário.
No geral, o objetivo do front end é tornar as funcionalidades do projeto acessíveis e fáceis de usar para o usuário, com um design minimalista e intuitivo que permita ao usuário realizar suas tarefas com eficiência e eficácia.

<img width="458" alt="Captura de tela 2023-02-23 133458" src="https://user-images.githubusercontent.com/99203402/221928794-ede07ddc-7292-4b67-9094-52fca4abd952.png">


<img width="458" alt="Captura de tela 2023-02-23 133522" src="https://user-images.githubusercontent.com/99203402/221929093-dc13fac2-6f54-4179-a820-b23311bec384.png">

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
