# -*- coding: utf-8 -*-
"""
notebooks_a_paginas.py
======================
Convierte los notebooks de notebooks/*.ipynb en páginas del sitio web
(docs/hands-on/*.mdx), con el botón "Abrir en Colab" en cada una.

Uso (desde la carpeta raíz del repositorio):
    python3 scripts/notebooks_a_paginas.py

Solo usa la biblioteca estándar de Python. El sitio lo ejecuta
automáticamente antes de publicarse (ver .github/workflows/deploy.yml).
"""
import base64, glob, json, os, re, shutil

USUARIO = "pesco13"
REPO = "QI452-Python-Quimica"
RAMA = "main"

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARPETA_NB = os.path.join(RAIZ, "notebooks")
CARPETA_DOCS = os.path.join(RAIZ, "docs", "hands-on")
CARPETA_IMG = os.path.join(RAIZ, "static", "img", "notebooks")
COLAB = f"https://colab.research.google.com/github/{USUARIO}/{REPO}/blob/{RAMA}/notebooks"
BADGE = "https://colab.research.google.com/assets/colab-badge.svg"

# Etiquetas HTML que se dejan pasar tal cual; cualquier otro "<" se escapa.
ETIQUETAS = r"/?(details|summary|b|i|em|strong|br|sub|sup|a|img|code|p|ul|ol|li|table|tr|td|th)\b"


def texto(campo):
    return "".join(campo) if isinstance(campo, list) else (campo or "")


def escapar_mdx(md):
    """Escapa { } y < fuera del código, para que MDX no los interprete."""
    partes = re.split(r"(```.*?```|`[^`\n]*`)", md, flags=re.S)
    for i in range(0, len(partes), 2):
        p = partes[i].replace("{", "&#123;").replace("}", "&#125;")
        p = re.sub(r"<(?!" + ETIQUETAS + r")", "&lt;", p)
        partes[i] = p
    md = "".join(partes)
    # MDX necesita <details> y <summary> en líneas propias y líneas en blanco
    # alrededor del contenido.
    md = re.sub(r"<details>\s*<summary>(?:<b>)?(.*?)(?:</b>)?</summary>\s*",
                r"<details>\n<summary>\1</summary>\n\n", md, flags=re.S)
    md = re.sub(r"\s*</details>", "\n\n</details>", md)
    return md


def salidas(celda, base, n_celda):
    """Texto e imágenes que el notebook guardó al ejecutarse en Colab."""
    bloques = []
    for k, out in enumerate(celda.get("outputs", [])):
        datos = out.get("data", {})
        if out.get("output_type") == "stream":
            bloques.append("```text\n" + texto(out.get("text")).rstrip() + "\n```")
        elif "image/png" in datos:
            os.makedirs(CARPETA_IMG, exist_ok=True)
            nombre = f"{base}_{n_celda}_{k}.png"
            with open(os.path.join(CARPETA_IMG, nombre), "wb") as f:
                f.write(base64.b64decode(texto(datos["image/png"])))
            bloques.append(f"![Resultado](/img/notebooks/{nombre})")
        elif "text/plain" in datos:
            bloques.append("```text\n" + texto(datos["text/plain"]).rstrip() + "\n```")
        elif out.get("output_type") == "error":
            bloques.append("```text\n" + out.get("ename", "") + ": " + out.get("evalue", "") + "\n```")
    return bloques


def convertir(ruta):
    archivo = os.path.basename(ruta)
    base = archivo[:-len(".ipynb")]
    numero = int(base[:2]) if base[:2].isdigit() else 99
    with open(ruta, encoding="utf-8") as f:
        nb = json.load(f)

    titulo = base.replace("_", " ")
    resumen = ""
    cuerpo = []
    for n, celda in enumerate(nb.get("cells", [])):
        fuente = texto(celda.get("source")).strip("\n")
        if celda.get("cell_type") == "markdown":
            if "colab-badge" in fuente:          # el botón viejo se reemplaza por uno nuevo
                continue
            m = re.match(r"#\s+(.+)", fuente)
            if m and not cuerpo:                 # el primer título es el de la página
                titulo = m.group(1).strip()
                fuente = fuente[m.end():].strip("\n")
                if not fuente:
                    continue
            if not resumen:                      # primer objetivo = resumen de la tarjeta
                m = re.search(r"^\s*[*-]\s+(.+)$", fuente, flags=re.M)
                if m:
                    resumen = re.sub(r"[*_`]", "", m.group(1)).strip()
            cuerpo.append(escapar_mdx(fuente))
        elif celda.get("cell_type") == "code" and fuente:
            cuerpo.append("```python\n" + fuente + "\n```")
            cuerpo.extend(salidas(celda, base, n))

    boton = f"[![Abrir en Colab]({BADGE})]({COLAB}/{archivo})"
    cabecera = "\n".join([
        "---",
        f"title: {json.dumps(titulo, ensure_ascii=False)}",
        f"description: {json.dumps(resumen, ensure_ascii=False)}",
        f"sidebar_position: {numero + 1}",
        f"slug: {base.lower().replace('_', '-')}",
        f"custom_edit_url: https://github.com/{USUARIO}/{REPO}/blob/{RAMA}/notebooks/{archivo}",
        "---",
    ])
    nota = (":::tip[Cómo usar esta página]\n"
            "Abra el notebook con el botón **Abrir en Colab**, guarde una copia en su Drive "
            "(Archivo › *Guardar una copia en Drive*) y ejecute las celdas en orden con **Shift + Enter**.\n:::")
    pagina = cabecera + "\n\n" + boton + "\n\n" + nota + "\n\n" + "\n\n".join(cuerpo) + "\n"
    destino = os.path.join(CARPETA_DOCS, base.lower().replace("_", "-") + ".mdx")
    with open(destino, "w", encoding="utf-8") as f:
        f.write(pagina)
    return destino


def main():
    os.makedirs(CARPETA_DOCS, exist_ok=True)
    for viejo in glob.glob(os.path.join(CARPETA_DOCS, "*.mdx")):
        os.remove(viejo)
    shutil.rmtree(CARPETA_IMG, ignore_errors=True)
    rutas = sorted(glob.glob(os.path.join(CARPETA_NB, "*.ipynb")))
    for ruta in rutas:
        print("✓", os.path.relpath(convertir(ruta), RAIZ))
    print(f"{len(rutas)} notebooks convertidos.")


if __name__ == "__main__":
    main()
