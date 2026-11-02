// Copia los recursos descargables (datos y herramientas) dentro de static/
// para que el sitio los publique y los notebooks los bajen desde la propia
// pagina web, sin pasar por GitHub.
import {cpSync, mkdirSync, rmSync} from 'node:fs';

const RECURSOS = ['datos', 'herramientas'];

for (const carpeta of RECURSOS) {
  const destino = `static/${carpeta}`;
  rmSync(destino, {recursive: true, force: true});
  mkdirSync(destino, {recursive: true});
  cpSync(carpeta, destino, {
    recursive: true,
    filter: (ruta) => !ruta.includes('__pycache__'),
  });
  console.log(`[recursos] ${carpeta} -> ${destino}`);
}
