import webbrowser
import random

#Lista linkkejä
lista = ["https://www.youtube.com/watch?v=dtER80sOjX4",
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "https://www.youtube.com/watch?v=PKQPey6L42M",
        "c:\Users\asennus\Documents\Koulutehtävät\gitkansi\omarepo\globglob.py"]

#Random valinta listasta
url = (random.choice(lista))

#avaa linkin selaimella
webbrowser.open(url)