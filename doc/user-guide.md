# Guía de Usuario — LLM Wiki

Esta guía explica cómo usar la LLM Wiki en el día a día. Para entender el diseño
del sistema, consulta la [[architecture|Arquitectura]]. Para capturas web, consulta
la [[web-clipper-setup|Configuración del Web Clipper]].

---

## 🛠 Herramientas Necesarias

Esta wiki está diseñada para funcionar con **dos herramientas en paralelo**:

### Obsidian — El Visualizador
**[Obsidian](https://obsidian.md)** es la aplicación de escritorio donde **lees y
navegas** la wiki. No escribes las notas tú: el agente lo hace. Tú las lees en Obsidian.

**Instalación:**
1. Descarga desde [obsidian.md](https://obsidian.md) (gratuito, Windows/Mac/Linux/iOS/Android).
2. Abre Obsidian → `Abrir carpeta como Vault` → selecciona la raíz de este proyecto.
3. Instala los plugins recomendados desde `Ajustes → Plugins de la Comunidad`:

| Plugin | Para qué sirve |
|--------|----------------|
| **Dataview** | Tablas dinámicas que consultan el frontmatter YAML de tus notas |
| **Marp Slides** | Genera presentaciones directamente desde Markdown |
| **Obsidian Web Clipper** | Captura artículos web en un clic → directamente a `/raw/` |
| **Graph Analysis** | Métricas avanzadas del grafo de conocimiento |

4. En `Ajustes → Archivos y enlaces`:
   - **Carpeta de adjuntos**: `raw/assets`
   - Asigna atajo `Ctrl+Shift+D` a "Descargar adjuntos del archivo actual".

### Agente LLM — El Mantenedor
El agente es quien **procesa, escribe y organiza** la wiki. Trabaja en paralelo
a Obsidian: tú ves los cambios en tiempo real mientras el agente los ejecuta.

**Agentes compatibles:**

| Agente | Descripción |
|--------|-------------|
| **Claude** (claude.ai o app de escritorio) | Conecta al proyecto vía carga de archivos o MCP |
| **Antigravity** | IDE con IA integrada; accede directamente al repo |
| **OpenCode / Codex** | Agente de terminal; usa `RULES.md` + `.agentic/` como contexto |

**Cómo iniciar una sesión con el agente:**

Envía al agente este prompt de inicialización al comenzar:

> *"Actúa como mantenedor de mi LLM Wiki. Estamos en la raíz del proyecto.
> Lee en este orden:
> 1. `RULES.md` — para entender las reglas del sistema
> 2. `.agentic/workflows/inicializacion.md` — para el protocolo de arranque
> 3. `wiki/index.md` — para conocer el estado actual del conocimiento
> 4. `wiki/registros/log.md` — para saber qué se hizo por última vez
>
> Confírmame cuando hayas leído y dime el estado actual."*

El agente recuperará todo el contexto sin necesidad de historial de chat previo.

---

## 📥 Añadir Fuentes Nuevas

### Opción A — Artículo Web
Usa el **Obsidian Web Clipper** (ver [[web-clipper-setup]]):
1. Clip del artículo → se guarda en `/raw/` automáticamente.
2. Dile al agente: *«Procesa el archivo `raw/<nombre>.md` y actualiza la wiki»*

### Opción B — Video de YouTube
Puedes pedírselo directamente al agente sin usar scripts:
> *«Procesa este video y guarda la transcripción en raw: `https://youtu.be/...`»*

O bien usando el script desde la terminal (el archivo quedará en `/raw/` listo para procesarlo):
```bash
python scripts/youtube_to_raw.py "https://youtu.be/ID_DEL_VIDEO"
python scripts/youtube_to_raw.py "https://youtu.be/ID_DEL_VIDEO" "nombre_descriptivo"
```
Después dile al agente: *«Procesa `raw/<nombre>.md` y guarda el conocimiento en la wiki»*

### Opción C — Archivo PDF
```bash
python scripts/pdf_to_raw.py "C:/ruta/al/archivo.pdf"
python scripts/pdf_to_raw.py "C:/ruta/al/archivo.pdf" "nombre_descriptivo"
```
Extrae el texto del PDF y lo convierte a Markdown en `/raw/`.
Requiere tener instalada al menos una librería de extracción (ver `scripts/requirements.txt`).

### Opción D — Texto o Markdown Manual
Copia el contenido en un nuevo archivo `.md` dentro de `/raw/`.
Usa el template `.agentic/templates/nota-fuente.md` como base para el frontmatter.

### Opción E — Imagen o Captura de Pantalla
1. Guarda la imagen en `/raw/assets/`.
2. Dile al agente: *«Describe la imagen `raw/assets/nombre.png` e intégrala en la wiki»*

---

## 💬 Cómo Hablarle al Agente — Guía de Instrucciones

El agente entiende **lenguaje natural en español**. No hace falta usar comandos exactos;
estas frases de ejemplo te sirven de referencia para saber qué puedes pedirle.

### 📥 Procesar fuentes nuevas

| Situación | Frase de ejemplo |
|-----------|------------------|
| Artículo ya guardado en `/raw/` | *«Procesa el archivo `raw/articulo-sobre-ia.md` y actualiza la wiki»* |
| Video de YouTube (directo) | *«Procesa este video y guarda la transcripción en raw: `https://youtu.be/...`»* |
| PDF ya importado a `/raw/` | *«Analiza y procesa `raw/informe-anual.md` extrayendo los datos clave»* |
| Varios archivos nuevos a la vez | *«Analiza y procesa los últimos documentos añadidos a /raw»* |
| Con orientación temática | *«Procesa `raw/video-economia.md` prestando especial atención a las métricas financieras»* |

### 🔍 Consultar el conocimiento acumulado

| Situación | Frase de ejemplo |
|-----------|------------------|
| Pregunta directa | *«¿Qué sabemos sobre inteligencia artificial según la wiki?»* |
| Listar notas de un tema | *«Muéstrame todas las notas relacionadas con modelos de lenguaje»* |
| Comparación | *«Compara las notas sobre Claude y GPT-4 que tenemos en la wiki»* |
| Síntesis | *«Haz un resumen de todo lo que hemos procesado este mes»* |
| Dashboard | *«¿Cuál es el estado actual de la wiki? ¿Qué tenemos?»* |

### 🔧 Mantenimiento y calidad

| Situación | Frase de ejemplo |
|-----------|------------------|
| Revisión general | *«Realiza un mantenimiento de la wiki»* |
| Solo los enlaces | *«Realiza un mantenimiento de los enlaces y corrige los que estén rotos»* |
| Contradicciones | *«Busca y lista las contradicciones marcadas que haya en la wiki»* |
| Estado del grafo | *«¿Hay páginas huérfanas o sin conectar en la wiki?»* |
| Buscar algo concreto | *«Busca en la wiki todo lo que menciona el concepto de RAG»* |

### 🗂 Organización

| Situación | Frase de ejemplo |
|-----------|------------------|
| Actualizar índice | *«Actualiza el índice de la wiki con las últimas notas creadas»* |
| Guardar análisis valioso | *«Guarda este análisis como una nueva nota en `wiki/conceptos/`»* |
| Fusionar notas similares | *«Fusiona las notas sobre "LLM" y "Modelo de Lenguaje" en una sola»* |

---

## 🔍 Navegar en Obsidian

| Vista | Para qué sirve |
|-------|----------------|
| **Graph View** (`Ctrl+G`) | Ver conexiones entre todas las notas |
| **Backlinks** (panel derecho) | Ver qué notas apuntan a la nota actual |
| **Dataview** | Tablas dinámicas con los metadatos de tus notas |
| `wiki/Home.md` | Punto de entrada principal |
| `wiki/index.md` | Catálogo navegable de todo el contenido |

---

## 🔧 Mantenimiento

De vez en cuando, pide al agente alguna de estas frases:
- *«Realiza un mantenimiento de la wiki»*
- *«Realiza un mantenimiento de los enlaces y corrige los que estén rotos»*

El agente auditará:
- Páginas huérfanas (sin enlaces entrantes)
- Wikilinks rotos
- Contradicciones marcadas con `[!CAUTION]` pendientes de resolución
- Consistencia del índice

También puedes ejecutar el linter directamente:
```bash
python scripts/lint.py              # Valida toda la wiki
python scripts/lint.py wiki/fuentes # Solo un directorio
```

---

## 📌 Reglas para no Romper Nada

| ✅ Puedes | ❌ No debes |
|-----------|------------|
| Añadir archivos a `/raw/` | Modificar o borrar archivos de `/raw/` |
| Leer y navegar `/wiki/` en Obsidian | Editar notas de `/wiki/` sin avisar al agente |
| Editar `.agentic/` con intención deliberada | Cambiar `RULES.md` sin revisar el impacto |
| Pedir al agente que añada una nota | Crear notas en `/wiki/` sin seguir el template |

---

## 💡 Consejos de Productividad

- **Sesión tipo**: Obsidian abierto en un monitor → agente en el otro. Los cambios
  se reflejan en Obsidian en tiempo real mientras el agente trabaja.
- **Procesamiento por lotes**: Puedes depositar varios archivos en `/raw/` y decirle
  *«Analiza y procesa los últimos documentos añadidos a /raw»*. Pero el procesamiento
  supervisado (uno a la vez) produce síntesis de mayor calidad.
- **Archivar respuestas valiosas**: Si el agente produce un análisis o comparación útil,
  pídele que lo guarde como nota en `/wiki/conceptos/` — así el conocimiento se acumula.

---

*Ver también: [[architecture]] · [[web-clipper-setup]] · [[faq]]*
