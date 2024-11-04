#   world[0] : 백그라운드 객체
#   world[1] : 포어그라운드 객체
world = [[], []]


def add_object(o, depth):
    world[depth].append(o)


def add_objects(ol, depth):
    world[depth] += ol


def update():
    for layer in world:
        for o in layer:
            o.update()


def render():
    for layer in world:
        for o in layer:
            o.draw()


def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return

    print(f"Can't find {o}")
