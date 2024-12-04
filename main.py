import pygame
import random
import sys

# Inicialización de PyGame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Supervivencia")
clock = pygame.time.Clock()

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Clases y funciones
def draw_text(screen, text, size, color, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def main_menu():
    while True:
        screen.fill(BLACK)
        draw_text(screen, "MENU PRINCIPAL", 50, WHITE, WIDTH // 4, HEIGHT // 4)
        draw_text(screen, "Presiona ESPACIO para jugar", 30, WHITE, WIDTH // 4, HEIGHT // 2)
        draw_text(screen, "Presiona ESC para salir", 30, WHITE, WIDTH // 4, HEIGHT // 2 + 50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()

def game():
    # Jugador
    player_radius = 25
    player_x = WIDTH // 2
    player_y = HEIGHT - 2 * player_radius
    player_speed = 5

    # Enemigos
    enemy_radius = 25
    enemy_x = random.randint(enemy_radius, WIDTH - enemy_radius)
    enemy_y = 0
    enemy_speed = 5

    running = True
    score = 0

    while running:
        screen.fill(BLACK)

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Movimiento del jugador
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x - player_radius > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x + player_radius < WIDTH:
            player_x += player_speed

        # Movimiento del enemigo
        enemy_y += enemy_speed
        if enemy_y > HEIGHT:
            enemy_x = random.randint(enemy_radius, WIDTH - enemy_radius)
            enemy_y = 0
            score += 1

        # Colisión
        distance = ((player_x - enemy_x) ** 2 + (player_y - enemy_y) ** 2) ** 0.5
        if distance < player_radius + enemy_radius:
            running = False

        # Dibujar en pantalla
        pygame.draw.circle(screen, BLUE, (player_x, player_y), player_radius)
        pygame.draw.circle(screen, RED, (enemy_x, enemy_y), enemy_radius)
        draw_text(screen, f"Puntaje: {score}", 30, WHITE, 10, 10)

        pygame.display.flip()
        clock.tick(30)

    game_over(score)

def game_over(score):
    while True:
        screen.fill(BLACK)
        draw_text(screen, "GAME OVER", 50, WHITE, WIDTH // 4, HEIGHT // 4)
        draw_text(screen, f"Puntaje final: {score}", 30, WHITE, WIDTH // 4, HEIGHT // 2)
        draw_text(screen, "Presiona ESPACIO para reiniciar", 30, WHITE, WIDTH // 4, HEIGHT // 2 + 50)
        draw_text(screen, "Presiona ESC para salir", 30, WHITE, WIDTH // 4, HEIGHT // 2 + 100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()

# Inicio del juego
main_menu()
while True:
    game()
