import pyglet
a = pyglet.media.load('gokitty.mp3', streaming=False)
a.play()
pyglet.app.run()
