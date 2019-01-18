from visual import *
import numpy as np
from Tkinter import *

#Ping Pong Projeto física
scene.title = 'Ping Pong Game by Ana Santos, João Silva & Venera Aitkul'

#Função para reniciar o jogo ou para o fazer começar
def renicia():
    vZ= 0
    aZ= 1
    #Fica a espera que haja alguma ação para não sair do ciclo
    while True:
        rate(50)
        if scene.kb.keys: 
            key = scene.kb.getkey()
            if key == "c":
                comeca()
                game = True
                return
        
#Põe todos os objetos visiveis
def comeca():
    base.visible = True
    teto.visible= True
    chao.visible= True
    bola.visible= True
    bola2.visible= True
    paddle.visible= True
    paddle2.visible= True
    vi = velocidade * vector(random.randint(-5,-1),random.randint(-4,3),1)
    vi2 = velocidade * vector(random.randint(1,5),random.randint(-4,3),1)
    bola.velocity = vi
    bola2.velocity = vi2

    
#Propriedades do cenário
scene.height = 750
scene.width = 900
scene.range = 30
scene.background = color.gray(0.3)

#Cores objetos 3D
corcaixa = color.orange
corbola = color.white
corpaddle = color.yellow
corbase = color.black


#Desenhar
base = box(pos=(0,0,-2), size = (50,25,1), color=corbase)
base.visible = False
#Teto
teto = box(pos=(0,12,0), size = (50,1,10), color=corcaixa)
#Põe o objeto teto não visivel
teto.visible= False
#Chão
chao = box(pos=(0,-12,0), size = (50,1,10), color=corcaixa)
#Põe o objeto chao não visivel
chao.visible= False
#Bola
bola = sphere(pos=(0,5,0), radius=0.5)
#Põe o objeto bola não visivel
bola.visible= False
#Bola2
bola2 = sphere(pos=(0,-5,0), radius=0.5)
#Põe o objeto bola2 não visivel
bola2.visible= False
#Paddle
paddle = box(pos=(18,0,0), size = (0.5,5,10), color=corpaddle)
#Põe o objeto paddle não visivel
paddle.visible= False
#Paddle2
paddle2=box(pos=(-18,0,0), size = (0.5,5,10), color=corpaddle)
#Põe o objeto paddle2 não visivel
paddle2.visible= False



#Velocidade inicial bola
velocidade = 3
vi = velocidade * vector(random.randint(-5,-1),random.randint(-6,5),1)
vi2 = velocidade * vector(random.randint(1,5),random.randint(-6,5),1)
bola.velocity = vi
bola2.velocity = vi2

#Intervalo de tempo
dt = 0.01

#velocidade e acelaração profundidade
vZ= 0
aZ= 0.5

#velocidade z maxima
vMax = 0.15

#Variáveis para score 
player1 = 0
player2 = 0


#Var para saber se o jogo corre
game = True

#Var para saber quando as bolas saem do jogo
bola1Fora = False
bola2Fora = False

#Texto Inicial
T=text(text='Sejam Bem vindos ao Ping Pong Game !', pos=(-10,0,0), depth=-0.3, color=color.white)
T1=text(text='Carregue C para iniciar o jogo !', pos=(-10,-3,0), depth=-0.3, color=color.white)

#Começar e pôr os objetos visiveis
renicia()
#Apaga o texto inicial
T.visible= False
T1.visible= False
comeca()


#Ciclo while
while 1:
    while game:
        #Ciclo executado 100x faz com que as animações parecem identicas em computadores de diferentes velocidades
        rate(100)

        #Mover a bola
        bola.pos = bola.pos + bola.velocity * dt

        #Mover a bola2
        bola2.pos = bola2.pos + bola2.velocity * dt

        #Mover as bolas em Z
        bola.pos.z = bola.pos.z + vZ
        bola2.pos.z = bola2.pos.z + vZ

        #Inverter velocidade ao colidir com o chão
        if (((bola.pos.z < 0)and (bola.visible==True)) or ((bola2.pos.z < 0)and (bola2.visible==True))):
            bola.pos.z=0
            bola2.pos.z=0
            vZ = -vZ
            if (vZ>vMax):
                vZ = vMax
            print "vZ: ", vZ , "bola.pos.z", bola.pos.z    
        else:
            vZ = vZ - aZ * dt
        

        ##Verifica as possíveis colisões bola
        #Colisão chão e teto
        if(bola.pos.y + bola.radius > teto.pos.y - teto.height/2):
            bola.pos = bola.pos - bola.velocity * dt
            bola.velocity.y = -bola.velocity.y
            #print "colisão 1"

        if(bola.pos.y - bola.radius < chao.pos.y + teto.height/2):
            bola.pos = bola.pos - bola.velocity * dt
            bola.velocity.y = -bola.velocity.y
            #print "colisão 2"

        #Colisão entre paddles
        if((bola.pos.x + bola.radius) > paddle.pos.x - paddle.length/2):
            if(bola.pos.y < paddle.pos.y + paddle.height/2 and bola.pos.y > paddle.pos.y - paddle.height/2):
                bola.pos = bola.pos - bola.velocity * dt
                bola.velocity.x = -bola.velocity.x
                
                #adicionar random a velocidade y (ângulo)
                bola.velocity.y += random.randint(-1,1)

        if((bola.pos.x - bola.radius) < paddle2.pos.x - paddle2.length/2):
            if(bola.pos.y < paddle2.pos.y + paddle2.height/2 and bola.pos.y > paddle2.pos.y - paddle2.height/2):
                bola.pos = bola.pos - bola.velocity * dt 
                bola.velocity.x = -bola.velocity.x
                
                #adicionar random a velocidade y (ângulo)
                bola.velocity.y += random.randint(-1,1)
        #Verifica as possíveis colisões bola2
        #Colisão chão e teto
        if(bola2.pos.y + bola2.radius > teto.pos.y - teto.height/2):
            bola2.pos = bola2.pos - bola2.velocity * dt
            bola2.velocity.y = -bola2.velocity.y 
            
            #print "colisão 1"

        if(bola2.pos.y - bola2.radius < chao.pos.y + teto.height/2):
            bola2.pos = bola2.pos - bola2.velocity * dt
            bola2.velocity.y = -bola2.velocity.y
            #print "colisão 2"

        #Colisão entre paddles
        if((bola2.pos.x + bola2.radius) > paddle.pos.x - paddle.length/2):
            if(bola2.pos.y < paddle.pos.y + paddle.height/2 and bola2.pos.y > paddle.pos.y - paddle.height/2):
                bola2.pos = bola2.pos - bola2.velocity * dt
                bola2.velocity.x = -bola2.velocity.x
                
                #adicionar random a velocidade y (ângulo)
                bola2.velocity.y += random.randint(-2,2)

        if((bola2.pos.x - bola2.radius) < paddle2.pos.x - paddle2.length/2):
            if(bola2.pos.y < paddle2.pos.y + paddle2.height/2 and bola2.pos.y > paddle2.pos.y - paddle2.height/2):
                bola2.pos = bola2.pos - bola2.velocity * dt
                bola2.velocity.x = -bola2.velocity.x
                
                #adicionar random a velocidade y (ângulo)
                bola2.velocity.y += random.randint(-2,2)


        #Verifica se a bola passa dos paddles
        #E
        #Regista as pontuações na consola
        if(bola.pos.x>18 and bola1Fora == False):
            player1 = player1 + 1
            bola.visible=False
        if(bola2.pos.x>18 and bola2Fora == False):
            player1 = player1 + 1
            bola2.visible=False
        if(bola.pos.x<-18 and bola1Fora == False):
            player2 = player2 + 1
            bola.visible=False
        if(bola2.pos.x<-18 and bola2Fora == False):
            player2 = player2 + 1
            bola2.visible=False


        #Quando sair qualquer uma das bolas, mostrar pontuação, mas apenas a primeira vez que a bola sair
        if ((bola.pos.x < -18 or bola.pos.x>18) and(bola1Fora == False)):
            print "\nscore: player1=", player1, ", player2=", player2
            bola1Fora= True
            
        if ((bola2.pos.x < -18 or bola2.pos.x>18) and(bola2Fora  == False)):
            print "\nscore: player1=", player1, ", player2=", player2
            bola2Fora= True
            
        
        #Se as duas bolas estiverem fora, acabar o jogo e mostrar vencedor    
        if ((bola.pos.x < -18 or bola.pos.x>18) and (bola2.pos.x < -18 or bola2.pos.x>18)):
            print "\nscore final: player1=", player1, ", player2=", player2
            #Escreve os textos em 3D
            P1=text(text='Player1 :  ' + str(player1), pos=(-8,8,0), depth=-0.3, color=color.white)
            P2=text(text='Player2 :  ' + str(player2), pos=(-8,-8,0), depth=-0.3, color=color.white)
            
            if (player1 == 2):
                print "Ganhou player 1 !"
                #Escreve os textos em 3D
                B=text(text='Player1 GANHOU, carregue C para recomeçar' ,pos=(-10,0,0), depth=-0.3, color=color.white)
                #Sai do ciclo while
                break
            elif (player2 == 2):
                print "Ganhou player 2 !"
                #Escreve os textos em 3D
                B=text(text='Player2 GANHOU, carregue C para recomeçar' ,pos=(-10,0,0), depth=-0.3, color=color.white)
                #Sai do ciclo while
                break
            else:
                print "Empatado !"
                #Escreve os textos em 3D
                B=text(text='EMPATE, carregue C para recomeçar' ,pos=(-5,0,0), depth=-0.3, color=color.white)
                #Sai do ciclo while
                break


            

        #Identifica as teclas e move o paddle

        moveP1UP = False
        moveP2UP = False
        moveP1DOWN = False
        moveP2DOWN = False
        pressed = False
            
  
        if scene.kb.keys: 
             key = scene.kb.getkey()
             
             
             if key == "up" and paddle.pos.y<9:
                 moveP1UP = True
                 
                     
             elif key == "down" and paddle.pos.y>-9:
                 moveP1DOWN = True

             elif key == "s"  and paddle2.pos.y<9:
                 moveP2UP = True

             elif key == "x" and paddle2.pos.y>-9:
                 moveP2DOWN = True
                 
        else:
            moveP1UP = False
            moveP2UP = False
            moveP1DOWN = False
            moveP2DOWN = False



        if (moveP1UP):
            paddle.pos.y = paddle.pos.y + 1
        if (moveP1DOWN):
            paddle.pos.y = paddle.pos.y - 1
        if (moveP2UP):
            paddle2.pos.y = paddle2.pos.y + 1
        if (moveP2DOWN):
            paddle2.pos.y = paddle2.pos.y - 1
        

    

    renicia()
    B.visible = False
    P1.visible = False
    P2.visible = False
    bola.pos=vector(0,5,0)
    bola2.pos=vector(0,-5,0)
    bola2Fora  = False
    bola1Fora  = False
    player1=0
    player2=0






















