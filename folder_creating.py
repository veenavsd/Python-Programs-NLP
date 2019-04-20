import os
import shutil

folder_name = input('enter the directory name:')
audio_path = ''
text_path = ''
for sub_folder_name in os.listdir(folder_name):
    if sub_folder_name == 'audio':
        audio_path = os.path.join(folder_name, sub_folder_name)
    if sub_folder_name == 'transcript':
        text_path = os.path.join(folder_name, sub_folder_name)
combined_folder = os.path.join(folder_name, 'combined_folder')
os.mkdir(combined_folder)
for each_raw_file in os.listdir(audio_path):
    for each_text_file in os.listdir(text_path):
        audio_file_path = os.path.join(audio_path, each_raw_file)
        text_file_path = os.path.join(text_path, each_text_file)
        raw_file_name = each_raw_file.split('.')[0]
        text_file_name = each_text_file.split('.')[0]

        if raw_file_name == text_file_name:
            new_folder_name = raw_file_name.rsplit('_')[-1]
            new_file_path = combined_folder + '\\' + new_folder_name
            os.mkdir(new_file_path)
            shutil.copy(audio_file_path, new_file_path)
            shutil.copy(text_file_path, new_file_path)
