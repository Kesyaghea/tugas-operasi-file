print("keysa ghea 12 rpl 2")

def bacafile():
    nama_file = 'motivasi.txt'
    with open("motivasi.txt","r") as membaca:
        text = membaca.read()
        print(text)

bacafile()

def tulisfile():
    text = input("")
    with open("motivasi.txt","a") as menulis:
        menulis.write(text)
        print(text)

tulisfile()