import qrcode
import urllib.parse

# Lista de tiendas
tiendas = ["ROKKIE PET", "OH My Pet"]

# Ruta local de tu formulario
archivo_local = "/Users/misaelabreu/Desktop/formulario_telegram/index.html"

for tienda in tiendas:
    # Generar URL local codificada
    url = f"file://{archivo_local}?tienda={urllib.parse.quote(tienda)}"
    
    # Crear QR
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    nombre_archivo = f"qr_{tienda.replace(' ','_')}.png"
    img.save(nombre_archivo)
    print(f"QR generado para {tienda} → {nombre_archivo}")