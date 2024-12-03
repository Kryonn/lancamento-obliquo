# Lançamento Oblíquo

A ideia geral do projeto é fazer uso de simulações em python, a fim de obter uma melhor compreensão a cerca da física do nosso cotidiano. O foco principal do projeto é mostrar um pouco mais sobre o lançamento oblíquo e suas principais características.

## Contextualização
Vamos começar com uma contextualização: um pirata percebe que tem um inimigo distante a 100 metros de seu navio e, sem pensar duas vezes, o atinge com o canhão. No dia seguinte, se encontra na mesma situação, ele percebe, através do som, que há um inimigo distante a 100 metros de seu navio, porém, dessa vez, o inimigo está do outro lado de uma pequena ilha. Sabendo disso, ele lembrou do dia anterior e então fez os seguintes questionamentos: se eu apenas aumentar o ângulo de inclinação do canhão será o suficiente para atingir os inimigos sem atingir parte da ilha? Se não, quanto eu preciso aumentar de pólvora(velocidade de lançamento) para que seja suficiente?


<div align="center">

![imagem_2024-11-27_204547949](https://github.com/user-attachments/assets/fac019fa-ba91-492c-9518-a69fc037014e)

</div>

## Física

### Trajetória

O movimento oblíquo, diferente da queda livre, possui duas direções de movimento, sendo, nesse caso, o eixo x referente ao eixo horizontal e o eixo y ao eixo vertical.

A trajetória é descrita por uma "parábola", mas por que? Isso ocorre devido as forças atuantes durante o movimento. Durante o lançamento, apenas as forças gravitacional($`\vec{F_{g}}`$) e viscosa($`\vec{F_{q}}`$) atuam no objeto, por isso, como a gravidade atua apontando para o solo, a velocidade no eixo y reduz a ponto de inverter o sentido, enquanto que no eixo x não há variação de velocidade.

A figura a seguir nos mostra o modelo geral de um lançamento oblíquo, sendo $\vec{v_{0}}$ a velocidade inicial do objeto, $\vec{F_{g}}$ a força gravitacional e $\vec{r}$ o vetor posição.

<div align="center">

![null(2)](https://github.com/user-attachments/assets/1c595f59-368a-43de-b5b1-eb050c24990e)

</div>

Temos a trajetória, mas como transformamos o desenho em física de fato? 

No sistema acima, atuam as seguintes forças:

<div align="center">

$\vec{F_{g}}=-mg\hat{j}, \ \vec{F_{v}}=-b\vec{v}.$

</div>

Sabendo disso, usaremos a segunda lei de Newton para conseguirmos montar uma EDO do movimento:

<div align="center">

$\vec{F_{R}}=\dot{\vec{p}}=m\ddot{x}\hat{i}+m\ddot{y}\hat{j}=-b\dot{x}\hat{i}-b\dot{y}\hat{j}-mg\hat{j}.$

</div>

Então, ao separarmos a força resultante, ficamos com:

<div align="center">
  
$m\ddot{x}=-b\dot{x}\Rightarrow\ddot{x}=-\frac{b}{m}\dot{x},$

$m\ddot{y}=-b\dot{y}-mg\Rightarrow\ddot{y}=-\frac{b}{m}\dot{y}-g.$


</div>

Por mera conveniência, substituiremos $b/m$ por $\omega_{0}$, obtendo as seguintes EDOS:

<div align="center">
  
$\ddot{x}=-\frac{b}{m}\dot{x}=-\omega_{0}\dot{x},$

$\ddot{y}=-\frac{b}{m}\dot{y}-g=-\omega_{0}\dot{y}-g.$

</div>

Nosso objetivo é, a partir das EDOS encontradas, obtermos as funções horárias no eixo x e y. Por enquanto, trabalharemos apenas com a EDO relativa ao eixo x.

Em relação ao eixo x, temos:

<div align="center">
  
$\ddot{x}=-\omega_{0}\dot{x}.$

</div>

Isso significa que precisamos de uma função da qual a segunda derivada é proporcional à primeira derivada dela. Para começarmos os cálculos, reescreveremos a EDO e integraremos os dois lados da igualdade:

<div align="center">
  
$\dfrac{d\dot{x}}{dt}=-\omega_{0}\dot{x}\Rightarrow \int\dfrac{d\dot{x}}{\dot{x}}=-\omega_{0}\int dt\Rightarrow ln\dot{x}=-\omega_{0}t + C^{'}\Rightarrow \dot{x}=e^{-\omega_{0}t}.e^{C^{'}}\Rightarrow \dot{x}=e^{-\omega_{0}t}.C.$

</div>

Porém, precisamos descobrir o valor de $C$, para que a função de $\dot{x}$ esteja completa. Para isso, já que sabemos que $\dot{x}(0)=0$, igualaremos $\dot{x}(t)=0$, em $t=0$:

<div align="center">
  
$\dot{x}=e^{-\omega_{0}t}.C, \dot{x}(0)=v_{0}\cos \theta \Rightarrow \dot{x}=v_{0}\cos \theta.e^{-\omega_{0}t}.$

</div>

Com isso, conseguimos obter $\dot{x}$. Agora, para obtermos $x$ e $y$, faremos o mesmo procedimento, obtendo os seguintes resultados:

<div align="center">
  
$x=-\frac{v_{0}\cos \theta}{\omega_{0}}(1-e^{-\omega_{0} t}),$

$y=\frac{1}{\omega_{0}}(v_{0}\sin \theta+\frac{g}{\omega_{0}})(1-e^{-\omega_{0}t})-\frac{gt}{\omega_{0}}.$

</div>

### O Problema do Pirata

Mas afinal, quais são as respostas para as dúvidas do pirata? Para entendermos melhor a situação, usaremos uma simulação/jogo. Com ela, é possível, a partir da mudança na angulação do canhão, notar que, se houver a manutenção da velocidade inicial, não será possível atingir o inimigo.

Sabendo disso, vem a seguinte pergunta: o quanto ele precisa aumentar de pólvora no canhão, para que consiga atingir o inimigo? Para responder essa pergunta, vamos começar considerando $x_{0}$ como a distância do inimigo no dia anterior e $x_{1}$ a distância do inimigo no dia seguinte. Sabemos que a distância permanece a mesma em ambos os dias, por isso igualaremos:

<div align="center">
  
$x_{0}=x_{1} \Rightarrow \frac{v_{0}\cos\theta}{\omega_{0}}\cdot(1-e^{-\omega_{0}t})=\frac{v_{1}\cos(\theta+\alpha)}{\omega_{0}}\cdot(1-e^{-\omega_{0}t})\Rightarrow v_{0}\cos\theta=v_{1}\cos(\theta+\alpha)\Rightarrow v_{1}=v{0}\frac{\cos\theta}{\cos(\theta+\alpha)}$

</div>

Com isso, concluímos que é necessário multiplicar o valor da velocidade por $\cos\theta / \cos(\theta+\alpha).$

## Implementação

- **Linguagens e Pacotes:**  
  O projeto foi implementado em Python, utilizando os pacotes NumPy, Pygame e Math. Com NumPy servindo para a manipulação e cálculo eficiente com arrays e álgebra linear, Pygame criando o jogo 2d em si com multimídia interativa e Math oferecendo operações matemáticas básicas e funções trigonométricas.

## Como Usar

- **Instalação e Dependências:**  
  - Certifique-se de que o Python 3.12.7 (ou outra versão de linguagem) está instalado. Assim como os pacotes do Pygame e do NumPy. Essas verificações podem ser feitas pelo prompt de comando digitando:
    ```bash
    python --version
    python -m pygame --version
    pip show numpy
    
  - Caso não estejam sigam os passos de instalação sugeridos pelos sites dos desenvolvedores das ferramentas.

  - **Exemplos de Uso:**  
  - Para rodar a simulação utilize o código:
    ```python
      python jogo.py
    ```
 - Certifique-se de baixar o repositório do github para correta execução.

   **Configuração e Uso:** Parâmetros iniciais podem ser ajustados:
    - Velocidade inicial - basta mexer na barra que aparce com o mouse.
    - Resistência do ar - basta mexer na barra que aparce com o mouse.
    - Ângulo do lançamento - com as seta para cima ou para baixo ajuste o ângulo.
    - A cada lançamento ou ajuste apertar o R pra resetar e poder lançar novamente.

  - **Informações sobre o projeto:**
 
  Esste projeto foi desenvolvido por:
  
      Beatriz Alves dos Santos
      Kevin Ryoji Nakashima
      Eduardo Neves Gomes da Silva
