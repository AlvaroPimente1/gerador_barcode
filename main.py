from PIL import Image
import os
from barcode import Code128
from barcode.writer import ImageWriter
import tkinter
from tkinter import filedialog

def criar_codigo():
    arquivo_selecionado = filedialog.askopenfilename()
    print(arquivo_selecionado)
    with open(arquivo_selecionado, 'r') as arquivo:
        for codigo in arquivo:
            print(codigo[:-1])
            codigo_barra = Code128(codigo, writer=ImageWriter())
            nome_arquivo = codigo[:-1]
            codigo_barra.save(nome_arquivo)
            #img = Image.open(f'{nome_arquivo}')
            #width = img.width // 10
            #height = img.height // 10
            #img_resized = img.resize((width, height))
            #img_resized.save(nome_arquivo)
        arquivo.close()



window = tkinter.Tk()
window.title("Gerador de codigo")
window.config(padx=80, pady=80, background='#d3d3d3')
label_button = tkinter.Label(text="Faça upload do arquivo txt para a impressão de etiquetas", font=500, background="#fff")
label_button.pack()

upload_button = tkinter.Button(window, text="Upload", command=criar_codigo, background='#fff', borderwidth=2)
upload_button.pack()

window.mainloop()

