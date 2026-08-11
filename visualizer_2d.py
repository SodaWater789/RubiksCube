"""
2D cube-net visualizer with an actual pop-up window (pygame).

Run it:
    pip install pygame        # one-time
    python3 pygame_visualizer.py

Close the window, or press Esc/Q, to quit.
Press R/L/U/D/F/B to apply moves.

Drop this file next to your existing cell.py / cube.py -- it imports Cube
directly, no changes needed on your end.
"""

import numpy as np
import pygame
from cube import Cube

COLOR_MAP = {
    "G": (46, 204, 113),
    "B": (52, 152, 219),
    "R": (231, 76, 60),
    "O": (230, 126, 34),
    "Y": (244, 208, 63),
    "W": (245, 245, 245),
}

# classic cross layout:
#         [ U ]
#   [ L ][ F ][ R ][ B ]
#         [ D ]
FACE_OFFSET = {
    (0, 0, 1): (0, 0),    # Front
    (-1, 0, 0): (-1, 0),  # Left
    (1, 0, 0): (1, 0),    # Right
    (0, 0, -1): (2, 0),   # Back
    (0, 1, 0): (0, 1),    # Up
    (0, -1, 0): (0, -1),  # Down
}

FACE_SPACING = 3.3   # world units between face origins
CELL_SIZE = 0.94      # world units, sticker width (< 1 leaves a grid gap)
SCALE = 70            # pixels per world unit
MARGIN = 40           # pixels of padding around the whole net


def face_basis(norm):
    """(right, up) unit vectors for looking straight at a face from outside."""
    normal = np.array(norm, dtype=float)
    forward = -normal
    world_up = np.array([0.0, 1.0, 0.0])
    if abs(np.dot(normal, world_up)) > 0.9:
        up_ref = np.array([0.0, 0.0, -1.0])
    else:
        up_ref = world_up
    right = np.cross(forward, up_ref)
    up = np.cross(right, forward)
    return right, up


def compute_layout(cube):
    """Return list of (world_x, world_y, color) for every sticker."""
    layout = []
    for cell in cube.cells:
        right, up = face_basis(cell.norm)
        point = np.array(cell.point, dtype=float)
        sx = np.dot(point, right)
        sy = np.dot(point, up)
        ox, oy = FACE_OFFSET[cell.norm]
        wx = ox * FACE_SPACING + sx
        wy = oy * FACE_SPACING + sy
        layout.append((wx, wy, cell.color))
    return layout


def main():
    cube = Cube()
    cube.move_R()  # Example move to demonstrate the visualizer
    layout = compute_layout(cube)

    xs = [p[0] for p in layout]
    ys = [p[1] for p in layout]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    width = int((max_x - min_x) * SCALE + 2 * MARGIN)
    height = int((max_y - min_y) * SCALE + 2 * MARGIN)
    half = CELL_SIZE / 2 * SCALE

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Cube Net")
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # --- KEYBOARD CONTROLS ---
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_ESCAPE, pygame.K_q):
                    running = False

                # Check which key was pressed, apply move, and update layout
                elif event.key == pygame.K_r:
                    cube.move_R()
                    layout = compute_layout(cube)
                elif event.key == pygame.K_l:
                    cube.move_L()
                    layout = compute_layout(cube)
                elif event.key == pygame.K_u:
                    cube.move_U()
                    layout = compute_layout(cube)
                elif event.key == pygame.K_d:
                    cube.move_D()
                    layout = compute_layout(cube)
                elif event.key == pygame.K_f:
                    cube.move_F()
                    layout = compute_layout(cube)
                elif event.key == pygame.K_b:
                    cube.move_B()
                    layout = compute_layout(cube)

        # Draw the background
        screen.fill((25, 25, 25))

        # Draw the stickers based on the (potentially updated) layout
        for wx, wy, color in layout:
            px = (wx - min_x) * SCALE + MARGIN
            py = (max_y - wy) * SCALE + MARGIN  # flip y: screen grows downward
            rect = pygame.Rect(px - half, py - half, half * 2, half * 2)
            pygame.draw.rect(screen, COLOR_MAP[color], rect, border_radius=4)
            pygame.draw.rect(screen, (0, 0, 0), rect, width=2, border_radius=4)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()