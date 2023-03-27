from barcode import Code128
from barcode.writer import ImageWriter
import PIL
import tkinter
from tkinter import filedialog

def criar_codigo():
    arquivo_selecionado = filedialog.askopenfilename()
    print(arquivo_selecionado)
    with open(arquivo_selecionado, 'r') as arquivo:
        #f = open(f'{nome_arquivo}.txt', 'w')
        #f.write('teste')
        codigo = arquivo.readline()
        for codigo in arquivo:
            print(codigo[:-2])
            codigo_barra = Code128(codigo, writer=ImageWriter())
            codigo_barra.save(str(codigo[:-2]), options={'width': 300, 'height': 200})

window = tkinter.Tk()
window.title("Gerador de codigo")
window.config(padx=80, pady=80, background='#d3d3d3')
label_button = tkinter.Label(text="Faça upload do arquivo txt para a impressão de etiquetas", font=500, background="#fff")
label_button.pack()
upload_button = tkinter.Button(window, text="Upload", command=criar_codigo, background='#fff', borderwidth=2)
upload_button.pack()

window.mainloop()

