#!/usr/bin/env python
# manual

"""
This script allows you to manually control the simulator or Duckiebot
using the keyboard arrows.
"""
from PIL import Image
import argparse
import sys
from time import time
import gym
import numpy as np
import pyglet
from pyglet.window import key
import turtle
from turtle import *
from random import randrange
import time
BREAK_FLAG = False
from gym_duckietown.envs import DuckietownEnv

# from experiments.utils import save_img

yo = turtle.Screen()
yo.title('yama')
yo.setup(650, 650, 650, 650)
yo.tracer(0)
yo.bgcolor('cyan')
border = turtle.Turtle()
border.hideturtle()
border.penup()
border.goto(-311, 311)
border.pendown()
border.goto(311, 311)
border.goto(311, -311)
border.goto(-311, -311)
border.goto(-311, 311)

snake=turtle.Turtle()
snake.pendown()
snake.left(90)

parser = argparse.ArgumentParser()
parser.add_argument("--env-name", default=None)
parser.add_argument("--map-name", default="udem1")
parser.add_argument("--distortion", default=False, action="store_true")
parser.add_argument("--camera_rand", default=False, action="store_true")
parser.add_argument("--draw-curve", action="store_true", help="draw the lane following curve")
parser.add_argument("--draw-bbox", action="store_true", help="draw collision detection bounding boxes")
parser.add_argument("--domain-rand", action="store_true", help="enable domain randomization")
parser.add_argument("--dynamics_rand", action="store_true", help="enable dynamics randomization")
parser.add_argument("--frame-skip", default=1, type=int, help="number of frames to skip")
parser.add_argument("--seed", default=1, type=int, help="seed")
args = parser.parse_args()

if args.env_name and args.env_name.find("Duckietown") != -1:
    env = DuckietownEnv(
        seed=args.seed,
        map_name=args.map_name,
        draw_curve=args.draw_curve,
        draw_bbox=args.draw_bbox,
        domain_rand=args.domain_rand,
        frame_skip=args.frame_skip,
        distortion=args.distortion,
        camera_rand=args.camera_rand,
        dynamics_rand=args.dynamics_rand,
    )
else:
    env = gym.make(args.env_name)

env.reset()
env.render()


@env.unwrapped.window.event
def on_key_press(symbol, modifiers):
    """
    This handler processes keyboard commands that
    control the simulation
    """

    if symbol == key.BACKSPACE or symbol == key.SLASH:
        print("RESET")
        env.reset()
        env.render()
    elif symbol == key.PAGEUP:
        env.unwrapped.cam_angle[0] = 0
    elif symbol == key.ESCAPE:
        env.close()
        sys.exit(0)

    # Take a screenshot
    # UNCOMMENT IF NEEDED - Skimage dependency
    # elif symbol == key.RETURN:
    #     print('saving screenshot')
    #     img = env.render('rgb_array')
    #     save_img('screenshot.png', img)


# Register a keyboard handler
key_handler = key.KeyStateHandler()
env.unwrapped.window.push_handlers(key_handler)

#start = time






alfa_0 = env.cur_angle * 57.30228433094796



def update(dt):





    global alfa_0
    """
    This function is called at every frame to handle
    movement/stepping and redrawing
    """
    wheel_distance = 0.102
    min_rad = 0.08

    alfa_1 = env.cur_angle * 57.30228433094796
    x=alfa_1 - alfa_0
    alfa_0 = env.cur_angle * 57.30228433094796
    action = np.array([0.0, 0.0])

#Ваш код
    # Speed boost
    if key_handler[key.UP]:
        action += (0.5, 0.0)
        snake.forward(1)

    if key_handler[key.LEFT]:
        action += (0.0, 1.0)
        snake.left(0.8509249024)


    if key_handler[key.DOWN]:
        action += (-0.5, 0.0)
        snake.back(1)


    if key_handler[key.RIGHT]:
        action += (0.0, -1.0)
        snake.right(0.8509249024)

    print(alfa_0, alfa_1, x)


    obs, reward, done, info = env.step(action)
    #print("step_count = %s, reward=%.3f" % (env.unwrapped.step_count, reward))



    if done:
        print("done!")
        env.reset()
        env.render()
        snake.reset()
        snake.left(90)
    yo.update()
    env.render()



pyglet.clock.schedule_interval(update, 1.0 / env.unwrapped.frame_rate)

# Enter main event loop
pyglet.app.run()

yo.mainloop()

env.close()
