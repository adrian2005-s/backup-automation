from datetime import datetime
import os
import shutil


def realizar_backup(origen, destino):
  fecha_actual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
  nombre_zip = os.path.join(destino, f"backup_{fecha_actual}")

  try:
    shutil.make_archive(nombre_zip, "zip", origen)
    mensaje = f"[{datetime.now()}] ÉXITO: Backup creado en {nombre_zip}.zip\n"
    print(mensaje)
  except Exception as e:
    mensaje = f"[{datetime.now()}] ERROR: No se pudo hacer el backup. Detalle: {e}\n"
    print(mensaje)

  with open("backup.log", "a") as log:
    log.write(mensaje)


if __name__ == "__main__":
  # Cambia estas rutas según tus carpetas de prueba
  origen_dir = "./mi_carpeta"
  destino_dir = "./backups"
  os.makedirs(destino_dir, exist_ok=True)
  realizar_backup(origen_dir, destino_dir)