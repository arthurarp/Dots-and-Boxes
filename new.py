# coding: utf-8

import time
import pygame
import time
import sys
from random import randint
from graph import Graph

# definindo cores (variáveis globais)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (30, 30, 29)

graph = Graph(6, 5)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.font = pygame.font.SysFont(None, 55)
        self.text = self.font.render("New game", True, BLACK)
        self.score_text_red = self.font.render("Score: 0", True, RED)
        self.score_text_blue = self.font.render("Score: 0", True, BLUE)
        self.endGame = self.font.render("End Game!", True, BLACK)
        self.red_wins = self.font.render("Red Wins!", True, RED)
        self.blue_wins = self.font.render("Blue Wins!", True, BLUE)
        pygame.display.set_caption('Dots & Boxes')
        self.exit_ = True
        self.init = True
        self.game = False
        self.red_score = 1
        self.blue_score = 0
        self.is_bot_turn = True

    def draw_game(self):
        self.screen.fill(BLACK) # fundo preto
        
        # # arestas horizontais
        # for x in range(0,253,84):
        #     for y in range(0,377,75):
        #         pygame.draw.rect(self.screen, GRAY, [x+240, y+75, 70, 7])

        # vértices
        for x in range(0,420,84): 
            for y in range(0,415,75):
                pygame.draw.ellipse(self.screen, WHITE, [x+220, y+65, 25, 25])

        # # arestas verticais
        # for x in range(0,337,84):
        #     for y in range(0,301,75):
        #         pygame.draw.rect(self.screen, GRAY, [x+229, y+90, 7, 50])

    def draw_edges(self, px, py, H_size, V_size, width_line):     
        i = 0
        self.is_bot_turn = False
        vertexs = graph.get_vertexs()
        for vertex in vertexs:
            x_r = vertex['center_of_mass']['x'] + 12.5  
            y_r = vertex['center_of_mass']['y']
            x_d = vertex['center_of_mass']['x'] - 2
            y_d = vertex['center_of_mass']['y'] + 14

            if px > 580 or py > 460:
                return 
        
            if px >= x_r and px <= x_r + 70 and py >= y_r - 12.5 and py <= y_r + 12.5:
                if not graph.is_already_connected(vertexs[i], vertexs[i + 1]):
                    pygame.draw.rect(self.screen, RED, [x_r, y_r, H_size, width_line])
                    graph.connect_edge(i, i + 1)
                    self.is_bot_turn = True
                else:
                    self.is_bot_turn = False
            
            if py >= y_d and py <= y_d + 50 and px >= x_d - 12.5 and px <= x_d + 12.5:
                if not graph.is_already_connected(vertexs[i], vertexs[i + 5]):
                    pygame.draw.rect(self.screen, RED, [x_d, y_d, width_line, V_size])
                    graph.connect_edge(i, i + 5)
                    self.is_bot_turn = True
                else:
                    self.is_bot_turn = False

            i = i + 1
        if self.is_bot_turn: 
            self.machine_action(px, py)

            

    def machine_action(self, px, py):
        if graph.is_graph_all_connected():
            return 
        vertexs = graph.get_vertexs()
        randomic = randint(0, graph.get_n_vertexs() - 1)
        v_or_h = randint(0, 1)
        print randomic

        x_r = vertexs[randomic]['center_of_mass']['x'] + 12.5
        y_r = vertexs[randomic]['center_of_mass']['y']
        x_d = vertexs[randomic]['center_of_mass']['x'] - 2
        y_d = vertexs[randomic]['center_of_mass']['y'] + 14

        
        
        if vertexs[randomic]['column'] != 4: 
            if not graph.is_already_connected(vertexs[randomic], vertexs[randomic + 1]) and x_r != 567.5 + 12.5:
                pygame.draw.rect(self.screen, BLUE, [x_r, y_r, 61, 7])
                graph.connect_edge(randomic, randomic + 1)
                return True
            elif vertexs[randomic]['row'] != 5:
                if not graph.is_already_connected(vertexs[randomic], vertexs[randomic + 5]) and y_d != 450 + 14:
                    pygame.draw.rect(self.screen, BLUE, [x_d, y_d, 7, 52.5])
                    graph.connect_edge(randomic, randomic + 5)
                    return True

        elif vertexs[randomic]['row'] != 5:
            if not graph.is_already_connected(vertexs[randomic], vertexs[randomic + 5]) and y_d != 450 + 14:
                # print(x_d, ' || ', y_d)
                pygame.draw.rect(self.screen, BLUE, [x_d, y_d, 7, 52.5])
                graph.connect_edge(randomic, randomic + 5)
                return True

        # recursivo, pois se a maquina nao achar, de primeira, uma posição para jogar ela tem que tentar de novo
        self.machine_action(px, py)

        return True

    def end_game(self):
        self.screen.fill(WHITE)
        self.screen.blit(self.endGame, [300, 200])
        self.game = False


    def play(self):
        H_size = 61
        V_size = 52.5
        width_line = 7
        self.game = True

        while self.exit_:
            while self.init:
                # MENU DO JOGO  
                self.screen.fill(WHITE)
                self.screen.blit(self.text, [300, 200])
                #185 tamanho do texto eixo y
                pygame.draw.rect(self.screen, GRAY, [280, 170, 235, 7])
                pygame.draw.rect(self.screen, GRAY, [280, 255, 235, 7])
                pygame.draw.rect(self.screen, GRAY, [280, 170, 7, 91])
                pygame.draw.rect(self.screen, GRAY, [515, 170, 7, 91])
                pygame.display.update()
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.exit_ = False
                        self.init = False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        px, py = pygame.mouse.get_pos()
                        print('[',px, ' ',py, ']')
                        self.init = False
                        self.draw_game()                   

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit_ = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    px, py = pygame.mouse.get_pos()
                    print('[', px, ' ', py, ']')
                    self.draw_edges(px, py, H_size, V_size, width_line)

                if(graph.is_graph_all_connected()):
                    self.end_game()

            if(self.game):
                self.screen.blit(self.score_text_red, [45, 500])
                self.screen.blit(self.score_text_blue, [545, 500])
            pygame.display.update()
            # pygame.display.flip()
            # frame.tick(25)


gameplay = Game()
gameplay.play()