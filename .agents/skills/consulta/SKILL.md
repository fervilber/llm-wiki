---
name: consulta
description: Gestión de respuestas a preguntas basadas exclusivamente en el contenido de la wiki.
metadata:
  author: F.VilBer
---

# Skill: Respuesta a Consultas

## Propósito
Define cómo el agente debe responder preguntas del usuario usando el contenido de la wiki.

## Regla de Fuente de Verdad
El agente responde **exclusivamente** desde `/wiki/`. No consulta `/raw/` directamente
salvo que el usuario lo solicite de forma explícita.

## Proceso de Consulta

1. **Interpretar la pregunta**: Identificar entidades, conceptos o períodos de tiempo relevantes.
2. **Leer el índice**: Consultar `wiki/index.md` para localizar páginas candidatas.
3. **Leer páginas relevantes**: Acceder en profundidad a las páginas identificadas.
4. **Sintetizar respuesta**: Formular la respuesta con citas a las notas fuente usando `[[wikilink]]`.
5. **Formato de salida**: Adaptar el formato según la naturaleza de la pregunta:
   - Respuesta narrativa → Markdown
   - Comparación → Tabla Markdown
   - Tendencia temporal → Lista cronológica
   - Datos → Bloque de código o gráfico (si se dispone de script)
6. **Archivar si es valioso**: Si la respuesta tiene valor acumulativo (análisis, comparación),
   proponer guardarla como nueva página en `/wiki/conceptos/` o `/wiki/entidades/`.
7. **Registrar**: Añadir entrada en `wiki/registros/log.md`.

## Límite de Conocimiento
Si la información no está en `/wiki/`, el agente debe indicarlo claramente y
sugerir fuentes para ingestar en lugar de inventar datos.
