import os

folder_path = "D:\Advik User\Documents\Music Player in JavaScript\Music Player in JavaScript\songs"

for i, filename in enumerate(os.listdir(folder_path)):
    if os.path.isfile(os.path.join(folder_path, filename)):
        original_file_path = os.path.join(folder_path, filename)
        new_file_path = os.path.join(folder_path, "music-" + str(i+1) + ".mp3")
        os.rename(original_file_path, new_file_path)
