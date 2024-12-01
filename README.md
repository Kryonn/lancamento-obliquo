# Lançamento Oblíquo

A ideia geral do projeto é fazer uso de simulações em python, a fim de obter uma melhor compreensão a cerca da física do nosso cotidiano. O foco principal do projeto é mostrar um pouco mais sobre o lançamento oblíquo e suas principais características, como a variação de energia, altura e alcance máximo. 

## Pirata
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

$\vec{F_{g}}=-mg\hat{j}, \ \vec{F_{v}}=-b\vec{v}$

</div>

Sabendo disso, usaremos a segunda lei de Newton para conseguirmos montar uma EDO do movimento:





