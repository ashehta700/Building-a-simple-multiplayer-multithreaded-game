import pygame
import socket
import threading

# set up the screen
pygame.init()
screen = pygame.display.set_mode((640, 480))
font = pygame.font.Font(None, 36)

# set up the client socket
host = 'localhost'
port = 8080
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

# thread function to handle incoming data from the server
def receive_data():
    while True:
        player_data = {'position': (100, 100), 'health': 100}
        data = client_socket.recv(1024)
        if not data:
            break
        # process the data received from the server
        print(f"Received data: {player_data}")

# create a new thread to handle incoming data
receive_thread = threading.Thread(target=receive_data)
receive_thread.start()

# main game loop
while True:
    # handle events
    # Handle user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Send a message to the server
                client_socket.sendall('FIRE'.encode())
    # draw the screen
    screen.fill((0, 0, 0))
    text = font.render("Press space to send data", True, (255, 255, 255))
    screen.blit(text, (10, 10))
    pygame.display.flip()
