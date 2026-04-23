# Configuración del Obsidian Web Clipper

Captura artículos, documentación y páginas web directamente en la carpeta `/raw/`
de tu LLM Wiki para que el agente pueda procesarlas.

> Consulta también la [[user-guide|Guía de Usuario]] para el flujo de trabajo completo
> y la [[architecture|Arquitectura del sistema]] para entender cómo encajan las piezas.

---

## ¿Por qué usar el Web Clipper?

El Web Clipper convierte el proceso de importar artículos web en un flujo de
un solo clic: clip → guardado en `/raw/` → listo para procesar.
Sin copiar, sin pegar, sin perder el formato.

---

## Opción 1: Obsidian Web Clipper (Oficial) ⭐ Recomendado

La extensión oficial de Obsidian para Chrome, Firefox y Safari.

### Instalación
1. Ve a [obsidian.md/clipper](https://obsidian.md/clipper) e instala la extensión.
2. Abre la extensión y en `Ajustes (⚙)` → **Vault**: selecciona este proyecto.
3. En **Carpeta de notas**, escribe: `raw`
4. En **Plantilla**, usa este template adaptado al proyecto:

```markdown
---
title: "{{title}}"
aliases: []
type: fuente
tags:
  - fuente/web
source_url: "{{url}}"
source_date: {{date:YYYY-MM-DD}}
created: {{date:YYYY-MM-DD}}
updated: {{date:YYYY-MM-DD}}
---

# {{title}}

> **Fuente**: [{{url}}]({{url}})
> **Capturado**: {{date:YYYY-MM-DD}}

---

{{content}}
```

5. Para capturar una página: haz clic en el icono de la extensión → **Clip**.
6. El archivo aparecerá en `raw/` con el nombre del artículo.
7. Dile al agente: `ingestar raw/<nombre-del-archivo>.md`

### Descarga de imágenes (opcional pero recomendado)
En `Obsidian → Ajustes → Archivos y enlaces`:
- **Carpeta de adjuntos**: `raw/assets`
- Asigna el atajo `Ctrl+Shift+D` a "Descargar adjuntos del archivo actual".

Después de capturar un artículo, pulsa el atajo y las imágenes se descargarán
localmente en `raw/assets/`, asegurando que el agente pueda verlas.

---

## Opción 2: MarkDownload (Alternativa con más control)

[MarkDownload](https://github.com/deathau/markdownload) ofrece más opciones
de personalización de plantillas.

### Instalación
- [Chrome Web Store](https://chrome.google.com/webstore/detail/markdownload-markdown-web/pcmpcfapbekmbjjkdalcgopdkipoggdi)
- [Firefox Add-ons](https://addons.mozilla.org/es/firefox/addon/markdownload/)

### Configuración
En `Opciones de la extensión`:
- **Carpeta de descarga**: Apunta a la carpeta `raw/` de tu vault de Obsidian.
- **Plantilla**:

```
---
title: "{{title}}"
type: fuente
tags:
  - fuente/web
source_url: {{url}}
source_date: {{date:YYYY-MM-DD}}
created: {{date:YYYY-MM-DD}}
updated: {{date:YYYY-MM-DD}}
---

# {{title}}

> **Fuente**: {{url}}

---

{{content}}
```

---

## Opción 3: iOS / macOS (Share Sheet)

En dispositivos Apple, puedes usar la hoja de compartir de Obsidian:
1. `Ajustes de Obsidian → Plugins core → Creador de notas → Ubicación predeterminada`: `raw`
2. Desde Safari → Compartir → Obsidian.

---

## Alternativa sin extensión: Importación Manual

La forma más simple: copia el contenido de la página web en un nuevo archivo `.md`
dentro de `/raw/`, respetando el frontmatter estándar del proyecto.

Puedes usar la plantilla de `.agentic/templates/nota-fuente.md` como base.

---

## Flujo Completo con Agente LLM

```
[Tú]
 1. Navegas y encuentras un artículo relevante
 2. Haces clic en Web Clipper → se guarda en raw/

[Agente LLM]
 3. Le dices: "ingestar raw/nombre-del-articulo.md"
 4. El agente lee la fuente, extrae entidades y conceptos,
    actualiza la wiki y el log

[Obsidian]
 5. Ves las nuevas notas y conexiones en el Graph View
```

---

## Consejos de Uso

- **Clip selectivo**: Antes de clipar, elimina del artículo barras de navegación,
  cookies banners y footers para que el agente procese solo contenido relevante.
- **Nombrado**: Si el nombre autogenerado no es descriptivo, renómbralo en `/raw/`
  antes de pedirle al agente que lo ingeste.
- **Revisión**: Tras la ingesta, verifica en `wiki/registros/log.md` qué páginas
  se crearon o actualizaron.

---

*Ver también: [[user-guide]] · [[faq]] · [[architecture]]*
