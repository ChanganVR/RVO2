import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sys
import re


def main():
    output_file = sys.argv[1]
    with open(output_file) as fo:
        lines = fo.readlines()
        steps = list()
        for line in lines:
            line = line.split()
            positions = [[float(x) for x in re.sub('[()]', '', po).split(',')] for po in line[1:]]
            steps.append(positions)

    xmax = max([x[0] for step in steps for x in step])
    xmin = min([x[0] for step in steps for x in step])
    ymax = max([x[1] for step in steps for x in step])
    ymin = min([x[1] for step in steps for x in step])

    fig, ax = plt.subplots()
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    scat = ax.scatter([x[0] for x in steps[0]], [x[1] for x in steps[0]])

    def update(frame_num):
        scat.set_offsets(steps[frame_num])

    animation = FuncAnimation(fig, update, frames=len(steps), interval=1)
    plt.show()


if __name__ == '__main__':
    main()