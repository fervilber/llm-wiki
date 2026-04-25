---
title: "Índice de Autores"
type: registro
tags:
  - registro/indice
created: 2026-04-25
updated: 2026-04-25
---

# 👤 Índice de Autores

Directorio de todos los autores cuyas fuentes han sido ingestadas en la wiki.
El agente actualiza esta página tras cada procesamiento que incluya un autor nuevo o existente.

```dataview
TABLE afiliacion AS "Afiliación", web AS "Web", length(file.inlinks) AS "Fuentes"
FROM "wiki/autores"
WHERE type = "autor"
SORT file.name ASC
```

---

## Lista Alfabética

> *(El agente poblará esta sección con enlaces [[nombre-apellido]] ordenados alfabéticamente)*

---

## 📊 Estado

- **Total autores registrados**: 0
- **Última actualización**: 2026-04-25
