# import os

# folder_path = "D:\Advik User\Documents\spotifydownloadedsong\This is Weeknd"
# js_code = "let allMusic = ["

# for filename in os.listdir(folder_path):
#     if os.path.isfile(os.path.join(folder_path, filename)):
#         file_name, file_ext = os.path.splitext(filename)
#         js_code += '\n {\n'
#         js_code += f'    name: "{file_name}",\n'
#         js_code += '    artist: "",\n' # you can assign artist name here or populate it from some other source
#         js_code += f'    img: "theweeknd",\n'
#         js_code += f'    src: "{filename}",\n'
#         js_code += '  },'

# js_code += '\n];'

# with open("music-data.js", "w") as js_file:
#     js_file.write(js_code)
 

import os

folder_path = "D:\Advik User\Documents\Music Player in JavaScript\Music Player in JavaScript\songs"
js_code = "let allMusic = ["

for i, filename in enumerate(os.listdir(folder_path)):
    if os.path.isfile(os.path.join(folder_path, filename)):
        file_name, file_ext = os.path.splitext(filename)
        js_code += '\n {\n'
        js_code += f'    name: "{file_name}",\n'
        js_code += '    artist: "",\n' # you can assign artist name here or populate it from some other source
        js_code += f'    img: "music-{i+1}",\n'
        js_code += f'    src: "music-{i+1}",\n'
        js_code += '  },'

js_code += '\n];'

with open("music-data.js", "w") as js_file:
    js_file.write(js_code)
