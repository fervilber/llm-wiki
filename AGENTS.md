# AGENTS.md — Contexto para Agentes de Codificación IA

**Mantenedor Principal:** F.VilBer (contactovilber@pm.me)

Este archivo documenta el proyecto LLM Wiki para que cualquier agente de IA pueda comprenderlo y operar sobre él de forma autónoma.

---

## Propósito del Proyecto

**LLM Wiki** es una base de conocimiento personal donde un agente de IA actúa como **mantenedor activo** que extrae, estructura y conecta conocimiento de fuentes crudas (`/raw/`) en una red interconectada de notas Markdown (`/wiki/`), visualizada en Obsidian.

> **Analogía**: Obsidian es el IDE. El agente LLM es el programador. La wiki es el código fuente. El usuario es el arquitecto.

---

## Estructura del Proyecto

```
raíz/
├── RULES.md                   # Constitución del sistema (léela primero)
├── AGENTS.md                 # Este archivo — contexto para IA
├── README.md                # Documentación para humanos
│
├── .agents/                # 🧠 Cerebro del agente (instrucciones operativas)
│   ├── skills/             # Reglas lógicas por tarea
│   │   ├── ingesta.md    # Procesamiento de fuentes → wiki
│   │   ├── consulta.md   # Respuesta a preguntas desde wiki
│   │   ├── mantenimiento.md # Calidad del grafo
│   │   ├── git.md        # Sincronización Git
│   │   └── excalidraw.md # Diagramas visuales
│   ├── workflows/          # Algoritmos secuenciales multitarea
│   │   ├── inicializacion.md # Arranque de sesión
│   │   ├── ingesta.md    # Flujo completo de procesamiento
│   │   └── revision.md  # Auditoría periódica
│   └── templates/         # Esquemas YAML+MD para notas
│       ├── nota-fuente.md
│       ├── nota-entidad.md
│       └── nota-concepto.md
│
├── doc/                    # 📄 Documentación humana
│   ├── user-guide.md      # Guía completa de uso
│   ├── architecture.md  # Diseño del sistema
│   └── faq.md           # Preguntas frecuentes
│
├── raw/                   # 📥 Entrada inmutable (no modificar)
│   └── assets/          # Imágenes/adjuntos
│
├── scripts/              # 🔧 Herramientas Python
│   ├── youtube_to_raw.py
│   ├── pdf_to_raw.py
│   ├── lint.py          # Validador de formato
│   └── search.py
│
└── wiki/                 # 📚 Grafo de conocimiento (salida del agente)
    ├── Home.md          # Página de inicio Obsidian
    ├── index.md        # Catálogo navegable
    ├── fuentes/        # Resúmenes de materiales
    ├── entidades/      # Personas, herramientas, orgs
    ├── conceptos/      # Ideas, métodos, teorías
    └── registros/
        └── log.md      # Historial de operaciones
```

---

## Protocolo de Descubrimiento (Orden de Lectura)

Al iniciar una sesión en este proyecto, el agente debe:

1. **Leer `RULES.md`** → comprende estructura y reglas operativas
2. **Leer `.agents/workflows/inicializacion.md`** → carga flujo de arranque
3. **Verificar estado Git** → `git status`, `git log --oneline`
4. **Cargar skills activas** → ingesta.md, consulta.md, mantenimiento.md
5. **Reportar estado** al usuario

**Prioridad de verdad**: Las instrucciones en `.agents/` tienen prioridad sobre `/doc/`.

---

## Skills Disponibles

| Skill | Ubicación | Función |
|-------|-----------|--------|
| Ingesta | `.agents/skills/ingesta/SKILL.md` | Procesa `/raw/` → `/wiki/` |
| Consulta | `.agents/skills/consulta/SKILL.md` | Responde desde `/wiki/` |
| Mantenimiento | `.agents/skills/mantenimiento/SKILL.md` | Calidad del grafo |
| Git | `.agents/skills/git/SKILL.md` | Sincronización |
| Excalidraw | `.agents/skills/excalidraw/SKILL.md` | Diagramas |

---

## Workflows Disponibles

| Workflow | Activación |
|----------|------------|
| Inicialización | Nueva sesión o restauración Git |
| Procesamiento | «Procesa [archivo]» |
| Revisión | «Realiza un mantenimiento» |

---

## Reglas Operativas Clave

### Ingesta y Síntesis
- **MVC** (Mínimo Valor de Conocimiento): Crear nota atómica solo si aporta ≥3 puntos de datos nuevos.
- **Contexto Temporal**: Registrar fecha de procesamiento y fecha original del material.
- **Multimodalidad**: Describir imágenes textualmente para indexabilidad.

### Gestión de Información
- `/raw/` es **inmutable** — nunca modificar.
- Responder consultas **exclusivamente** desde `/wiki/`.

### Integridad del Grafo
- **Bidireccionalidad**: Si A → `[[B]]`, entonces B debe tener enlace de retorno.
- **Detección de menciones**: Convertir términos existentes en wikilinks activos.

### Metadatos (YAML)
Todas las notas en `/wiki/` siguen este esquema:
```yaml
---
title: "Título"
aliases: [Sinónimo1, Sinonimo2]
type: [entidad | concepto | fuente | registro]
tags: [clase/subclase]  # kebab-case, singular, jerárquico
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

### Tags
- **YAML** (clasificación): qué es la nota
- **Línea** (contexto): atributos transversales
- **Wikilink** (entidades/conceptos): si tienen página propia

---

## Comandos del Usuario (Ejemplos)

```
«Inicia sesión»                      → protocolo de arranque
«Procesa raw/articulo.md»              → procesar fuente
«¿Qué sabemos sobre [X]?»          → consultar wiki
«Compara [A] y [B]»               → comparación
«Realiza un mantenimiento»          → revisión de calidad
«Crea un diagrama de...»           → Excalidraw
«Actualiza el índice»              → sync index.md
```

---

## Integración con Obsidian

- Abrir la raíz del proyecto como **Vault** en Obsidian.
- Plugins recomendados: Dataview, Graph Analysis, Excalidraw, Obsidian Web Clipper.
- Carpeta de adjuntos: `raw/assets/`.

---

## Siguiente Pasos para el Agente

1. Leer `RULES.md` completo
2. Leer `.agents/workflows/inicializacion.md`
3. Verificar estado del proyecto
4. Confirmar disponibilidad al usuario

---

*Última actualización: 2026-04-23*