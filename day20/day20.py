particles = []

with open('input.txt') as f:
    for line in f.read().splitlines():
        particles.append([map(int, vec[3:-1].split(',')) for vec in line.split(', ')])
        # line = line.replace('\n', '')
        # px, py, pz = map(int, p[3:-1].split(','))
        # vx, vy, vz = map(int, v[3:-1].split(','))
        # ax, ay, az = map(int, a[3:-1].split(','))
        # particles.append([[px, py, pz], [vx, vy, vz], [ax, ay, az]])

for x in range(50):
    for i, particle in enumerate(particles):
        [[px, py, pz], [vx, vy, vz], [ax, ay, az]] = particle
        particles[i] = [[px+vx+ax, py+vy+ay, pz+vz+az], [vx+ax, vy+ay, vz+az], [ax, ay, az]] 

    # if x % 1000 == 0: 
    #     mindist = 1000000000
    #     mini = 0
    #     for i, particle in enumerate(particles):
    #         [[px, py, pz], [vx, vy, vz], [ax, ay, az]] = particle
    #         dist = abs(px) + abs(py) + abs(pz)
    #         if dist < mindist:
    #             mindist = dist
    #             mini = i
    #     print(mini, x)

    collided = set()
    for i, particle in enumerate(particles):
        for i2, particle2 in enumerate(particles):
            if particle[0] == particle2[0] and i != i2:
                collided.add(i)
                collided.add(i2)

    for collidedIdx in reversed(sorted(collided)):
        del particles[collidedIdx]
    
    print(len(particles))

