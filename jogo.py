"""
Simulação de Lançamento Oblíquo

Descrição:
     Esse programa é uma simulação interativa de lançamento oblíquo, onde o usuário pode ajustar os parâmetros
     de velocidade inicial e resistência do ar. O objetivo principal é permitir a observação do comportamento
     do sistema em diferentes condições. Obstáculos e alvos também são adicionados para tornar a experiência 
     mais divertida e desafiadora!

Autores: 
     Beatriz Alves dos Santos (15588630)
     Kevin Ryoji Nakashima (15675936)
     Eduardo Neves Gomes da Silva (13822710)

Este projeto faz parte do processo avaliativo da disciplina 7600105 - Física Básica I (2024) da USP-São Carlos ministrada pela(o) [Prof. Krissia de Zawadzki/Esmerindo de Sousa Bernardes]
"""

import pygame # type: ignore
import numpy
import math

# Variáveis gerais
pontuacao = 0
altura_display = 600
largura_display = 1000

altura_seta = 10
largura_seta = 10
comp_seta = 60

angulo_ = 45
angulo = 45
raio_bola = (0.5*20)
origem_canhao = (37, altura_display - 27)
pos_bola_conv = (origem_canhao[0], origem_canhao[1])
contar_tempo = False
colisao = False
acerto = False
cor = "red"

tempo = 0
omega = 0.4    # Atrito do ar
vel_inicial = 20   
vel_inicial_ = 20 
g = 9.8
flag = 0   # Flag para verificação da primeira colisão

obstaculo_x = 450
obstaculo_y = 350
obstaculo_larg = 120
obstaculo_alt = altura_display - obstaculo_y

quad = pygame.Rect(850, 500, 100, 100)

# Configuração do pygame
pygame.init()
tela = pygame.display.set_mode((largura_display, altura_display))
pygame.display.set_caption("Lançamento Oblíquo com Resistência do Ar")
clock = pygame.time.Clock()

# Configuração da imagem do canhão
img_canhao = pygame.image.load('canhao.png')
img_canhao = pygame.transform.scale(img_canhao, (60, 60))  

# Variáveis e configuração dos sliders de velocidade inicial e resistência do ar
slider_tam = 200
slider_h = 10
sliderVel_x = 50
sliderVel_y = 50

sliderVel_rect = pygame.Rect(sliderVel_x, sliderVel_y, slider_tam, slider_h)  
sliderVel_handle = pygame.Rect(sliderVel_x+(vel_inicial*2), sliderVel_y-5, 20, 20)  
sliderVel_min = sliderVel_x
sliderVel_max = sliderVel_x + slider_tam

sliderAtr_x = 50
sliderAtr_y = 120

sliderAtr_rect = pygame.Rect(sliderAtr_x, sliderAtr_y, slider_tam, slider_h)  
sliderAtr_handle = pygame.Rect(sliderAtr_x+(omega*20), sliderAtr_y-5, 20, 20)  
sliderAtr_min = sliderAtr_x
sliderAtr_max = sliderAtr_x + slider_tam  

# Funções

def calcula_trajetoria(tempo):
     """
     Calcula a posição da bola ao longo do tempo, considerando o ângulo inicial,
     velocidade inicial e resistência do ar.

     Parâmetros:
     - tempo (float): O tempo em segundos para o qual a posição será calculada.

     Retorna:
     - tuple[float, float]: Coordenadas da posição (x, y) da bolinha.
     """
     angulo_rad = numpy.radians(angulo)

     pos_x = (vel_inicial*numpy.cos(angulo_rad)*(1-numpy.exp(-omega*tempo)))/omega
     pos_y = (1/omega)*(vel_inicial*numpy.sin(angulo_rad) + (g/omega))*(1-numpy.exp(-omega*tempo)) - (g/omega)*tempo

     # Ajusta para escala de visualização
     escala = 20
     pos_x *= escala
     pos_y *= escala

     return pos_x, pos_y

def desenha_tela():
     """
     Desenha todos os elementos da tela, incluindo o canhão, a bola, sliders,
     informações textuais, obstáculos e alvos. Também verifica colisão entre
     a bola e o obstáculo.

     Não possui parâmetros ou retorno.
     """
     global colisao
     cor_tela = (153, 201, 239)
     tela.fill(cor_tela)
     desenhar_seta(origem_canhao, comp_seta)
     desenha_slider_vel()
     texto_Vel(vel_inicial)

     desenha_slider_atr()
     texto_Atr(omega)
     texto_Info()
     desenha_quadrado()
     desenha_barco()

     if flag == 1:
          obstaculo = pygame.Rect(obstaculo_x, obstaculo_y, obstaculo_larg, obstaculo_alt) 
          desenha_obstaculo(obstaculo)

          bola_rect = pygame.Rect(
               pos_bola_conv[0] - raio_bola,  
               pos_bola_conv[1] - raio_bola,  
               raio_bola * 2,                 
               raio_bola * 2                  
          )

          # Verifica colisão
          if bola_rect.colliderect(obstaculo) == True:
               colisao = True
               
     if acerto == 1:
          texto_acerto()

     pygame.draw.circle(tela, cor, pos_bola_conv, raio_bola)

     # Rotaciona a imagem, centraliza com o canhão e publica
     imagem_rotacionada = pygame.transform.rotate(img_canhao, angulo_-45)
     rect = imagem_rotacionada.get_rect(center=origem_canhao)
     tela.blit(imagem_rotacionada, rect.topleft)

def desenha_barco():
     """
     Desenha a imagem do alvo (barco) em sua posição predefinida.

     Não possui parâmetros ou retorno.
     """
     barco_img = pygame.image.load('barco.png')  
     barco_img = pygame.transform.scale(barco_img, (210, 210))
     tela.blit(barco_img, (quad.x-40, quad.y-70))  

def desenhar_seta(origem, comp):
     """
     Desenha uma seta rotacionada que representa a direção do disparo.

     Parâmetros:
     - origem (tuple[int, int]): Coordenadas da base do canhão (ponto inicial da seta).
     - comp (float): Comprimento da seta em pixels.

     Não possui retorno.
     """
     angulo_rad = numpy.radians(angulo_)
     # Desenha a reta
     dest = (
          origem[0] + (comp*(numpy.cos(angulo_rad))), 
          origem[1] - (comp*(numpy.sin(angulo_rad)))
     )
     pygame.draw.line(tela, "black", origem, dest)

     # Seta sem rotação
     base_pontos = [
          (0, -altura_seta // 2),  
          (-largura_seta // 2, altura_seta // 2), 
          (largura_seta // 2, altura_seta // 2)  
     ]

     angulo_seta = angulo_ + 90
     angulo_seta_rad = numpy.radians(angulo_seta)

     # Seta rotacionada
     pontos_rotacionados = []
     for px, py in base_pontos:
          x_rot = px * math.cos(angulo_seta_rad) - py * math.sin(angulo_seta_rad)
          y_rot = px * math.sin(angulo_seta_rad) + py * math.cos(angulo_seta_rad)
          pontos_rotacionados.append((x_rot + dest[0], -y_rot + dest[1]))  

     pygame.draw.polygon(tela, "black", pontos_rotacionados)

def desenha_quadrado():
     """
     Desenha um quadrado para referência da posição do alvo.

     Não possui parâmetros ou retorno.
     """
     pygame.draw.rect(tela, "black", quad)

def desenha_obstaculo(obstaculo):
     """
     Desenha um retângulo para referência da posição do obstáculo e adiciona a imagem da palmeira.

     Não possui parâmetros ou retorno.
     """
     pygame.draw.rect(tela, "black", obstaculo)
     palmeira_img = pygame.image.load('palmeira.png')  
     palmeira_img = pygame.transform.scale(palmeira_img, (300, 350))  # Ajusta o tamanho
     tela.blit(palmeira_img, (obstaculo.x-80, obstaculo.y-50))  

def desenha_slider_vel():
    """
    Desenha o slider que ajusta a velocidade inicial do disparo.

    Não possui parâmetros ou retorno.
    """

    pygame.draw.rect(tela, "gray", sliderVel_rect)  
    pygame.draw.rect(tela, "red", sliderVel_handle) 

def desenha_slider_atr():
    """
    Desenha o slider que ajusta o coeficiente de resistência do ar.

    Não possui parâmetros ou retorno.
    """
    pygame.draw.rect(tela, "gray", sliderAtr_rect)  
    pygame.draw.rect(tela, "red", sliderAtr_handle) 

def texto_Vel(value):
    """
    Exibe o valor atual da velocidade inicial abaixo do slider correspondente.

    Parâmetros:
    - value (float): Velocidade inicial em m/s.

    Não possui retorno.
    """
    font = pygame.font.SysFont("Arial", 20)
    text = font.render(f'Velocidade Inicial: {value:.1f} m/s', True, (0, 0, 0))
    tela.blit(text, (sliderVel_x + slider_tam // 2 - text.get_width() // 2, sliderVel_y + slider_h + 10)) 

def texto_Atr(value):
    """
    Exibe o valor atual da resistência do ar abaixo do slider correspondente.

    Parâmetros:
    - value (float): Coeficiente de resistência do ar em s⁻¹.

    Não possui retorno.
    """
    font = pygame.font.SysFont("Arial", 20)
    text = font.render(f'Resistência do Ar: {value:.1f} s⁻¹', True, (0, 0, 0))
    tela.blit(text, (sliderAtr_x + slider_tam // 2 - text.get_width() // 2, sliderAtr_y + slider_h + 10)) 

def texto_Info():
    """
    Exibe as instruções de como jogar na parte superior da tela.

    Não possui parâmetros ou retorno.
    """
    font = pygame.font.SysFont("Arial", 20)
    text = font.render(f'Use as setas CIMA/BAIXO para mover o canhão.', True, (0, 0, 0))
    text2 = font.render(f'Pressione ESPAÇO para atirar!', True, (0, 0, 0))
    tela.blit(text, (350, 30)) # Posição do texto
    tela.blit(text2, (420, 60)) # Posição do texto

def texto_acerto():
    """
    Exibe um texto indicando que acertou o alvo no canto superior da tela.

    Não possui parâmetros ou retorno.
    """
    font = pygame.font.SysFont("Arial", 20)
    text = font.render(f'Você acertou o alvo!', True, "red")
    tela.blit(text, (500, 120)) # Posição do texto

# Funções para verificar as colisões
def colisao_alvo():
    """
    Verifica se a bola colidiu com o alvo (quadrado/barco).

    Retorna:
    - bool: `True` se houver colisão, `False` caso contrário.
    """
    # Cria o retângulo da bola com base na posição e raio da bola
    bola_rect = pygame.Rect(
        pos_bola_conv[0] - raio_bola,  
        pos_bola_conv[1] - raio_bola,  
        raio_bola * 2,                 
        raio_bola * 2                  
    )

    # Verifica colisão
    return pygame.Rect.colliderect(quad, bola_rect)


def main():
     """
     Função principal que inicializa o programa, gerencia o loop principal e 
     controla a interação do usuário com a simulação.

     Não possui parâmetros ou retorno.
     """
     global acerto, angulo, angulo_, tempo, vel_inicial, vel_inicial_, omega, cor, pos_bola_conv, contar_tempo, pontuacao, flag, colisao
     sair = False
     dragging_vel = False
     dragging_atr = False

     while sair == False:
          pos_bola = calcula_trajetoria(tempo)
          pos_bola_conv = (pos_bola[0] + origem_canhao[0], (altura_display - pos_bola[1]) - 27)
          desenha_tela()
          
          # Atualiza o angulo da trajetória da bola
          if contar_tempo == 0:
               vel_inicial = vel_inicial_
               angulo = angulo_
               colisao = 0

          if colisao_alvo():
               contar_tempo = False  # Para a simulação
               tempo = 0  # Reseta o tempo
               flag = 1
               acerto = 1

          elif colisao == 1 or pos_bola_conv[1] > altura_display or pos_bola_conv[0] > largura_display:
               contar_tempo = False  
               tempo = 0 

          if contar_tempo == True:
               tempo += clock.get_time() / 300    

          eventos = pygame.event.get()
          for evento in eventos:
               if evento.type == pygame.QUIT:  # Fechar o programa
                    sair = True
               if evento.type == pygame.MOUSEBUTTONDOWN:
                    if sliderVel_handle.collidepoint(evento.pos):  # Verifica se clicou no controle de velocidade
                         dragging_vel = True
                    if sliderAtr_handle.collidepoint(evento.pos):  # Verifica se clicou no controle de atrito do ar
                         dragging_atr = True

               if evento.type == pygame.MOUSEBUTTONUP:
                    dragging_vel = False
                    dragging_atr = False

               if evento.type == pygame.MOUSEMOTION:   # Verifica se está arrastando o mouse
                    if dragging_vel:
                         new_x_vel = max(sliderVel_min, min(evento.pos[0], sliderVel_max - sliderVel_handle.width))
                         sliderVel_handle.x = new_x_vel
                         vel_inicial_ = (new_x_vel - sliderVel_min)*0.5    # Ajusta a velocidade
                         
                    if dragging_atr:
                         new_x_atr = max(sliderAtr_min, min(evento.pos[0], sliderAtr_max - sliderAtr_handle.width))
                         sliderAtr_handle.x = new_x_atr
                         omega = max(0.001, (new_x_atr - sliderAtr_min)*0.05)   # Ajusta o atrito do ar

          teclas = pygame.key.get_pressed()

          # Controle de ângulo e disparo
          if teclas[pygame.K_UP] and angulo_ < 90:     
               angulo_ += 1

          if teclas[pygame.K_DOWN] and angulo_ > 0:
               angulo_ -= 1
          
          if teclas[pygame.K_SPACE]:
               contar_tempo = True
               acerto = 0

          pygame.display.flip()
          clock.tick(60)
                    
     pygame.quit()           

if __name__ == "__main__":
    main()
