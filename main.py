import os
import yt_dlp
import flet as ft
import sys
def main(page: ft.Page):
    # Función para manejar la descarga
    def iniciar_descarga(e):
        url = url_input.value.strip()
        ruta = ruta_input.value.strip()
        tipo = tipo_selector.value
        calidad = tipo_calidad.value
        formato = ''
        if tipo =="video":
            if calidad == "Alta":
                formato = "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best"
            elif calidad == "Media":
                formato = "bv*+ba/best[height<=480]"
            elif calidad == "Baja":
                formato = "bv*+ba/best[height<=240]"
            else:
                formato = "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best"
        else:
            if calidad == "Alta":
                formato = "bestaudio[ext=m4a]/bestaudio"
            elif calidad == "Media":
                formato = "bestaudio[ext=mp3]/bestaudio"
            elif calidad == "Baja":
                formato = "bestaudio[ext=webm]/bestaudio"


        
        if not url or not ruta or not tipo:
            estado_texto.value = "Por favor, completa todos los campos."
            page.update()
            return
        
        # Crear directorio si no existe
        os.makedirs(ruta, exist_ok=True)

        # Configuración según el tipo
        options = {}
        if getattr(sys, 'frozen', False):  # Si está empaquetado como exe
            base_path = sys._MEIPASS  # Carpeta temporal donde PyInstaller coloca archivos
        else:
            base_path = os.path.abspath(".")  # Carpeta del script fuente
        ffmpeg_path = os.path.join(base_path, "bin", "ffmpeg.exe")


        if tipo == "audio":
            options = {
                'format': formato,
                'outtmpl': f'{ruta}/%(title)s.%(ext)s',
                'noplaylist': True,
                'ffmpeg_location': ffmpeg_path, 
            }
        elif tipo == "video":
            options = {
                'format': formato,
                'outtmpl': f'{ruta}/%(title)s.%(ext)s',
                'noplaylist': True,
                'ffmpeg_location': ffmpeg_path, 
            }

        # Intentar la descarga
        try:
            with yt_dlp.YoutubeDL(options) as ydl:
                estado_texto.value = "Descargando..."
                page.update()
                ydl.download([url])
            estado_texto.value = "¡Descarga completa!"
        except Exception as error:
            estado_texto.value = f"Error: {error}"
        
        page.update()

    # Componentes de la interfaz
    url_input = ft.TextField(label="URL del video", width=400, autofocus=True)
    ruta_input = ft.TextField(label="Ruta de descarga", width=400)
    tipo_selector = ft.Dropdown(
        label="Selecciona el tipo de descarga",
        options=[
            ft.dropdown.Option("audio"),
            ft.dropdown.Option("video"),
        ],
        width=400,
    )
    tipo_calidad = ft.Dropdown(
        label="Selecciona la calidad",
                options=[
            ft.dropdown.Option("Alta"),
            ft.dropdown.Option("Media"),
            ft.dropdown.Option("Baja")
        ],
        width=400,
    )
    estado_texto = ft.Text(value="", color=ft.Colors.GREEN)
    descargar_boton = ft.ElevatedButton(
        text="Iniciar descarga",
        on_click=iniciar_descarga,
    )
    marca_awa = ft.Text(value="Baxo Technologies", color=ft.Colors.BLUE, )

    # Agregar componentes a la página
    page.add(
        ft.Column([
            ft.Text("BaxYoutubeConverter", size=24, weight="bold"),
            url_input,
            tipo_selector,
            tipo_calidad,
            ruta_input,
            descargar_boton,
            estado_texto,
            marca_awa
        ])
    )
    

# Ejecutar la aplicación
if __name__ == "__main__":
    import traceback
    try:
        ft.app(target=main)
    except Exception as e:
        with open("error_log.txt", "w") as f:
            f.write(traceback.format_exc())
