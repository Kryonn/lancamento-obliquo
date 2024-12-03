# Adicionar documentação!!!

import pygame # type: ignore
import numpy
import math

# Variáveis
pontuacao = 0
altura_display = 600
largura_display = 1000

altura_seta = 10
largura_seta = 10
comp_seta = 60

angulo_ = 45 # Angulo em tempo real
angulo = 45
raio_bola = (0.5*20)
origem_canhao = (37, altura_display - 27)
pos_bola_conv = (origem_canhao[0], origem_canhao[1])
contar_tempo = False
cor = "red"

tempo = 0
omega = 0.4 # atrito do ar
vel_inicial = 20   
vel_inicial_ = 20   # velocidade em tempo real
g = 9.8
flag = 0

colisao = False
obstaculo_x = 450
obstaculo_y = 400
obstaculo_larg = 100
obstaculo_alt = altura_display - obstaculo_y

# Configuração do pygame
pygame.init()
tela = pygame.display.set_mode((largura_display, altura_display))
pygame.display.set_caption("Lançamento Oblíquo com Resistência do Ar")
clock = pygame.time.Clock()

# Configuração da imagem
img_canhao = pygame.image.load('canhao.png')  # Substitua pelo nome correto do arquivo da seta
img_canhao = pygame.transform.scale(img_canhao, (60, 60))  # Ajuste o tamanho da seta, se necessário

# Funções

def calcula_trajetoria(tempo):
     angulo_rad = numpy.radians(angulo)

     pos_x = (vel_inicial*numpy.cos(angulo_rad)*(1-numpy.exp(-omega*tempo)))/omega
     pos_y = (1/omega)*(vel_inicial*numpy.sin(angulo_rad) + (g/omega))*(1-numpy.exp(-omega*tempo)) - (g/omega)*tempo

     # Ajusta para escala de visualização
     escala = 20
     pos_x *= escala
     pos_y *= escala

     return pos_x, pos_y

def desenha_tela():
    global colisao
    cor_tela = (153, 201, 239)
    tela.fill(cor_tela)
    desenhar_seta(origem_canhao, comp_seta)

    pygame.draw.circle(tela, cor, pos_bola_conv, raio_bola)

    # Rotaciona a imagem, centraliza com o canhão e publica
    imagem_rotacionada = pygame.transform.rotate(img_canhao, angulo_-45)
    rect = imagem_rotacionada.get_rect(center=origem_canhao)
    tela.blit(imagem_rotacionada, rect.topleft)

    desenha_slider_vel()
    texto_Vel(vel_inicial)

    desenha_slider_atr()
    texto_Atr(omega)
    desenha_quadrado()
    texto_Info()
    desenha_barco()

    # Desenha o obstáculo se necessário
    if flag == 1:
          obstaculo = pygame.Rect(obstaculo_x, obstaculo_y, obstaculo_larg, obstaculo_alt) 
          desenha_obstaculo(obstaculo)
          # Cria o retângulo da bola com base na posição e raio da bola
          bola_rect = pygame.Rect(
               pos_bola_conv[0] - raio_bola,  
               pos_bola_conv[1] - raio_bola,  
               raio_bola * 2,                 
               raio_bola * 2                  
          )

          # Verifica se há colisão entre a bola e o obstáculo
          if bola_rect.colliderect(obstaculo) == True:
               colisao = True


# Função para desenhar o alvo (barco)
def desenha_barco():
    barco_img = pygame.image.load('barco.png')  
    barco_img = pygame.transform.scale(barco_img, (180, 180))
    tela.blit(barco_img, (quad.x, quad.y-40))  

def desenhar_seta(origem, comp):
     angulo_rad = numpy.radians(angulo_)
     # Desenha a reta
     dest = (
          origem[0] + (comp*(numpy.cos(angulo_rad))), 
          origem[1] - (comp*(numpy.sin(angulo_rad)))
     )
     pygame.draw.line(tela, "black", origem, dest)

     # Seta sem rotação
     base_pontos = [
          (0, -altura_seta // 2),  # Ponta superior
          (-largura_seta // 2, altura_seta // 2),  # Inferior esquerdo
          (largura_seta // 2, altura_seta // 2)  # Inferior direito
     ]

     angulo_seta = angulo_ + 90
     angulo_seta_rad = numpy.radians(angulo_seta)

     # Seta rotacionada
     pontos_rotacionados = []
     for px, py in base_pontos:
          x_rot = px * math.cos(angulo_seta_rad) - py * math.sin(angulo_seta_rad)
          y_rot = px * math.sin(angulo_seta_rad) + py * math.cos(angulo_seta_rad)
          pontos_rotacionados.append((x_rot + dest[0], -y_rot + dest[1]))  # Ajusta para o centro (x, y)

     # Desenha o polígono
     pygame.draw.polygon(tela, "black", pontos_rotacionados)


# Variáveis do slider para velocidade inicial
slider_tam = 200
slider_h = 10
sliderVel_x = 50
sliderVel_y = 50

sliderVel_rect = pygame.Rect(sliderVel_x, sliderVel_y, slider_tam, slider_h)  # Posição e tamanho da barra
sliderVel_handle = pygame.Rect(sliderVel_x+(vel_inicial*2), sliderVel_y-5, 20, 20)  # Controle do slider
sliderVel_min = sliderVel_x
sliderVel_max = sliderVel_x + slider_tam  # Valores mínimo e máximo do slider

# Variáveis do slider para resistência do ar
sliderAtr_x = 50
sliderAtr_y = 120

sliderAtr_rect = pygame.Rect(sliderAtr_x, sliderAtr_y, slider_tam, slider_h)  # Posição e tamanho da barra
sliderAtr_handle = pygame.Rect(sliderAtr_x+(omega*20), sliderAtr_y-5, 20, 20)  # Controle do slider
sliderAtr_min = sliderAtr_x
sliderAtr_max = sliderAtr_x + slider_tam  # Valores mínimo e máximo do slider

# Quadrado alvo
quad = pygame.Rect(800, 500, 50, 50)
# obstaculo = pygame.Rect(obstaculo_x, obstaculo_y, obstaculo_larg, obstaculo_larg) 

def desenha_quadrado():
     pygame.draw.rect(tela, "black", quad)

def desenha_obstaculo(obstaculo):
     pygame.draw.rect(tela, "black", obstaculo)
     palmeira_img = pygame.image.load('palmeira.png')  # Carrega a imagem da palmeira
     palmeira_img = pygame.transform.scale(palmeira_img, (250, 300))  # Ajusta o tamanho da imagem para o tamanho do obstáculo
     tela.blit(palmeira_img, (obstaculo.x-80, obstaculo.y-20))  # Desenha a imagem na posição do obstáculo

# Função para desenhar o slider
def desenha_slider_vel():
    pygame.draw.rect(tela, "gray", sliderVel_rect)  # Barra do slider
    pygame.draw.rect(tela, "red", sliderVel_handle)  # Controle do slider

def desenha_slider_atr():
    pygame.draw.rect(tela, "gray", sliderAtr_rect)  # Barra do slider
    pygame.draw.rect(tela, "red", sliderAtr_handle)  # Controle do slider


# Funções para renderizar os textos
def texto_Vel(value):
    font = pygame.font.SysFont("Arial", 20)
    text = font.render(f'Velocidade Inicial: {value:.1f} m/s', True, (0, 0, 0))
    tela.blit(text, (sliderVel_x + slider_tam // 2 - text.get_width() // 2, sliderVel_y + slider_h + 10)) # Posição do texto

def texto_Atr(value):
    font = pygame.font.SysFont("Arial", 20)
    text = font.render(f'Resistência do Ar: {value:.1f} s⁻¹', True, (0, 0, 0))
    tela.blit(text, (sliderAtr_x + slider_tam // 2 - text.get_width() // 2, sliderAtr_y + slider_h + 10)) # Posição do texto

def texto_Info():
    font = pygame.font.SysFont("Arial", 20)
    text = font.render(f'Pressione ESPAÇO para atirar!', True, (0, 0, 0))
    tela.blit(text, (350, 30)) # Posição do texto

# Funções para verificar as colisões
def colisao_alvo():
    # Cria o retângulo da bola com base na posição e raio da bola
    bola_rect = pygame.Rect(
        pos_bola_conv[0] - raio_bola,  
        pos_bola_conv[1] - raio_bola,  
        raio_bola * 2,                 
        raio_bola * 2                  
    )

    # Verifica colisão
    return pygame.Rect.colliderect(quad, bola_rect)

def colisao_obst():
    # Cria o retângulo da bola com base na posição e raio da bola
    bola_rect = pygame.Rect(
        pos_bola_conv[0] - raio_bola,  
        pos_bola_conv[1] - raio_bola,  
        raio_bola * 2,                 
        raio_bola * 2                  
    )

    # Cria o retângulo do obstáculo
    obstaculo = pygame.Rect(obstaculo_x, obstaculo_y, obstaculo_larg, obstaculo_alt) 
    
    # Debugging: verifique as posições
    print(f"Bola: {bola_rect}, Obstáculo: {obstaculo}")
    
    # Verifica se há colisão entre o retângulo da bola e o retângulo do obstáculo
    return bola_rect.colliderect(obstaculo)


def main():
     global angulo, angulo_, tempo, vel_inicial, vel_inicial_, omega, cor, pos_bola_conv, contar_tempo, pontuacao, flag, colisao
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
                    if sliderVel_handle.collidepoint(evento.pos):  # Verifica se clicou no controle
                         dragging_vel = True
                    if sliderAtr_handle.collidepoint(evento.pos):  # Verifica se clicou no controle
                         dragging_atr = True
               if evento.type == pygame.MOUSEBUTTONUP:
                    dragging_vel = False
                    dragging_atr = False
               if evento.type == pygame.MOUSEMOTION:
                    if dragging_vel:
                         # Atualizar a posição do controle do slider
                         new_x_vel = max(sliderVel_min, min(evento.pos[0], sliderVel_max - sliderVel_handle.width))
                         sliderVel_handle.x = new_x_vel
                         vel_inicial_ = (new_x_vel - sliderVel_min)*0.5
                    if dragging_atr:
                         # Atualizar a posição do controle do slider
                         new_x_atr = max(sliderAtr_min, min(evento.pos[0], sliderAtr_max - sliderAtr_handle.width))
                         sliderAtr_handle.x = new_x_atr
                         omega = max(0.001, (new_x_atr - sliderAtr_min)*0.05)

          teclas = pygame.key.get_pressed()

          if teclas[pygame.K_UP] and angulo_ < 90:
               angulo_ += 1

          if teclas[pygame.K_DOWN] and angulo_ > 0:
               angulo_ -= 1
          
          if teclas[pygame.K_SPACE]:
               contar_tempo = True

          pygame.display.flip()
          clock.tick(60)
                    
     pygame.quit()           

if __name__ == "__main__":
    main()
