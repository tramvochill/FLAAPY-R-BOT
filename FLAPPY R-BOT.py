import pygame,sys,random

# Khởi tạo Pygame
pygame.init()

# Cài đặt màn hình
WIDTH, HEIGHT = 864, 768
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu")
bgintro = pygame.image.load('C:/Users/Admin/Downloads/bg.png').convert()
bg_music = pygame.mixer.Sound('C:/Users/Admin/Downloads/bgm1.wav')

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Font chữ
font_large = pygame.font.Font('C:/Users/Admin/Downloads/04B_19.ttf', 100)
font_medium = pygame.font.Font('C:/Users/Admin/Downloads/04B_19.ttf', 35)
font = pygame.font.Font('C:/Users/Admin/Downloads/04B_19.ttf',50)

# Trạng thái ứng dụng
STATE_MENU = "menu"
STATE_MODE_PLAY = "mode_play"
STATE_START_GAME = "start_game"
state = STATE_MENU
play_mode = "space"

# Hàm vẽ nút
def draw_button(rect, text, is_hovered=False):
    color = GRAY if is_hovered else WHITE
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, BLACK, rect, 2)
    text_surface = font_medium.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

# Hàm chạy game sau khi chọn nhân vật
def run_game(start):

	# Cài đặt màn hình
    WIDTH, HEIGHT = 864,768
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chọn Nhân Vật")
    bgintro = pygame.image.load('C:/Users/Admin/Downloads/bg.png').convert()

    # Danh sách nhân vật
    characters = ["r-bot 1", "r-bot 2" , "r-bot 3" , "r-bot 4"]
    characters_images={
        "r-bot 1": pygame.image.load("C:/Users/Admin/Downloads/thuan.png"),
        "r-bot 2": pygame.image.load("C:/Users/Admin/Downloads/tram.png"),
        "r-bot 3": pygame.image.load("C:/Users/Admin/Downloads/anh.png"),
        "r-bot 4": pygame.image.load("C:/Users/Admin/Downloads/ngan.png") }
    character_buttons = []

    # Kích thước hình ảnh
    image_width, image_height = 100, 100 

    # Tạo các nút nhân vật
    button_width, button_height = 200, 150 
    for i, character in enumerate(characters):
        x = (WIDTH - button_width) // 2
        y = 50 + i * (button_height + 20)
        rect = pygame.Rect(x, y, button_width, button_height)
        character_buttons.append((rect, character))
    
    # Hàm vẽ nút
    def draw_button(rect, character, is_hovered=False):
        color = GRAY if is_hovered else WHITE 
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, BLACK, rect, 2)
        #Vẽ Chữ
        text_surface = font_medium.render(character, True, BLACK)
        text_rect = text_surface.get_rect(center=(rect.centerx, rect.y + image_height + 30))
        screen.blit(text_surface, text_rect)
        # Vẽ hình ảnh
        image = pygame.transform.scale(characters_images[character], (image_width, image_height))
        image_x = rect.centerx - image_width // 2
        image_y = rect.y + 10
        screen.blit(image, (image_x, image_y))
    def draw_buttonn(rect, text, is_hovered=False):
        color = GRAY if is_hovered else WHITE
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, BLACK, rect, 2)
        text_surface = font_medium.render(text, True, BLACK)
        text_rect = text_surface.get_rect(center=rect.center)
        screen.blit(text_surface, text_rect) 

    # Hàm chạy game sau khi chọn nhân vật
    def run_game(selected_character):
        print(f"Bắt đầu game với nhân vật: {selected_character}")
        
        #Tạo hàm cho trò chơi
        def draw_button(rect, text, is_hovered=False):
            color = GRAY if is_hovered else WHITE
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, BLACK, rect, 2)
            text_surface = font_medium.render(text, True, BLACK)
            text_rect = text_surface.get_rect(center=rect.center)
            screen.blit(text_surface, text_rect)

        def draw_floor():
            screen.blit(floor,(floor_x_pos,650))
            screen.blit(floor,(floor_x_pos+WIDTH,650))
        def create_pipe():
            random_pipe_pos = random.choice(pipe_height)
            bottom_pipe = pipe_surface.get_rect(midtop =(730,random_pipe_pos))
            top_pipe = pipe_surface.get_rect(midtop =(730,random_pipe_pos-700))
            return bottom_pipe, top_pipe
        def move_pipe(pipes):
            for pipe in pipes :
                pipe.centerx -=7
            return pipes
        def draw_pipe(pipes):
            for pipe in pipes:
                if pipe.bottom >= 600 : 
                    screen.blit(pipe_surface,pipe)
                else:
                    flip_pipe = pygame.transform.flip(pipe_surface,False,True)
                    screen.blit(flip_pipe,pipe)
        def check_collision(pipes):
            for pipe in pipes:
                if bird_rect.colliderect(pipe):
                    hit_sound.play()
                    return False
                if bird_rect.top <= -75 or bird_rect.bottom >= 650:
                    return False
            return True 
        def rotate_bird(bird1):
            new_bird = pygame.transform.rotozoom(bird1,-bird_movement*3,1)
            return new_bird
        def bird_animation():
            new_bird = bird_list[bird_index]
            new_bird_rect = new_bird.get_rect(center = (100,bird_rect.centery))
            return new_bird, new_bird_rect
        def score_display(game_state):
            if game_state == 'main game':
                score_surface = game_font.render(str(int(score)),True,(255,255,255))
                score_rect = score_surface.get_rect(center = (WIDTH/2, 100))
                screen.blit(score_surface,score_rect)
            if game_state == 'game_over':
                score_surface = game_font.render(f'Score: {int(score)}',True,(255,255,255))
                score_rect = score_surface.get_rect(center = (WIDTH/2, 100))
                screen.blit(score_surface,score_rect)
                high_score_surface = game_font.render(f'High Score: {int(high_score)}',True,(255,255,255))
                high_score_rect = high_score_surface.get_rect(center = (WIDTH/2,630))
                screen.blit(high_score_surface,high_score_rect)
        def update_score(score,high_score):
            if score > high_score:
                high_score = score
            return high_score

        pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
        pygame.init()
        screen= pygame.display.set_mode((WIDTH, HEIGHT))
        clock = pygame.time.Clock()
        game_font = pygame.font.Font('C:/Users/Admin/Downloads/04B_19.ttf',35)
        #Tạo các biến cho trò chơi
        gravity = 0.3
        bird_movement = 0
        game_active = True
        score = 0
        high_score = 0

        #chèn background
        bg = pygame.image.load('C:/Users/Admin/Downloads/bg.png').convert()

        #chèn sàn
        floor = pygame.image.load('C:/Users/Admin/Downloads/floor1.png').convert()
        floor = pygame.transform.scale2x(floor)
        floor_x_pos = 0

        # Tạo chim từ hình ảnh của nhân vật được chọn
        bird = (characters_images[selected_character])
        bird_rect = bird.get_rect(center=(100, 384))
    
        #tạo timer cho bird
        birdflap = pygame.USEREVENT + 1
        pygame.time.set_timer(birdflap,200)
        #tạo ống
        i = 0
        pipe_surface = pygame.transform.scale2x(pygame.image.load('C:/Users/Admin/Downloads/csb1.png').convert_alpha())
        pipe_surface1 = pygame.transform.scale2x(pygame.image.load('C:/Users/Admin/Downloads/csn1.png').convert_alpha())
        pipe_surface2 = pygame.transform.scale2x(pygame.image.load('C:/Users/Admin/Downloads/csvl1.png').convert_alpha())
        pipe_surface3 = pygame.transform.scale2x(pygame.image.load('C:/Users/Admin/Downloads/bus1.png').convert_alpha())
        pipe_surface4 = pygame.transform.scale2x(pygame.image.load('C:/Users/Admin/Downloads/cucai.png').convert_alpha())
        pipe_surface5 = pygame.transform.scale2x(pygame.image.load('C:/Users/Admin/Downloads/ao.png').convert_alpha())
        pipess = [pipe_surface,pipe_surface1,pipe_surface2,pipe_surface3,pipe_surface4,pipe_surface5]
        pipe_list =[]

        #tạo timer
        spawnpipe= pygame.USEREVENT
        pygame.time.set_timer(spawnpipe, 1800)
        pipe_height = [300,350,400,450,500]
    
        #Chèn âm thanh
        flap_sound = pygame.mixer.Sound('C:/Users/Admin/Downloads/sfx_wing1.wav')
        hit_sound = pygame.mixer.Sound('C:/Users/Admin/Downloads/sfx_hit1.wav')
        score_sound = pygame.mixer.Sound('C:/Users/Admin/Downloads/sfx_point1.wav')
        die_sound = pygame.mixer.Sound('C:/Users/Admin/Downloads/sfx_die1.wav')
        score_sound_countdown = 100
       #while loop của trò chơi
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and play_mode == "space":
                    if event.key == pygame.K_SPACE and game_active:
                        bird_movement = 0
                        bird_movement = -7.2
                        flap_sound.play()
                if event.type == pygame.MOUSEBUTTONDOWN and play_mode == "mouse":
                    if game_active:
                        bird_movement = 0
                        bird_movement = -7.2
                        flap_sound.play()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and  game_active==False:
                        game_active = True 
                        pipe_list.clear()
                        bird_rect.center = (100,384)
                        bird_movement = 0 
                        score = 0
                if event.type == spawnpipe:
                    pipe_surface = pipess[i]
                    pipe_list.extend(create_pipe())
                    i+=1
                    if i>5: i=0
            
            screen.blit(bg,(0,0))
            if game_active:
                #chim
                bird_movement += gravity
                rotated_bird = rotate_bird(bird)       
                bird_rect.centery += bird_movement
                screen.blit(rotated_bird,bird_rect)
                game_active= check_collision(pipe_list)
            
                #ống
                pipe_list = move_pipe(pipe_list)
                draw_pipe(pipe_list)
                score += 0.01
                score_display('main game')
                score_sound_countdown -= 1

                if score_sound_countdown <= 0:
                    score_sound.play()
                    score_sound_countdown = 100
            if not game_active:
                high_score = update_score(score,high_score)
                score_display('game_over')
                
                # Hiển thị thông báo khi kết thúc
                over_image = pygame.transform.scale2x(pygame.image.load('C:/Users/Admin/Downloads/gameover.png').convert_alpha())
                over_surface = game_font.render("Space to restart the game", True, (0, 0, 0))
                over_rect = over_surface.get_rect(center=(WIDTH/2, 350 ))
                screen.blit(over_image,(250,180))
                screen.blit(over_surface, over_rect)


                # Nút "Back"
                btn_back = pygame.Rect((WIDTH - 300) // 2, 450, 300, 80)
                draw_button(btn_back, "Back", btn_back.collidepoint(pygame.mouse.get_pos()))
            
          
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if btn_back.collidepoint(pygame.mouse.get_pos()):
                        return

            #sàn
            floor_x_pos -= 1
            draw_floor()
            if floor_x_pos <= -432:
                floor_x_pos =0

            pygame.display.set_caption("Flappy r-bot")
            pygame.display.update()
            clock.tick(100)
    # Vòng lặp chính
    runningg = True
    while runningg:
        screen.blit(bgintro, (0, 0))
        mouse_pos = pygame.mouse.get_pos()
        bg_music.play()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if btn_back.collidepoint(pygame.mouse.get_pos()):
                    return
            if event.type == pygame.MOUSEBUTTONDOWN:
                for rect, character in character_buttons:
                    if rect.collidepoint(mouse_pos):
                        bg_music.stop()
                        selected_character = character
                        run_game(selected_character)          

        # Vẽ các nút
        for  rect, character in character_buttons:
            is_hovered = rect.collidepoint(mouse_pos)
            draw_button(rect, character, is_hovered)

        btn_back = pygame.Rect(600, 650, 200, 80)
        draw_buttonn(btn_back, "Back", btn_back.collidepoint(pygame.mouse.get_pos()))

        pygame.display.flip()


# Vòng lặp chính
running = True
while running:
    screen.blit(bgintro, (0, 0))
    mouse_pos = pygame.mouse.get_pos()
    bg_music.play()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if state == STATE_MENU:
                if btn_start.collidepoint(mouse_pos):  
                    run_game(start)
                elif btn_mode_play.collidepoint(mouse_pos):
                    state = STATE_MODE_PLAY
                elif btn_quit.collidepoint(mouse_pos):
                    running = False
            elif state in [STATE_MODE_PLAY]:
                if btn_back.collidepoint(mouse_pos):
                    state = STATE_MENU

    # Hiển thị giao diện theo trạng thái
    if state == STATE_MENU:
        # Màn hình menu chính
        title_surface = font_large.render("Flappy R-Bot", True, BLACK)
        title_rect = title_surface.get_rect(center=(WIDTH / 2, 150))
        screen.blit(title_surface, title_rect)

        # Các nút
        btn_start = pygame.Rect((WIDTH - 300) // 2, 250, 300, 80)
        btn_mode_play = pygame.Rect((WIDTH - 300) // 2, 400, 300, 80)
        btn_quit = pygame.Rect((WIDTH - 300) // 2, 550, 300, 80)

        start = draw_button(btn_start, "Start", btn_start.collidepoint(mouse_pos))
        draw_button(btn_mode_play, "Mode Play", btn_mode_play.collidepoint(mouse_pos))
        draw_button(btn_quit, "Quit", btn_quit.collidepoint(mouse_pos))         
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if btn_start.collidepoint(mouse_pos):  
                    result = run_game(start)  # Chạy game
                elif btn_mode_play.collidepoint(mouse_pos):
                    state = STATE_MODE_PLAY
                elif btn_quit.collidepoint(mouse_pos):
                    running = False
    elif state == STATE_MODE_PLAY:
        # Màn hình chế độ chơi
        title_surface = font_large.render("Mode Play", True, BLACK)
        title_rect = title_surface.get_rect(center=(WIDTH / 2, 150))
        screen.blit(title_surface, title_rect)

        # Các nút
        btn_back = pygame.Rect((WIDTH - 300) // 2, 450, 300, 80)
        draw_button(btn_back, "Back", btn_back.collidepoint(mouse_pos))
        btn_mouse = pygame.Rect((WIDTH - 300) // 2, 350, 300, 80)
        draw_button(btn_mouse, "Mouse", btn_mouse.collidepoint(mouse_pos))
        btn_space = pygame.Rect((WIDTH - 300) // 2, 250, 300, 80)
        draw_button(btn_space, "Space", btn_space.collidepoint(mouse_pos))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_mouse.collidepoint(mouse_pos):
                    play_mode = "mouse"  # Chế độ chơi bằng chuột
                elif btn_space.collidepoint(mouse_pos):
                    play_mode = "space"  # Chế độ chơi bằng phím cách
                elif btn_back.collidepoint(mouse_pos):
                    state = STATE_MENU
    
    pygame.display.flip()

pygame.quit()


    