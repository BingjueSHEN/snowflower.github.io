text_left='<ul><img src="./image/progress/ppt'
text_right='.JPG"></ul>'
with open('progress1.txt', 'w') as file:
    for i in range(1, 24):
        file.write((text_left+'{:01d}.JPG"></ul>\n'.format(i)))