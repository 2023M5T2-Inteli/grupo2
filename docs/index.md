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
- [Arquitetura do Sistema](#arquitetura-do-sistema)
  - [Módulos do Sistema e Visão Geral (Big Picture)](#módulos-do-sistema-e-visão-geral-big-picture)
  - [V1](#v1)
  - [Descrição dos Subsistemas](#descrição-dos-subsistemas)
  - [Requisitos de software](#requisitos-de-software)
  - [Tecnologias Utilizadas](#tecnologias-utilizadas)
  - [Testes de atuadores, sensores e do microcontrolador](#testes-de-atuadores-sensores-e-do-microcontrolador)
    - [Braço Robótico](#braço-robótico)
    - [Eletroimã](#eletroimã)
    - [Bomba de água](#bomba-de-água)
- [Materiais e métodos da fabricação dos dispositivos eletrônicos e mecânicos](#arquitetura-do-sistema)
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

Além disso, para estarmos cientes dos possíveis riscos durante o desenvolvimento do projeto, e para que tenhamos alguma forma de combatê-los, desenvolvemos também uma matriz de riscos. Os riscos descritos na matriz foram estudados pela aquipe, para que não venham a acontecer ou possam ser remediados.

Dentre os três métodos de entendimento do projeto, aquele que mais se destaca para a compreensão do problema foi o workshop, no qual pudemos conhecer as instalações do cliente e discutir possíveis features e necessidades que este tem em relação a ferramenta que será desenvolvida. As informações obtidas durante o workshop estão diluídas nas três análises documentadas abaixo.

## Análise da área de atuação

_Descrição*da_análise_da*área_de_atuação_

## Análise do cenário: Matriz de Oceano Azul

![img](https://github.com/2023M5T2-Inteli/grupo2/blob/main/docs/img/project/Matriz-Oceano-Azul.png)
Com a matriz de oceano azul, é possível obserar onde nosso protótipo tem seu destaque e qual seu diferencial. Através dele, podemos criar muitos ganhos para o cliente, e diferenciá-lo da concorrência. Reduzimos ou eliminamos o que não julgamos tão importante, e elevamos e criamos os ganhos e diferenciais.
## Proposta de Valor: Value Proposition Canvas

![img](https://github.com/2023M5T2-Inteli/grupo2/blob/main/docs/img/project/Canvas-Value-Propostion-1.png)
Aliada à matriz anterior, o value proposition canvas permite observar quais serão os ganhos obtidos com o uso do protótipo, quais as dores serão tratadas e as facilidades que serão trazidas ao cliente.

## Matriz de Risco

![img](https://github.com/2023M5T2-Inteli/grupo2/blob/main/docs/img/project/Matriz-Risco.png)
A matriz de riscos nos permite estar ciente dos riscos e nos incentiva a buscar algum paleativo. Por outro lado, também trazemos as oportunidades, as quais estamos trabalhando para que possam se cumprir.
De forma geral, os riscos com probabilidades descritas como "muito baixas", já foram superados. O restante, estamos desempenhando uma boa organização e acreditamos que tudo estará dentro das metas estabelecidas até a entrega final.

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

- Backend-Microcontrolador: MicroPython
- Backend-Aplicação: Python
- Frontend: PySimpleGUI

## Testes de atuadores, sensores e do microcontrolador (Sprint 2)

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

## Testes de atuadores, sensores e do microcontrolador (Sprint 3)

Na sprint 3 fizemos a implementação dos componentes eletrônicos juntamente com o robo para testar o modelo conceito que estava sendo desenvolvido anteriormente. 

Desta forma, utilizando uma peça quadrangular de circuito impresso fizemos uma base para acoplar os 4 imãs utilizados e verificar se área de varredura pensada até então atendia o objetivo da solução. Como é possível ver no vídeo abaixo. 

[Teste de Conceito](https://drive.google.com/file/d/1xd4uUyERMX7U0zyBkPTvCpRegGQAV03W/view?usp=sharing)

Utilizando um computador foi realizada a comunicação entre Raspberry Pi Pico W e os eletroimãs supramencionados, de modo a verificar se o código desenvolvido realizava as funções de ativação dos eletroimãs, inversão da corrente para inverter o momento dipolar do imã, evitando que ele se torne um ímã permanente, e desativação deste componente. Com o teste pudemos observar que o microcontrolador estava adequado à solução, tendo em vista que este fez o controle pretendido dos atuadores. 

Outrossim, através da interface gráfica desenvolvida em PySimpleGUI, conseguimos realizar a gravação de uma rotina para o robô, aquela demonstrada no vídeo, para um cenário comum de utilização. Comprovando novamente que o conceito pensado até então se adequava a solução pretendida na sprint 2. 

# Materiais e Métodos da Fabricação dos Dispositivos Eletrônicos e Mecânicos

## Materiais utilizados 
| Quantidade | Nome do Material  |
|---|---|
| 1x | Placa de Circuito Impresso |
| 1x | Raspberry Pi Pico W |
| 1x | Ponte H L298N  |
| 1x | Módulo de Conversor para Sensor de Peso HX711|
| 1x | Módulo regulador de Tensão (Stepup) MT3608|
| 4x | Eletroimã convencional (12v) |
| 10x | Jumpers |
| 3x | Bandejas |


## Dispositivos eletrônicos fabricados
 - 4 eletroimãs, cada par ligado em paralelo para utilização dos dois canais da ponte H.
 - Ponte H, utilizada para possibilitar a inversão do campo magnético nos eletroimãs utilizados.
 - PCB, que contém raspberry PI e a ponte H, devidamente soldados, que permitem a ativação e inversão da ponte H pelo microcontrolador.

## Método de fabricação dos dispositivos eletrônicos
  - Foram soldados, em paralelo, 2 eletroimãs nas duas saídas da ponte H.
  - Foi anexada à ponte H dois cabos para a possibilidade de conexção com uma fonte de 12 V e com o GND do Raspberry Pi Pico W.
  - O Raspberry Pi Pico W, que está conectado a um computador, tem mais 4 ligações com a ponte H, a fim de controlar a polariadade de suas saídas.

![img](https://github.com/2023M5T2-Inteli/grupo2/blob/main/docs/img/project/Raspberry-PonteH-Imas.jpeg)

|Conexões                            |Cores                         |
|-------------------------------------|:----------------------------:|
| Ponte H com Eletroimãs              | Verde, Marrom, Azul, Laranja |
| Ponte H com Raspberry Pi Pico W     | Verde, Amarelo               |
| Ponte H com fonte e GND do Raspberry| Vermelho, Azul               |

## Funcionamento dos dispositivos eletrônicos
Ao ser energizado, o Raspberry Pi Pico W atua de acordo com seu código de operação, assim ativando as ligações com a ponte H, isso fará com que os eletroimãs proporcionem campos magnéticos. Em um dado momento, o microcontrolador fará a ponte H inverter a polaridade de suas saídas, criando assim um pequeno campo invertido nos imãs em relação ao anterior, e imediatamente depois, o rasberry vai desliga-los, resultando na desativação pretendida do magnetismo do eletroimã.

## Esquemático descritivo dos dispositivos eletrônicos fabricados:
O esquemático descritivo das conexões foi feito utilizando o software EasyEDA, contendo os componentes, ponte h e o módulo de carga HX711, e as respectivas portas utilizadas para conectá-los ao Raspberry Pi Pico W. Este esquemático pode ser visto abaixo. 
![img](https://github.com/2023M5T2-Inteli/grupo2/blob/main/docs/diagrama/SCHEMA-PROJETO-1.png) 

Com o esquemático pronto, produzimos o PCB do diagrama utilizando o software supracitado, EasyEDA, de modo a compreender como os componentes estariam dispostos em uma placa, como pode ser observado abaixo. 

![img](https://github.com/2023M5T2-Inteli/grupo2/blob/main/docs/diagrama/PCB-PROJETO-1.png)


## Dispositivos mecânicos fabricados 

O design a seguir contempla a parte mecânica principal do projeto, a peça que irá segurar os eletroímãs, sobretudo de extrema importância principalmente quando os eletroímãs forem desligados na terceira bandeja para desprender os materiais eletrodomésticos por completo. Assim, o design da peça a ser fabricada, como um todo, valoriza consideravelmente o minimalismo e a praticidade, visto que não será necessário a fabricação de um elemento do zero, pois, usaremos a peça que já vem no kit do robô Dobot Mágico Lite, mais especificamente a peça que prende a caneta ao robô. 
  
Dessa maneira, a fabricação da peça irá ser feita com base apenas em um  paralelepípedo vazado que irá substituir o tubo da caneta e terá a função primordial de armazenar no seu interior toda a fiação elétrica dos eletroímãs, levando todos os fios a serem conectados com a ponte H e o microcontrolador Raspberry Py Picpo W que se localizará na parte traseira do robô, não ocasionando assim uma possível interferência na movimentação do braço,  consequentemente também será de suma importância um cubo que conseguirá armazenar as quatro unidades dos eletroímãs que iremos utilizar para a separação do material nas três bandejas. 

![img](https://github.com/2023M5T2-Inteli/grupo2/blob/main/docs/img/project/Rob%C3%B4-com-a-pe%C3%A7a-acoplada.jpg)
Figura representativa do croqui esquemático com a peça fabricada acoplada à peça que segura a caneta, e a fiação dos eletroímãs sendo conectada também com o circuito elétrico, encontrado na parte posterior do robô. 

![img](https://github.com/2023M5T2-Inteli/grupo2/blob/main/docs/img/project/Rob%C3%B4-com-a-caneta.png)
Figura do robô com a peça que iremos utilizar como base para a fabricação da peça que irá acoplar os eletroímãs. 

![img](https://github.com/2023M5T2-Inteli/grupo2/blob/main/docs/img/project/Pe%C3%A7a-acoplada.jpg)
Figura representativa do croqui esquemático com a peça fabricada, através do desenho é possível verificar como os eletroímãs ficaram posicionados no interior do cubo, também vemos como os fios irão se conectar com os componentes percorrendo o caminho por dentro do paralelepípedo.

![img](https://github.com/2023M5T2-Inteli/grupo2/blob/main/docs/img/project/Medidas-da-pe%C3%A7a.png)
Desenho em 3D da peça fabricada junto com a peça irá segurá-la, através do desenho é possível verificar as medidas principais da peça que irá ser acoplada a outra peça já existente. 

![img](https://github.com/2023M5T2-Inteli/grupo2/blob/main/docs/img/project/Medidas-da-pe%C3%A7a2.png)
Desenho em 3D da peça fabricada, através do desenho é possível verificar as medidas principais da peça. Como elementos geométricos temos: um cubo principal onde os eletroímãs serão posicionados com a medida de 4 centímetros por comprimento e largura e um paralelepípedo vazado que irá dar caminho para a fiação elétrica com 5 centímetros e de 1 centímetro  de largura. 
Para a construção da peça iremos utilizar o único filamento que é hidrofóbico (material que não absorve água) o  PP (polipropileno), visto que, é um material bastante resistente e é frequentemente utilizado em projetos que requerem resistência à água como: a fabricação de embalagens para alimentos, bebidas, produtos químicos e farmacêuticos. 

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

OBS.: Esta interface ainda está em estágio de desenvolvimento, e será aprimorada conforme as próximas sprints, e necessidades que surgirem.

# Detalhamento da criação do executável
é possível criar um arquivo .EXE único que pode ser distribuído para usuários do Windows, eliminando a necessidade de instalar o interpretador Python em cada computador que deseja executá-lo. Para isso, você pode usar o PyInstaller, uma ferramenta que converte um script Python em um arquivo executável autocontido.

Para usar o PyInstaller, você precisará instalá-lo primeiro, bem como o PySimpleGUI se ainda não estiver instalado em seu sistema. A instalação do PyInstaller e do PySimpleGUI é simples e requer apenas um comando no terminal do seu sistema.

```
pip install PySimpleGUI
pip install PyInstaller
```
Para criar seu arquivo EXE a partir de seu programa que usa PySimpleGUI, "nome do seu arquivo.py" digite este comando no prompt de comando do Windows:

```
pyinstaller -wF nomeDoArquivo.py
```

Você ficará com um único arquivo, nomeDoArquivo.exe, localizado em uma pasta chamada dist sob a pasta onde você executou o pyinstaller comando.
Seu arquivo EXE deve ser executado sem criar uma "janela shell". Somente a janela da GUI deve aparecer na barra de tarefas.

Se você tiver uma falha com algo como:

```
ValueError: script '.......\src\tkinter' not found
```

Em seguida, tente adicionar --hidden-import tkinterao seu comando

# Testes entre interface o robô
Fizemos testes de usabilidade para avaliar a interação entre o robô Dobot Magician Lite e o PySimpleGUI. Para isso, criamos um arquivo executável do programa e testamos em diversos computadores com o objetivo principal de confirmar se o programa estava funcionando corretamente.

Com o arquivo executável em mãos, você pode facilmente executar o programa em sua máquina e, ao conectar o robô Dobot Magician Lite através de um cabo USB, pode realizar o ciclo de ensaio previamente programado. Além disso, você também pode gerar novos ensaios e testá-los, tudo isso sem a necessidade de instalar o Python ou outras bibliotecas no seu computador.

Com essa abordagem, torna-se mais fácil e prático testar a funcionalidade do programa em diferentes máquinas e ambientes, sem precisar passar por processos de instalação ou configuração complexos. O arquivo executável empacota todo o código e dependências necessárias para o programa funcionar corretamente em um único arquivo, simplificando a distribuição e a utilização do aplicativo.


https://user-images.githubusercontent.com/99203402/224576115-a0a9aa83-9ee1-4f89-82d6-70484bd09211.mp4

O vídeo apresenta um dos testes realizados entre o PySimpleGUI e o robô Dobot Magician Lite, mostrando a interação entre os dois e a rota que o robô segue após o início do ensaio. Além disso, o vídeo destaca que não é necessária a conexão WiFi durante a execução do programa, tornando o processo mais simples e acessível.

Ao observar o vídeo, é possível notar como o PySimpleGUI permite que o usuário execute o ensaio de forma intuitiva, sem a necessidade de conhecimento prévio em programação ou robótica. Com apenas alguns cliques, o robô segue uma rota pré-programada e realiza as tarefas desejadas.

A demonstração também enfatiza que não é necessário estar conectado a uma rede WiFi para executar o programa, tornando-o mais prático e portátil. Isso significa que você pode executar o programa em qualquer lugar, desde que tenha uma conexão USB com o robô.

Em resumo, o vídeo mostra a facilidade de uso do PySimpleGUI em conjunto com o robô Dobot Magician Lite, bem como a praticidade de não precisar de uma conexão WiFi para executar o programa.



## Design de Interface - Guia de Estilos
Desenvolvemos nossa interface utilizando várias linhas (rows) que contêm elementos minimalistas e de fácil compreensão. Os ícones utilizados são destacados para facilitar a identificação e as instruções são simples e diretas. Além disso, as imagens foram usadas para melhorar a aparência geral da interface.

Para manter a consistência visual, optamos por usar a fonte "Montserrat" em toda a interface, o que contribui para uma aparência mais moderna e sofisticada. A paleta de cores foi desenvolvida a partir das cores padrão do IPT, garantindo uma harmonização visual com outros projetos e sistemas desenvolvidos pela instituição.

Com essa abordagem, buscamos criar uma interface agradável e fácil de usar, que possa ser compreendida facilmente pelos usuários, independentemente do seu nível de habilidade ou experiência com a utilização de programas e aplicativos. Acreditamos que a combinação de elementos minimalistas, instruções claras e imagens atraentes cria uma interface atraente e intuitiva que facilita o uso e aumenta a satisfação do usuário.


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
