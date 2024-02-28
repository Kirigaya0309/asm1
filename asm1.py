import pygame
from sys import exit
from random import randint, choice

# class Zombie(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         zombie_head = pygame.image.load('zombie_head.png').convert_alpha()
#         self.pos_list = [(50, 200), (200, 70), (350, 200), (500, 70), (650, 200)]
#         self.index = 0
#         self.image = zombie_head
#         self.pos = self.pos_list[self.index]
#         self.rect = self.image.get_rect(topleft = choice(self.pos_list))

#     def spawn(self):


#     def update(self):

def zombie_animation():
    global zombie_surf, zombie_frame_index
    zombie_frame_index += 1
    zombie_surf = zombie_frames[int(zombie_frame_index) % 2]

def display_score():
    global hit_score, miss_score
    score_surf = text_font.render(f'Hit: {hit_score}', False, (64, 64, 64))
    score_rect = score_surf.get_rect()

pygame.init()

screen = pygame.display.set_mode((800, 400))
surface = pygame.Surface((100, 200))
surface.fill((94, 129, 162))

text_font = pygame.font.Font('Pixeltype.ttf', 50)
text_surface = text_font.render('My game', False, (64, 64, 64)).convert()
text_rect = text_surface.get_rect(center = (400, 50))

hit_score = 0
miss_score = 0

zombie_img = pygame.image.load('zombie_head.png').convert_alpha()
zombie_frame1 = pygame.transform.rotozoom(zombie_img, 45, 0.05)
zombie_frame2 = pygame.transform.rotozoom(zombie_img, -45, 0.05)
zombie_frames = [zombie_frame1, zombie_frame2]
zombie_frame_index = 0
zombie_surf = zombie_frames[zombie_frame_index]

zombie_pos_list = [(100, 250), (250, 120), (400, 250), (550, 120), (700, 250)]
zombie_rect = zombie_surf.get_rect(center = choice(zombie_pos_list))

pygame.display.set_caption("Zombie")

clock = pygame.time.Clock()

hit = False

# Zombie timer
zombie_rotate_timer = pygame.USEREVENT + 1
pygame.time.set_timer(zombie_rotate_timer, 400)

zombie_timer = pygame.USEREVENT + 2
pygame.time.set_timer(zombie_timer, 3000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if zombie_rect.collidepoint(event.pos):
                hit = True
                pos_list = [(100, 250), (250, 120), (400, 250), (550, 120), (700, 250)]
                pos_list.remove(zombie_rect.center)
                zombie_rect = zombie_surf.get_rect(center = choice(pos_list))
            else: print('miss!')
        if event.type == zombie_rotate_timer:
            if zombie_frame_index == 0: zombie_frame_index = 1
            else: zombie_frame_index = 0
            zombie_surf = zombie_frames[zombie_frame_index]
        if event.type == zombie_timer:
            if hit == False:
                pos_list = [(100, 250), (250, 120), (400, 250), (550, 120), (700, 250)]
                pos_list.remove(zombie_rect.center)
                zombie_rect = zombie_surf.get_rect(center = choice(pos_list))
            else: hit = False


    screen.fill((94, 129, 162))
    hole1 = pygame.draw.ellipse(screen, 'Black', pygame.Rect(50, 200, 100, 100))
    hole2 = pygame.draw.ellipse(screen, 'Black', pygame.Rect(200, 70, 100, 100))
    hole3 = pygame.draw.ellipse(screen, 'Black', pygame.Rect(350, 200, 100, 100))
    hole4 = pygame.draw.ellipse(screen, 'Black', pygame.Rect(500, 70, 100, 100))
    hole5 = pygame.draw.ellipse(screen, 'Black', pygame.Rect(650, 200, 100, 100))
    # hole6 = pygame.draw.ellipse(screen, 'Black', pygame.Rect(750, 200, 100, 100))

    screen.blit(zombie_surf, zombie_rect)

    pygame.display.update()
    clock.tick(60)