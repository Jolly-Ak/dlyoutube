import tkinter as tk
from tkinter import messagebox, filedialog
import yt_dlp

def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_path.set(folder_selected)

def download_youtube_video():
    url = url_entry.get()
    format_choice = format_var.get()
    output_folder = folder_path.get()
    
    if not url:
        messagebox.showerror("Erreur", "Veuillez entrer une URL")
        return

    if not output_folder:
        messagebox.showerror("Erreur", "Veuillez sélectionner un dossier de destination")
        return

    try:
        print(f"Téléchargement de la vidéo depuis l'URL : {url}")
        
        if format_choice == "mp4":
            ydl_opts = {
                'format': 'bestvideo+bestaudio/best',
                'outtmpl': f'{output_folder}/%(title)s.%(ext)s',  # Nom du fichier de sortie
            }
        elif format_choice == "audio":
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'outtmpl': f'{output_folder}/%(title)s.%(ext)s',  # Nom du fichier de sortie
            }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Succès", "Téléchargement terminé")
    except yt_dlp.utils.DownloadError as e:
        messagebox.showerror("Erreur de téléchargement", f"Erreur de téléchargement: {e}")
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur s'est produite: {e}")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Téléchargeur de vidéos YouTube")

# Création des widgets
url_label = tk.Label(root, text="URL de la vidéo YouTube:")
url_label.pack(pady=5)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

format_var = tk.StringVar(value="mp4")

mp4_radio = tk.Radiobutton(root, text="MP4", variable=format_var, value="mp4")
mp4_radio.pack(pady=5)

audio_radio = tk.Radiobutton(root, text="Audio (MP3)", variable=format_var, value="audio")
audio_radio.pack(pady=5)

folder_path = tk.StringVar()

browse_button = tk.Button(root, text="Parcourir", command=browse_folder)
browse_button.pack(pady=5)

folder_label = tk.Label(root, textvariable=folder_path)
folder_label.pack(pady=5)

download_button = tk.Button(root, text="Télécharger", command=download_youtube_video)
download_button.pack(pady=20)

# Lancement de la boucle principale
root.mainloop()