# Workflow: Inicialización del Proyecto

## Propósito
Secuencia de arranque que el agente debe ejecutar la primera vez que se accede
a este proyecto, o tras una restauración desde Git.

## Pasos

### Paso 1 — Leer el entorno
1. Leer `RULES.md` en la raíz → comprender estructura y reglas operativas.
2. Leer este archivo → cargar el flujo de inicialización.
3. Verificar que todos los directorios definidos en `RULES.md §1` existen.

### Paso 2 — Verificar archivos críticos
Comprobar la existencia de:
- [ ] `wiki/index.md`
- [ ] `wiki/registros/log.md`
- [ ] `.agents/templates/nota-fuente.md`
- [ ] `.agents/templates/nota-entidad.md`
- [ ] `.agents/templates/nota-concepto.md`

Si alguno falta → crearlo usando el template vacío correspondiente.

### Paso 3 — Verificar estado Git
```bash
git status
git log --oneline origin/main..HEAD
git remote -v
```
Informar al usuario de:
- Rama activa (`git branch --show-current`)
- Commits locales pendientes de push (si los hay)
- Remoto configurado (debe apuntar a `github.com/fervilber/llm-wiki`)

Si hay commits locales sin push → **preguntar al usuario** si quiere hacer push ahora.
No ejecutar push automáticamente durante la inicialización.

### Paso 4 — Cargar skills activas
El agente debe conocer las skills disponibles:
- `.agents/skills/ingesta/SKILL.md` → procesamiento de fuentes
- `.agents/skills/consulta/SKILL.md` → respuesta a preguntas
- `.agents/skills/mantenimiento/SKILL.md` → calidad del grafo
- `.agents/skills/git/SKILL.md` → sincronización automática con GitHub ⬆️
- `.agents/skills/excalidraw/SKILL.md` → creación de diagramas

### Paso 5 — Reportar estado al usuario
Informar brevemente:
- Número de páginas en `/wiki/`
- Última entrada en `/wiki/registros/log.md`
- Estado de sincronización Git
- Cualquier anomalía detectada (páginas huérfanas, índice desactualizado)

### Paso 6 — Confirmar disponibilidad
El agente debe indicar explícitamente que está listo para recibir instrucciones.
Recordar al usuario los comandos principales:

```
«Procesa [fuente]»          → procesamiento de nueva fuente
«¿Qué sabemos sobre [X]?»  → consulta a la wiki
«Realiza un mantenimiento» → revisión de calidad
«Crea un diagrama de...»   → Excalidraw
```
