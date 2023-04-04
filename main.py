# Troy Tural 404
# TP4

import arcade
import random

# Width et height sont ceux qui determinet la grandeur et la largeur de l`écran
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Ceci agit de la liste de coleurs possibles que nos formes peuvent être
COLORS = [arcade.color.AERO_BLUE, arcade.color.ALIZARIN_CRIMSON,
          arcade.color.AQUAMARINE, arcade.color.BAKER_MILLER_PINK]


class Balle:
    def __init__(self, centre_x, centre_y, change_x, change_y, rayon, color):
        self.centre_x = centre_x
        self.centre_y = centre_y
        self.change_x = change_x
        self.change_y = change_y
        self.rayon = rayon
        self.color = color

    # Cette ligne va permettre de faire afficher une balle
    def draw(self):
        arcade.draw_circle_filled(self.centre_x, self.centre_y, self.rayon, self.color)

    # Cette partie de code est celui qui va permettre à note balle de bouger sur l'écran ainsi que de faire en sorte
    # qu'elles ne sortent pas de l'écran
    def update(self):

        self.centre_x += self.change_x
        self.centre_y += self.change_y

        if self.centre_x < self.rayon:
            self.change_x *= -1
        if self.centre_x > SCREEN_WIDTH - self.rayon:
            self.change_x *= -1
        if self.centre_y < self.rayon:
            self.change_y *= -1
        if self.centre_y > SCREEN_HEIGHT - self.rayon:
            self.change_y *= -1


# Ces lignes de codes sont ceux qui permettent a crée des rectangles
class Rectangle:
    def __init__(self, centre_x, centre_y, change_x, change_y, hauteur, largeur, color):
        self.centre_x = centre_x
        self.centre_y = centre_y
        self.change_x = change_x
        self.change_y = change_y
        self.hauteur = hauteur
        self.largeur = largeur
        self.color = color

    # Même principe que le dernier on_update mais avec des rectangle
    def update(self):

        self.centre_x += self.change_x
        self.centre_y += self.change_y

        if self.centre_x < self.largeur:
            self.change_x *= -1
        if self.centre_x > SCREEN_WIDTH - self.largeur:
            self.change_x *= -1
        if self.centre_y < self.hauteur:
            self.change_y *= -1
        if self.centre_y > SCREEN_HEIGHT - self.hauteur:
            self.change_y *= -1

    # Cette ligne va permettre a afficher des rectangles
    def draw(self):
        arcade.draw_rectangle_filled(self.centre_x, self.centre_y, self.hauteur, self.largeur, self.color)


# Cette class permet de créer une liste pour contenir les données de nos balles et nos rectangles
class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "TP4")
        self.liste_cercles = []
        self.liste_rectangles = []

    # La fonction on_draw est qu'est-ce-qui va permettre a notre code de faire apparaitre soit une balle ou une rectangele respectivement
    def on_draw(self):
        arcade.start_render()

        for cercle in self.liste_cercles:
            cercle.draw()

        for rectangle in self.liste_rectangles:
            rectangle.draw()

    # Cette fonction va faire en sorte que l'ecran va reconnaitre lorsque tu la clique
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        # Le if et elif s'agit du moyen de faire en sorte que le code fera apparaitre soit une balle ou un rectangle dependament de quelle boutton du souris ete cliquer
        if button == arcade.MOUSE_BUTTON_LEFT:
            rayon = random.randint(10, 30)
            centre_x = random.randint(0 + rayon, SCREEN_WIDTH - rayon)
            centre_y = random.randint(0 + rayon, SCREEN_HEIGHT - rayon)
            color = random.choice(COLORS)
            change_x = random.randint(5, 15)
            change_y = random.randint(5, 15)
            cercle = Balle(centre_x, centre_y, change_x, change_y, rayon, color)
            self.liste_cercles.append(cercle)

        elif button == arcade.MOUSE_BUTTON_RIGHT:
            largeur = random.randint(10, 30)
            hauteur = random.randint(10, 30)
            centre_x = random.randint(0 + largeur, SCREEN_WIDTH - largeur)
            centre_y = random.randint(0 + hauteur, SCREEN_HEIGHT - hauteur)
            color = random.choice(COLORS)
            change_x = random.randint(5, 15)
            change_y = random.randint(5, 15)
            rectangle = Rectangle(centre_x, centre_y, change_x, change_y, hauteur, largeur, color)
            self.liste_rectangles.append(rectangle)
#Cette partie du code va faire en sorte que chaque fois qu'on cree une forme diffrente , elle va avoir des caracteristiques au hasard mais reliee a leur liste de variables
    def on_update(self, delta_time: float):
        for balle in self.liste_cercles:
            balle.update()

        for rectangle in self.liste_rectangles:
            rectangle.update()


# Ce sont ces lignes de codes qui permet au code de s'effectuer
def main():
    my_game = MyGame()

    arcade.run()


main()
