#!/usr/bin/env python3
import datetime
import ui_server
import os


def main():
    res = paint_server()

    # with open('test.sh',"w") as f:
    #     f.write("eeeh")
    #     f.write(str(res))
    print(res)
    print(eval(res))


# Serve web frontend allowing user to draw the graphics.
# Server blocks until user submits a drawing.
def paint_server():
    return ui_server.run()

if __name__ == "__main__":
    main()
