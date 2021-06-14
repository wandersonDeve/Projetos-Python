###   Importar modulos  ###
import pygame
import random

pygame.init()

###   TUPLAS COM CORES RGB  ###
azul = (0,0,128)
laranja = (205,102,0)
cinza = (25,25,25)
vermelho = (255,0,0)
ouro = (218,165,32)

###   DEFININDO AS DIMENSÕES DA TELA    ###
dimensoes = (600,600)

###   VALORES INICIAIS  ###
x = 300
y = 300
d = 20
x_comida = round(random.randrange(0,600-d)/20)*20
y_comida = round(random.randrange(0,600-d)/20)*20
x_barreira = 601
y_barreira = 601
fonte = pygame.font.SysFont('hack',25)
lista_cobra = [[x,y]]

dx = 0
dy = 0

tela = pygame.display.set_mode((dimensoes))
pygame.display.set_caption("Wand's Snake")

tela.fill(cinza)

clock = pygame.time.Clock()

def desenha_cobra(lista_cobra):
    tela.fill(cinza)
    for unidade in lista_cobra:
        pygame.draw.rect(tela,vermelho,[unidade[0],unidade[1],d,d])

def mover_cobra(dx, dy, lista_cobra):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -d
                dy = 0
            elif event.key == pygame.K_RIGHT:
                dx = d
                dy = 0
            elif event.key == pygame.K_UP:
                dx = 0
                dy = -d
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = d
    x_novo = lista_cobra[-1][0] + dx
    y_novo = lista_cobra[-1][1] + dy

    lista_cobra.append([x_novo,y_novo])
    del lista_cobra[0]

    return dx, dy, lista_cobra

def verifica_comida(dx,dy,x_comida,y_comida, lista_cobra):
    head = lista_cobra[-1]
    x_novo = head[0] + dx
    y_novo = head[1] + dy
    if head[0] == x_comida and head[1] == y_comida:
        x_comida = round(random.randrange(0,600-d)/20)*20
        y_comida = round(random.randrange(0,600-d)/20)*20
        lista_cobra.append([x_novo,y_novo])
    pygame.draw.rect(tela,azul,[x_comida,y_comida,d,d])
    return x_comida, y_comida, lista_cobra

def verifica_parede(lista_cobra,x_barreira,y_barreira):
    head = lista_cobra[-1]
    x = head[0]
    y = head[1]
    if x not in range(600) or y not in range(600):
        raise Exception
    if x == x_barreira and y == y_barreira:
        raise Exception

def verifica_mordeu_cobra(lista_cobra):
    head = lista_cobra[-1]
    corpo = lista_cobra.copy()

    del corpo[-1]
    for x,y in corpo:
        if x == head[0] and y == head[1]:
            raise Exception

def atualizar_pontos(lista_cobra):
    pts = str(len(lista_cobra))
    score = fonte.render('Pontuação: ' + pts,True, ouro)
    tela.blit(score,[0,0])

while True:
    pygame.display.update()
    desenha_cobra(lista_cobra)
    dx, dy, lista_cobra = mover_cobra(dx, dy, lista_cobra)
    x_comida, y_comida, lista_cobra = verifica_comida(dx,dy,x_comida,y_comida, lista_cobra)
    verifica_parede(lista_cobra,x_barreira,y_barreira)
    verifica_mordeu_cobra(lista_cobra)
    atualizar_pontos(lista_cobra)
    clock.tick(10)
    print(lista_cobra)
