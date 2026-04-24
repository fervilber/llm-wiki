# Workflow: Procesamiento de Nueva Fuente

## Propósito
Algoritmo completo para procesar un archivo de `/raw/` e integrarlo en la wiki.

## Activación
El usuario dice: `«Procesa [ruta o nombre del archivo]»` o `«Analiza y procesa [ruta]»`

## Pasos

### Paso 1 — Cargar la skill
Leer `.agents/skills/ingesta/SKILL.md` para aplicar las reglas de procesamiento.

### Paso 2 — Leer la fuente
- Acceder al archivo indicado en `/raw/` (nunca modificarlo).
- Si es una imagen o PDF no procesable, solicitar al usuario una transcripción o descripción.

### Paso 3 — Analizar y extraer
Identificar:
- **Puntos clave** (hechos, datos, afirmaciones importantes)
- **Entidades** (personas, organizaciones, herramientas, productos)
- **Conceptos** (ideas, métodos, teorías)
- **Fecha de creación** del material original (si existe)

### Paso 4 — Confirmar con el usuario
Presentar un resumen breve de lo extraído y preguntar si el enfoque es correcto
antes de escribir en la wiki. *(Opcional: omitir si el usuario ha dado autonomía total.)*

### Paso 5 — Ejecutar escritura
Aplicar la lógica de `ingesta.md`:
- Consultar `wiki/index.md` para detectar páginas relacionadas existentes.
- Crear o actualizar páginas en `/wiki/fuentes/`, `/wiki/entidades/`, `/wiki/conceptos/`.
- Usar los templates de `.agents/templates/`.
- Insertar `[[wikilinks]]` y verificar bidireccionalidad.

### Paso 6 — Validar con linter
Si el script `scripts/lint.py` está disponible, ejecutarlo sobre las páginas modificadas.

### Paso 7 — Actualizar registros
- Añadir entrada en `wiki/registros/log.md`:
  ```
  ## [YYYY-MM-DD] procesa | Nombre del Archivo
  - Páginas creadas: X
  - Páginas actualizadas: Y
  - Notas: ...
  ```
- Actualizar `wiki/index.md` con las nuevas páginas.

### Paso 8 — Commit local
Guardar los cambios en git localmente (ver `.agents/skills/git/SKILL.md`):
```bash
git add -A
git commit -m "procesa(fuentes): <nombre descriptivo de la fuente procesada>"
```
El push a GitHub **no es automático** — se hace solo cuando el usuario lo pide
o al cerrar la sesión de trabajo.

### Paso 9 — Informar al usuario
Listar brevemente: páginas creadas, páginas actualizadas, posibles contradicciones detectadas.
Indicar el número de commits locales pendientes de push si el usuario quiere sincronizar.
