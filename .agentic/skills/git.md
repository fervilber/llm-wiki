# Skill: Git — Sincronización Automática con GitHub

## Propósito

Mantener el repositorio de GitHub sincronizado con cada operación significativa del
agente: procesamiento de fuentes, creación de notas en la wiki, mantenimiento y
organización. El usuario nunca tiene que pensar en hacer un commit manual.

---

## Regla Fundamental

> **Después de CUALQUIER operación que modifique archivos del proyecto, el agente
> DEBE ejecutar automáticamente el ciclo git: `add → commit → push`.**

Esto incluye:
- Procesar un archivo de `/raw/` (se crean notas en `/wiki/`)
- Añadir un archivo a `/raw/` desde el agente
- Crear o editar una nota en `/wiki/`
- Crear un diagrama en `/wiki/diagramas/`
- Actualizar `wiki/index.md` o `wiki/registros/log.md`
- Ejecutar una revisión de mantenimiento con cambios

---

## Convención de Mensajes de Commit

El formato estándar es:

```
<tipo>(<ámbito>): <descripción breve en español>
```

### Tipos permitidos

| Tipo | Cuándo usarlo |
|------|---------------|
| `procesa` | Procesamiento de una fuente nueva en /raw/ |
| `wiki` | Creación o actualización de notas en /wiki/ |
| `diagrama` | Nuevo o actualizado diagrama Excalidraw |
| `raw` | Nuevo archivo añadido a /raw/ |
| `mantiene` | Revisión de mantenimiento, arreglo de enlaces |
| `config` | Cambios en .agentic/, scripts/, RULES.md |
| `docs` | Cambios en doc/ o README |

### Ámbito (opcional)

Nombre corto del archivo, tema o sección afectada. Ejemplo: `fuentes`, `conceptos`, `log`.

### Ejemplos de mensajes reales

```bash
git commit -m "procesa(fuentes): añade resumen del video 'Intro a LLMs'"
git commit -m "wiki(conceptos): nueva nota sobre RAG y modelos de embedding"
git commit -m "diagrama: arquitectura del sistema LLM Wiki"
git commit -m "mantiene: corrige enlaces rotos y actualiza índice"
git commit -m "raw: importa PDF 'informe-openai-2024'"
git commit -m "config: actualiza skill excalidraw con nuevos anti-patrones"
```

---

## Procedimiento de Sincronización (ejecutar siempre al final de cada operación)

### Paso 1 — Verificar estado del repositorio
```bash
git status
```
Si no hay cambios → no hacer nada (indicar "Sin cambios para guardar").

### Paso 2 — Añadir todos los cambios al staging
```bash
git add -A
```

> **¿Qué incluye `-A`?**
> - Archivos nuevos (notas creadas, archivos raw añadidos)
> - Archivos modificados (notas actualizadas, índice, log)
> - Archivos eliminados (si se borró algo intencionalmente)

### Paso 3 — Hacer el commit con mensaje descriptivo
```bash
git commit -m "<tipo>(<ámbito>): <descripción>"
```

Construir el mensaje a partir de:
- El **tipo** según la tabla de convención
- El **ámbito** = nombre del tema o archivo principal afectado
- La **descripción** = resumen de una línea en español de lo que se hizo

### Paso 4 — Enviar a GitHub
```bash
git push origin main
```

> Si la rama se llama `master` en lugar de `main`, usar `git push origin master`.
> El agente debe verificar la rama activa con `git branch --show-current` si hay duda.

---

## Manejo de Errores

### Error: "nothing to commit"
→ No hay cambios que guardar. Indicar al usuario y continuar.

### Error: "rejected" en el push (conflicto remoto)
```bash
git pull --rebase origin main
git push origin main
```
Si persiste el conflicto, NO forzar el push. Indicar al usuario:
> *«Hay cambios en GitHub que no están en local. Necesito que revises el conflicto manualmente con `git status` para no perder datos.»*

### Error: "not a git repository"
→ El repositorio no está inicializado. Indicar al usuario:
> *«El directorio no tiene git inicializado. ¿Quieres que ejecute `git init && git remote add origin <URL>`?»*

### Error: autenticación SSH/HTTPS
→ El agente no puede resolver credenciales por sí solo. Indicar al usuario que configure su acceso a GitHub:
> *«Git pide credenciales. Configura tu acceso con `gh auth login` (GitHub CLI) o con una clave SSH.»*

---

## Cuándo NO hacer push automático

Solo omitir el push automático si el usuario indica explícitamente:
- *«Guarda los cambios pero no subas a GitHub todavía»*
- *«Trabaja en modo offline»*
- *«Acumula los cambios y haz un solo commit al final»*

En ese caso, hacer el `git add + commit` pero omitir el `push`, e indicar los commits pendientes.

---

## Comandos Útiles de Referencia

```bash
# Ver estado actual
git status

# Ver últimos commits
git log --oneline -10

# Ver rama activa
git branch --show-current

# Ver diferencias antes de commitear
git diff --stat

# Deshacer último commit (sin perder los cambios)
git reset --soft HEAD~1

# Ver el remoto configurado
git remote -v

# Sincronizar con el remoto (sin push)
git pull --rebase origin main
```

---

## Commit Combinado (múltiples operaciones en sesión larga)

Si en la misma sesión se hacen varias operaciones menores (crear 3 notas, arreglar
2 enlaces y actualizar el índice), el agente puede agruparlas en un solo commit
al final de la sesión usando la convención:

```bash
git commit -m "wiki: sesión YYYY-MM-DD — X notas nuevas, Y actualizadas, mantenimiento"
```

Esto mantiene el historial limpio sin un commit por cada archivo individual.
