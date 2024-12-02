# Adicionar documentação!!!

import pygame # type: ignore
import numpy
import math

# Variáveis
altura_display = 600
largura_display = 1000

altura_seta = 10
largura_seta = 10
comp_seta = 60

raio_bola = (0.5*20)
origem_canhao = (37, altura_display - 27)
angulo = 45
pos_bola_conv = (origem_canhao[0], origem_canhao[1])
contar_tempo = False

tempo = 0
omega = 0.4 # atrito do ar
vel_inicial = 20   
g = 9.8

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
     tela.fill((0, 224, 243))
     desenhar_seta(origem_canhao, comp_seta)

     pos_bola = calcula_trajetoria(tempo)
     pos_bola_conv = (pos_bola[0] + origem_canhao[0], (altura_display - pos_bola[1]) - 27)
     pygame.draw.circle(tela, "red", pos_bola_conv, raio_bola)

     # Rotaciona a imagem, centraliza com o canhão e publica
     imagem_rotacionada = pygame.transform.rotate(img_canhao, angulo-45)
     rect = imagem_rotacionada.get_rect(center=origem_canhao)
     tela.blit(imagem_rotacionada, rect.topleft)

     desenha_slider_vel()
     desenha_textVel(vel_inicial)

     desenha_slider_atr()
     desenha_textAtr(omega)
     desenha_quadrado()

def desenhar_seta(origem, comp):
     angulo_rad = numpy.radians(angulo)
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

     angulo_seta = angulo + 90
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
sliderVel_handle = pygame.Rect(sliderVel_x, sliderVel_y-5, 20, 20)  # Controle do slider
sliderVel_min = sliderVel_x
sliderVel_max = sliderVel_x + slider_tam  # Valores mínimo e máximo do slider

# Variáveis do slider para resistência do ar
sliderAtr_x = 50
sliderAtr_y = 120

sliderAtr_rect = pygame.Rect(sliderAtr_x, sliderAtr_y, slider_tam, slider_h)  # Posição e tamanho da barra
sliderAtr_handle = pygame.Rect(sliderAtr_x, sliderAtr_y-5, 20, 20)  # Controle do slider
sliderAtr_min = sliderAtr_x
sliderAtr_max = sliderAtr_x + slider_tam  # Valores mínimo e máximo do slider

# Quadrado alvo
quad = pygame.Rect(800, 500, 20, 20)

def desenha_quadrado():
     pygame.draw.rect(tela, "black", quad)

# Função para desenhar o slider
def desenha_slider_vel():
    pygame.draw.rect(tela, "gray", sliderVel_rect)  # Barra do slider
    pygame.draw.rect(tela, "red", sliderVel_handle)  # Controle do slider

def desenha_slider_atr():
    pygame.draw.rect(tela, "gray", sliderAtr_rect)  # Barra do slider
    pygame.draw.rect(tela, "red", sliderAtr_handle)  # Controle do slider


# Função para renderizar o texto
def desenha_textVel(value):
    font = pygame.font.SysFont("Arial", 20)
    text = font.render(f'Velocidade Inicial: {value:.2f}', True, (0, 0, 0))
    tela.blit(text, (sliderVel_x + slider_tam // 2 - text.get_width() // 2, sliderVel_y + slider_h + 10)) # Posição do texto

def desenha_textAtr(value):
    font = pygame.font.SysFont("Arial", 20)
    text = font.render(f'Resistência do Ar: {value:.2f}', True, (0, 0, 0))
    tela.blit(text, (sliderAtr_x + slider_tam // 2 - text.get_width() // 2, sliderAtr_y + slider_h + 10)) # Posição do texto

def colisao():
    # Cria o retângulo da bola com base na posição e raio da bola
    bola_rect = pygame.Rect(
        pos_bola_conv[0] - raio_bola,  
        pos_bola_conv[1] - raio_bola,  
        raio_bola * 2,                 
        raio_bola * 2                  
    )
    # Verifica colisão
    return bola_rect.colliderect(quad)

def main():
     global angulo
     global tempo
     global vel_inicial
     global omega
     sair = False
     global contar_tempo
     dragging_vel = False
     dragging_atr = False
     while sair == False:
          desenha_tela()
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
                         vel_inicial = (new_x_vel - sliderVel_min)*0.5
                    if dragging_atr:
                         # Atualizar a posição do controle do slider
                         new_x_atr = max(sliderAtr_min, min(evento.pos[0], sliderAtr_max - sliderAtr_handle.width))
                         sliderAtr_handle.x = new_x_atr
                         omega = max(0.001, (new_x_atr - sliderAtr_min)*0.05)

          teclas = pygame.key.get_pressed()

          if teclas[pygame.K_UP] and angulo < 90:
               angulo += 1

          if teclas[pygame.K_DOWN] and angulo > 0:
               angulo -= 1
          
          if teclas[pygame.K_SPACE]:
               contar_tempo = True
          
          if teclas[pygame.K_r]:
               tempo = 0
               contar_tempo = False

          pygame.display.flip()
          clock.tick(60)
     
                    
     pygame.quit()  
                

if __name__ == "__main__":
    main()
