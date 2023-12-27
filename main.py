import pygame
from board import Game
from helper import WIDTH, HEIGHT, BLACK,WHITE,GREY, pos_on_button
from stone import STONES, stone_from_pos
from q import get_move_from_q_learner,learner
import time
import sys
import os

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TUFF")
screen.fill(WHITE)
pygame.display.update()

def main():    
    running = True
    game = Game(screen)
    move_was_made = False
    i=0
    while running:
        reward = 0
        screen.fill(WHITE)
        game.draw(screen)
        pygame.draw.rect(screen,BLACK,pygame.Rect(30, 400, 60, 60))
        pygame.display.update()

        if move_was_made:
            ex = get_move_from_q_learner(game.getState())
            time.sleep(2)
            state_bf_learner_move = game.getState()
            game.move_enemy(ex)
            move_was_made = False
            continue

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if pos_on_button(pos):
                    if game.selected_stones!=[]:
                        i+=1
                        move_was_made = True
                    game.remove()
                    state_af_opponent_move = game.getState()
                    continue
                game.add_selected(stone_from_pos(pos))
                pygame.display.update()
            if event.type == pygame.QUIT:
                running = False
        if i>1:
            learner.learn(state_bf_learner_move,ex,state_af_opponent_move,reward,game.isOver,0.5,0.5)

        if game.isOver():
            i=0
            if move_was_made:
                reward = 1
            else:
                reward = -1
            #print('cooooool')
            game.reset()
            move_was_made = False
        learner

if __name__ == "__main__":
    main()
