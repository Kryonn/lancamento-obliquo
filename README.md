# Lançamento Oblíquo

A ideia geral do projeto é fazer uso de simulações em python, a fim de obter uma melhor compreensão acerca da física do nosso cotidiano. O foco principal do projeto é mostrar um pouco mais sobre o lançamento oblíquo e suas principais características.

## Contextualização
Vamos começar com uma contextualização: um pirata percebe que tem um inimigo distante a 100 metros de seu navio e, sem pensar duas vezes, o atinge com o canhão. No dia seguinte, se encontra na mesma situação, ele percebe, através do som, que há um inimigo distante a 100 metros de seu navio, porém, dessa vez, o inimigo está do outro lado de uma pequena ilha. Sabendo disso, ele lembrou do dia anterior e então fez os seguintes questionamentos: se eu apenas aumentar o ângulo de inclinação do canhão será o suficiente para atingir os inimigos sem atingir parte da ilha? Se não, quanto eu preciso aumentar de pólvora(velocidade de lançamento) para que seja suficiente?


<div align="center">

![imagem_2024-11-27_204547949](https://github.com/user-attachments/assets/fac019fa-ba91-492c-9518-a69fc037014e)

</div>

## Física

### Trajetória

O movimento oblíquo, diferente da queda livre, possui duas direções de movimento, sendo, nesse caso, o eixo x referente ao eixo horizontal e o eixo y ao eixo vertical.

A trajetória é descrita por uma parábola, mas por que? Isso ocorre devido às forças atuantes durante o movimento. Durante o lançamento, apenas a força gravitacional($`\vec{F_{g}}`$) atua no objeto, por isso, há uma desaceleração na direção do eixo y do movimento, fazendo com que a velocidade diminua, enquanto que, na direção do eixo x, a velocidade se mantém constante.

A figura a seguir nos mostra o modelo geral de um lançamento oblíquo, sendo $\vec{v_{0}}$ a velocidade inicial do objeto, $\vec{F_{g}}$ a força gravitacional e $\vec{r}$ o vetor posição.

<div align="center">

![null (2)](https://github.com/user-attachments/assets/675602b0-3d6f-4b36-a5f9-0707ddfae92b)

</div>

### Construção das EDOs:

<div align="center">

$\vec{r}=(x(t),\ y(t),\ 0), \vec{v}=(\dot{x}(t),\ \dot{y}(t),\ 0), \vec{a}=(\ddot{x}(t),\ \ddot{y}(t),\ 0).$

</div>

Temos o esboço da trajetória, mas como transformamos o desenho em números? 

No sistema acima, atuam as seguintes forças:

<div align="center">

$\vec{F_{g}}=-mg\hat{j}.$

</div>

Sabendo disso, usaremos a segunda lei de Newton para conseguirmos montar uma EDO do movimento:

<div align="center">

$\vec{F_{R}}=\dot{\vec{p}}=m\ddot{x}\hat{i}+m\ddot{y}\hat{j}=-mg\hat{j}.$

</div>

Então, ao separarmos a força resultante, ficamos com:

<div align="center">
  
$m\ddot{x}=0,$

$m\ddot{y}=-mg.$


</div>

Logo, chegamos nas seguintes EDOs:

<div align="center">

$\ddot{x}=0,$

$\ddot{y}=-g.$

</div>

### Resolução das EDOs:

Nosso objetivo, resolvendo as EDOs, é determinar a função horária do movimento. Para isso, começaremos obtendo x:

<div align="center">

$\ddot{x}=0 \Rightarrow \dot{x}=C.$

</div>

Porém, sabemos que $\dot{x}(0)=v_{0}.\cos\theta$, por isso, para obter $C$, faremos uma substituição:

<div align="center">

$\dot{x}=C \Rightarrow \dot{x}=v_{0}.\cos\theta.$

</div>

Agora que temos $dot{x}$, podemos integrar novamente, para obtermos $x$:

<div align="center">

$\dot{x}=v_{0}.\cos \theta \Rightarrow x=v_{0}.\cos \theta t+C.$

</div>

Mas, sabemos que $x(0)=0$. Fazendo a substituição, ficamos com:

<div align="center">

$x=v_{0}.\cos \theta t+C \Rightarrow x=v_{0}.\cos \theta t.$

</div>

Temos a função horária do movimento no eixo x. Agora, resolveremos a EDO relativa ao eixo y. Para isso, faremos o mesmo procedimento realizado no eixo x, começaremos integrando:

<div align="center">

$\ddot{y}=-g \Rightarrow \dot{y}=-gt+C.$

</div>

Sabemos que $\dot{y}(0)=v_{0}.\sin \theta$, com isso podemos substituir $C$:

<div align="center">

$\dot{y}=-gt+C \Rightarrow \dot{y}=-gt+v_{0}.\sin \theta.$

</div>

Por fim, faremos a última integração e substituição para obter $y$:

<div align="center">

$\dot{y}=-gt+v_{0}.\sin \theta \Rightarrow y=-\frac{gt^{2}}{2}+v_{0}.\sin \theta t + C,y(0)=0 \Rightarrow y=-\frac{gt^{2}}{2}+v_{0}.\sin \theta t$

</div>

Portanto, a nossa trajetória é descrita por essas duas funções horárias:

<div align="center">

$x=v_{0}.\cos \theta t,$

$y=v_{0}.\sin \theta t-\frac{gt^{2}}{2}.$

</div>

### O Problema do Pirata

Mas afinal, quais são as respostas para as dúvidas do pirata? Para entendermos melhor a situação, usaremos uma simulação/jogo. Com ela, é possível, a partir da mudança na angulação do canhão, notar que, se houver a manutenção da velocidade inicial, não será possível atingir o inimigo.

<div align="center">

![traj](https://github.com/user-attachments/assets/6e9ee1d3-6bd3-443e-b93d-241751240da8)

</div>

Sabendo disso, vem a seguinte pergunta: o quanto ele precisa aumentar de pólvora(proporcional a velocidade inicial) no canhão, para que consiga atingir o inimigo? Para responder essa pergunta, vamos começar obtendo o tempo de queda do lançamento ($t_{q}$). Para isso, igualaremos a função relativa a posição no eixo y, quando $t=t_{q}$, a zero, uma vez que, no fim da trajetória, a altura é nula.

<div align="center">

$y(t_{q})=v_{0}.\sin \theta t_{q}-\frac{gt_{q}^{2}}{2}=0 \Rightarrow t_{q}(v_{0}\sin \theta - \frac{gt_{q}}{2})=0.$

</div>

Em uma multiplicação, só resulta em zero caso um dos fatores é zero. Logo, $t_{q}=0$ ou $v_{0}\sin \theta - \frac{gt_{q}}{2}=0$, se $t_{q}=0$, então não terá trajetória, então concluímos que $v_{0}\sin \theta - \frac{gt_{q}}{2}=0$. Ao isolarmos $t_{q}$, ficamos com:

<div align="center">

$v_{0}\sin \theta - \frac{gt_{q}}{2}=0 \Rightarrow t_{q}=\frac{2v_{0}.\sin \theta}{g}.$

</div>

Porém, precisamos calcular o tempo de queda, tanto do primeiro dia, quanto do segundo. Por isso, vamos considerar $t_{1}$ e $t_{2}$ como tempo de queda do primeiro e do segundo dia, e $v_{1}$ e $v_{2}$, como velocidade inicial no primeiro e no segundo dia, respectivamente. Então, temos que:

<div align="center">

$t_{1}=\frac{2v_{1}.\sin (\theta)}{g},$

$t_{2}=\frac{2v_{2}.\sin (\theta+\phi)}{g}.$

</div>

Agora, tendo o tempo de queda em mãos, é possível calcular o quanto da velocidade é necessário aumentar. Para isso, consideraremos que $x_{1}$ é a distância entre o barco do pirata e o inimigo no primeiro dia e que $x_{2}$ é a distância no segundo dia:

<div align="center">

$x_{1}=v_{1}.\cos\theta t_{1},$

$x_{2}=v_{2}.\cos(\theta+\phi) t_{2}.$

</div>

Mas, segundo o problema, a distância em ambos os dias eram iguais, logo podemos igualar as expressões:

<div align="center">

$x_{1}=x_{2} \Rightarrow v_{1}.\cos\theta t_{1}=v_{2}.\cos(\theta+\phi) t_{2}.$

</div>

Substituindo os valores de $t_{1}$ e $t_{2}$ e isolando $v_{2}$, ficamos com:

<div align="center">

$v_{1}.\cos\theta t_{1}=v_{2}.\cos(\theta+\phi) t_{2} \Rightarrow \frac{2v_{1}.\cos\theta.v_{1}\sin\theta}{g}=\frac{2v_{2}.\cos(\theta+\phi).v_{2}\sin(\theta + \phi)}{g} \Rightarrow v_{2}^{2}=v_{1}^{2}.\frac{\cos\theta\sin \theta}{\cos(\theta + \phi)\sin(\theta+\phi)} \Rightarrow v_{2}=v_{1}.\sqrt{\frac{\cos\theta\sin \theta}{\cos(\theta + \phi)\sin(\theta+\phi)}}.$

</div>

Portanto, com esse resultado, podemos concluir que, para que o pirata consiga atingir o inimigo aumentando $\phi$ graus de angulação, será necessário aumentar $\sqrt{\cos\theta\sin \theta}$ / $\sqrt{\cos(\theta + \phi)\sin(\theta+\phi)}$ vezes o número de pólvora no canhão. Exemplo teste: 

<div align="center">

$Ang_{1}=42°, v_{1}=21 m/s, Ang_{2}=76°, v_{2}=?$

</div>

### Resistência do ar

O lançamento oblíquo possui uma variação em que inclui a resistência do ar na descrição da trajetória. A resistência, mais conhecida como força viscosa($\vec{F_{v}}$), atua de maneira contrária à velocidade, sendo uma força dissipativa. O processo para obter as expressões relativas a descrição do movimento é o mesmo: montar as EDOs e depois resolvê-las.

### Construção das EDOs:

No lançamento oblíquo com força viscosa, atuam as seguintes forças:

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

### Resolução das EDOs:

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
    
  - Caso não estejam sigam os passos de instalação sugeridos pelos sites dos desenvolvedores das ferramentas ([NumPy](https://numpy.org/pt/install/),  [Pygame](https://www.pygame.org/wiki/GettingStarted)).

  - **Exemplos de Uso:**  
  - Para rodar a simulação utilize o código:
    ```python
      python jogo.py
    ```
 - Certifique-se de baixar o repositório do github para correta execução.

   **Configuração e Uso:** Parâmetros iniciais podem ser ajustados:
    - Velocidade inicial - basta mexer na barra que aparece com o mouse.
    - Ângulo do lançamento - com as seta para cima ou para baixo ajuste o ângulo.

  - **Informações sobre o projeto:**
 
  Esste projeto foi desenvolvido por:
  
      Beatriz Alves dos Santos
      Kevin Ryoji Nakashima
      Eduardo Neves Gomes da Silva

## Referências

Bernardes, E. de S. (2024). Dinâmica-v4 (Notas de aula). 7600105 - Física Básica I. Universidade de São Paulo, São Carlos.
