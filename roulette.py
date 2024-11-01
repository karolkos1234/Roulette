import random
import matplotlib.pyplot as plt
import pygame


class Ruleta:
    def __init__(self):
        self.wheel = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23,
                      10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 2, 18, 29, 7, 28, 12, 35, 3, 26]
        self.num_counts = {}
        self.color_counts = {}
    
    def roll(self):
        rng = random.randrange(0, 37)
        num = self.wheel[rng]
        col = self.color(rng)
        
        return num, col
    
    @staticmethod
    def color(num):
        if num == 0:
            return '0'
        elif num % 2 == 1:
            return 'red'
        else:
            return 'black'
    
    def stat_roll(self):
        num, col = self.roll()
        if num not in self.num_counts:
            self.num_counts[num] = 0
        self.num_counts[num] += 1
        
        if col not in self.color_counts:
            self.color_counts[col] = 0
        self.color_counts[col] += 1
        
        
def stat_count(dny: int,num_reps: int, rou: Ruleta):
    results = []
    for x in range(num_reps):
        s = 0
        for y in range(dny):
            num, col = rou.roll()
            if col == 'red' :
                s += 20
        
        results.append(s)
        
    return results


def hist_creation(data: list):
    data_min = min(data)
    data_max = max(data)
    ran = [x * 20 for x in range((int(data_min/20)), (int(data_max/20) + 2))]
    length = len(data)
    
    plt.hist(data, bins = ran,edgecolor='black')
    plt.title('Histogram')
    plt.xlabel('Values')
    plt.ylabel('Frequencies')
    plt.show()


if __name__ == '__main__':
    # ruleta = Ruleta()
    # rep = 10000
    # days = 20
    
    # res = stat_count(days, rep, ruleta)
    
    # hist_creation(res)

    pygame.init()

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = pygame.Rect((300, 250, 50, 50))

    run = True
    
    while run:

        pygame.draw.rect(screen, (255,0,0), player)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    
    pygame.quit()

    
  