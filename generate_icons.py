#!/usr/bin/env python3
"""Génère les icônes PWA pour l'application Ma Foi"""

import struct, zlib, base64, os

def make_png(size, bg=(14,14,18), accent=(124,92,191), text_color=(196,174,240)):
    """Crée une icône PNG simple avec croissant de lune et étoile"""
    # Crée une image RGBA
    img = []
    cx, cy = size // 2, size // 2
    r_outer = int(size * 0.35)
    r_inner = int(size * 0.26)
    offset = int(size * 0.08)
    star_cx = int(size * 0.65)
    star_cy = int(size * 0.28)
    star_r = int(size * 0.07)

    for y in range(size):
        row = []
        for x in range(size):
            # Fond arrondi
            dx, dy = x - cx, y - cy
            in_circle = (dx*dx + dy*dy) <= (cx - size*0.02)**2

            if not in_circle:
                row.extend([*bg, 0])
                continue

            # Croissant
            d_outer = dx*dx + dy*dy
            d_inner = (x - cx - offset)**2 + (y - cy - offset)**2

            in_crescent = d_outer <= r_outer**2 and d_inner > r_inner**2

            # Étoile (cercle simple)
            d_star = (x - star_cx)**2 + (y - star_cy)**2
            in_star = d_star <= star_r**2

            if in_star:
                row.extend([*text_color, 255])
            elif in_crescent:
                row.extend([*accent, 255])
            else:
                row.extend([*bg, 255])
        img.append(row)

    # Encode en PNG
    def png_chunk(name, data):
        c = zlib.crc32(name + data) & 0xffffffff
        return struct.pack('>I', len(data)) + name + data + struct.pack('>I', c)

    raw = b''
    for row in img:
        raw += b'\x00'
        raw += bytes(row)

    compressed = zlib.compress(raw, 9)

    png = b'\x89PNG\r\n\x1a\n'
    png += png_chunk(b'IHDR', struct.pack('>IIBBBBB', size, size, 8, 6, 0, 0, 0))
    png += png_chunk(b'IDAT', compressed)
    png += png_chunk(b'IEND', b'')
    return png

os.makedirs('icons', exist_ok=True)
for size in [192, 512]:
    with open(f'icons/icon-{size}.png', 'wb') as f:
        f.write(make_png(size))
    print(f'✅ icons/icon-{size}.png créé')
print("Icônes générées avec succès !")
