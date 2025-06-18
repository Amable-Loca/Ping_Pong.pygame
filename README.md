# Descripción del Código: Juego de Ping-Pong con Pygame
Este código Python implementa un juego básico de Ping-Pong para dos jugadores utilizando la librería Pygame. El objetivo es simple: controlar tu raqueta para golpear la pelota y hacer que pase del lado de tu oponente, ¡anotando así un punto!

¿Cómo Funciona?
Configuración Inicial: El juego establece el tamaño de la ventana, carga las imágenes para el fondo, las raquetas (roja para el Jugador 1, azul para el Jugador 2) y la pelota. También define la velocidad de los fotogramas (FPS) para un movimiento suave y fluido.
Objetos del Juego:
La clase GameSprite sirve como base para cualquier elemento visual. Se encarga de cargar la imagen, escalarla al tamaño correcto y posicionarla en la pantalla.
La clase Player extiende GameSprite y añade la lógica de movimiento específica para las raquetas.
El Jugador 1 se controla con las teclas W (arriba) y S (abajo).
El Jugador 2 se controla con las FLECHAS ARRIBA y FLECHA ABAJO.
Bucle Principal: El corazón del juego es un bucle infinito que se ejecuta constantemente:
Eventos: Detecta acciones del usuario como cerrar la ventana o presionar teclas. Si presionas R, el juego se reinicia, colocando la pelota en su posición inicial y restableciendo su velocidad.
Actualización del Juego:
Dibuja el fondo y todos los elementos (raquetas y pelota) en sus posiciones actuales.
Las raquetas se mueven según las teclas presionadas por los jugadores.
La pelota se desplaza por la pantalla, y su dirección cambia (rebota) al golpear los bordes superior e inferior de la ventana.
Cuando la pelota choca con una raqueta, su dirección horizontal se invierte, simulando un rebote.
Puntuación y Victoria: Si la pelota cruza el límite lateral derecho, el Jugador 1 gana. Si cruza el límite lateral izquierdo, el Jugador 2 gana. Cuando un jugador anota, aparece un mensaje de "GANADOR" en pantalla y el juego se detiene hasta que se reinicie.
Renderizado: Finalmente, la pantalla se actualiza para mostrar todos los cambios, y el juego mantiene una velocidad constante gracias al control de FPS.
Cómo Jugar
Jugador 1 (Raqueta Roja): Usa las teclas W (arriba) y S (abajo).
Jugador 2 (Raqueta Azul): Usa las teclas FLECHA ARRIBA (arriba) y FLECHA ABAJO (abajo).
Reiniciar: Después de que un jugador anote, presiona R para empezar una nueva ronda.
Este código te proporciona un juego de Ping-Pong funcional y es un excelente punto de partida para aprender a desarrollar con Pygame.
