import os
directory = r'C:\Users\Reverie-PC\Downloads\00\00'
file_list = [files for files in os.listdir(directory)]
i = 0
for filename in file_list:
    if filename.endswith(".txt"):
        fname = os.path.join(directory, filename)
        fptr = open(fname, 'r+', encoding='utf-8')
        lines = fptr.read().split('\n')
        fptr.seek(0,0)
        for each_line in lines:
            w = each_line.split('\t')
            number = w[0]
            with open(os.path.join(directory, 'transcript.txt'), 'a+', encoding='utf-8') as infile:
                infile.write(w[2])
                infile.write('\n')
            audio_fname = os.path.join(directory, file_list[1])
            for f1 in os.listdir(audio_fname):
                audio_num = f1.split('.')[0]
                if number == audio_num:
                    new_audio_number = '0000000' + str(i)
                    new_fname = new_audio_number + '.raw'
                    src = os.path.join(audio_fname, f1)
                    dst = os.path.join(audio_fname, new_fname)
                    os.rename(src, dst)
                    i = i + 1
                    w[0] = new_audio_number
                    w = '\t'.join(w)
                    fptr.write(w + '\n')
                    fptr.truncate()
                    break
        fptr.close()