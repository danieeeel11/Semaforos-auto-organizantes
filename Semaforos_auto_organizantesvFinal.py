# Instalar pygame por consola -> pip install pygame 
import pygame 
import time
import random
import sys

# Inicializar Pygame
pygame.init()

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY_ASFALTO = (128, 128, 128)
GRAY_SEMAFORO = (24, 23, 28)
GREEN_PASTO = (72, 123, 64)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Semaforos Auto Organizantes")

# Variables de la calle 1
street_1_width = WIDTH
street_1_height = 100
street_1_y = (HEIGHT/2) - (street_1_height/2)

# Variables de la calle 2
street_2_width = 100
street_2_height = HEIGHT
street_2_x = (WIDTH/2) - (street_2_width/2)

# Variables del semaforo 1
semaphore_radius = 20
semaphore_1_rect_x = WIDTH//2 - 105
semaphore_1_rect_y = HEIGHT//2 - 125
semaphore_1_rect_height = 50
semaphore_1_rect_width = 55
semaphore_1_color_x = WIDTH//2 - 80
semaphore_1_color_y = HEIGHT//2 - 100
semaphore_1_color = RED
# Variables del semaforo 2
semaphore_2_rect_x = WIDTH//2 - 105
semaphore_2_rect_y = HEIGHT//2 + 50
semaphore_2_rect_height = 55
semaphore_2_rect_width = 50
semaphore_2_color_x = WIDTH//2 - 80
semaphore_2_color_y = HEIGHT//2 + 75
semaphore_2_color = GREEN

# Variables del vehículo calle 1
car_1_width = 30
car_1_height = 15
car_1_x = 0
car_1_y = HEIGHT // 2 - car_1_height // 2
car_1_speed = 4
# Variables del vehículo calle 2
car_2_width = 15
car_2_height = 30
car_2_x = WIDTH // 2 - car_2_width // 2
car_2_y = 0
car_2_speed = 4
# Listas de vehiculos
cars_1 = []
cars_2 = []
# Posibles posiciones iniciales de los vehiculos calle 1
pos_calle_1 = [-50, -200, -450, -790, -1030]
# Posibles posiciones iniciales de los vehiculos calle 2
pos_calle_2 = [-150, -300, -550, -890, -1130]
# Variable que indica el tiempo
start_time = 0
# Minimo tiempo semaforo en verde
time_green = 5
# Variable que indica el tiempo en verde de semadoro 1
time_smf1 = 0
# Variable que indica el tiempo en verde de semadoro 2
time_smf2 = 0
# Variable de distancia de un carro a luz verde y cambiar a roja calle 1
dist_change = 80
# Variable de distancia de un carro a luz verde y cambiar a roja calle 2
dist_change_2 = -10
# Variable de indice de carro que aleatoriamente se detiene en medio de la calle 1
ind_carro_smf1 = 10000
# Variable de indice de carro que aleatoriamente se detiene en medio de la calle 2
ind_carro_smf2 = 10000
# Variable que indica el tiempo transcurrido en un evento aleatorio calle 1
time_event_1 = 0
# Variable que indica el tiempo transcurrido en un evento aleatorio calle 2
time_event_2 = 0
# Variable que indica la propabilidad de que pase un evento aleatorio
prob_event_aleatorio = 0.001

# Función para crear vehículos calle 1
def create_car_1(width, height):
    #x = random.randint(-1400, 0)
    x = random.choice(pos_calle_1)
    pos_calle_1.remove(x)
    y = HEIGHT // 2 - car_1_height // 2
    return pygame.Rect(x, y, width, height)
# Función para crear vehículos calle 2
def create_car_2(width, height):
    x = WIDTH // 2 - car_2_width // 2
    y = random.choice(pos_calle_2)
    pos_calle_2.remove(y)
    #y = random.randint(-1400, 0)
    return pygame.Rect(x, y, width, height)
# Crear vehículos para calle 1
for _ in range(5):  # Número de vehículos
    car = create_car_1(50, 30)  # Ancho y alto del vehículo
    cars_1.append(car)
# Crear vehículos para calle 2
for _ in range(5):  # Número de vehículos
    car = create_car_2(30, 50)  # Ancho y alto del vehículo
    cars_2.append(car)
    
# Funcion para cambiar el color del semaforo
def draw_circle(color, x, y):
    pygame.draw.circle(screen, color, (x, y), semaphore_radius)

# Funcion para dibujar las calles y los carros    
def dibujar_calles_carros():
    # Dibujar la calle 1
    pygame.draw.rect(screen, GRAY_ASFALTO, (0, street_1_y, street_1_width, street_1_height))
    # Dibujar la calle 2
    pygame.draw.rect(screen, GRAY_ASFALTO, (street_2_x, 0, street_2_width, street_2_height))
    
    # Dibujar los vehículos calle 1
    for car in cars_1:
        pygame.draw.rect(screen, BLACK, car)
    # Dibujar los vehículos calle 2
    for car in cars_2:
        pygame.draw.rect(screen, BLACK, car)

# Funcion para dibujar los semaforos
def dibujar_semaforos():
    global semaphore_1_color, semaphore_2_color, start_time, time_green
    # Dibujar semáforo 1
    pygame.draw.rect(screen, GRAY_SEMAFORO, (semaphore_1_rect_x, semaphore_1_rect_y, semaphore_1_rect_width, semaphore_1_rect_height))
    draw_circle(semaphore_1_color, semaphore_1_color_x, semaphore_1_color_y)
    start_time += 1
    #time_smf1 += 1
    
    #if semaphore_1_color == GREEN: 
    #    print("hola")
    
    # 1000 = 33 segundos
    # 300 = 10 segundos
    # 150 = 5 segundos
    #if start_time % 300 == 0:
    #    if semaphore_1_color == RED:
    #        semaphore_1_color = GREEN
    #    elif semaphore_1_color == GREEN:
    #        semaphore_1_color = RED
    
    # Dibujar semáforo 2
    pygame.draw.rect(screen, GRAY_SEMAFORO, (semaphore_2_rect_x, semaphore_2_rect_y, semaphore_2_rect_width, semaphore_2_rect_height))
    #pygame.draw.circle(screen, semaphore_2_color, (semaphore_2_color_x, semaphore_2_color_y), semaphore_radius)
    draw_circle(semaphore_2_color, semaphore_2_color_x, semaphore_2_color_y)
    #if start_time % 300 == 0:
    #    if semaphore_2_color == RED:
    #        semaphore_2_color = GREEN
    #    elif semaphore_2_color == GREEN:
    #        semaphore_2_color = RED

# Funcion para detener los vehiculos calle 1
posiciones_smf1 = [290, 220, 150, 80, 10]
cont = 0
def speed_calle_1(car_i_x):
    global cont
    global ind_carro_smf1, ind_carro_smf2
    speed = 4
    if semaphore_2_color == RED:
        if (car_i_x > (posiciones_smf1[0]-10)) and (car_i_x < (posiciones_smf1[0]+10)):
            if cont == 0:
                cont += 1
            elif cont > 0:
                speed = 0
        elif (car_i_x > (posiciones_smf1[1]-10)) and (car_i_x < (posiciones_smf1[1]+10)):
            if cont == 1:
                cont += 1
            elif cont > 1:
                speed = 0
        elif (car_i_x > (posiciones_smf1[2]-10)) and (car_i_x < (posiciones_smf1[2]+10)):
            if cont == 2:
                cont += 1
            elif cont > 2:
                speed = 0
        elif (car_i_x > (posiciones_smf1[3]-10)) and (car_i_x < (posiciones_smf1[3]+10)):
            if cont == 3:
                cont += 1
            elif cont > 3:
                speed = 0
        elif (car_i_x > (posiciones_smf1[4]-10)) and (car_i_x < (posiciones_smf1[4]+10)):
            if cont == 4:
                speed = 0
        
        if ind_carro_smf1 != 10000:
            if car_i_x <= ind_carro_smf1:
                speed = 0
    else:
        speed = 4
        cont = 0
    return speed

# Funcion para detener los vehiculos calle 2
posiciones_smf2 = [190, 120, 50, -80, -110]
cont2 = 0
def speed_calle_2(car_i_y):
    global cont2
    global ind_carro_smf1, ind_carro_smf2
    speed = 4
    if semaphore_1_color == RED:
        if (car_i_y > (posiciones_smf2[0]-10)) and (car_i_y < (posiciones_smf2[0]+10)):
            if cont2 == 0:
                cont2 += 1
            elif cont2 > 0:
                speed = 0
        elif (car_i_y > (posiciones_smf2[1]-10)) and (car_i_y < (posiciones_smf2[1]+10)):
            if cont2 == 1:
                cont2 += 1
            elif cont2 > 1:
                speed = 0
        elif (car_i_y > (posiciones_smf2[2]-10)) and (car_i_y < (posiciones_smf2[2]+10)):
            if cont2 == 2:
                cont2 += 1
            elif cont2 > 2:
                speed = 0
        elif (car_i_y > (posiciones_smf2[3]-10)) and (car_i_y < (posiciones_smf2[3]+10)):
            if cont2 == 3:
                cont2 += 1
            elif cont2 > 3:
                speed = 0
        elif (car_i_y > (posiciones_smf2[4]-10)) and (car_i_y < (posiciones_smf2[4]+10)):
            if cont2 == 4:
                speed = 0
                
        if ind_carro_smf2 != 10000:
            if car_i_y <= ind_carro_smf2:
                speed = 0
    else:
        speed = 4
        cont2 = 0
    return speed

# Funcion para mover los vehiculos
def mov_cars():
    # Mover vehículos calle 1
    for car in cars_1:
        #car.x += car_1_speed
        
        # Verificar si el vehiculo paso por el semaforo de la calle 1
        #parar_vehiculos_calle_1()
        car.x += speed_calle_1(car.x)
        # Verificar si el vehículo sale de la pantalla y reiniciarlo
        if car.x > WIDTH:
            numeros_posibles = list(range(-900, 0, 200))
            random.shuffle(numeros_posibles)
            numero_random = numeros_posibles[0]
            car.x = numero_random - car.width
            #car.x = random.randint(-400, -200) - car.width
    # Mover vehículos calle 2
    for car in cars_2:
        #car.y += car_2_speed
        car.y += speed_calle_2(car.y)
        # Verificar si el vehículo sale de la pantalla y reiniciarlo
        if car.y > HEIGHT:
            #car.y = -car.width
            numeros_posibles = list(range(-900, 0, 200))
            random.shuffle(numeros_posibles)
            numero_random = numeros_posibles[0]
            car.y = numero_random - car.height

# Funcion para definir la primera regla
# En cada paso de tiempo agregar a un contador el número de vehículos que se acercan o
# esperan ante una luz roja a una distancia d. Cuando este contador exceda un umbral n, 
# cambie el semáforo. (Siempre que el semáforo cambia, reiniciar el contador a cero)
def reg_1():
    global semaphore_1_color
    global semaphore_2_color
    if cont >= 3:
        #if time_smf1 % 150 > 5 :
        if ((time_smf1*5)/150) > time_green:
            if reg_3(1) == True:
                semaphore_2_color = GREEN
                semaphore_1_color = RED
    if cont2 >= 3:
        if ((time_smf2*5)/150) > time_green:
            if reg_3(2) == True:
                semaphore_2_color = RED
                semaphore_1_color = GREEN
        
# Funcion para definir la segunda regla
# Los semáforos deben permanecer un mínimo de tiempo u en verde
def reg_2():
    global time_smf1, time_smf2
    if semaphore_1_color == GREEN:
        time_smf1 += 1
        # 150 = 5 segundos
        #if time_smf1 % 150 == 0:
        #    semaphore_1_color = RED
    if semaphore_1_color == RED:
        time_smf1 = 0
    
    if semaphore_2_color == GREEN:
        time_smf2 += 1
    if semaphore_2_color == RED:
        time_smf2 = 0
        
# Funcion para definir la tercera regla
# Si pocos vehículos (m o menos, mayor de cero) están por cruzar una 
# luz verde a una corta distancia r, no cambiar el semáforo 
# (los vehículos que estén cerca del semáforo no frenen de golpe)
def reg_3(calle):
    if calle == 1:
        if semaphore_2_color == GREEN and ((time_smf1*5)/150) > time_green: 
            for car in cars_1:
                if car.x>270 and car.x<291:
                    return False
    elif calle == 2:
        if semaphore_1_color == GREEN and ((time_smf2*5)/150) > time_green: 
            for car in cars_2:
                if car.y>170 and car.y<191:
                    return False
    return True

# Funcion para definir la cuarta regla
# Si no hay un vehículo que se acerque a una luz verde a una distancia d y 
# por lo menos un vehículo se aproxima a una luz roja a una distancia d, 
# entonces cambiar el semáforo
def reg_4():
    global semaphore_1_color
    global semaphore_2_color
    if semaphore_2_color == GREEN: 
        if not any(dist_change <= carro.x <= 391 for carro in cars_1):
            semaphore_1_color = GREEN
            semaphore_2_color = RED
    if semaphore_1_color == GREEN:
        if not any(dist_change_2 <= carro.y <= 291 for carro in cars_2):
            semaphore_1_color = RED
            semaphore_2_color = GREEN

# Funcion para definir la quinta regla
# Si hay un vehículo detenido en el camino a una corta distancia e más allá 
# de una luz verde, cambiar el semáforo
def event_aleatorio():
    prob = random.random()
    if prob < prob_event_aleatorio:
        return True
    return False
def quitar_evento():
    global ind_carro_smf1, ind_carro_smf2, semaphore_1_color, semaphore_2_color, time_event_1, time_event_2
    if ind_carro_smf1 != 10000 and ((time_event_1*5)/150) > 2:
        ind_carro_smf1 = 10000
        time_event_1 = 0
        semaphore_1_color = GREEN
    if ind_carro_smf2 != 10000 and ((time_event_2*5)/150) > 2:
        ind_carro_smf2 = 10000
        time_event_2 = 0
        semaphore_2_color = GREEN
def reg_5():
    global ind_carro_smf1, ind_carro_smf2, semaphore_1_color, semaphore_2_color, time_event_1, time_event_2
    if semaphore_2_color == GREEN and ind_carro_smf1==10000:
        #if any(391 <= carro.x <= 759 for carro in cars_1):
        #    if event_aleatorio() == True:
        carros_filtrados = [indice for indice, carro in enumerate(cars_1) if 391 <= carro.x <= 759]
        if carros_filtrados:
            if event_aleatorio() == True:
                # Elegir un índice al azar de los carros filtrados
                indice_elegido = random.choice(carros_filtrados)
                #ind_carro_smf1 = indice_elegido
                # Obtener el carro correspondiente al índice elegido
                carro_e = cars_1[indice_elegido]
                carro_e.x += 0
                ind_carro_smf1 = carro_e.x
                time_event_1 += 1
                #semaphore_1_color = GREEN
                semaphore_2_color = RED
    elif ind_carro_smf1!=10000:
        time_event_1 += 1
                
    if semaphore_1_color == GREEN and ind_carro_smf2==10000:
        carros_filtrados = [indice for indice, carro in enumerate(cars_2) if 291 <= carro.y <= 559]
        if carros_filtrados:
            if event_aleatorio() == True:
                # Elegir un índice al azar de los carros filtrados
                indice_elegido = random.choice(carros_filtrados)
                #ind_carro_smf2 = indice_elegido
                # Obtener el carro correspondiente al índice elegido
                carro_e = cars_2[indice_elegido]
                carro_e.y += 0
                ind_carro_smf2 = carro_e.y
                time_event_2 += 1
                semaphore_1_color = RED
    elif ind_carro_smf2!=10000:
        time_event_2 += 1
    quitar_evento()


clock = pygame.time.Clock()

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Dibujar la pantalla
    screen.fill(GREEN_PASTO)
    dibujar_calles_carros()
    dibujar_semaforos()
    # Movimiento de los vehiculos
    mov_cars()
    
    # Reglas
    reg_1()
    reg_2()
    reg_4()
    reg_5()
    
    pygame.display.flip()
    # Controlar la velocidad de actualización
    clock.tick(30)
