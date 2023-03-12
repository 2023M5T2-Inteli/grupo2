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
- [Materiais e métodos da fabricação dos dispositivos eletrônicos e mecânicos](#arquitetura-do-sistema-lembrar-aqui)
  - [Funcionamento dos dispositivos mecânicos](#Funcionamento-dos-dispositivos-mecânicos)
  - [Dispositivos eletrônicos fabricados](#Dispositivos-eletrônicos-fabricados)
  - [Método de fabricação dos dispositivos eletrônicos](#Método-de-fabricação-dos-dispositivos-eletrônicos)
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

Ao fenalizar a testagem com as células de carga, foi possível concluir que não o equipamento de pesagem não funcionou como o esperado. Em vista disso, recorremos a uma nova arquitetura do sistema, retirando a célula de carga e possibilitando uma construção mais compacta para a solução, tendo apenas uma função principal de separação dos materiais com o uso dos eletroímãs.

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
[vídeo do braço carregando imã](https://drive.google.com/file/d/1U3UM0020-NH9rNW-j4T8iVwKVBouk3X4/view?usp=sharing)

### Eletroimã

Além do teste que realizamos da garra levantando imã (citado na seção acima) realizamos um teste para medir a capacidade magnética do ima. Ligamos o imã a uma fonte de voltagem variável e fomos gradativamente aumentando a voltagem. Percebemos que quanto maior a voltagem maior a capacidade de captação do ima. Magnetizamos moedas pois sabendo o peso das moedas poderemos estimar a massa de metal que o imã é capaz de reter (ainda não realizamos esse cálculo). Concluimos também que a forma como os metais se acumulam no imã impacta a massa que ele consegue segurar, já que se o material for depositado no sentido horizontal ele afeta o impacto di imã negativamente já que o campo magnético é inversamente proporcional a distância por isso deve-se botar o material na vertical.
[vídeo do imã sendo testado](https://drive.google.com/file/d/1GvG1zHHmeROZmBOhi5rblqbd3_31_6Tq/view?usp=share_link)

### Bomba de água

Foram realizados teste com a bomba e percebemos que ele foi capaz de agitar a água, porém chegamos a conclusão de que quando o material for disperso na água a chance da bomba não atuar de forma similar ao nossos teste é grande. Logo, mais testes devem ser realizados.

# Materiais e Métodos da Fabricação dos Dispositivos Eletrônicos e Mecânicos

## Dispositivos eletrônicos fabricados
Foram fabricados:
 - 4 eletroimãs, cada par ligado em paralelo para utilização dos dois canais da ponte H.
 - Ponte H, utilizada para possibilitar a inversão do campo magnético nos eletroimãs utilizados.
 - PCB, que contém raspberry PI e a ponte H, devidamente soldados, que permitem a ativação e inversão da ponte H pelo microcontrolador.

## Método de fabricação dos dispositivos eletrônicos
  - Foram soladados, em paralelo, 2 eletroimãs em cada uma das duas saídas da ponte H.
  - Foi anexada à ponte H dois cabos para a possibiidade de conexção com uma fonte de 12 V e com o GND do Raspberry Pi Pico W.
  - O Raspberry Pi Pico W, que está conectado a um computador, tem mais 4 ligações com a ponte H, a fim de controlar a polariadade de suas saídas.

## Funcionamento dos dispositivos mecânicos
Ao ser energizado, o Raspberry Pi Pico W atua de acordo com seu código de operação, assim ativando as ligações com a ponte H. Isso fará com que os eletroimãs proporcionem campos magnéticos. Em um dado momento, o microcontrolador fará a ponte H inverter a polaridade de suas saídas, criando assim um pequeno campo invertido nos imãs em relação ao anterior, e imediatamente depois o rasberry vai os desligar, resultando na desativação pretendida do magnetismo no eletroimã.

## Esquemático descritivo dos dispositivos eletrônicos fabricados:
O esquemático descritivo das conexões foi feito utilizando o software EasyEDA, contendo os componentes, ponte h e o módulo de carga HX711, e as respectivas portas utilizadas para conectá-los ao Raspberry Pi Pico W. Este esquemático pode ser visto abaixo. 
![img](https://github.com/2023M5T2-Inteli/grupo2/blob/main/docs/diagrama/SCHEMA-PROJETO-1.png) 

Com o esquemático pronto, produzimos o PCB do diagrama utilizando o software supracitado, EasyEDA, de modo a compreender como os componentes estariam dispostos em uma placa, como pode ser observado abaixo. 

![img](https://github.com/2023M5T2-Inteli/grupo2/blob/main/docs/diagrama/PCB-PROJETO-1.png)
# UX e UI Design

## Wireframe + Storyboard
O front end a ser desenvolvido é um arquivo executável criado em Python utilizando a biblioteca PySimpleGUI, que permitirá ao usuário acessar as principais funcionalidades do projeto de forma fácil e intuitiva. O aplicativo apresentará a funcionalidade de executar e salvar a rota selecionada, permitindo assim que possa ser usada posteriormente, sem precisar ser reconfigurada novamente. Além disso, o usuário poderá controlar a intensidade do ímã utilizado no braço robótico por meio de um controle deslizante. Isso pode ser útil em diferentes situações, dependendo das necessidades específicas do usuário.

Uma das vantagens de utilizar um aplicativo .exe é que ele pode fazer o controle do robô sem acesso à internet, além de que pode ser facilmente utilizado em diversos dispositivos sem precisar instalar dependências adicionais, o que facilita o uso e distribuição do projeto. O objetivo do aplicativo é tornar as funcionalidades do projeto acessíveis e fáceis de usar para o usuário, podendo ser executado no mais básico dos computadores e notebooks, contando com um design minimalista e intuitivo que permita ao usuário realizar suas tarefas com eficiência e eficácia.

<img width="296" alt="Captura de tela 2023-03-08 171918" src="https://user-images.githubusercontent.com/99210055/223841450-2c107631-9f8d-4472-a3dc-713380fda4ea.png">

# Detalhamento da interface
Ao programa ser executado, é possível observar a interface apresentada na imagem acima. A função dos botões será descrita abaixo:
"Iniciar Ensaio" -> Executa a rotina de ensaio padrão. O robô percorre pelas 3 bandejas, de forma preestabelecida. Por enquanto, esse ensaio padrão não pode ser modificado pelo usuário.
"Salvar novo ciclo" -> A cada clique nesse botão, a posição do robô atual é salva em um banco de dados. Após salvar toda a rota desejada, é possível que ela seja executada. (O botão de executar as rotas salvas pelo usuário ainda não foi implementao, mas é algo planejado para a próxima sprint)

Para fechar o progama, basta clicar no botão X, no canto superior direito da guia, bem como em qualquer programa.

OBS.: Esta interface ainda está em estági ode desenvolvimento, e será aprimorada conforme as próximas sprints, e necessidades que surgirem.


## Design de Interface - Guia de Estilos
Nossa interface é desenvolvida utilizando várias rows com elementos contidos nelas. Os elementos são minimalistas, com ícones destacados e instruções simples.
Além disso, são utilizadas imagens para incrementar a interface. A fonte utilizada é "Mont Serrat", e a paleta de cores utiliza as cores padrão do IPT.


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
