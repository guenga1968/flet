import flet as ft
import os
import asyncio
import pygame
from mutagen.mp3 import MP3


class Song:
    def __init__(self, filename):
        self.filename = filename
        self.title = os.path.splitext(os.path.basename(filename))[0]
        self.duration = self.get_duration()

    def get_duration(self):
        audio = MP3(os.path.join("src/assets/musica", self.filename))
        print(audio.info.length)
        return audio.info.length


async def main(page: ft.Page):
    page.title = "Reproductor de Musica"
    page.bgcolor = ft.Colors.BLUE_GREY_900
    page.padding = 20

    titulo = ft.Text("Reproductor de Música", size=30, color="white")
    pygame.mixer.init()
    play_list = [Song(f) for f in os.listdir("src/assets/musica") if f.endswith(".mp3")]
    current_song_index = 0

    def load_song():
        pygame.mixer.music.load(
            os.path.join("src/assets/musica", play_list[current_song_index].filename)
        )

    def play_pausa(e):
        song_info.value = play_list[current_song_index].title
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            play_btn.icon = ft.Icons.PLAY_ARROW
        else:
            if pygame.mixer.music.get_pos() == -1:
                load_song()
                pygame.mixer.music.play()
            else:
                pygame.mixer.music.unpause()
            play_btn.icon = ft.Icons.PAUSE
        page.update()

    def change_song(delta):
        nonlocal current_song_index
        current_song_index = (current_song_index + delta) % len(play_list)
        load_song()
        pygame.mixer.music.play()
        update_song_info()
        play_btn.icon = ft.Icons.PAUSE
        page.update()

    def update_song_info():
        song = play_list[current_song_index]
        song_info.value = f"{song.title}"
        duration.value = format_time(song.duration)
        progress_bar.value = 0.0
        current_time_text.value = "00:00"
        page.update()

    def format_time(seconds):
        minutes, seconds = divmod(int(seconds), 60)
        return f"{minutes:02d}:{seconds:02d}"

    async def update_progress():
        while True:
            if pygame.mixer.music.get_busy():
                current_time = pygame.mixer.music.get_pos() / 1000
                progress_bar.value = (
                    current_time / play_list[current_song_index].duration
                )
                current_time_text.value = format_time(current_time)
                page.update()
            await asyncio.sleep(1)

    song_info = ft.Text(size=20, color="white")
    current_time_text = ft.Text("00:00", color=ft.Colors.WHITE60)
    duration = ft.Text("00:00", color=ft.Colors.WHITE60)
    progress_bar = ft.ProgressBar(value=0.0, width=300, color="white", bgcolor="red")
    play_btn = ft.IconButton(
        icon=ft.Icons.PLAY_ARROW, icon_color=ft.Colors.WHITE, on_click=play_pausa
    )
    prev_btn = ft.IconButton(
        icon=ft.Icons.SKIP_PREVIOUS,
        icon_color=ft.Colors.WHITE,
        on_click=lambda _: change_song(-1),
    )
    next_btn = ft.IconButton(
        icon=ft.Icons.SKIP_NEXT,
        icon_color=ft.Colors.WHITE,
        on_click=lambda _: change_song(1),
    )

    botones = ft.Row(
        controls=[prev_btn, play_btn, next_btn], alignment=ft.MainAxisAlignment.CENTER
    )
    fila_reproductor = ft.Row(
        controls=[current_time_text, progress_bar, duration],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    columna = ft.Column(
        controls=[song_info, fila_reproductor, botones],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20,
    )

    page.add(columna)

    if play_list:
        load_song()
        update_song_info()
        page.update()
        await update_progress()
    else:
        song_info.value = "No hay canciones en la lista de reproducción"
        page.update()


ft.app(main)
