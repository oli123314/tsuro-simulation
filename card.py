from global_variables import *


class Card:
    def __init__(self, n, edges, random=False, display_weights=True):
        self.points = []
        self.edges = edges
        self.weight_spots = []
        self.n = n
        self.random = random
        self.display_weights = display_weights
        if self.random:
            self.edges = []
            numbers = []
            for i in range(2*n):
                numbers.append(i+1)
            for i in range(n):
                c1 = r.choice(numbers)
                numbers.remove(c1)
                c2 = r.choice(numbers)
                numbers.remove(c2)
                edge = [c1, c2]
                edge.sort()
                self.edges.append(edge)

        for i in range(2*self.n):
            theta = (m.pi/self.n)*i
            self.points.append([(sd/2)+(rad*m.sin(theta)), (sd/2)-(rad*m.cos(theta))])
        self.calculate_weight_spots()

    def calculate_weight_spots(self):
        self.weight_spots = []
        if self.display_weights:
            for edge in self.edges:
                i = edge[0] - 1
                theta = (m.pi / self.n) * i
                dth = (int(edge[1] - edge[0] >= self.n - 1)) * (m.pi / self.n) / 6
                self.weight_spots.append([(sd / 2) + (0.90 * rad * m.sin(theta + dth)),
                                          (sd / 2) - (0.90 * rad * m.cos(theta + dth))])

    def tsuro(self):
        tsuro = True
        found_weights = []
        for edge in self.edges:
            weight = self.n - abs((edge[1] - edge[0]) - self.n)
            if weight in found_weights:
                tsuro = False
                break
            else:
                found_weights.append(weight)
        return tsuro

    def add_conjecture_edges(self):
        if self.n % 4 == 0 and self.n > 4:
            card = self
            card.edges = [[1, card.n + 1]]
            for i in range(int(card.n / 2) - 1):
                card.edges.append([2 + i, (2 * card.n) - i])
            card.edges.append([(int(card.n / 2) + 1), card.n])
            for i in range(int(card.n / 4)):
                card.edges.append([int((3 / 2) * card.n + 1 - i), int((1 / 2) * card.n + 2 + i)])
            for i in range(int((card.n / 4) - 2)):
                m = ((3 / 4) * card.n) + 2
                card.edges.append([int(m + i), int(m + (card.n / 2) - 3 - i)])
            card.edges.append([int((5 / 4) * card.n), int(((5 / 4) * card.n) + 1)])
            for edge in card.edges:
                edge.sort()
            card.calculate_weight_spots()
        elif self.n % 4 == 1 and self.n > 5:
            card = self
            card.edges = [[1, card.n + 1]]
            for i in range(int((card.n-1) / 2)):
                card.edges.append([2 + i, (2 * card.n) - i])
            card.edges.append([(int((card.n-1) / 2)+2), card.n])
            for i in range(int((card.n-1) / 4)):
                card.edges.append([int((3 / 2) * (card.n-1) + 2 - i), int((1 / 2) * (card.n-1) + 3 + i)])
            for i in range(int(((card.n-1) / 4) - 2)):
                m = ((3 / 4) * card.n) + 2
                card.edges.append([int(m + i)+1, int(m + (card.n / 2) - 3 - i)])
            card.edges.append([int((5 / 4) * (card.n-1))+1, int(((5 / 4) * (card.n-1)+2))])
            for edge in card.edges:
                edge.sort()
            card.calculate_weight_spots()
        else:
            print(f"conjecture does not apply to n={self.n}, because {self.n}%4!=0,1")

    def display(self):
        pygame.draw.circle(screen, "gray", (sd/2, sd/2), sd*size/2)
        pygame.draw.circle(screen, bg_color, (sd / 2, sd / 2), (sd*size/2)-thk)
        i = 0
        for point in self.points:
            pygame.draw.circle(screen, "turquoise", (point[0], point[1]), 12)

            text_surface = text_stuff.render(f"{i + 1}", False, "turquoise")
            text_point = [point[0] + (0.15*(point[0]-(sd/2))), point[1] + (0.15*(point[1]-(sd/2)))]
            screen.blit(text_surface, (text_point[0]-12, text_point[1]-12))
            i += 1

        if self.edges:
            for i in range(self.n):
                if len(self.edges) > i:
                    edge = self.edges[i]
                    start_pos = self.points[edge[0]-1]
                    end_pos = self.points[edge[1]-1]

                    pygame.draw.line(screen, "turquoise", end_pos, start_pos, 8)

                    if self.display_weights:
                        weight = self.n - abs((edge[1] - edge[0]) - self.n)
                        weight_spot = self.weight_spots[i]
                        text_surface = text_stuff.render(f"{weight}", False, "orange")
                        screen.blit(text_surface, (weight_spot[0] - 12, weight_spot[1] - 12))

