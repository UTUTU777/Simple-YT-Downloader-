
BaxYoutubeConverter es una aplicación para descargar videos y audios de YouTube con una interfaz gráfica amigable. 
Permite seleccionar la calidad de las descargas y funciona como un ejecutable independiente.

## Tecnologías utilizadas
- [Flet](https://flet.dev): para la interfaz gráfica.
- [yt-dlp](https://github.com/yt-dlp/yt-dlp): para la descarga de videos y audios.
- [FFmpeg](https://ffmpeg.org): para la conversión y fusión de archivos multimedia.

Para pasar el programa a un exe, ejecuta en la terminal:

              pyinstaller --onefile --add-binary "bin/ffmpeg.exe;bin" main.py

## Agradecimientos
- A la comunidad de [yt-dlp](https://github.com/yt-dlp/yt-dlp) por su increíble biblioteca.
