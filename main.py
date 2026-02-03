from card import *
from sys import exit

# card = Card(21, [[1, 22], [20, 37], [8, 16], [17, 28], [26, 41], [27, 29], [9, 32], [6, 13], [38, 39], [21, 25], [10, 23], [19, 33], [11, 35], [3, 12], [4, 7], [5, 42], [15, 31], [2, 14], [18, 40], [30, 36], [24, 34]])

card = Card(9, [[1, 10], [8, 14], [4, 11], [3, 18], [2, 7], [12, 16], [9, 17], [13, 15], [5, 6]], False, False)


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

# Method for n = c/4
'''card.edges = [[1, card.n+1]]
for i in range(int(card.n/2)-1):
    card.edges.append([2+i, (2*card.n)-i])
card.edges.append([(int(card.n/2)+1), card.n])
for i in range(int(card.n/4)):
    card.edges.append([int((3/2)*card.n+1-i), int((1/2)*card.n+2+i)])
for i in range(int((card.n/4)-2)):
    m = ((3/4)*card.n) + 2
    card.edges.append([int(m+i), int(m+(card.n/2)-3-i)])
card.edges.append([int((5/4)*card.n), int(((5/4)*card.n)+1)])
for edge in card.edges:
    edge.sort()
card.calculate_weight_spots()'''

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill(bg_color)
    card.display()
    pygame.display.update()
    clock.tick(fps)
