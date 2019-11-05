import os
import docx

# 将txt格式的文件去除换行符之后变成docx文件

file_path = "D:/data_study/script/字幕文件/sql"
file_name = os.listdir(file_path)
local = {}
everyfile = []
print(file_name)
for i in file_name:
    everyweek = file_path + "/" + i +"/"
    for k in os.listdir(everyweek):
        everyfile.append(everyweek + k)
    local[i] = everyfile


for o in local.keys():
    for u in local[o]:
        print(u)
        file = open(u,"r")

        str = file.read()
        file.close()
        k = docx.Document()
        while True:
            str = str.replace("\r"," ").replace("\n"," ")
            if "\r" and "\n" not in str:
                break
        k.add_paragraph(str)
        k.save(u[:-4]+".docx")


