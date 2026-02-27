import os, zipfile


for i in range(3000,0,-1):
    print(i)
    if(i==0):
        if(os.path.exists('flag.zip')):
            archivio = zipfile.ZipFile(pos + 'flag.zip')
            archivio.extractall("solv")
            archivio.close()
        else:
            break
    nome= f"flag{i}.zip"
    print(nome)
    archivio = zipfile.ZipFile(nome)
    archivio.extractall()
    archivio.close()
    
    