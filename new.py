# coding: utf-8

import time
import pygame
import time
import sys
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
        pygame.display.set_caption('Dots & Boxes')
        self.exit_ = True
        self.init = True

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
            for vertex in graph.get_vertexs():
                x_r = vertex['center_of_mass']['x'] + 12.5  
                y_r = vertex['center_of_mass']['y']
                x_d = vertex['center_of_mass']['x'] - 2
                y_d = vertex['center_of_mass']['y'] + 14
                
                if px > 580 or py > 460:
                    continue
                if px >= x_r and px <= x_r + 70 and py >= y_r - 12.5 and py <= y_r + 12.5:
                    pygame.draw.rect(self.screen, RED, [x_r, y_r, H_size, width_line])
                    graph.connect_edge(i, i + 1)
                    # vertex['adjacency_list'].append(i + 1)

                elif py >= y_d and py <= y_d + 50 and px >= x_d - 12.5 and px <= x_d + 12.5:
                    pygame.draw.rect(self.screen, RED, [x_d, y_d, width_line, V_size])
                    graph.connect_edge(i, i + 5)
                    # vertex['adjacency_list'].append(i + 5)

                i = i + 1
            graph._print()
    def play(self):
        H_size = 61
        V_size = 52.5
        width_line = 7

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

            pygame.display.update()
            # pygame.display.flip()
            # frame.tick(25)


gameplay = Game()

gameplay.play()