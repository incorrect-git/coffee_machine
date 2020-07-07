class Painting:
    n_pictures = 0

    def __init__(self, title, painting, year):
        self.title = title
        self.painting = painting
        self.year = year
        print(f'"{self.title}" by {self.painting} ({self.year}) hangs in the Louvre.')


title_input = input()
painting_input = input()
year_input = input()

pic = Painting(title_input, painting_input, year_input)
