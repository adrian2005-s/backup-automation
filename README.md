Script en Python diseñado para automatizar copias de seguridad locales. Comprime una carpeta de origen en formato `.zip` con la fecha y hora actual, y registra cada éxito o error en un archivo de logs (`backup.log`).

## Características
- Compresión automática mediante la librería estándar `shutil`.
- Control de excepciones para evitar caídas inesperadas.
- Registro detallado de eventos con marca temporal en `backup.log`.

## Requisitos
- Python 3.x instalado.

## Uso
Modifica las rutas `origen_dir` y `destino_dir` en el script según tus necesidades y ejecuta:
```bash
python backup.py