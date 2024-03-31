import pygame

#Создаём таймер, контролирующий кол-во телодвижений
clock = pygame.time.Clock()

#N = input() - если хотим сделать так чтобы наше сообщение выводилось на экран и ставим N в text_surface -> text:
pygame.init()
screen = pygame.display.set_mode((450, 225))
#screen = pygame.display.set_mode((626, 357), flags=pygame.NOFRAME) - Убрать рамки у приложения
pygame.display.set_caption('eqnq game')
#Выводимые изображения и песенки
tnt = pygame.image.load('images/tnt.png')
pygame.display.set_icon(tnt)
background = pygame.image.load('images/backgr.jpg')

walk_right = [
    pygame.image.load('images/right_run/right_run_1.png'),
    pygame.image.load('images/right_run/right_run_2.png'),
    pygame.image.load('images/right_run/right_run_3.png'),
    pygame.image.load('images/right_run/right_run_4.png'),
    pygame.image.load('images/right_run/right_run_5.png'),
    pygame.image.load('images/right_run/right_run_6.png'),
    pygame.image.load('images/right_run/right_run_7.png'),
    pygame.image.load('images/right_run/right_run_8.png')
]
walk_left = [
    pygame.image.load('images/left_run/left_run_1.png'),
    pygame.image.load('images/left_run/left_run_2.png'),
    pygame.image.load('images/left_run/left_run_3.png'),
    pygame.image.load('images/left_run/left_run_4.png'),
    pygame.image.load('images/left_run/left_run_5.png'),
    pygame.image.load('images/left_run/left_run_6.png'),
    pygame.image.load('images/left_run/left_run_7.png'),
    pygame.image.load('images/left_run/left_run_8.png')
]
player_animation_count = 0

swap_background = 0
#Текст
myfont = pygame.font.Font('fonts/RuslanDisplay-Regular.ttf', 40)
text_surface = myfont.render('MOSCOW NEVER SLEEP', True, 'Black')

#Мелодии
bg_song = pygame.mixer.Sound('songs/bg_song.mp3')
bg_song.play()

#Движение
player_speed = 5
player_x = 0
player_y = 150

is_jump = False
jump_counter = 7

running_programm = True
while running_programm:


    screen.blit(background, (swap_background, 0))
    screen.blit(background, (swap_background + 450, 0))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        screen.blit(walk_left[player_animation_count], (player_x, player_y))
    else:
        screen.blit(walk_right[player_animation_count], (player_x, player_y))

    if keys[pygame.K_a] and player_x > 0:
        player_x -= player_speed
    elif keys[pygame.K_d] and player_x < 150:
        player_x += player_speed

    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_counter >= -7:
            if jump_counter > 0:
                player_y -= (jump_counter ** 2) / 2
            else:
                player_y += (jump_counter ** 2) / 2
            jump_counter -= 1
        else:
            is_jump = False
            jump_counter = 7

    if player_animation_count == 7:
        player_animation_count = 0
    else:
        player_animation_count += 1

        swap_background -= 1
        if swap_background == -450:
            swap_background = 0

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_programm = False
            pygame.quit()

    clock.tick(17)



