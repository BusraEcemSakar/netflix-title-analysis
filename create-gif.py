# Load images and create GIF
images = [Image.open(img) for img in sorted(glob.glob('wordclouds/*.png'))]
gif_path = 'wordclouds/wordclouds.gif'
images[0].save(gif_path, save_all=True, append_images=images[1:], duration=500, loop=0)
