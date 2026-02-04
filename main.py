from card import *
from sys import exit

# card = Card(21, [[1, 22], [20, 37], [8, 16], [17, 28], [26, 41], [27, 29], [9, 32], [6, 13], [38, 39], [21, 25], [10, 23], [19, 33], [11, 35], [3, 12], [4, 7], [5, 42], [15, 31], [2, 14], [18, 40], [30, 36], [24, 34]])

card = Card(41,  [], False, False)
card.add_conjecture_edges()
print(card.tsuro())

'''special_n = []
for i in range(6):
    special_n.append(4 * i)
    special_n.append((4 * i) + 1)
special_n.remove(0)

for i in range(1, 22):
    if i in special_n:
        edges = find_tsuro_random(i, 100000000)
        card = Card(i, edges)
    else:
        edges = find_tsuro_random(i, m.floor((2.5**i)*2))
        card = Card(i, edges)
'''


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill(bg_color)
    card.display()
    pygame.display.update()
    clock.tick(fps)
