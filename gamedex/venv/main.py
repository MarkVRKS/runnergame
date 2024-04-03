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

eye = pygame.image.load('images/eye.png').convert_alpha()
eye_list = []
eye_timer = pygame.USEREVENT + 1
pygame.time.set_timer(eye_timer, 2500)

missle_pudge = pygame.image.load('images/missle_pudge.png').convert_alpha()
missles = []
missles_left = 5

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
mlabel = pygame.font.Font('fonts/RuslanDisplay-Regular.ttf', 15)
missles5_lable = mlabel.render('Осталось: 5 пуджей', True, 'White')
missles4_lable = mlabel.render('Осталось: 4 пуджа', True, 'White')
missles3_lable = mlabel.render('Осталось: 3 пуджа', True, 'White')
missles2_lable = mlabel.render('Осталось: 2 пуджа', True, 'White')
missles1_lable = mlabel.render('Остался: 1 пудж', True, 'White')
missles0_lable = mlabel.render('Остался: 0 пуджей', True, 'White')
label = pygame.font.Font('fonts/RuslanDisplay-Regular.ttf', 30)
lose_label = label.render('Ты проиграл, бооо(((', True, 'Black')
restart_label = label.render('Начать заново', True, 'White', 'Red')
restart_label_rect = restart_label.get_rect(topleft=(97, 175))

#Мелодии
mem_song = pygame.mixer.Sound('songs/songmem.mp3')
mem_song.play()

#Движение
player_speed = 5
player_x = 0
player_y = 150

is_jump = False
jump_counter = 7

gameplay = True

running_programm = True
while running_programm:


    screen.blit(background, (swap_background, 0))
    screen.blit(background, (swap_background + 450, 0))
    if gameplay:
        player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))
        # eye_rect = eye.get_rect(topleft=(eye_x, 225)) #мб лишнее
        if eye_list:
            for (i, el) in enumerate(eye_list):
                screen.blit(eye, el)
                el.x -= 8
                if el.x < -20:
                    eye_list.pop(0)
                if player_rect.colliderect(el):
                    gameplay = False

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
        if missles_left == 5:
            screen.blit(missles5_lable, (0, 3))
            missles_left = 5
        elif missles_left == 4:
            screen.blit(missles4_lable, (0, 3))
            missles_left = 4
        elif missles_left == 3:
            screen.blit(missles3_lable, (0, 3))
            missles_left = 3
        elif missles_left == 2:
            screen.blit(missles2_lable, (0, 3))
            missles_left = 2
        elif missles_left == 1:
            missles_left = 1
            screen.blit(missles1_lable, (0, 3))
        elif missles_left == 0:
            missles_left = 0
            screen.blit(missles0_lable, (0, 3))
        if missles:
            for (i, el) in enumerate(missles):
                screen.blit(missle_pudge, (el.x, el.y))
                el.x += 4
                if el.x > 475:
                    missles.pop(i)
                if eye_list:
                    for (index, eye_el) in enumerate(eye_list):
                        if el.colliderect(eye_el):
                            eye_list.pop(index)

    else:

        screen.blit(lose_label, (65, 145))
        screen.blit(restart_label, restart_label_rect)
        mouse = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            player_x = 0
            eye_list.clear()
            missles.clear()
            missles_left = 5

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_program = False
            pygame.quit()
        if event.type == eye_timer:
            eye_list.append(eye.get_rect(topleft=(454, 150)))
        if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_f and missles_left > 0:
            missles.append(missle_pudge.get_rect(topleft=(player_x + 13, player_y + 3)))
            missles_left -= 1
            if missles_left == 5:
                screen.blit(missles5_lable, (0, 3))
                missles_left = 5
            elif missles_left == 4:
                screen.blit(missles4_lable, (0, 3))
                missles_left = 4
            elif missles_left == 3:
                screen.blit(missles3_lable, (0, 3))
                missles_left = 3
            elif missles_left == 2:
                screen.blit(missles2_lable, (0, 3))
                missles_left = 2
            elif missles_left == 1:
                missles_left = 1
                screen.blit(missles1_lable, (0, 3))
            elif missles_left == 0:
                missles_left = 0
                screen.blit(missles0_lable, (0, 3))
    clock.tick(17)
