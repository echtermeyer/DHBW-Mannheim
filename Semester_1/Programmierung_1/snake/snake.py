import pygame
import random
from typing import Optional, List, Tuple

TILE_SIZE = 20


# Item definiert eine Klasse, um gegebene (x, y) Werte mit anderen zu vergleichen
class Item:
    def __init__(self, x: int, y: int) -> None:
        self._x = x
        self._y = y

    # True, wenn die übergebenen Koordination mit denen von Item übereinstimmen
    def occupies(self, x: int, y: int) -> bool:
        if (self._x, self._y) == (x, y):
            return True
        else:
            return False


# Erbt von Item, stellt die Wände des Spielfeldes dar
class Brick(Item):
    # Übergabe der x,y Werte an die Elternklasse
    def __init__(self, x: int, y: int):
        super().__init__(x, y)

        self._x = x
        self._y = y

    # Zeichnen des Bricks als Rechteck
    def draw(self, surface: pygame.Surface) -> None:
        surface.fill(
            (0, 0, 255),
            pygame.Rect(
                self._x * TILE_SIZE,
                self._y * TILE_SIZE,
                1 * TILE_SIZE,
                1 * TILE_SIZE
            )
        )


# Kirsche erbt ebenfalls von Item und stellt die zu fressende Kirsche dar
class Cherry(Item):
    def __init__(self) -> None:
        super().__init__(0, 0)

    # Zeichnen der Kirsche als Ellipse
    def draw(self, surface) -> None:
        pygame.draw.ellipse(
            surface,
            (255, 0, 0),
            pygame.Rect(
                self._x * TILE_SIZE,
                self._y * TILE_SIZE,
                1 * TILE_SIZE,
                1 * TILE_SIZE
            )
        )

    # Bewegen der Kirsche, nachdem diese gefressen wurde
    def move(self, grid: List[Tuple[int, int]], snake: List[Tuple[int, int]], wall: List[Tuple[int, int]]) -> None:
        # Es wird mithilfe von Mengenoperationen die Menge aller verfügbarer Koordination herausgefunden
        # und dann ein zufälliger Wert hiervon gewählt
        valid_fields = list(set(grid) - set(snake) - set(wall))

        # Zufällige Auswahl des Feldes
        new_cherry = random.choice(valid_fields)

        self._x = new_cherry[0]
        self._y = new_cherry[1]

    # (x, y) Koordinaten werden zurückgegeben
    def get_coords(self) -> tuple[int, int]:
        return self._x, self._y


# Klasse, welche die Schlange erzeugt
class Snake:
    def __init__(self, x: int, y: int) -> None:
        self.__x = x
        self.__y = y
        self._occupies = [(self.__x, self.__y)]

        self._direction = (1, 0)
        self._last_direction = self._direction
        self._grow = 0

        # Initiales Wachstum der Schlange
        self.grow(4)

    # Gibt die Koordinaten des Heads der Schlange zurück
    def get_head(self) -> Tuple[int, int]:
        return self._occupies[0]

    # Gibt alle durch die Schlange belegten werden zurück
    def get_occupies(self) -> List[Tuple[int, int]]:
        return self._occupies

    # Updaten der direction, in welche die Schlange geht
    def set_direction(self, direction: Tuple[int, int]) -> None:
        if self._last_direction != (direction[0] * -1, direction[1] * -1):
            self._direction = direction

    # Überprüft, ob das übergebene Feld von der Schlange eingenommen wird
    def occupies(self, x: int, y: int) -> bool:
        if (x, y) in self._occupies:
            return True
        else:
            return False

    # Zeichen der Schlange, indem alle Elemente der Schlange einzelnd gedruckt werden
    def draw(self, surface: pygame.Surface) -> None:
        for x, y in self._occupies:
            surface.fill(
                (0, 255, 0),
                pygame.Rect(
                    x * TILE_SIZE,
                    y * TILE_SIZE,
                    1 * TILE_SIZE,
                    1 * TILE_SIZE
                )
            )

    # Wachstum der Schlange
    def grow(self, grow: int) -> None:
        self._grow += grow

    # Updaten der Position der Schlange
    def step(self, forbidden: List[Tuple[int, int]]) -> bool:
        # Neue Koordinaten des Heads
        self.__x = self.__x + self._direction[0]
        self.__y = self.__y + self._direction[1]

        # Überprüfen, ob die Schlange in sich selbst gefahren ist
        # Falls nicht, wird ein Teil hinzugefügt
        if self.occupies(self.__x, self.__y):
            return False
        else:
            self._occupies.insert(0, (self.__x, self.__y))

        # Überprüfung, ob das hinzugefügte Stück bleiben darf, falls nicht wird es gelöscht
        if self._grow > 0:
            self._grow -= 1
        else:
            del self._occupies[-1]

        # Überprüfung, ob Schlange in die Mauer gefahren ist
        if (self.__x, self.__y) in forbidden:
            return False

        # Updaten der letzten direction
        self._last_direction = self._direction

        return True


def main():
    width = 20
    height = 20
    speed = 7

    grid = []
    wall = []
    wall_bricks = []

    # Erstellen von grid (alle Werte), wall und bricks (beide nur die Randwerte des grids)
    for x in range(width):
        for y in range(height):
            grid.append((x, y))

            if (x == 0) or (x == width - 1) or (y == 0) or (y == height - 1):
                wall.append((x, y))
                wall_bricks.append(Brick(x, y))

    pygame.init()
    screen = pygame.display.set_mode((
        TILE_SIZE * width,
        TILE_SIZE * height
    ))

    clock = pygame.time.Clock()

    # Erstellen der Objekte
    snake = Snake(width // 2, height // 2)
    cherry = Cherry()

    # Initiale Bewegung der Kirsche
    cherry.move(grid, snake.get_occupies(), wall)

    running = True
    while running:
        screen.fill((20, 20, 20))

        for brick in wall_bricks:
            brick.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Spiel beenden
                running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.set_direction((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.set_direction((1, 0))
                elif event.key == pygame.K_UP:
                    snake.set_direction((0, -1))
                elif event.key == pygame.K_DOWN:
                    snake.set_direction((0, 1))

        # Überprüfen, ob Schlange noch lebt
        running = snake.step(wall)

        if not running:
            break

        # Zeichnen der Schlange
        snake.draw(screen)

        # Wachstum der Schlange, wenn Kirsche gefressen wurde
        if snake.occupies(*cherry.get_coords()):
            snake.grow(2)
            cherry.move(grid, snake.get_occupies(), wall)

        # Zeichnen einer neuen Kirsche
        cherry.draw(screen)

        pygame.display.flip()
        clock.tick(speed)

    pygame.display.quit()
    pygame.quit()


if __name__ == '__main__':
    main()
