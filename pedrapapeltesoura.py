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
escolha = ""
escolha_ia = ["pedra", "papel", "tesoura"]
adversario = random.choice(escolha_ia)

#escolha = input("escolha: ")

pedra_img = image.load("pedra.png")
pedra = transform.scale(pedra_img, (300,300))

papel_img = image.load("papel.webp")
papel = transform.scale(papel_img, (300,300))

tesoura_img = image.load("tesoura.png")
tesoura = transform.scale(tesoura_img, (310,190))

background_color = (112, 128, 144)
fonte = font.Font("fonte.ttf", 40)
chique = font.Font("fontechique.ttf", 60)
chique_pequena = font.Font("fontechique.ttf", 35)

def ia_pedra(escolha):
    global adversario, timer, soma, soma_adv
    if timer > 0:
        if escolha == "pedra":
            if timer > 0:
                result_empate = chique.render(f"empate", True, (255,255,0))
                escolha_adversario = chique.render(f"a ia escolheu {adversario}", True, (255,255,0))
                window.blit(result_empate, (600,200))
                window.blit(escolha_adversario, (490,20))
                draw.rect(window, (255, 255, 0), (100, 300,350,300))
                draw.rect(window, (0, 0, 0), (100, 300,350,300),5)
                timer -=1
            if timer == 0:
                    reiniciar_jogo()
        elif escolha == "papel":
            if timer > 0:
                result_vit = chique.render(f"voce ganhou!!!", True, (0,255,0))
                escolha_adversario = chique.render(f"a ia escolheu {adversario}", True, (255,255,0))
                window.blit(result_vit, (530,200))
                window.blit(escolha_adversario, (490,20))
                draw.rect(window, (0, 255, 0), (500, 300,350,300))
                draw.rect(window, (0, 0, 0), (500, 300,350,300),5)
                timer -=1
            if timer == 239:
                    soma +=1
            if timer == 0:
                    reiniciar_jogo()
        elif escolha == "tesoura":
            if timer > 0:
                result_derrota = chique.render(f"voce perdeu :(", True, (255,0,0))
                escolha_adversario = chique.render(f"a ia escolheu {adversario}", True, (255,255,0))
                window.blit(result_derrota, (550,200))
                window.blit(escolha_adversario, (490,20))
                draw.rect(window, (255, 0, 0), (900, 300,350,300))
                draw.rect(window, (0, 0, 0), (900, 300,350,300),5)
                timer -=1
            if timer == 239:
                    soma_adv +=1
            if timer == 0:
                reiniciar_jogo()



def ia_papel(escolha):
    global adversario, timer, soma, soma_adv
    if timer > 0:
        if escolha == "pedra":
            if timer > 0:
                result_derrota = chique.render(f"voce perdeu :(", True, (255,0,0))
                escolha_adversario = chique.render(f"a ia escolheu {adversario}", True, (255,255,0))
                window.blit(result_derrota, (550,200))
                window.blit(escolha_adversario, (490,20))
                draw.rect(window, (255, 0, 0), (100, 300,350,300))
                draw.rect(window, (0, 0, 0), (100, 300,350,300),5)
                timer -=1
            if timer == 239:
                soma_adv +=1
            if timer == 0:
                reiniciar_jogo()
        if escolha == "papel":
                if timer > 0:
                    result_empate = chique.render(f"empate", True, (255,255,0))
                    escolha_adversario = chique.render(f"a ia escolheu {adversario}", True, (255,255,0))
                    window.blit(result_empate, (600,200))
                    window.blit(escolha_adversario, (490,20))
                    draw.rect(window, (255, 255, 0), (500, 300,350,300))
                    draw.rect(window, (0, 0, 0), (500, 300,350,300),5)
                    timer -=1
                if timer == 0:
                    reiniciar_jogo()
        elif escolha == "tesoura":
            if timer > 0:
                result_vit = chique.render(f"voce ganhou!!!", True, (0,255,0))
                escolha_adversario = chique.render(f"a ia escolheu {adversario}", True, (255,255,0))
                window.blit(result_vit, (530,200))
                window.blit(escolha_adversario, (490,20))
                draw.rect(window, (0, 255, 0), (900, 300,350,300))
                draw.rect(window, (0, 0, 0), (900, 300,350,300),5)
                timer -=1
            if timer == 239:
                soma +=1
            if timer == 0:
                    reiniciar_jogo()
    


def ia_tesoura(escolha):
    global adversario, timer, soma, soma_adv
    if timer > 0:
        if escolha == "pedra":
            if timer > 0:
                result_vit = chique.render(f"voce ganhou!!!", True, (0,255,0))
                escolha_adversario = chique.render(f"a ia escolheu {adversario}", True, (255,255,0))
                window.blit(result_vit, (530,200))
                window.blit(escolha_adversario, (490,20))
                draw.rect(window, (0, 255, 0), (100, 300,350,300))
                draw.rect(window, (0, 0, 0), (100, 300,350,300),5)
                timer -=1
            if timer == 239:
                soma +=1
            if timer == 0:
                reiniciar_jogo()
        elif escolha == "papel":
            if timer > 0:
                result_derrota = chique.render(f"voce perdeu :(", True, (255,0,0))
                escolha_adversario = chique.render(f"a ia escolheu {adversario}", True, (255,255,0))
                window.blit(result_derrota, (550,200))
                window.blit(escolha_adversario, (490,20))
                draw.rect(window, (255, 0, 0), (500, 300,350,300))
                draw.rect(window, (0, 0, 0), (500, 300,350,300),5)
                timer -=1
            if timer == 239:
                soma_adv +=1
            if timer == 0:
                reiniciar_jogo()
        elif escolha == "tesoura":
            if timer > 0:
                result_empate = chique.render(f"empate", True, (255,255,0))
                escolha_adversario = chique.render(f"a ia escolheu {adversario}", True, (255,255,0))
                window.blit(result_empate, (600,200))
                window.blit(escolha_adversario, (490,20))
                draw.rect(window, (255, 255, 0), (900, 300,350,300))
                draw.rect(window, (0, 0, 0), (900, 300,350,300),5)
                timer -=1
            if timer == 0:
                reiniciar_jogo()


def reiniciar_jogo():
    global adversario, timer, escolha
    escolha = ""
    adversario = random.choice(escolha_ia)


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

        if timer == 0:
            if ev.type == MOUSEBUTTONDOWN:
                    if 100<mouse_x<450 and 300<mouse_y<600:
                        if ev.button == 1:
                            escolha = "pedra"
                            timer = 240
                            draw.rect(window, (255, 0, 0), (100, 300,350,300))

                
            if ev.type == MOUSEBUTTONDOWN:
                    if 500<mouse_x<850 and 300<mouse_y<600:
                        if ev.button == 1:
                            escolha = "papel"
                            timer = 240

            
            if ev.type == MOUSEBUTTONDOWN:
                    if 900<mouse_x<1250 and 300<mouse_y<600:
                        if ev.button == 1:
                            escolha = "tesoura"
                            timer = 240

    #choice_ia = chique.render(f"ia escolheu {adversario}", True, (255,255,0))
    #window.blit(choice_ia, (600,0))

    texto_base = chique.render(f"escolha:", True, (255,255,255))
    window.blit(texto_base, (600,100))

    pontos = chique_pequena.render(f"Pontos: {soma}", True, (255,255,255))
    window.blit(pontos, (50,100))

    pontos_ia = chique_pequena.render(f"Pontos ia: {soma_adv}", True, (255,255,255))
    window.blit(pontos_ia, (50,200))

    draw.rect(window, (120, 120, 120), (100, 300,350,300))
    draw.rect(window, (120, 120, 120), (500, 300,350,300))
    draw.rect(window, (120, 120, 120), (900, 300,350,300))

    draw.rect(window, (0, 0, 0), (100, 300,350,300),5)
    draw.rect(window, (0, 0, 0), (500, 300,350,300),5)
    draw.rect(window, (0, 0, 0), (900, 300,350,300),5)

    

    #print(timer)
    #print(mouse_x, mouse_y)

    if adversario == "pedra":
        ia_pedra(escolha)
    
    if adversario == "papel":
        ia_papel(escolha)
    
    if adversario == "tesoura":
        ia_tesoura(escolha)

    window.blit(pedra, (130,300))
    window.blit(papel, (530,300))
    window.blit(tesoura, (930,350))

    display.update()