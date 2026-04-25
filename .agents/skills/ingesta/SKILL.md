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
3. **Verificación de duplicados**: Consultar `wiki/index.md` para detectar páginas existentes relacionadas.
4. **Contraste**: Comparar nueva información con páginas existentes:
   - Si confirma → reforzar la síntesis existente.
   - Si contradice → añadir bloque `> [!CAUTION] Contradicción` con ambas versiones.
5. **Creación / Actualización**: Escribir o actualizar los archivos afectados en `/wiki/`.
6. **Enlazado**: Insertar `[[wikilinks]]` bidireccionales entre notas relacionadas.
7. **Registro**: Añadir entrada en `wiki/registros/log.md` con el formato estándar.
8. **Índice**: Actualizar `wiki/index.md` con las nuevas páginas creadas.

## Reglas de Metadatos Obligatorias
Cada nota creada debe incluir el bloque YAML del estándar definido en `RULES.md §4`.

## Manejo de Imágenes
Todo archivo visual en `/raw/assets/` debe tener su descripción textual en la wiki
para garantizar indexabilidad semántica.
