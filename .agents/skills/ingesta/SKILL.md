---
name: ingesta
description: Procesamiento estructurado de fuentes externas para su integración en el grafo de conocimiento.
metadata:
  author: F.VilBer
---

# Skill: Ingesta de Alta Densidad

## Propósito
Define la lógica que el agente debe aplicar al procesar un nuevo archivo en `/raw/`.

## Criterio MVC (Mínimo Valor de Conocimiento)
- Una información merece nota propia en `/wiki/` si aporta **≥ 3 ideas o datos sustanciales**.
- Si no alcanza el umbral, integrar en la página de la fuente padre.

## Proceso de Ingesta (paso a paso)

1. **Lectura**: Leer el archivo fuente en `/raw/` sin modificarlo.
2. **Extracción**: Identificar:
   - Entidades con nombre propio → candidatas a `/wiki/entidades/`
   - Conceptos abstractos → candidatos a `/wiki/conceptos/`
   - Datos cuantitativos o afirmaciones clave → para integrar en páginas existentes
3. **Protocolo de Autoría** *(siempre tras la extracción)*:
   - Extraer el/los autor/es de la fuente (campo YAML, firma del artículo, descripción del canal, portada del libro, créditos del video, etc.)
   - Si el autor es identificable:
     - Buscar si existe `wiki/autores/nombre-apellido.md` (kebab-case del nombre completo)
     - **Si existe** → abrir la ficha y añadir la nueva fuente en la sección `## Fuentes Procesadas`
     - **Si no existe** → crear ficha nueva usando el template `.agents/templates/nota-autor.md`
     - Añadir campo `authors: ["Nombre Apellido"]` en el YAML de la nota-fuente
     - Añadir sección `## Autor/es` con el wikilink `[[wiki/autores/nombre-apellido|Nombre Apellido]]`
     - Garantizar backlink en la ficha del autor → fuente (bidireccionalidad)
     - Actualizar `wiki/autores/_index-autores.md` con el nuevo autor (si es nuevo)
   - Si el autor es desconocido:
     - Añadir tag `autor/anonimo` al YAML de la nota-fuente
     - Omitir la sección `## Autor/es` y la creación de ficha
4. **Verificación de duplicados**: Consultar `wiki/index.md` para detectar páginas existentes relacionadas.
5. **Contraste**: Comparar nueva información con páginas existentes:
   - Si confirma → reforzar la síntesis existente.
   - Si contradice → añadir bloque `> [!CAUTION] Contradicción` con ambas versiones.
6. **Creación / Actualización**: Escribir o actualizar los archivos afectados en `/wiki/`.
7. **Enlazado**: Insertar `[[wikilinks]]` bidireccionales entre notas relacionadas.
8. **Registro**: Añadir entrada en `wiki/registros/log.md` con el formato estándar.
9. **Índice**: Actualizar `wiki/index.md` con las nuevas páginas creadas.

## Reglas de Metadatos Obligatorias
Cada nota creada debe incluir el bloque YAML del estándar definido en `RULES.md §4`.

## Manejo de Imágenes
Todo archivo visual en `/raw/assets/` debe tener su descripción textual en la wiki
para garantizar indexabilidad semántica.
