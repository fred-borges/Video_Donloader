from pytube import YouTube
from tkinter import *
from tkinter import filedialog, ttk



def baixar():
    url = entrada.get()  # Obtém a URL da entrada

    yt = YouTube(url)
    print("Aguarde...")
    video = yt.streams.get_highest_resolution()
    print("Baixando...")
    video.download()
    print("Concluído")

def salvar_arquivo():
    file_path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("Video Files", "*.mp4")])

    if file_path:
        print("Salvando em:", file_path)


def iniciar_baixar():
    botao.config(state=DISABLED)  # Desativa o botão enquanto o download ocorre
    salvar_arquivo()
    progressbar.start()
    baixar()
    botao.config(state=NORMAL)  # Ativa o botão depois que o download é concluído


window = Tk()
window.geometry("300x200+200+200")
window.title("Video Downloader")

texto = Label(window, text="Video Downloader", font="impact 20 bold")
texto.pack()

entrada = Entry(window)
entrada.pack()

botao = Button(window, text="Baixar vídeo", command=iniciar_baixar)
botao.pack()

progressbar = ttk.Progressbar(mode="indeterminate")
progressbar.pack()

window.mainloop()
