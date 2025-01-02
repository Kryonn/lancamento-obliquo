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

# Variáveis gerais

# velocidade e angulo de referência para um acerto
vel_ref = 22.8
ang_ref = 60
nova_vel = 0

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
omega_ = 0.4   
vel_inicial = 20   
vel_inicial_ = 20 
g = 9.8

# Constantes do slider de velocidade
vel_min = 0 
vel_max_ = 100 
vel_max = vel_max_*(10/9)  # valor corrigido para caber no slider
slider_range = vel_max - vel_min
slider_increment = 0.2

# Flags para indicar o estado dos botões 
flag_obst = 0   # Flag para verificação da primeira colisão
flag_atr = 0   # Flag para verificação da inclusão de resistência do ar
flag_calc = 0  # Flag para verificação do cálculo de uma nova velocidade

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
sliderVel_y = 100

const_omega = 0.025 # Constante de multiplicação para o slider

sliderVel_rect = pygame.Rect(sliderVel_x, sliderVel_y, slider_tam, slider_h)  
sliderVel_handle = pygame.Rect(sliderVel_x+(vel_inicial*2), sliderVel_y-5, 20, 20)  
sliderVel_min = sliderVel_x
sliderVel_max = sliderVel_x + slider_tam

sliderAtr_x = 650
sliderAtr_y = 100

sliderAtr_rect = pygame.Rect(sliderAtr_x, sliderAtr_y, slider_tam, slider_h)  
sliderAtr_handle = pygame.Rect(sliderAtr_x+(omega_*(1/const_omega)), sliderAtr_y-5, 20, 20)  
sliderAtr_min = sliderAtr_x
sliderAtr_max = sliderAtr_x + slider_tam  

# Configuração do botão de ativar atrito
botaoAtr_x = 70
botaoAtr_y = 160
botaoAtr_comp = 300
botaoAtr_h = 40
botaoAtr_rect = pygame.Rect(botaoAtr_x, botaoAtr_y, botaoAtr_comp, botaoAtr_h)

# Configuração do botão de calcular a velocidade recomendada
botaoCalcular_x = 670
botaoCalcular_y = 160
botaoCalcular_comp = 220
botaoCalcular_h = 40
botaoCalcular_rect = pygame.Rect(botaoCalcular_x, botaoCalcular_y, botaoCalcular_comp, botaoCalcular_h)

# Configuração do botão de ativar obstáculo
botaoObst_x = 420
botaoObst_y = 160
botaoObst_comp = 200
botaoObst_h = 40
botaoObst_rect = pygame.Rect(botaoObst_x, botaoObst_y, botaoObst_comp, botaoObst_h)

textAng_x = 350
textAng_y = 100

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
     
     if flag_atr == 1:
          # Cálculo com resistência do ar
          pos_x = (vel_inicial*numpy.cos(angulo_rad)*(1-numpy.exp(-omega*tempo)))/omega
          pos_y = (1/omega)*(vel_inicial*numpy.sin(angulo_rad) + (g/omega))*(1-numpy.exp(-omega*tempo)) - (g/omega)*tempo
     else:
          # Cálculo sem resistência do ar
          pos_x = vel_inicial*numpy.cos(angulo_rad)*tempo
          pos_y = vel_inicial*numpy.sin(angulo_rad)*tempo - ((g*numpy.power(tempo, 2))/2)

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
     global colisao, omega, pos_bola_conv
     pos_bola = calcula_trajetoria(tempo)
     pos_bola_conv = (pos_bola[0] + origem_canhao[0], (altura_display - pos_bola[1]) - 27)

     cor_tela = (153, 201, 239)
     tela.fill(cor_tela)
     desenhar_seta(origem_canhao, comp_seta)
     desenha_slider_vel()
     texto_Vel(vel_inicial)

     texto_Info()
     texto_Ang(angulo)
     desenha_quadrado()
     desenha_barco()

     if flag_obst == 1:
          texto_botaoObst = "Remover Obstáculo"
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
     else:
          texto_botaoObst = "Adicionar Obstáculo"

     if flag_atr == 1:
          desenha_slider_atr()
          texto_botaoAtr = "Retirar resistência do ar (bônus)"
          texto_Atr(omega_)
     else:
          omega = 0.00001
          texto_botaoAtr = "Adicionar resistência do ar (bônus)"
          desenha_botao_calcularVel("Calcular velocidade")
          if flag_calc == 1:
               texto_novaVel(nova_vel)

     desenha_botao_atr(texto_botaoAtr)
     desenha_botao_obst(texto_botaoObst)

     if acerto == 1:
          texto_acerto()

     pygame.draw.circle(tela, cor, pos_bola_conv, raio_bola)

     # Rotaciona a imagem, centraliza com o canhão e publica
     imagem_rotacionada = pygame.transform.rotate(img_canhao, angulo_-45)
     rect = imagem_rotacionada.get_rect(center=origem_canhao)
     tela.blit(imagem_rotacionada, rect.topleft)

def desenha_botao_atr(texto):
     """
     Desenha o botão e o texto de ativar/desativar a resistência do ar em sua posição predefinida.

     Não possui parâmetros ou retorno.
     """
     font = pygame.font.SysFont("Arial", 18)
     text_color = pygame.Color('black')
     button_text = font.render(texto, True, text_color)

     mouse_pos = pygame.mouse.get_pos()
     botao_cor = pygame.Color(235,207,95) if botaoAtr_rect.collidepoint(mouse_pos) else pygame.Color(252,221,98)

     pygame.draw.rect(tela, botao_cor, botaoAtr_rect, border_radius=10)  # Desenha o botão
     text_rect = button_text.get_rect(center=botaoAtr_rect.center)
     tela.blit(button_text, text_rect)  # Adiciona o texto no botão

def desenha_botao_calcularVel(texto):
     """
     Desenha o botão e o texto de calcular a velocidade recomendada.

     Não possui parâmetros ou retorno.
     """
     font = pygame.font.SysFont("Arial", 18)
     text_color = pygame.Color('black')
     button_text = font.render(texto, True, text_color)

     mouse_pos = pygame.mouse.get_pos()
     botao_cor = pygame.Color(235,207,95) if botaoCalcular_rect.collidepoint(mouse_pos) else pygame.Color(252,221,98)

     pygame.draw.rect(tela, botao_cor, botaoCalcular_rect, border_radius=10)  # Desenha o botão
     text_rect = button_text.get_rect(center=botaoCalcular_rect.center)
     tela.blit(button_text, text_rect)  # Adiciona o texto no botão

def desenha_botao_obst(texto):
     """
     Desenha o botão e o texto de ativar/desativar o obstáculo em sua posição predefinida.

     Não possui parâmetros ou retorno.
     """
     font = pygame.font.SysFont("Arial", 18)
     text_color = pygame.Color('black')
     button_text = font.render(texto, True, text_color)

     mouse_pos = pygame.mouse.get_pos()
     botao_cor = pygame.Color(235,207,95) if botaoObst_rect.collidepoint(mouse_pos) else pygame.Color(252,221,98)

     pygame.draw.rect(tela, botao_cor, botaoObst_rect, border_radius=10)  # Desenha o botão
     text_rect = button_text.get_rect(center=botaoObst_rect.center)
     tela.blit(button_text, text_rect)  # Adiciona o texto no botão

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
          x_rot = px * numpy.cos(angulo_seta_rad) - py * numpy.sin(angulo_seta_rad)
          y_rot = px * numpy.sin(angulo_seta_rad) + py * numpy.cos(angulo_seta_rad)
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

def texto_Ang(value):
    """
    Exibe o valor atual do ângulo do canhõa em relação a terra.

    Parâmetros:
    - value (float): Ângilo em graus.

    Não possui retorno.
    """
    font = pygame.font.SysFont("Arial", 20)
    text = font.render(f'Ângulo do canhão: {value:.1f}°', True, (0, 0, 0))
    tela.blit(text, (textAng_x, textAng_y)) 

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

def texto_novaVel(value):
    """
    Exibe o valor da velocidade recomendada para acertar o alvo.

    Parâmetros:
    - value (float): Velocidade inicial em m/s.

    Não possui retorno.
    """
    font = pygame.font.SysFont("Arial", 18)
    text = font.render(f'Velocidade recomendada: {value:.1f} m/s', True, (0, 0, 0))
    tela.blit(text, (640, 210)) 

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
    pos_x = 280
    pos_y = 20
    tela.blit(text, (pos_x, pos_y)) # Posição do texto
    tela.blit(text2, (pos_x+70, pos_y+30)) # Posição do texto

def texto_acerto():
    """
    Exibe um texto indicando que acertou o alvo no canto superior da tela.

    Não possui parâmetros ou retorno.
    """
    font = pygame.font.SysFont("Arial", 20)
    text = font.render(f'Você acertou o alvo!', True, "red")
    tela.blit(text, (400, 210)) # Posição do texto

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


def reiniciar():
     """
     Para a simulação e reseta a contagem de tempo, para retornar a bolinha
     na posição correta.

     Não possui parâmetros ou retorno.
     """
     global contar_tempo, tempo
     contar_tempo = False  # para a simulação
     tempo = 0  # reseta o tempo
     
def main():
     """
     Função principal que inicializa o programa, gerencia o loop principal e 
     controla a interação do usuário com a simulação.

     Não possui parâmetros ou retorno.
     """
     global flag_calc, nova_vel, ang_ref, vel_ref, flag_atr, flag_obst, acerto, angulo, angulo_, tempo, vel_inicial, vel_inicial_, omega, omega_, cor, pos_bola_conv, contar_tempo, pontuacao, flag, colisao
     sair = False
     dragging_vel = False
     dragging_atr = False
     incremento_angulo = 0.25

     while sair == False:
          desenha_tela()
          
          # Atualiza o angulo da trajetória da bola
          if contar_tempo == 0:
               vel_inicial = vel_inicial_
               angulo = angulo_
               omega = omega_
               colisao = 0

          if colisao_alvo():
               reiniciar()
               flag = 1
               acerto = 1

          elif colisao == 1 or pos_bola_conv[1] > altura_display or pos_bola_conv[0] > largura_display:
               reiniciar()

          if contar_tempo == True:
               tempo += clock.get_time() / 300    

          eventos = pygame.event.get()
          for evento in eventos:
               if evento.type == pygame.QUIT:  # Fechar o programa
                    sair = True

               if evento.type == pygame.MOUSEBUTTONDOWN:             
                    if botaoAtr_rect.collidepoint(evento.pos):  # Verifica se clicou no botão de atrito
                         flag_atr = not flag_atr
                    if botaoObst_rect.collidepoint(evento.pos):  # Verifica se clicou no botão de obstáculo
                         flag_obst = not flag_obst

                    if botaoCalcular_rect.collidepoint(evento.pos):  # Verifica se clicou no botão de calcular velocidade
                         ang_ref_rad = numpy.radians(ang_ref)
                         angulo_rad = numpy.radians(angulo_)

                         nova_vel = vel_ref * numpy.sqrt((numpy.cos(ang_ref_rad)*numpy.sin(ang_ref_rad))/(numpy.cos(angulo_rad)*numpy.sin(angulo_rad)))    
                         flag_calc = True

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
                         vel_inicial_ = round((new_x_vel - sliderVel_min) / slider_tam * slider_range / slider_increment) * slider_increment

                         
                    if dragging_atr:
                         new_x_atr = max(sliderAtr_min, min(evento.pos[0], sliderAtr_max - sliderAtr_handle.width))
                         sliderAtr_handle.x = new_x_atr
                         omega_ = max(0.001, (new_x_atr - sliderAtr_min)*const_omega)   # Ajusta o atrito do ar

          teclas = pygame.key.get_pressed()

          # Controle de ângulo e disparo
          if teclas[pygame.K_UP] and angulo_ < 90:     
               angulo_ += incremento_angulo
               flag_calc = False

          if teclas[pygame.K_DOWN] and angulo_ > 0:
               angulo_ -= incremento_angulo
               flag_calc = False
          
          if teclas[pygame.K_SPACE]:
               contar_tempo = True
               acerto = 0

          pygame.display.flip()
          clock.tick(60)
                    
     pygame.quit()           

if __name__ == "__main__":
    main()
