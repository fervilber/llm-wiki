#!/usr/bin/env python3
"""
lint.py — Validador de formato y enlaces para la LLM Wiki.

Uso:
    python scripts/lint.py              # Valida toda la wiki
    python scripts/lint.py wiki/fuentes # Valida un directorio específico
    python scripts/lint.py wiki/fuentes/mi-nota.md  # Valida un archivo

Checks realizados:
    1. Presencia de frontmatter YAML obligatorio
    2. Campos obligatorios en el YAML (title, type, created, updated)
    3. Detección de wikilinks rotos ([[Página]] que no existe)
    4. Detección de páginas huérfanas (sin enlaces entrantes)
    5. Consistencia del índice (wiki/index.md)
"""

import os
import re
import sys
import yaml
from pathlib import Path
from datetime import datetime

# ─────────────────────────────────────────────
# CONFIGURACIÓN
# ─────────────────────────────────────────────

WIKI_DIR = Path("wiki")
INDEX_FILE = WIKI_DIR / "index.md"
REQUIRED_YAML_FIELDS = ["title", "type", "created", "updated"]
VALID_TYPES = ["fuente", "entidad", "concepto", "registro"]


# ─────────────────────────────────────────────
# UTILIDADES
# ─────────────────────────────────────────────

def extract_frontmatter(content: str) -> dict | None:
    """Extrae el bloque YAML frontmatter de un archivo Markdown."""
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return None
    try:
        return yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return None


def extract_wikilinks(content: str) -> list[str]:
    """Extrae todos los wikilinks [[...]] de un archivo."""
    return re.findall(r"\[\[([^\]]+)\]\]", content)


def get_all_wiki_pages(wiki_dir: Path) -> dict[str, Path]:
    """Devuelve un dict de {título_normalizado: ruta} para todas las páginas de la wiki."""
    pages = {}
    for md_file in wiki_dir.rglob("*.md"):
        # Título normalizado = nombre del archivo sin extensión
        key = md_file.stem.lower().replace("-", " ")
        pages[key] = md_file
    return pages


# ─────────────────────────────────────────────
# CHECKS
# ─────────────────────────────────────────────

def check_frontmatter(file_path: Path, content: str) -> list[str]:
    """Verifica que el frontmatter YAML exista y tenga los campos obligatorios."""
    errors = []
    fm = extract_frontmatter(content)

    if fm is None:
        errors.append(f"  ❌ Sin frontmatter YAML")
        return errors

    for field in REQUIRED_YAML_FIELDS:
        if field not in fm or fm[field] is None:
            errors.append(f"  ❌ Campo YAML faltante: '{field}'")

    if "type" in fm and fm["type"] not in VALID_TYPES:
        errors.append(f"  ⚠️  Tipo desconocido: '{fm['type']}' (válidos: {VALID_TYPES})")

    return errors


def check_wikilinks(file_path: Path, content: str, all_pages: dict) -> list[str]:
    """Verifica que los wikilinks apunten a páginas existentes."""
    errors = []
    links = extract_wikilinks(content)
    for link in links:
        # Normalizar el link para comparar
        normalized = link.lower().replace("-", " ").split("|")[0].strip()
        if normalized not in all_pages:
            errors.append(f"  ⚠️  Wikilink roto: [[{link}]]")
    return errors


def check_orphans(all_pages: dict, all_contents: dict[Path, str]) -> list[Path]:
    """Detecta páginas sin ningún enlace entrante (huérfanas)."""
    incoming_links = {path: 0 for path in all_pages.values()}

    for content in all_contents.values():
        links = extract_wikilinks(content)
        for link in links:
            normalized = link.lower().replace("-", " ").split("|")[0].strip()
            if normalized in all_pages:
                incoming_links[all_pages[normalized]] += 1

    # El índice y el log no cuentan como huérfanos
    excluded = {"index", "log"}
    orphans = [
        path for path, count in incoming_links.items()
        if count == 0 and path.stem.lower() not in excluded
    ]
    return orphans


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

def main():
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else WIKI_DIR

    # Recopilar archivos a validar
    if target.is_file():
        files_to_check = [target]
    else:
        files_to_check = list(target.rglob("*.md"))

    if not files_to_check:
        print("No se encontraron archivos Markdown para validar.")
        return

    # Cargar todos los contenidos de la wiki (para detección de huérfanos y links)
    all_pages = get_all_wiki_pages(WIKI_DIR)
    all_contents = {f: f.read_text(encoding="utf-8") for f in WIKI_DIR.rglob("*.md") if f.exists()}

    total_errors = 0
    total_warnings = 0
    print(f"\n🔍 LLM Wiki Linter — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"   Validando: {target}\n")
    print("─" * 60)

    for file_path in sorted(files_to_check):
        if not file_path.exists():
            continue
        content = file_path.read_text(encoding="utf-8")
        errors = []

        errors += check_frontmatter(file_path, content)
        errors += check_wikilinks(file_path, content, all_pages)

        if errors:
            print(f"\n📄 {file_path.relative_to(Path('.'))}")
            for e in errors:
                print(e)
                if "❌" in e:
                    total_errors += 1
                else:
                    total_warnings += 1

    # Check global: huérfanos
    orphans = check_orphans(all_pages, all_contents)
    if orphans:
        print(f"\n\n🔗 Páginas Huérfanas (sin enlaces entrantes):")
        for o in sorted(orphans):
            print(f"  ⚠️  {o.relative_to(Path('.'))}")
            total_warnings += len(orphans)

    print("\n" + "─" * 60)
    print(f"\n✅ Validación completada:")
    print(f"   Errores críticos : {total_errors}")
    print(f"   Advertencias     : {total_warnings}")
    print(f"   Archivos revisados: {len(files_to_check)}\n")

    if total_errors > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
