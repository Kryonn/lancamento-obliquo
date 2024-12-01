# Lançamento Oblíquo

A ideia geral do projeto é fazer uso de simulações em python, a fim de obter uma melhor compreensão a cerca da física do nosso cotidiano. O foco principal do projeto é mostrar um pouco mais sobre o lançamento oblíquo e suas principais características, como a variação de energia, altura e alcance máximo. 

## Contextualização
Vamos começar com uma contextualização: um pirata percebe que tem um inimigo distante a 100 metros de seu navio e, sem pensar duas vezes, o atinge com o canhão. No dia seguinte, se encontra na mesma situação, ele percebe, através do som, que há um inimigo distante a 100 metros de seu navio, porém dessa vez o inimigo está do outro lado de uma pequena ilha. Sabendo disso, ele lembrou do dia anterior e então fez os seguintes questionamentos: se eu apenas aumentar o ângulo de inclinação do canhão será o suficiente para atingir os inimigos sem atingir parte da ilha? Se não, quanto eu preciso aumentar de pólvora(velocidade de lançamento) para que seja suficiente?


<div align="center">

![imagem_2024-11-27_204547949](https://github.com/user-attachments/assets/fac019fa-ba91-492c-9518-a69fc037014e)

</div>

## Física

O movimento oblíquo, diferente da queda livre, possui duas direções de movimento, sendo, nesse caso, o eixo x referente ao eixo horizontal e o eixo y ao eixo vertical.

A trajetória é descrita por uma parábola, mas por que? Isso ocorre devido as forças atuantes durante o movimento. Durante o lançamento, apenas a força gravitacional($`\vec{F_{g}}`$) atua no objeto, por isso, como a gravidade atua apontando para o solo, a velocidade no eixo y reduz a ponto de inverter o sentido, enquanto que no eixo x não há variação de velocidade, ou seja, sendo constante durante todo o movimento.

A figura a seguir nos mostra o modelo geral de um lançamento oblíquo, sendo $\vec{v_{0}}$ a velocidade inicial do objeto, $\vec{F_{g}}$ a força gravitacional e $\vec{r}$ o vetor posição.

<div align="center">

![imagem_2024-11-27_204547949](https://github.com/user-attachments/assets/fac019fa-ba91-492c-9518-a69fc037014e)

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

Porém, precisamos descobrir o valor de C, para que a função de $\dot{x}$ esteja completa. Para isso, já que sabemos que $\dot{x}(0)=0$, igualaremos $\dot{x}(t)=0$, em $t=0$:

<div align="center">
  
$\dot{x}=e^{-\omega_{0}t}.C, \dot{x}(0)=v_{0}\cos \theta \Rightarrow \dot{x}=v_{0}\cos \theta.e^{-\omega_{0}t}.$

</div>

Com isso, conseguimos obter $\dot{x}$. Agora, para obtermos $x$, $y$, faremos o mesmo procedimento, obtendo os seguintes resultados:

<div align="center">
  
$x=-\frac{v_{0}\cos \theta}{\omega_{0}}(1-e^{-\omega_{0} t}),$

$y=\frac{1}{\omega_{0}}(v_{0}\sin \theta+\frac{g}{\omega_{0}})(1-e^{-\omega_{0}t})-\frac{gt}{\omega_{0}}.$

</div>









