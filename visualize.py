import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys
import re
import os
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    parser.add_argument('--video', default=False, action='store_true')
    args = parser.parse_args()
    trajectory_file = sys.argv[1]
    with open(trajectory_file) as fo:
        lines = fo.readlines()[2:]
        steps = list()
        for line in lines:
            line = line.split()
            positions = [[float(x) for x in re.sub('[()]', '', po).split(',')] for po in line[1:]]
            steps.append(positions)

    # xmax = max([x[0] for step in steps for x in step])
    # xmin = min([x[0] for step in steps for x in step])
    # ymax = max([x[1] for step in steps for x in step])
    # ymin = min([x[1] for step in steps for x in step])

    fig, ax = plt.subplots()
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    scat = ax.scatter([x[0] for x in steps[0]], [x[1] for x in steps[0]])
    ax.add_artist(plt.Circle((50, 50), 40, fill=False, edgecolor='g', lw=1))

    def update(frame_num):
        scat.set_offsets(steps[frame_num])

    anim= animation.FuncAnimation(fig, update, frames=len(steps), interval=1)
    if args.video:
        Writer = animation.writers['ffmpeg']
        writer = Writer(fps=60, metadata=dict(artist='Me'), bitrate=1800)
        output_file = os.path.basename(trajectory_file).replace('txt', 'mp4')
        anim.save(output_file, writer=writer)
    else:
        plt.show()


if __name__ == '__main__':
    main()
