import pygame
import math as m
import random as r
sd = 750
thk = 10
size = 0.8
rad = (sd*size/2)-(thk/2)
screen_dimensions = (sd, sd)
fps = 60
bg = 0
bg_color = (bg, bg, bg)
title = "R26#1"

pygame.init()
pygame.display.set_caption(title)
clock = pygame.time.Clock()
text_stuff = pygame.font.Font(None, 50)
screen = pygame.display.set_mode(screen_dimensions)


def permutations(n):
    return int(m.factorial(2*n)/(m.factorial(n)*(2**n)))


def find_tsuro_random(n, depth):
    print(f"Searching for tsuro {n}-card at a depth of {depth}")
    searches = 1
    for j in range(depth):
        edges = [[1, n+1]]
        numbers = []
        for i in range(2 * n):
            numbers.append(i + 1)
        numbers.remove(1)
        numbers.remove(n+1)
        if numbers:
            for i in range(n-1):
                c1 = r.choice(numbers)
                numbers.remove(c1)
                c2 = r.choice(numbers)
                numbers.remove(c2)
                edge = [c1, c2]
                edge.sort()
                edges.append(edge)
        tsuro = True
        found_weights = []
        for edge in edges:
            weight = n - abs((edge[1] - edge[0]) - n)
            if weight in found_weights:
                tsuro = False
                break
            else:
                found_weights.append(weight)

        if tsuro:
            print(f"tsuro found after {searches} searches!")
            print(edges)
            print([n - abs((edge[1] - edge[0]) - n) for edge in edges])
            print("")
            return edges
        searches += 1
    print(f"no tsuro found after {searches-1} searches.")
    print("")
    return []

