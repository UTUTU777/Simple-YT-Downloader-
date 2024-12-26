#English:

BaxYoutubeConverter is an application for downloading videos and audio from YouTube with a user-friendly graphical interface.  
It allows users to select the download quality and works as a standalone executable.

## Technologies Used
- Flet (https://flet.dev): for the graphical interface.  
- yt-dlp (https://github.com/yt-dlp/yt-dlp): for downloading videos and audio.  
- FFmpeg (https://ffmpeg.org): for media file conversion and merging.  

To convert the program into an executable, run the following command in the terminal:

              pyinstaller --onefile --add-binary "bin/ffmpeg.exe;bin" main.py  

## Acknowledgments  
- To the yt-dlp (https://github.com/yt-dlp/yt-dlp) community for their amazing library.


#Español:

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
