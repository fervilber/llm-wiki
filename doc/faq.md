# FAQ — Preguntas Frecuentes

---

## 🛠 Instalación y Configuración

### ¿Qué necesito instalar para empezar?
Dos cosas:
1. **[Obsidian](https://obsidian.md)** (gratuito) → para visualizar la wiki.
2. **Un agente LLM** → para mantenerla. Opciones: Claude, Antigravity u OpenCode.

Para los scripts de importación también necesitas **Python 3.8+** y las dependencias:
```bash
pip install -r scripts/requirements.txt
```

### ¿Qué es Obsidian y por qué lo necesito?
Obsidian es una aplicación de notas que funciona con archivos Markdown locales.
En este proyecto lo usas para **leer y navegar** la wiki que el agente construye.
Su Graph View es especialmente útil para ver las conexiones entre conceptos.

### ¿Qué agente LLM debo usar?
Cualquiera de estos tres funciona bien:
- **Claude** (claude.ai o app de escritorio): ideal si prefieres interfaz de chat.
- **Antigravity**: ideal si trabajas dentro de un IDE y quieres que el agente
  acceda directamente a los archivos del proyecto.
- **OpenCode**: para flujos de terminal y mayor control sobre las operaciones.

La elección no afecta al funcionamiento de la wiki: todos leen los mismos archivos.

### ¿Puedo usar la wiki sin el agente, solo con Obsidian?
Sí para leer. No para procesar. Las notas de `/wiki/` las escribe el agente.
Puedes crear notas manualmente siguiendo los templates de `.agents/templates/`,
pero el mantenimiento de enlaces y el índice debe hacerlo el agente.

---

## 📥 Importación de Fuentes

### ¿Cómo importo un video de YouTube?
```bash
python scripts/youtube_to_raw.py "https://youtu.be/ID_DEL_VIDEO"
```
Luego dile al agente: *«Procesa `raw/<nombre-generado>.md` y actualiza la wiki»*

### ¿Cómo importo un PDF?
```bash
python scripts/pdf_to_raw.py "C:/ruta/al/archivo.pdf"
```
Requiere tener instalado `pymupdf`, `pdfplumber` o `pypdf2`.
Luego dile al agente: `ingestar raw/<nombre>.md`

### ¿Qué hago si el PDF contiene solo imágenes (escaneo)?
El script no puede extraer texto de PDFs escaneados sin OCR.
Opciones:
- Usa un servicio OCR online (Adobe, ilovepdf, etc.) para convertirlo a texto primero.
- Describe las páginas al agente directamente subiéndole capturas de pantalla.

### ¿Cómo importo un artículo web directamente?
Instala el [Obsidian Web Clipper](https://obsidian.md/clipper) y configúralo
para guardar en la carpeta `raw/`. Consulta [[web-clipper-setup]] para la
configuración detallada y el template de frontmatter correcto.

### ¿Por qué mi pregunta no tiene respuesta en la wiki?
El agente solo responde desde `/wiki/`. Si la información aún no ha sido
ingestada, añade la fuente a `/raw/` y ejecuta `ingestar [archivo]`.

---

## 💬 Uso con el Agente

### ¿Cómo inicio una nueva sesión?
Envía al agente este prompt:
> *"Lee en este orden: 1) `RULES.md` 2) `.agents/workflows/inicializacion.md`
> 3) `wiki/index.md` 4) `wiki/registros/log.md`. Confírmame cuando hayas leído."*

### ¿Qué pasa si cambio de agente (de Claude a OpenCode, por ejemplo)?
No pasa nada. Toda la memoria está en los archivos. El nuevo agente retoma
exactamente donde lo dejó el anterior usando el mismo prompt de inicialización.

### ¿Puedo pedirle al agente que procese varios archivos a la vez?
Sí: `ingestar todo lo nuevo en /raw/`. Pero la ingesta supervisada (un archivo
a la vez) produce síntesis de mejor calidad porque puedes orientar al agente.

### ¿Por qué el agente me pide confirmación antes de escribir?
Es la salvaguarda del `workflow ingesta, Paso 4`. Si prefieres operación
sin interrupciones, dile: *"procede con autonomía total en esta sesión."*

---

## 🔧 Mantenimiento

### ¿Cómo sé qué fuentes ya han sido procesadas?
Consulta `wiki/registros/log.md`. Todas las ingestas quedan registradas ahí.
También puedes revisar `wiki/index.md` → columna "Fecha Ingesta".

### ¿Puedo editar las notas de `/wiki/` manualmente?
Sí, pero hazlo con cuidado. Si editas una nota, avisa al agente para que
actualice los enlaces y el índice correspondientes.

### ¿Puedo cambiar las reglas de los templates o skills?
Sí. Los archivos en `.agents/` son configuración editable. Si cambias una regla,
indica al agente que recargue el archivo al inicio de la próxima sesión.

### ¿Qué hace `revisar wiki`?
Ejecuta el workflow de revisión periódica: detecta páginas huérfanas, wikilinks
rotos, contradicciones pendientes y desincronías entre la wiki y el índice.
También puedes ejecutar el linter directamente: `python scripts/lint.py`

---

## 🔭 Obsidian — Plugins Recomendados

| Plugin | Función |
|--------|---------|
| **Dataview** | Consultas dinámicas sobre el frontmatter YAML |
| **Marp Slides** | Presentaciones desde Markdown |
| **Obsidian Web Clipper** | Captura artículos web en un clic → `/raw/` |
| **Graph Analysis** | Análisis de conectividad del grafo |

---

*Ver también: [[user-guide]] · [[architecture]] · [[web-clipper-setup]]*
