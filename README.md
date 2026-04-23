# 🧠 LLM Wiki — Base de Conocimiento Personal con Agente IA

Base de conocimiento personal (Personal Knowledge Base) construida con el patrón
**LLM Wiki**: un agente de IA actúa como mantenedor activo que extrae, estructura
y conecta el conocimiento de fuentes crudas en una red interconectada de notas
Markdown, visualizada en **Obsidian**.

> **Analogía de flujo:** Obsidian es el IDE. El agente LLM es el programador.
> La wiki es el código fuente. Tú eres el arquitecto.

---

## 🎯 ¿Qué hace este proyecto?

A diferencia de los sistemas RAG tradicionales (donde el LLM redescubre el
conocimiento desde cero en cada consulta), este sistema **compila el conocimiento
una sola vez** y lo mantiene actualizado de forma acumulativa:

- Cuando añades una nueva fuente, el agente la lee, extrae lo relevante
  e integra la información en la wiki existente.
- Las referencias cruzadas ya existen. Las contradicciones ya están marcadas.
- La síntesis refleja todo lo que has leído hasta hoy.

---

## 🛠 Herramientas Necesarias

Este proyecto está diseñado para funcionar con **dos herramientas en paralelo**:

### 1. Obsidian (Visualización)
**[Obsidian](https://obsidian.md)** es la aplicación de escritorio que usarás
para leer, navegar y explorar la wiki. Instálala y abre la carpeta raíz de este
proyecto como un **Vault**.

Plugins recomendados (instalar desde `Ajustes → Plugins de la Comunidad`):
| Plugin | Función |
|--------|---------|
| **Dataview** | Consultas dinámicas sobre el frontmatter YAML |
| **Marp Slides** | Generación de presentaciones desde Markdown |
| **Obsidian Web Clipper** | Captura artículos web directamente a `/raw/` |
| **Graph Analysis** | Análisis avanzado del grafo de conocimiento |
| **Excalidraw** | Diagramas y esquemas visuales creados por el agente ⭐ |

### 2. Agente LLM (Mantenimiento y Operación)
El agente es quien **escribe y organiza** la wiki. Puedes usar cualquiera de estos:

| Agente | Cómo usarlo |
|--------|-------------|
| **Claude** (claude.ai) | Chat directo; dale acceso a los archivos del proyecto |
| **Antigravity** | IDE con IA integrada; trabaja directamente sobre el repo |
| **OpenCode / Codex** | Terminal con IA; usa `RULES.md` como contexto |

**Flujo de trabajo típico:**
```
[Tú]         →  Buscas fuentes, formulas preguntas, defines objetivos
[Agente LLM] →  Lee /raw/, procesa, escribe en /wiki/, mantiene el grafo
[Obsidian]   →  Tú visualizas el resultado en tiempo real
```

---

## 📂 Estructura del Proyecto

```
/ (Raíz)
├── RULES.md                   # Constitución del sistema (el agente la lee primero)
├── README.md                  # Este archivo
├── .gitignore
│
├── .agentic/                  # 🧠 Cerebro del agente (no editar sin intención)
│   ├── skills/
│   │   ├── ingesta.md         # Reglas de procesamiento de fuentes
│   │   ├── consulta.md        # Reglas de respuesta a preguntas
│   │   └── mantenimiento.md   # Reglas de calidad del grafo
│   ├── workflows/
│   │   ├── inicializacion.md  # Protocolo de arranque de sesión
│   │   ├── ingesta.md         # Algoritmo completo de ingesta
│   │   └── revision.md        # Auditoría periódica de la wiki
│   └── templates/
│       ├── nota-fuente.md     # Template YAML+MD para fuentes
│       ├── nota-entidad.md    # Template para entidades
│       └── nota-concepto.md   # Template para conceptos
│
├── doc/                       # 📄 Documentación para humanos
│   ├── user-guide.md          # Guía completa de uso
│   ├── architecture.md        # Diagrama y diseño del sistema
│   ├── web-clipper-setup.md   # Configuración del Web Clipper de Obsidian
│   └── faq.md                 # Preguntas frecuentes
│
├── raw/                       # 📥 Material bruto (INMUTABLE — no modificar)
│   └── assets/                # Imágenes y adjuntos descargados
│
├── scripts/                   # 🔧 Herramientas de soporte
│   ├── youtube_to_raw.py      # Descarga transcripciones de YouTube → /raw/
│   ├── pdf_to_raw.py          # Extrae texto de PDFs → /raw/
│   ├── lint.py                # Valida formato, YAML y wikilinks
│   ├── search.py              # Búsqueda local sobre la wiki
│   └── requirements.txt       # Dependencias Python
│
└── wiki/                      # 📚 Grafo de conocimiento (escrito por el agente)
    ├── Home.md                # Página de inicio de Obsidian
    ├── index.md               # Catálogo navegable de todo el contenido
    ├── fuentes/               # Resúmenes de materiales originales
    ├── entidades/             # Personas, herramientas, organizaciones
    ├── conceptos/             # Ideas abstractas, métodos, teorías
    └── registros/
        └── log.md             # Historial cronológico de operaciones
```

---

## 🚀 Primeros Pasos

### Paso 1 — Instalar Obsidian
1. Descarga e instala [Obsidian](https://obsidian.md).
2. Abre la carpeta raíz de este proyecto como Vault: `Abrir carpeta como Vault`.
3. Instala los plugins recomendados (ver tabla arriba).
4. En `Ajustes → Archivos y enlaces`, configura la carpeta de adjuntos en `raw/assets/`.

### Paso 2 — Configurar el entorno Python
```bash
# Instalar dependencias desde la raíz del proyecto
pip install -r scripts/requirements.txt
```

### Paso 3 — Iniciar una sesión de trabajo
Abre tu agente LLM y envíale el **Prompt de Inicialización**:

> *"Actúa como mantenedor de mi LLM Wiki. Estamos en la raíz del proyecto.
> Lee en este orden: 1) `RULES.md` 2) `.agentic/workflows/inicializacion.md`
> 3) `wiki/index.md` 4) `wiki/registros/log.md`.
> Confírmame cuando hayas leído y dime el estado actual de la wiki."*

---

## 📥 Fuentes de Entrada Soportadas

Añade contenido a `/raw/` y después dile al agente que lo procese.

| Tipo de fuente | Cómo añadirla a `/raw/` | Qué decirle al agente |
|---------------|------------------------|-----------------------|
| **Artículo web** | Obsidian Web Clipper (1 clic) | *«Procesa el archivo `raw/nombre.md` y actualiza la wiki»* |
| **Video YouTube** | `python scripts/youtube_to_raw.py <URL>` | *«Procesa este video y guarda la transcripción en raw: `<URL>`»* |
| **PDF** | `python scripts/pdf_to_raw.py <ruta.pdf>` | *«Analiza y procesa `raw/nombre.md` extrayendo los datos clave»* |
| **Texto / Markdown** | Copiar manualmente en `/raw/` | *«Analiza y procesa los últimos documentos añadidos a /raw»* |
| **Imagen / Captura** | Guardar en `/raw/assets/` | *«Describe la imagen `raw/assets/nombre.png` e intégrala en la wiki»* |

### Ejemplos de frases para el agente

```
# Procesar una fuente concreta
«Procesa el archivo raw/articulo-sobre-ia.md y actualiza la wiki»
«Procesa este video y guarda la transcripción en raw: https://youtu.be/xyz»
«Analiza y procesa los últimos documentos añadidos a /raw»

# Consultar el conocimiento acumulado
«¿Qué sabemos sobre inteligencia artificial según la wiki?»
«Compara las notas sobre Claude y GPT-4 que tenemos en la wiki»
«Haz un resumen de todo lo que hemos procesado este mes»

# Mantenimiento
«Realiza un mantenimiento de la wiki»
«Realiza un mantenimiento de los enlaces y corrige los que estén rotos»
«¿Hay páginas huérfanas o sin conectar en la wiki?»

# Organización
«Actualiza el índice de la wiki con las últimas notas creadas»
«Guarda este análisis como una nueva nota en wiki/conceptos/»
```

> Para la referencia completa de instrucciones, consulta [Guía de Usuario](doc/user-guide.md) § Cómo Hablarle al Agente.

---

## 📖 Documentación Completa

| Documento | Descripción |
|-----------|-------------|
| [Guía de Usuario](doc/user-guide.md) | Flujos de trabajo, instrucciones al agente, comandos |
| [Arquitectura](doc/architecture.md) | Diseño del sistema y filosofía |
| [Web Clipper Setup](doc/web-clipper-setup.md) | Captura de artículos web con un clic |
| [FAQ](doc/faq.md) | Preguntas frecuentes |
| [RULES.md](RULES.md) | Constitución del sistema (para el agente) |

---

## 🔄 Continuidad entre Sesiones

El proyecto está diseñado para que **cualquier agente pueda retomar el trabajo**
desde cualquier punto sin historial de chat previo. Toda la memoria está en los archivos:

- `wiki/index.md` → estado actual del conocimiento acumulado
- `wiki/registros/log.md` → última operación realizada
- `RULES.md` + `.agentic/` → instrucciones operativas completas

---

*Basado en el patrón [LLM Wiki](idea.md) — el conocimiento se compila una vez y se mantiene.*
