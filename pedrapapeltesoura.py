from pygame import *
import sys
import random


init()

window = display.set_mode((1280,720))

running = True
clock=time.Clock()

soma = 0
soma_adv = 0
timer = 0

escolha_ia = ["pedra", "papel", "tesoura"]
adversario = random.choice(escolha_ia)

escolha = input("escolha: ")

pedra_img = image.load("pedra.png")
pedra = transform.scale(pedra_img, (300,300))

papel_img = image.load("papel.webp")
papel = transform.scale(papel_img, (300,300))

tesoura_img = image.load("tesoura.png")
tesoura = transform.scale(tesoura_img, (310,190))

background_color = (112, 128, 144)
fonte = font.Font("fonte.ttf", 40)
chique = font.Font("fontechique.ttf", 60)
chique_pequena = font.Font("fontechique.ttf", 25)

def ia_pedra(escolha):
    global adversario
    if escolha == "pedra":
        result_empate = chique.render(f"Empate", True, (255,255,0))
        escolha_adversario = chique.render(f"A IA escolheu {adversario}", True, (255,255,0))
        window.blit(result_empate, (600,200))
        window.blit(escolha_adversario, (600,300))
    elif escolha == "papel":
        result_vit = chique.render(f"VOCE GANHOU!!!", True, (255,255,0))
        escolha_adversario = chique.render(f"A IA escolheu {adversario}", True, (255,255,0))
        window.blit(result_vit, (600,200))
        window.blit(escolha_adversario, (600,300))
        soma +=1
    elif escolha == "tesoura":
        result_derrota = chique.render(f"voce perdeu :(", True, (255,255,0))
        escolha_adversario = chique.render(f"A IA escolheu {adversario}", True, (255,255,0))
        window.blit(result_derrota, (600,200))
        window.blit(escolha_adversario, (600,300))
        soma_adv +=1


def ia_papel(escolha):
    global adversario
    if escolha == "pedra":
        result_derrota = chique.render(f"voce perdeu :(", True, (255,255,0))
        escolha_adversario = chique.render(f"A IA escolheu {adversario}", True, (255,255,0))
        window.blit(result_derrota, (600,200))
        window.blit(escolha_adversario, (600,300))
        timer -=1
        soma_adv +=1
    if escolha == "papel":
        result_empate = chique.render(f"Empate", True, (255,255,0))
        escolha_adversario = chique.render(f"A IA escolheu {adversario}", True, (255,255,0))
        window.blit(result_empate, (600,200))
        window.blit(escolha_adversario, (600,300))
        timer -=1
    elif escolha == "tesoura":
        result_vit = chique.render(f"VOCE GANHOU!!!", True, (255,255,0))
        escolha_adversario = chique.render(f"A IA escolheu {adversario}", True, (255,255,0))
        window.blit(result_vit, (600,200))
        window.blit(escolha_adversario, (600,300))
        timer -=1
        soma +=1


def ia_tesoura(escolha):
    global adversario
    if escolha == "pedra":
        result_vit = chique.render(f"VOCE GANHOU!!!", True, (255,255,0))
        escolha_adversario = chique.render(f"A IA escolheu {adversario}", True, (255,255,0))
        window.blit(result_vit, (600,200))
        window.blit(escolha_adversario, (600,300))
        soma +=1
    elif escolha == "papel":
        result_derrota = chique.render(f"voce perdeu :(", True, (255,255,0))
        escolha_adversario = chique.render(f"A IA escolheu {adversario}", True, (255,255,0))
        window.blit(result_derrota, (600,200))
        window.blit(escolha_adversario, (600,300))
        soma_adv +=1
    elif escolha == "tesoura":
        result_empate = chique.render(f"Empate", True, (255,255,0))
        escolha_adversario = chique.render(f"A IA escolheu {adversario}", True, (255,255,0))
        window.blit(result_empate, (600,200))
        window.blit(escolha_adversario, (600,300))


while running:
    clock.tick(60)
    key_pressed = key.get_pressed()
    window.fill(background_color)
    mouse_x, mouse_y = mouse.get_pos()

    for ev in event.get():
        if ev.type == QUIT:
            quit()
            running = False
            sys.exit()
    
    choice_ia = chique.render(f"{adversario}", True, (255,255,0))
    window.blit(choice_ia, (600,0))

    texto_base = chique.render(f"escolha:", True, (255,255,255))
    window.blit(texto_base, (600,100))

    draw.rect(window, (120, 120, 120), (100, 300,350,300))
    draw.rect(window, (120, 120, 120), (500, 300,350,300))
    draw.rect(window, (120, 120, 120), (900, 300,350,300))

    draw.rect(window, (0, 0, 0), (100, 300,350,300),5)
    draw.rect(window, (0, 0, 0), (500, 300,350,300),5)
    draw.rect(window, (0, 0, 0), (900, 300,350,300),5)

    window.blit(pedra, (130,300))
    window.blit(papel, (530,300))
    window.blit(tesoura, (930,350))

    if escolha_ia == pedra:
        timer = 240
        ia_pedra(escolha)
    
    if escolha_ia == papel:
        timer = 240
        ia_papel(escolha)
    
    if escolha_ia == tesoura:
        timer = 240
        ia_tesoura(escolha)






    display.update()