import os
import shutil
for file in os.listdir(os.getcwd()):
    if file.endswith("AI.pdf"):
        print(file)
os.mkdir("AI")
os.mkdir("WEB")
for file in os.listdir(os.getcwd()):
    print(file)
    if file.endswith("AI.pdf"):
        shutil.copy(file,'AI\\'+file )
    elif file.endswith("WEB.pdf"):
        shutil.copy(file,'WEB\\'+file )